function setCurrentTime() {
    let now = new Date(new Date().toLocaleString("en-US",{timeZone: 'Asia/Dhaka'}));
    let time_text = now.toLocaleTimeString('en-US', {hour: 'numeric', minute: 'numeric'});
    let date_text = now.toLocaleDateString('en-US', {year: 'numeric', month: 'long', day: 'numeric'});
    $('#current-time-text').text(time_text);
    $('#current-date-text').text(date_text);
    let current_hour = now.getHours();
    if (current_hour >= 6 && current_hour < 18) {
        $('#current-time-icon').removeClass('fa-moon').addClass('fa-sun');
    } else {
        $('#current-time-icon').removeClass('fa-sun').addClass('fa-moon');
    }
}

function setCurrentWeather() {
    $.getJSON($SCRIPT_ROOT + '/api/v1/today', function (result) {
        $('#current_temperature').html(result['temperature'] + ' &deg;C');
        $('.today .temperature').html(result['temperature'] + ' &deg;C');
        $('.today .pressure_mb').text(result['pressure_mb']);
        $('.today .rain').text(result['rain']);
        $('.today .humidity').text(result['humidity']);
    });
}

$(function () {
    console.log('$SCRIPT_ROOT = "' + $SCRIPT_ROOT + '"');

    setInterval(setCurrentTime, 1000);
    setCurrentTime();

    setInterval(setCurrentWeather, 60000);
    setCurrentWeather();
});
