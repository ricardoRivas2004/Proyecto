document.addEventListener("DOMContentLoaded", function() {
    var books = document.querySelectorAll(".book");
    books.forEach(function(book, index) {
        setTimeout(function() {
            book.classList.add("visible");
        }, index * 300);  // delay de las imagenes de las portadas :)
    });
});