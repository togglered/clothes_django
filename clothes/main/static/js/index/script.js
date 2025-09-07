const SLIDES = document.querySelectorAll('.slide');
const MINI_SLIDES = document.querySelectorAll('.slide-mini');
const SLIDESHOW = document.querySelector('.slideshow');
let index = 0;

function showSlide(i) {
  SLIDES.forEach(slide => slide.classList.remove('slide-active'));
  SLIDES[i].classList.add('slide-active');
}

function nextSlide() {
  index = (index + 1) % SLIDES.length;
  showSlide(index);
}

showSlide(index);

let interval_id = setInterval(nextSlide, 3000);

MINI_SLIDES.forEach((mini_slide, i) => {
    mini_slide.addEventListener('click', () => {
        clearInterval(interval_id);
        SLIDES.forEach(slide => slide.classList.remove('slide-active'));
        SLIDES[i].classList.add('slide-active');
        index = i;
        interval_id = setInterval(nextSlide, 3000);
    });
});

SLIDES.forEach(slide => {
  slide.addEventListener('click', () => {
    window.location = slide.dataset.link
  })
});