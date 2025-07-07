//map setup
var map = L.map('map').setView([51.505, -0.09], 13);

//tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//marker
var marker = L.marker([51.5, -0.09]).addTo(map);

function OnMarkerClick() {
    window.open("/view");
}

marker.on('dblclick', OnMarkerClick);