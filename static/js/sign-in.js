$(document).ready(function () {

    let loginLink = $('#sign-in');
    let registerLink = $('#register');
    let csrf = $("input[name=csrfmiddlewaretoken]").val();

    loginLink.on("click", function () {
        let singInDisplay = $("#sign-in_display");
        let registerDisplay = $("#register_display");
        if (registerDisplay.hasClass("d-none") !== true)
            registerDisplay.toggleClass("d-none");
        singInDisplay.toggleClass("d-none");
    });

    registerLink.on("click", function () {
        let registerDisplay = $("#register_display");
        let singInDisplay = $("#sign-in_display");
        if (singInDisplay.hasClass("d-none") !== true)
            singInDisplay.toggleClass("d-none");
        registerDisplay.toggleClass("d-none");
    });

    let $message = $('.messages');
    if ($message[0] !== undefined){
        setTimeout(function () {
            $message.stop().animate({
                opacity: 0,
            }, 800, function () {
                $(this).remove();
            })
        }, 8000);

        $message.children('li').click(function () {
            $(this).stop().animate({
                opacity: 0,
            }, 800, function () {
                $(this).remove();
            })
        })
    }

});