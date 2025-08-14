let total = 0;

do {
  let input = prompt("Enter a number:");
  let number = Number(input);
  
  if (!isNaN(number)) {
    total += number;
  } else {
    alert("Please enter a valid number!");
  }

} while (total <= 100);

alert("Total exceeded 100! Final total: " + total);
