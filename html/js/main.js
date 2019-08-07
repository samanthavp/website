// TODO: since jQ is from cdn: no internet = stuck on loader :(
$(window).on("load",function(){
  // exit the loader
  $(".load-content").removeClass("hidden");
  $(".loader").addClass("hidden");
});
// document.addEventListener("DOMContentLoaded", function(e) { 
//   document.getElementsByClassName("load-content").classList.remove("hidden");
//   document.getElementsByClassName("loader").classList.add("hidden");
// });
