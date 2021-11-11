let menu = document.querySelector('#menu-btn');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
}


var loader1 = (e) => {
    let file = e.target.files;
    let show = "<b><span>Selected file : </span>" + file[0].name + "</b>";

    let output = document.getElementById("selector1");
    output.innerHTML = show;
    output.classList.add("active");
    submitButton.disabled = false;
};

var loader2 = (e) => {
    let file = e.target.files;
    let show = "<b><span>Selected file : </span>" + file[0].name + "</b>";

    let output = document.getElementById("selector2");
    output.innerHTML = show;
    output.classList.add("active");
    submitButton.disabled = false;
};

var loader3 = (e) => {
    let file = e.target.files;
    let show = "<b><span>Selected file : </span>" + file[0].name + "</b>";

    let output = document.getElementById("selector3");
    output.innerHTML = show;
    output.classList.add("active");
    submitButton.disabled = false;
};

var loader4 = (e) => {
    let file = e.target.files;
    let show = "<b><span>Selected file : </span>" + file[0].name + "</b>";

    let output = document.getElementById("selector4");
    output.innerHTML = show;
    output.classList.add("active");
    submitButton.disabled = false;
};
var loader5 = (e) => {
    let file = e.target.files;
    let show = "<b><span>Selected file : </span>" + file[0].name + "</b>";

    let output = document.getElementById("selector5");
    output.innerHTML = show;
    output.classList.add("active");
    submitButton.disabled = false;
};
var loader6 = (e) => {
    let file = e.target.files;
    let show = "<b><span>Selected file : </span>" + file[0].name + "</b>";

    let output = document.getElementById("selector6");
    output.innerHTML = show;
    output.classList.add("active");
    submitButton.disabled = false;
};

//Event listener for input
const submitButton = document.getElementById("btn1");
let fileinput1 = document.getElementById("file1");
let fileinput2 = document.getElementById("file2");
let fileinput3 = document.getElementById("file3");
let fileinput4 = document.getElementById("file4");
let fileinput5 = document.getElementById("file5");
let fileinput6 = document.getElementById("file6");
fileinput1.addEventListener("change",loader1);
fileinput2.addEventListener("change",loader2);
fileinput3.addEventListener("change",loader3);
fileinput4.addEventListener("change",loader4);
fileinput5.addEventListener("change",loader5);
fileinput6.addEventListener("change",loader6);
