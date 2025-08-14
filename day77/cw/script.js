let myList = [1, 2, 3, 4, 5];

// ინტერვალის გარეთ ვცვლით ყველა ელემენტის მნიშვნელობას
for (let i = 0; i < myList.length; i++) {
  myList[i] = myList[i] * 2; // გავაორმაგეთ ყველა
}

// for loop და ინტერვალი – ყოველი ელემენტი ყოველ 1 წამში გამოჩნდება
let index = 0;
let intervalId = setInterval(() => {
  if (index < myList.length) {
    console.log(myList[index]);
    index++;
  } else {
    clearInterval(intervalId); // რომ გავაჩეროთ როცა ყველა დაიბეჭდება
  }
}, 1000);
