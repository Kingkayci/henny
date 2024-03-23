window.addEventListener('scroll', function() {
    if (this.window.scrollY > 30) {
        this.document.querySelector('#main-header').style.opacity = 0;
    } else {
        this.document.querySelector('#main-header').style.opacity = 1;
    }
});


window.addEventListener('scroll', function() {
    if (this.window.scrollY > 30) {
        this.document.querySelector('#navbar-header').style.opacity = 0.98;
    } else {
        this.document.querySelector('#navbar-header').style.opacity = 1;
    }
});


window.addEventListener('scroll', function() {
    if (this.window.scrollY > 30) {
        this.document.querySelector('.dashboard-navbar').style.opacity = 0.98;
    } else {
        this.document.querySelector('.dashboard-navbar').style.opacity = 1;
    }
});


