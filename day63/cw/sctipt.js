function greet() {
    const paragraph = document.getElementById("greeting");
    paragraph.textContent = "welcome გიორგი!"; // შეცვალე "გიორგი" შენი სახელით
}

// პარაგრაფზე event listener-ის დამატება
document.addEventListener("DOMContentLoaded", function () {
    const paragraph = document.getElementById("greeting");
    paragraph.addEventListener("click", greet);
});