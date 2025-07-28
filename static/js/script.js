document.addEventListener('DOMContentLoaded', function () {
    const burger = document.getElementById('burger');
    const navLinks = document.getElementById('nav-links');
    const slides = document.querySelectorAll('.slide');
    const mybutton = document.getElementById("backToTop");

    // Animation burger
    burger.addEventListener('click', function () {
        navLinks.classList.toggle('active');
        burger.classList.toggle('active');
    });

    // Carousel automatique
    let currentSlide = 0;
    function showNextSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }
    setInterval(showNextSlide, 4000);

    // Back to top button
    window.addEventListener('scroll', function () {
        if (window.scrollY > 200) {
            mybutton.style.display = "block";
        } else {
            mybutton.style.display = "none";
        }
    });

    // Smooth scroll top
    mybutton.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Scroll Reveal Anim
    ScrollReveal().reveal('.gallery-item', {
        distance: '50px',
        duration: 1000,
        easing: 'ease-in-out',
        origin: 'bottom',
        interval: 200
    });
});

// Effet fade-in au scroll
const faders = document.querySelectorAll('.fade-in');
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
});
faders.forEach(el => observer.observe(el));

// Popup image
document.querySelectorAll('.gallery-item img').forEach(img => {
    img.style.cursor = 'pointer';
    img.addEventListener('click', () => {
        const popup = document.createElement('div');
        popup.className = 'popup-overlay';
        popup.style.display = 'flex';
        const fullImg = document.createElement('img');
        fullImg.src = img.src;
        popup.appendChild(fullImg);
        document.body.appendChild(popup);
        popup.addEventListener('click', () => popup.remove());
    });
});
