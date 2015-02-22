$(document).ready(function() {
  $('.block').waypoint(function() {
    $('header.share-header').toggleClass('active');
  });
});
