//davaleba
function printEvenNumbers(...numbers) {
  for (let num of numbers) {
    
    if (num % 2 === 0) {
      console.log(num);
    }
  }
}
printEvenNumbers(3, 8, 11, 20, 7, 4, 9, 2, 14, 13);


//davaleba2
const sayHelloFunc = function() {
  console.log("hello");
};

const sayHelloArrow = () => {
  console.log("hello");
};

sayHelloFunc();
sayHelloArrow();

//davaleba3
console.log(
  (function() {
    return "Hello from IIFE!";
  })()
);

//davaleba4
let globalVar = "I'm global";

function showGlobal() {
  console.log(globalVar);
}

showGlobal(); 
