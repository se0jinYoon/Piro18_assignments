from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt #보안 관련 부분


# 폼 처리시 GET과 POST둘 다 처리
# GET에서는 입력폼 보여줌 / POST에서는 데이터 받아서 검증 후 저장하고 리스트 페이지로 redirect
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
        else:
            context = {
                'form': form
            }
            return render(request, 'post_new.html', context)
    elif request.method == 'GET':
        form = PostForm()
        context = {
            'form' : form,
        }
        return render(request, 'post_new.html', context)

def post_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'posts' : posts,
        'comments' : comments,
    }
    return render(request, 'post_list.html', context=context)

def post_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

@csrf_exempt
def like_ajax(request, *args, **kwargs):
    req = json.loads(request.body)

    post_id = req['id']
    post = Post.objects.get(id = post_id)

    if post.like == True:
        post.like = False
    else:
        post.like = True
    post.save()

    liked = post.like
    return JsonResponse({'id': post_id, 'liked': liked})

@csrf_exempt #403에러 방지
def comment_ajax(request, *args, **kwargs):
    req = json.loads(request.body) #{id:1, content: ...}

    post_id = req['id'] #1
    content = req['content'] #...

    comment = Comment.objects.create(
        post = Post.objects.get(id=post_id),
        content = content,
    )

    return JsonResponse({'post_id': post_id, 'comment_id': comment.id, 'content': comment.content})

@csrf_exempt
def comment_del_ajax(request, *args, **kwargs):
    req = json.loads(request.body)

    post_id = req['post_id']
    comment_id = req['comment_id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'post_id': post_id, 'comment_id': comment_id})