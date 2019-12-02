var widget_app = new Vue({
  el: '#widget-app',
  data: {
    celestial: '',
    time: '',
    date: '',
  },
  methods: {
    setNow: function () {
      now = new Date();
      current_hour = now.getHours();
      if (current_hour >= 6 && current_hour < 18) {
        this.celestial = '<i class="fas fa-sun"></i>';
      } else {
        this.celestial = '<i class="fas fa-moon"></i>';
      }
      this.time = now.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric' });
      this.date = now.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
    },
  },
  created: function () {
    this.setNow();
    setInterval(this.setNow, 1000);
  },
});

var app_day = new Vue({
  el: '#app_day',
  data: {
    days: [
      {
        name: 'Monday',
        temperature: '10',
        pressure: '20',
        rain: '30',
        humidity: '40',
      },
      {
        name: 'Tuesday',
        temperature: '10',
        pressure: '20',
        rain: '30',
        humidity: '40',
      },
      {
        name: 'Wednesday',
        temperature: '10',
        pressure: '20',
        rain: '30',
        humidity: '40',
      },
      {
        name: 'Thursday',
        temperature: '10',
        pressure: '20',
        rain: '30',
        humidity: '40',
      },
      {
        name: 'Friday',
        temperature: '10',
        pressure: '20',
        rain: '30',
        humidity: '40',
      },
      {
        name: 'Saturday',
        temperature: '10',
        pressure: '20',
        rain: '30',
        humidity: '40',
      },
    ]
  }
});

function drawClock() {
  //Get Humidity Temperature and Rain Data
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var txt = this.responseText;
      var obj = JSON.parse(txt); //Ref: https://www.w3schools.com/js/js_json_parse.asp
      document.getElementById("rain").innerHTML = obj.Rain + "%";
      document.getElementById("temperature").innerHTML = Math.round(obj.Temperature) + "&deg;C";
      document.getElementById("temp").innerHTML = Math.round(obj.Temperature) + "&deg;C";
      document.getElementById("humidity").innerHTML = Math.round(obj.Humidity) + "%";
      document.getElementById("pressure").innerHTML = Math.round(obj.Pressuremb) + " mb";
    }
  };
  xhttp.open("GET", "readADC", true); //Handle readADC server on ESP8266
  xhttp.send();
}
