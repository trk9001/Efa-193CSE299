function setCurrentTime() {
    let now = new Date();
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

$(function () {
    setInterval(setCurrentTime, 1000);
    setCurrentTime();
});
