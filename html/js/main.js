
$(document).ready(function(){
  // setup the spotlight
  var spotcon = $(".spotlight-container");
  var spotlight = $("#spotlight");
  $(".profile-img").click(function(){
    spotlight.html($("#"+this.id+"-details").html());
    spotcon.removeClass("hidden");
  });
  spotcon.find(".close").click(function(){spotcon.addClass("hidden");});
  $(document).keyup(function(e){if (e.key === "Escape") {spotcon.addClass("hidden");}});
});
$(window).on("load",function(){
  // exit the loader
  $(".load-content").removeClass("hidden");
  $(".loader").addClass("hidden");
});
