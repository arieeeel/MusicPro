
$(document).ready(function() {
   $(".toggle").on('click','this',function() {
      var elem = $this.text();
      if (elem == "Más Información") {

         $(".toggle").text("Ocultar");
         $(".text-game").slideDown();
         
      } else {

         $(".toggle").text("Más Información");
         $(".text-game").slideUp();
      }
   });
});
