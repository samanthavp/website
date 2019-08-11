// TODO: since jQ is from cdn: no internet = stuck on loader :(
$(window).on("load",function(){
  // exit the loader
  $(".load-content").removeClass("hidden");
  $(".loader").addClass("hidden");
});

var qregex = /[\?&]q=([^&]+)/g;
var matches = qregex.exec(window.location.search);
if (matches && matches[1]) {
  var q = decodeURIComponent(matches[1].replace(/\+/g, "%20"));
  $.getJSON("search/episodes.json").then(function(episodes) {
    options = {
      keys: ["no","title","notes","authors","links"],
      id: "no",
      location: null,
      tokenize: true,
      matchAllTokens: true,
      distance: 5,
      shouldSort: true,
      threshold: 0.1,
    }
    var fuse = new Fuse(episodes, options)
    var ids = fuse.search(q)
    $(".tile-episode").each(function() {
      if (ids.includes($(this).attr("id")) === false) {
        $(this).hide();
      }
    })
    var searchbar = $("#searchbar")
    searchbar.addClass("show")
    searchbar.find("input").val(q)
  });
}
