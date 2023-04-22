// wait until the document is loaded and ready
$(document).ready(function () {

    // set the initial desktop to be shown as the first desktop
    let currentDesktop = $("#desktop1");
    // show the initial desktop
    currentDesktop.show();

    $(".desktop").click(function () {
        const windowHeight = $(window).height();  // the height of the current window
        // animate the current desktop to slide down to the bottom of the window
        currentDesktop.animate({  // set the top position of the desktop to the height of the window
            top: windowHeight,    // set the top position of the desktop to the height of the window
            opacity: 0            // set the opacity to 0, progressively making the disappearing desktop transparent
        }, 1000, function () {    // duration of the animation is 1 sec
            // when the animation is complete, move the current desktop out of the view and reset its position and opacity
            currentDesktop.css({top: "-100%", opacity: 1});
            // get the next desktop
            var nextDesktop = currentDesktop.next(".desktop");
            // if there is no next desktop, set it to be the first desktop
            if (nextDesktop.length === 0) {
                nextDesktop = $(".desktop").first();
            }
            // move the next desktop to the top of the window and set its opacity to 0, making it transparent
            nextDesktop.css({top: -windowHeight, opacity: 0});
            // show the next desktop
            nextDesktop.show();
            // animate the desktop to slide in from the top of the window and fade in
            nextDesktop.animate({top: "0%", opacity: 1}, 1000);
            // set the next desktop as the new current desktop
            currentDesktop = nextDesktop;
        });
    });
});
