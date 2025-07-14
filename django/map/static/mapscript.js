//map setup
var map = L.map('map').setView([60.73958103204708, 24.75605680821921], 13);

//tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//marker
var mascotIcon = L.icon({
    iconUrl: '/static/icons/mascot_ico.png',
    shadowUrl: '/static/icons/mascot_ico_shadow.png',
    iconSize:     [50, 50],
    shadowSize:   [50, 50],
    iconAnchor:   [0, 0],
    shadowAnchor: [0, 0],
    popupAnchor:  [25, 0]
});

var marker = L.marker([60.73958103204708, 24.75605680821921], {icon:mascotIcon}, {alt:'alttext'}).addTo(map);

var popup = L.popup()
    .setContent('<b>Hello world!</b><br><img src="/static/testthumbnail.jpg" alt="thumbnail" style="height:125px;width:auto;max-width:220px;display:block;margin-left:auto;margin-right:auto;padding:5px;"><br>I am a popup. Click me twice to view a scene.');

marker.bindPopup(popup);

function OnMarkerClick() {
    window.open("/view");
}

marker.on('dblclick', OnMarkerClick);