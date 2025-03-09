var activeList = []
confirmed = document.querySelector(".confirmed").textContent
if(confirmed == "f"){
    confirmed = false
}
else{
    confirmed = true
}
if(document.querySelector(".activeButtons")){
    activeButtons = document.querySelector(".activeButtons").textContent
}

var minLength = document.querySelector(".minLength").textContent
const maxLength = document.querySelector(".maxLength").textContent
const mainStr = "http://127.0.0.1:50/"
const buttonNext = document.querySelector(".next")
const buttonSend = document.querySelector(".send")
if(activeList.length > minLength){
    buttonNext.classList.toggle("active")
}
const buttonList = document.querySelectorAll(".variant")
const radioList = document.querySelectorAll("#radio")
if(confirmed){
    var i = 0
    var t = []
    radioList.forEach(function (element) {
        //console.log(element.value)
        if(activeButtons == "-1"){
            if(element.value == activeButtons){
                t.push(i)
            }
        }
        else{
            for(j=0;j<activeButtons.length; j++){
                if(element.value == activeButtons[j]){
                    t.push(i)
                }
            }
        }
        i+=1
    })
    t.forEach(function(tElement){
        buttonList[tElement].classList.toggle("active")
    })
    
}
if(confirmed){
    buttonSend.style.display = "block"
}
//radioList.forEach(function (element) {
//    console.dir(element)
//})
var radioIdList = []
const btnSubmit = document.querySelectorAll("#btnSubmit")
if(!document.querySelector("#myrange")){
    buttonList.forEach(function (element) {
        if(confirmed & !buttonNext.classList.contains("active")){
            buttonNext.classList.toggle("active")
        }
        element.addEventListener("click", function () {
            //for(i=0; i<radioList.length; i++){
            //    console.log(radioList[i].checked)
            //}
            
    
            if(!confirmed){
                if(activeList.indexOf(element) == -1){ //не нашел элемент в списке => добавляем
                    if(activeList.length >= maxLength){ // если место не осталось, удаляем что-нибудь
                        activeList[0].classList.toggle("active")
                        radioIdList.shift()
                        activeList.shift()
                    }
                    activeList.push(element)
                    element.classList.toggle("active")
                    for(i=0; i<buttonList.length; i++){
                        if(buttonList[i] == element){
                            radioIdList.push(i)
                        }
                    }
                    //console.log(buttonList.indexOf(element))
                    
                    
                }
                else{ // нашел => убираем
                    activeList.splice(activeList.indexOf(element), 1);
                    element.classList.toggle("active")
                    for(i=0; i<buttonList.length; i++){
                        if(buttonList[i] == element){
                            radioIdList.splice(radioIdList.indexOf(i), 1)
                        }
                    }
                }
        
                if(activeList.length > minLength & !buttonSend.classList.contains("active")){
                    buttonSend.classList.toggle("active")
                }
                if(activeList.length <= minLength & buttonSend.classList.contains("active")){
                    buttonSend.classList.toggle("active")
                }
            }
        })
    })
}
function myFunc(){
    if(!confirmed){
        confirmed = true
        buttonNext.classList.toggle("active")
        for(i=0; i<radioIdList.length; i++){
            radioList[radioIdList[i]].checked = true
        }
        return false
    }
}

//console.log(btnSubmit)
//btnSubmit.onmousedown = function(){
//    alert(9)
//    //document.location.href = document.querySelector(".link").textContent
//}
//hh = document.getElementById("enot")
//buttonSend.addEventListener("click", function(){
//    aleft(9)
//})
const container = document.querySelector(".container")
if(document.baseURI == mainStr + "testing" || document.baseURI.indexOf(mainStr + "q") != -1){
    if(!container.classList.contains("withBackground")){
        container.classList.toggle("withBackground")
    }
}

if(document.querySelector("#myrange")){
    document.querySelector("#myrange").value = activeButtons
    buttonSend.classList.toggle("active")
    buttonNext.classList.toggle("active")
    document.querySelector("#textRange").textContent=document.querySelector("#myrange").value + "%"
    document.querySelector("#myrange").addEventListener("mousemove", function(){
        document.querySelector("#textRange").textContent=document.querySelector("#myrange").value + "%"
    })
    document.querySelector("#myrange").addEventListener("click", function(){
        document.querySelector("#textRange").textContent=document.querySelector("#myrange").value + "%"
    })
}