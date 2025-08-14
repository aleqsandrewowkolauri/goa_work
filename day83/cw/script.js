//davaleba1//
let numbers = [5, 10, 8, 12, 20, 7, 6];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];


  if (sum > 50) {
    break;
  }
}

console.log("ჯამი:", sum);


//davaleba2//
const filterLongStrings = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].length <= 5) {
      continue;
    }

    console.log(arr[i]);
  }
};

const myStrings = ["apple", "banana", "car", "elephant", "sky", "orange", "tree", "bottle", "cat", "computer"];

filterLongStrings(myStrings);

//davaleba3//
const printEvenNumbers = () => {
  let count = 0; 

  for (let i = 1; i <= 100; i++) { 
    if (i % 2 !== 0) {
      continue; // 
    }

    console.log(i); 
    count++;

    if (count === 5) {
      break; 
    }
  }
};

printEvenNumbers();



