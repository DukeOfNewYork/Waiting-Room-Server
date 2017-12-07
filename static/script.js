$('#Save').click(function () {
    user = $('#user').val();
    state = $('#state').val();
    console.log(user + " " + state);
    $.ajax({
        type: "POST",
        ContentType: 'application/json',
        url: "http://127.0.0.1:8000/app/administration",
        data: JSON.stringify({computer: user, state: state}),
        dataType: "json",
        success: function (data) {
            var parsed = (JSON.parse(data));
            var status = parsed[0].fields.status;
            console.log(status);
        },
        failure:
            function (err) {
                console.log(err);
            }
    });
});