const paragraphs = document.querySelectorAll('p');

const texts = [];

for (let i = 0; i < paragraphs.length; i++) {
  texts.push(paragraphs[i].textContent);
}

console.log(texts);
