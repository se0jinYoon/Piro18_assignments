let startBtn = document.getElementById('startBtn')
let stopBtn = document.getElementById('stopBtn')
let resetBtn = document.getElementById('resetBtn')

// let timeSec = document.getElementById('timeSec')
// let timeMilisec = document.getElementById('timeMilisec')
// let recordsTarget = document.getElementById('recordsTarget')

let clickedTime = 0 //시작 시간 저장
let stopTime= 0 //멈춘 시간 저장
let timerStart

let sec
let milisec
let i = 0
// let records = ""


startBtn.addEventListener('click', function() {
    if(!clickedTime) { //처음 시작
        clickedTime = Date.now()  
    } else {
        clickedTime += (Date.now() - stopTime) //재시작 시간
    }

    //화면에 표시할 시간
    timerStart = setInterval(function() {
        let newTime = new Date(Date.now() - clickedTime) // 현재 시간이랑 누른 시간 차이 계산

        sec = addZero(newTime.getSeconds()) //초
        milisec = addZero(Math.floor(newTime.getMilliseconds() / 10)) //밀리초

        //스톱와치 메인화면에 표시
        document.getElementById('timeSec').innerText = sec
        document.getElementById('timeMilisec').innerText = milisec
    }, 1)

})

stopBtn.addEventListener('click', function() {
    if(timerStart){ //한 번이라도 start가 눌려서 값을 저장하고 있다면
        clearInterval(timerStart) //stop! setInterval이 return해주는 값 사용
        stopTime = Date.now()
    }
})

$('#stopBtn').click(function(){
    
    let records = ""
    records += sec + ' : ' + milisec +'\n'
    let checkboxTest  = `<div id="test" class="d-flex flex-row"><input type="checkbox" name="check" class="col-3"/><span id="test" class="col-9">${records}</span></div>`
    // let timeTest = `<span id="test" class="col-9">${records}</span></div>`
    
    $('#recordsTarget').append(checkboxTest)
    // $('#recordsTarget').append(timeTest)

    i = i + 1
    
})

$('#deletebtn').click(function() {
    $("input:checkbox[name='check']:checked").each(function(k,kVal){
        let a = kVal.parentElement;
        $(a).remove();
    })
});

function selectAll(selectAll) {
    const checkboxes = document.getElementsByName('check')

    checkboxes.forEach((checkbox) => {
        checkbox.checked = selectAll.checked;
    })
}



document.getElementById("record")

resetBtn.addEventListener('click', function() {
    clickedTime = 0
    sec = 0
    milisec = 0
    timeSec.innerText = '00'
    timeMilisec.innerText = '00'
    timerStart = null;
    recordList.innerHTML = ''
})

//한 자리면 앞에 0채워서 출력 형식 맞추기
function addZero(num) {
    return (num < 10? '0'+num : ''+num)
}

// records += addZero(sec) + ' : ' + addZero(milisec) +'\n'

// // let checkbox = document.createElement('input')
// // checkbox.type = 'checkbox';
// // checkbox.id = 'recordList';

// recordsTarget.append()

// // records += addZero(sec) + ' : ' + addZero(milisec) +'\n'
// recordsTarget.innerText = records;