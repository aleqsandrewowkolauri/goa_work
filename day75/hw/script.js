let count = 1;

const intervalId = setInterval(() => {
  console.log(count);
  count++;

  // Stop when count goes past 5
  if (count > 5) {
    clearInterval(intervalId);
  }
}, 1000); // 1000 milliseconds = 1 second
