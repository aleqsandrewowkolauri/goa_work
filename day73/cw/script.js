window.onload = function modifyContent() {
  const div = document.getElementById("myDiv");
  const button = document.getElementById("myButton");
  const paragraph = document.getElementById("myParagraph");

  if (button) {
    div.removeChild(button);
  }

  if (paragraph) {
    const italic = document.createElement("i");
    italic.textContent = "ეს არის შეცვლილი ტექსტი i თეგში";
    div.replaceChild(italic, paragraph);
  }
};
