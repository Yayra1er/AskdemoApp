
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}


// Script for carousel
var carouselIndex = 0;
showCarousel();

function showCarousel() {
  var i;
  var slides = document.getElementsByClassName("carousel-item");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  carouselIndex++;
  if (carouselIndex > slides.length) {carouselIndex = 1}
  slides[carouselIndex-1].style.display = "block";
  setTimeout(showCarousel, 5000); // Change image every 5 seconds
}
