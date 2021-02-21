$(document).ready(function() {
  
  $('body').on('click', '.overlayButton', function(e) {
	  var id = $(e.target).attr('id');
	  var overlayID = '#m' + id;
	  console.log(overlayID);
	  $('#overlayToggle').fadeIn();
	  $(overlayID).fadeIn();
  });
  
  $('body').on('click', '.closeOverlayButton', function(e1) {
	  var id = $(e1.target).attr('id');
	  var overlayID = '#m' + id.substring(1);
	  console.log(overlayID);
	  $('#overlayToggle').fadeOut();
	  $(overlayID).fadeOut();
  });
  
});
