$(document).ready(function () {

    let loginLink = $('#sign-in');
    let logoutLink = $('#logout');
    // let loginSubmit = $('#login-submit');
    let csrf = $("input[name=csrfmiddlewaretoken]").val();

    loginLink.on("click", function () {
        $("#sign-in_display").toggleClass("d-none");
    });

    // loginSubmit.click(function () {
    //    let username = $("#login_username").val();
    //    let password = $("#login_password").val();
    //    let url = '/ajax/login/';
    //    let method = 'GET';
    //    let data = {
    //        csrfmiddlewaretoken: csrf,
    //        username: username,
    //        password: password
    //    };
    //    ajaxQuery(url, method, data);
    //    console.log(username);
    //    console.log(password);
    // });
    //
    // logoutLink.on("click", function () {
    //     let
    //         url = '/ajax/logout/',
    //         method = 'GET',
    //         data = {
    //             csrfmiddlewaretoken: csrf
    //         };
    //     let result = ajaxQuery(url, method, data);
    //
    //     console.log(result.ajax.success());
    //     // else if (result.error) console.log(result);
    // })

});