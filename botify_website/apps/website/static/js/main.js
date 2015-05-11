$(document).ready(function() {

    /* ======= Twitter Bootstrap hover dropdown ======= */
    /* Ref: https://github.com/CWSpear/bootstrap-hover-dropdown */
    /* apply dropdownHover to all elements with the data-hover="dropdown" attribute */

    $('[data-hover="dropdown"]').dropdownHover();

    /* ======= Fixed header when scrolled ======= */
    $(window).bind('scroll load', function() {
         if ($(window).scrollTop() > 40) {
             $('#header').addClass('navbar-fixed-top');
             //$('body').addClass('body-navbar-fixed');
             //$('body').css('padding-top', '80px');
         }
         else {
             $('#header').removeClass('navbar-fixed-top');
             //$('body').removeClass('body-navbar-fixed');
             //$('body').css('padding-top', '0px');
         }
    });

    /* ======= jQuery Placeholder ======= */
    /* Ref: https://github.com/mathiasbynens/jquery-placeholder */

    $('input, textarea').placeholder();

    /* ======= jQuery FitVids - Responsive Video ======= */
    /* Ref: https://github.com/davatron5000/FitVids.js/blob/master/README.md */

    $(".video-container").fitVids();

    /* ======= FAQ accordion ======= */
    function toggleIcon(e) {
    $(e.target)
        .prev('.panel-heading')
        .find('.panel-title a')
        .toggleClass('active')
        .find("i.fa")
        .toggleClass('fa-plus-square fa-minus-square');
    }
    $('.panel').on('hidden.bs.collapse', toggleIcon);
    $('.panel').on('shown.bs.collapse', toggleIcon);


    /* ======= Header Background Slideshow - Flexslider ======= */
    /* Ref: https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties */

    $('.bg-slider').flexslider({
        animation: "fade",
        directionNav: false, //remove the default direction-nav - https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties
        controlNav: false, //remove the default control-nav
        slideshowSpeed: 8000
    });

	/* ======= Stop Video Playing When Close the Modal Window ====== */
    $("#modal-video .close").on("click", function() {
        $("#modal-video iframe").attr("src", $("#modal-video iframe").attr("src"));
    });


     /* ======= Testimonial Bootstrap Carousel ======= */
     /* Ref: http://getbootstrap.com/javascript/#carousel */
    $('#testimonials-carousel').carousel({
      interval: 8000
    });


    /* ======= Scroll Inviter ======= */
    $("#invite-scroll").click(function() {
        $('html, body').animate({
            scrollTop: $("#begin-content").offset().top + 1
        }, 500);
    });

    /* ======= Contact Forms ======= */
    function cleanContactForm(){
        // remove error messages
        $("form.contact .controls p").remove();

        // remove error class
        $("form.contact .control-group").removeClass('error');
    }

    // Contact Form
    function setFieldError(field, message){
        // search field by name
        var input = $('input[name="' + field + '"], textarea[name="' + field + '"]');

        // add error message
        input.parent().append('<p class="help-block"><strong class="text-danger">' + message + '</strong></p>');

        // add error class
        input.parents('.control-group').addClass('error');
    }

    $("form.contact").on('submit', function(e){
        e.preventDefault();
        var form = $(this);
        var data = form.serialize();
        $.ajax({
            url: form.attr('action'),
            data: data,
            type: "POST",
            statusCode: {
                400: function(xhr) {
                    var errors = $.parseJSON(xhr.responseText);

                    cleanContactForm();

                    // show errors
                    $.each( errors, function(field, message) {
                        setFieldError(field, message);
                    });
                }
            }
        }).done(function(data){
            form.remove();
            $('#success-message').removeClass("hide");
        });
    });
});