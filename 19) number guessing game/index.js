const min = 1;
const max = 100;

const ans = Math.floor(Math.random()*(max-min+1));
console.log(ans);

let attempts = 0;
let guess;
let running = true;

while(running){
    guess = window.prompt(`guess a number between ${min} and ${max}`)
    guess = Number(guess);
    if(isNaN(guess)){
        window.alert(`pls enter a valid number`)
    }
    else if(guess<min || guess>max){
        window.alert(`pls enter a valid number`)
    }
    else{
        attempts++;
        if (guess<ans){
            window.alert(`too low`)
        }
        else if(guess>ans){
            window.alert(`too high`)
        }
        else{
            window.alert(`correct! it took u ${attempts} attempts`)
            running = false;
        }
    }
}