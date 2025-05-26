// ობიექტის შექმნა
const student = {
  name: "ნიკო",
  surname: "კვარაცხელია",
  academy: "GOA",
  city: "თბილისი",
  role: "მოსწავლე",
  favColor: "ლურჯი",

  // მეთოდი, რომელიც გამოიტანს სახელს და გვარს
  fullName: function() {
    console.log(this.name + " " + this.surname);
  },

  // მეთოდი, რომელიც გამოიტანს საყვარელ ფერს
  printFavColor: function() {
    console.log(this.favColor);
  }
};

// 1. კონსოლში დაბეჭდეთ მთლიანი ობიექტი
console.log(student);

// 2. კონსოლში დაბეჭდეთ ნებისმიერი კუთვნილება ობიექტის
console.log(student.city);

// 3. გამოიძახეთ ობიექტის რომელიმე მეთოდი
student.fullName();
student.printFavColor();

// 4. შეცვალეთ ობიექტის რომელიმე მნიშვნელობა და შემდეგ დაბეჭდეთ
student.favColor = "მწვანე";
console.log(student.favColor);
