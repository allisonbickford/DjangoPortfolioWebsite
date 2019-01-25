$(document).ready( function() {
	$('.project-image').on('click', '.project-detail', function () {
		$('.project-image-container').css("display", "block");
	});
	
	$('.next').on('click', '.project-detail', function() {
		
	});

	$('.prev').on('click', '.project-detail', function() {

	});

	$('.close').on('click', '.project-detail', function() {
		$('.project-image-container').css("display", "none");
	});
});

