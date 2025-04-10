
let randomNum1 = Math.floor(Math.random()*6) + 1; //random number b/w 1-6. 
//Math.random() -> random num b/w [0-1)
console.log(`b/w 1 and 6 =`, randomNum1);

const min1=50;
const max1=100;
let randomNum2 = Math.floor(Math.random()*(max1 - min1)) + min1; //b/w 50 and 100
console.log(`b/w 50 and 100 =`, randomNum2);
console.log(``);

const mybtn = document.getElementById("mybtn");
const mylbl = document.getElementById("mylbl");
const min = 1;
const max = 6;
let randn;
mybtn.onclick = function(){
    randn = Math.floor(Math.random()*max)+min;
    mylbl.textContent = randn;
}


