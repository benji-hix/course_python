$("a").hover(
    function () {
      $(this).addClass("mouseover-text");
    },
    function () {
      $(this).removeClass("mouseover-text");
    });
  
  $(".button").hover(function (){
      $(this).addClass("mouseover-button");
  },
  function () {
      $(this).removeClass("mouseover-button");
  });