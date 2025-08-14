let isHello = true;

const intervalId = setInterval(() => {
  document.title = isHello ? "Hello" : "Goodbye";
  isHello = !isHello;
}, 1000);

// Stop after 6 seconds
setTimeout(() => {
  clearInterval(intervalId);
}, 6000);
