$(document).ready(function () {
    const pathname = window.location.pathname;
    if (pathname === "/" || pathname === "/index") {
      initIndexPage();
      btnAnimation();
    } else if (pathname === "/company") {
      initCompanyPage();
    } else if (pathname === "/agreements") {
      initAgreementsPage();
    } else if (pathname === "/employee") {
      initEmployeePage();
    } else if (pathname === "/login"){
      initLoginPage();
    }
  });

function btnAnimation(){ 
  $('#newpagebtn').click(function () {
    $(this).animate({
      width: '+=20px',
      height: '+=10px',
      opacity: 0.7
    }, 600, function () {
      window.open('https://www.amc.com/shows/better-call-saul-employee-training--1002212', '_blank');
    });

    $(this).animate({
      width: '-=20px',
      height: '-=10px',
      opacity: 1
    }, 600);
  });
}
  
function initSlider(images, texts) {
    if (!images.length) return;
  
    let current = 0;
    let userInteracted = false;
    const sliderImage = $('#sliderImage');
    const sliderText = $('#sliderText');
    const prevButton = $('#prevSlide');
    const nextButton = $('#nextSlide');
  
    function showSlide(index) {
      sliderImage.fadeOut(500, function () {
        sliderImage.attr('src', images[index]).fadeIn(500);
      });
      sliderText.fadeOut(500, function () {
        sliderText.text(texts[index]).fadeIn(500);
      });
    }
  
    sliderImage.attr('src', images[current]);
    sliderText.text(texts[current]);
  
    prevButton.on('click', function () {
      userInteracted = true;
      current = (current - 1 + images.length) % images.length;
      showSlide(current);
    });
  
    nextButton.on('click', function () {
      userInteracted = true;
      current = (current + 1) % images.length;
      showSlide(current);
    });
  
    setInterval(function () {
      if (!userInteracted) {
        current = (current + 1) % images.length;
        showSlide(current);
      } else {
        userInteracted = false;
      }
    }, 5000);
}

function initIndexPage() {
    initSlider(
      ['static/IMG/slide1.jpg', 'static/IMG/slide2.jpg', 'static/IMG/slide3.jpg'],
      [
        'Наша компанія співпрацює десятки років з успішними компаніями.',
        'Ми пропонуємо інноваційні рішення для бізнесу.',
        'Довіряйте професіоналам з багаторічним досвідом.'
      ]
    );
}

function initEmployeePage() {
    initCounter();
}  

function initCounter() {
      animateCounter('#contracts', 0, 150, 2000);
      animateCounter('#employees', 0, 30, 2000);
      animateCounter('#salary', 0, 105000, 2000);
}
  
function animateCounter(element, start, end, duration) {
    $({ count: start }).animate({ count: end }, {
      duration: duration,
      easing: 'swing',
      step: function () {
        $(element).text(Math.floor(this.count));
      }
    });
}

function initLoginPage() {
    const logo = $('#login-logo');
    
    function pulseLogo() {
        const logo = $('header img');
    
        logo.css('transition', 'transform 0.5s ease, opacity 0.5s ease');
        logo.css('transform', 'scale(1.1) rotate(15deg)');
        logo.css('opacity', '0.8');
    
        setTimeout(() => {
            logo.css('transform', 'scale(1) rotate(0deg)');
            logo.css('opacity', '1');
        }, 500);
    }
    
    let pulseInterval = setInterval(pulseLogo, 2000);
    
    setTimeout(() => clearInterval(pulseInterval), 10000);
}

function initAgreementsPage(){
    initReviewSlider();
}

function initCompanyPage() {
    initSlider(
      ['static/IMG/slide4.jpg', 'static/IMG/slide5.jpg', 'static/IMG/slide6.jpg'],
      [
        'Наша команда — найцінніший актив компанії.',
        'Ми цінуємо кожного співробітника.',
        'Розвиток персоналу — наш пріоритет.'
      ]
    );
  }

function initReviewSlider() {
    const reviews = [
      {
        text: '"Співпраця була на найвищому рівні! Швидко, чітко, професійно."',
        author: 'ТОВ "БудПроект"'
      },
      {
        text: '"Надійна система обліку, допомогла нам оптимізувати документообіг."',
        author: 'ПП "Енергосвіт"'
      },
      {
        text: '"Сервіс на високому рівні, підтримка завжди на зв\'язку."',
        author: 'ТОВ "Інтехбуд"'
      }
    ];
  
    let currentReview = 0;
    const reviewText = $('#reviewText');
    const reviewAuthor = $('#reviewAuthor');
  
    function showReview(index) {
      reviewText.fadeOut(300, () => {
        reviewText.text(reviews[index].text).fadeIn(300);
      });
      reviewAuthor.fadeOut(300, () => {
        reviewAuthor.text(reviews[index].author).fadeIn(300);
      });
    }
  
    showReview(currentReview);
  
    $('#prevReview').on('click', function () {
      currentReview = (currentReview - 1 + reviews.length) % reviews.length;
      showReview(currentReview);
    });
  
    $('#nextReview').on('click', function () {
      currentReview = (currentReview + 1) % reviews.length;
      showReview(currentReview);
    });
  
    setInterval(() => {
      currentReview = (currentReview + 1) % reviews.length;
      showReview(currentReview);
    }, 7000);
  }      