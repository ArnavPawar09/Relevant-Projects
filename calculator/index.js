const output = document.getElementById("screen");
const one = document.getElementById("one");
const two = document.getElementById("two");
const three = document.getElementById("three");
const four = document.getElementById("four");
const five = document.getElementById("five");
const six = document.getElementById("six");
const seven = document.getElementById("seven");
const eight = document.getElementById("eight");
const nine = document.getElementById("nine");
const zero = document.getElementById("zero");
const plus = document.getElementById("plus");
const minus = document.getElementById("minus");
const divide = document.getElementById("divide");
const multiply = document.getElementById("multiply");
const c = document.getElementById("c");
const equal = document.getElementById("equal");


output.textContent = "";
one.onclick = function(){
    output.textContent = output.textContent+"1"
}
two.onclick = function(){
    output.textContent = output.textContent+"2"
}
three.onclick = function(){
    output.textContent = output.textContent+"3"
}
four.onclick = function(){
    output.textContent = output.textContent+"4"
}
five.onclick = function(){
    output.textContent = output.textContent+"5"
}
six.onclick = function(){
    output.textContent = output.textContent+"6"
}
seven.onclick = function(){
    output.textContent = output.textContent+"7"
}
eight.onclick = function(){
    output.textContent = output.textContent+"8"
}
nine.onclick = function(){
    output.textContent = output.textContent+"9"
}
zero.onclick = function(){
    output.textContent = output.textContent+"0"
}

plus.onclick = function(){
    output.textContent = output.textContent+" + "
}
minus.onclick = function(){
    output.textContent = output.textContent+" - "
}
divide.onclick = function(){
    output.textContent = output.textContent+" / "
}
multiply.onclick = function(){
    output.textContent = output.textContent+" x "
}
c.onclick = function(){
    output.textContent = ""
}

let a = "";
equal.onclick = function(){
    out = output.textContent.replace("x", "*");
    a = eval(out);
    output.textContent = a;
}

