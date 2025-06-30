//map setup
var map = L.map('map').setView([51.505, -0.09], 13);

//tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//marker
var marker = L.marker([51.5, -0.09]).addTo(map);
marker.bindPopup('<b>Hello world!</b><br><img src="/static/testthumbnail.jpg" alt="thumbnail" style="height:125px;width:auto;display:block;margin-left:auto;margin-right:auto;"><br>I am a popup. Click me twice to view a scene.').openPopup();

function OnMarkerClick() {
    window.open("/view");
}

marker.on('dblclick', OnMarkerClick);