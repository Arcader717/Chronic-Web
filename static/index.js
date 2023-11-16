window.addEventListener('scroll', function () {
    if (window.scrollY > 250) {
        document.getElementById('about').style.opacity = 1;
    } else {
        document.getElementById('about').style.opacity = 0;
    };
});