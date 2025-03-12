const images = [
    "./images/img1.jpg",
    "./images/img2.jpg",
    "./images/img3.jpg",
    "./images/img4.jpg",
    "./images/img5.jpg"
];

let currentImageIndex = 0;
const background = document.querySelector(".background");

function changeBackground() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    background.style.backgroundImage = `url(${images[currentImageIndex]})`;
}

setInterval(changeBackground, 10000);
background.style.backgroundImage = `url(${images[currentImageIndex]})`;
