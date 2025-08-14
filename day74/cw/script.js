const paragraph = document.getElementById("myParagraph");

paragraph.onmouseover = function() {
  paragraph.style.textAlign = "center";
};


 
const button = document.getElementById("myButton");

button.addEventListener("click", function(event) {
  
  console.log(event);

  document.body.style.backgroundColor = "black";

  document.body.style.color = "white";
});



const link = document.getElementById("myLink");

link.addEventListener("pointerover", function(e) {
  const target = e.target;

  for (let attr of target.attributes) {
    console.log(`${attr.name} = ${attr.value}`);
  }

  console.log("Target ელემენტი:", target);
});

