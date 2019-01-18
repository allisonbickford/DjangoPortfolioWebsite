$(document).ready(function () {
	//in the preview-menu-container, we perform this function during a click event
	//on a .preview-option item
	$('#preview-menu-container').on('click','.preview-option', function() {
		//change the html of project preview to data attributes from preview-option
		$(this).addClass(".selected-preview-option");
		$(".project-preview").html("<h2>"+$(this).data('title')+"</h2><p>"+$(this).data('text')+"</p>");
	});
});

