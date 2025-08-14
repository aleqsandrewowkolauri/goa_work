function printArguments() {
  for (let i = 0; i < arguments.length; i++) {
    console.log(arguments[i]);
  }
}
 
printArguments("apple", 42, true, "banana");
