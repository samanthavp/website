// TODO: since jQ is from cdn: no internet = stuck on loader :(
// $(document).ready(function(){
//   setup the profile-popup
//   var modal = $("#modal-content");
//   $(".modal-button").click(function(){
//     modal.html($("#"+this.id+"-details").html());
//   });
//   var popupcon = $(".profile-popup-container");
//   var popup    = $("#profile-popup");
//   $(".profile-img").click(function(){
//     popup.html($("#"+this.id+"-details").html());
//     popupcon.removeClass("hidden");
//   });
//   popupcon.find(".close").click(function(){popupcon.addClass("hidden");});
//   $(document).keyup(function(e){if (e.key === "Escape") {popupcon.addClass("hidden");}});
// });
$(window).on("load",function(){
  // exit the loader
  $(".load-content").removeClass("hidden");
  $(".loader").addClass("hidden");
});
