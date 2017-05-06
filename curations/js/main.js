$(document).ready(function(){

    var app = new Vue({
        el: '#app',
        data: data["1"]
    });
    var owl = $(".owl-carousel").owlCarousel({
        items:1,
        loop:false,
        center:true,
        margin:10,
        URLhashListener:true,
        startPosition: 'URLHash',
        nav: true,
        dots: true,
        autoHeight:true,
        navContainer: ".carousel-nav",
        dotsContainer: ".carousel-dots"
    });
    // embedly('on', 'card.rendered', function(iframe){
    //     owl.trigger('refresh.owl.carousel');
    // });
});
