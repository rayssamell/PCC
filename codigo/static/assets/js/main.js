<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
(function($) {
  
  "use strict";  

  $(window).on('load', function() {

    /* 
   MixitUp
   ========================================================================== */
  $('#portfolio').mixItUp();

  /* 
   One Page Navigation & wow js
   ========================================================================== */
    var OnePNav = $('.onepage-nev');
    var top_offset = OnePNav.height() - -0;
    OnePNav.onePageNav({
      currentClass: 'active',
      scrollOffset: top_offset,
    });
  
  /*Page Loader active
    ========================================================*/
    $('#preloader').fadeOut();

  // Sticky Nav
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 200) {
            $('.scrolling-navbar').addClass('top-nav-collapse');
        } else {
            $('.scrolling-navbar').removeClass('top-nav-collapse');
        }
    });

    /* slicknav mobile menu active  */
    $('.mobile-menu').slicknav({
        prependTo: '.navbar-header',
        parentTag: 'liner',
        allowParentLinks: true,
        duplicate: true,
        label: '',
        closedSymbol: '<i class="icon-arrow-right"></i>',
        openedSymbol: '<i class="icon-arrow-down"></i>',
      });

      /* WOW Scroll Spy
    ========================================================*/
     var wow = new WOW({
      //disabled for mobile
        mobile: false
    });

    wow.init();

    /* Nivo Lightbox 
    ========================================================*/
    $('.lightbox').nivoLightbox({
        effect: 'fadeScale',
        keyboardNav: true,
      });

    /* Counter
    ========================================================*/
    $('.counterUp').counterUp({
     delay: 10,
     time: 1000
    });


    /* Back Top Link active
    ========================================================*/
      var offset = 200;
      var duration = 500;
      $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
          $('.back-to-top').fadeIn(400);
        } else {
          $('.back-to-top').fadeOut(400);
        }
      });

      $('.back-to-top').on('click',function(event) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: 0
        }, 600);
        return false;
      });



  });      

}(jQuery));


$(document).ready(function() {
    // Atualizar mensagem
    $('.btn-atualizar-mensagem').click(function() {
        var mensagemId = $(this).data('mensagem-id');
        var mensagemElement = $('.mensagem[data-mensagem-id="' + mensagemId + '"]');
        var novoConteudo = prompt('Digite o novo conteúdo da mensagem:');
        if (novoConteudo !== null) {
            $.ajax({
                url: '{% url "atualizar_mensagem" %}',
                type: 'POST',
                data: {
                    mensagem_id: mensagemId,
                    novo_conteudo: novoConteudo,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    if (response.success) {
                        // Atualizar o conteúdo da mensagem na página
                        mensagemElement.find('p').text(response.conteudo);
                    } else {
                        alert('Ocorreu um erro ao atualizar a mensagem.');
                    }
                },
                error: function() {
                    alert('Ocorreu um erro ao processar a solicitação.');
                }
            });
        }
    });

    // Excluir mensagem
    $('.btn-excluir-mensagem').click(function() {
        if (confirm('Deseja excluir esta mensagem?')) {
            var mensagemId = $(this).data('mensagem-id');
            var mensagemElement = $('.mensagem[data-mensagem-id="' + mensagemId + '"]');
            $.ajax({
                url: '{% url "excluir_mensagem" %}',
                type: 'POST',
                data: {
                    mensagem_id: mensagemId,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(response) {
                    if (response.success) {
                        // Remover a mensagem da página
                        mensagemElement.remove();
                    } else {
                        alert('Ocorreu um erro ao excluir a mensagem.');
                    }
                },
                error: function() {
                    alert('Ocorreu um erro ao processar a solicitação.');
                }
            });
        }
    });
});
