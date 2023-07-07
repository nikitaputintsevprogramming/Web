$(document).ready(function(){
    $('.multiple-items').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        arrows: false,
        dots: true,
        dotsClass: 'dots-style',
        responsive: [{
           breakpoint: 1025,
           settings: {
              slidesToShow: 2,
              slidesToScroll: 2,
           }
        }, {
           breakpoint: 688,
           settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
           }
        }]
     });
});