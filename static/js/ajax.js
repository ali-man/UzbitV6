function ajaxQuery(_url, _method, _data) {
    $.ajax({
        url: _url,
        method: _method,
        data: _data,
        dataType: 'json',
        beforeSend: function () {
            console.log('Идёт загрузка');
        },
        success: function (data) {
            console.log(data);
            window.location.replace('/');
        }
    });
}