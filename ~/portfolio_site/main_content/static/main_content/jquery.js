console.log("you found me!");
        $(document).ready(function() {
                alert("JQuery is active!");
                var banner = jQuery('#banner');
                banner.bind('click', function() {
                        alert("Hello!");
                        $(".project-preview").html("<h2>You clicked this!</h2>");
                });
        });


