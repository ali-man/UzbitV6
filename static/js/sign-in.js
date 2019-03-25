$(document).ready(function () {

    let
        loginBtn = $('#login'),
        logoutBtn = $('#logout'),
        csrf = $("input[name=csrfmiddlewaretoken]").val();

    logoutBtn.on("click", function () {
        let
            url = '/ajax/logout/',
            method = 'GET',
            data = {
                csrfmiddlewaretoken: csrf
            };
        let result = ajaxQuery(url, method, data);

        console.log(result.ajax.success());
        // else if (result.error) console.log(result);
    })

});