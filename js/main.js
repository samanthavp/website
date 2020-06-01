$(window).on("load",function(){
  // exit the loader
  $(".load-content").removeClass("hidden");
  $(".loader").addClass("hidden");
});

// search
var qregex = /[\?&]q=([^&]+)/g;
var matches = qregex.exec(window.location.search);
if (matches && matches[1]) {
  // extract the search query
  var q = decodeURIComponent(matches[1].replace(/\+/g, "%20"));
  // load the searchable content (episodes)
  $.getJSON("search/episodes.json").then(function(episodes) {
    // fuse search options
    options = {
      keys: ["no","title","notes","authors","links"],
      id: "no",
      location: null,
      tokenize: true,
      matchAllTokens: true,
      distance: 5,
      shouldSort: true,
      threshold: 0.1,
    };
    // do the search
    var fuse = new Fuse(episodes, options);
    var ids = fuse.search(q);
    // hide episodes which don't match
    $(".tile-episode").each(function() {
      if (ids.includes($(this).attr("id")) === false) {
        $(this).hide();
      }
    });
    // if no matches: show #no-search-results
    if (ids.length == 0) {
      $("#no-search-results").show();
    } else {
      $("#no-search-results").hide();
    }
    // add back the searchbar with the query
    $(".section-header").hide();
    var searchbar = $("#searchbar");
    searchbar.addClass("show");
    searchbar.find("input").val(q);
  });
}
