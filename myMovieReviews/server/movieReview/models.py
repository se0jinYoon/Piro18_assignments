from django.conf import settings
from django.db import models
from django.utils import timezone


class MovieReview(models.Model):
    #영화제목 / 개봉 년도 / 장르 / 별점
    title = models.CharField(max_length = 200)
    released = models.IntegerField()
    genre = models.CharField(max_length = 200)
    star = models.FloatField()
    director = models.CharField(max_length=200)
    cast = models.CharField(max_length=200)
    runtime = models.CharField(max_length=200)
    review = models.TextField()

# class MovieDetail(models.Model):
#     #영화 제목, 감독, 주연, 장르, 별점, 러닝타임, 리뷰내용
#     title = models.CharField(max_length=200)
#     director = models.CharField(max_length=200)
#     cast = models.CharField(max_length=200)
#     genre = models.CharField(max_length=200)
#     star = models.FloatField()
#     runtime = models.CharField(max_length=200)
#     review = models.TextField()
