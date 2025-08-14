const logPositiveNumbers = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      console.log(arr[i]);
    }
  }
};

// Example usage:
const numbers = [-3, 7, 0, -1, 5, 12, -9];
logPositiveNumbers(numbers);
