$(function () {

    var url= window.location.href;

    var id = url.split('=')[1];

    $.getJSON('/api/students/', + id+ '/', function (data) {
        console.log(data);
        $('#student_name').html(data['name']);

        $('#student_age').html(data['age']);

    })
})