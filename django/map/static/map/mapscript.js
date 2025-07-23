//map setup
let map = L.map('map').setView([60.73958103204708, 24.75605680821921], 13);

//tile layer
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 25,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//icon
let mascotIcon = L.icon({
    iconUrl: '/static/map/icons/mascot_ico.png',
    shadowUrl: '/static/map/icons/mascot_ico_shadow.png',
    iconSize:     [50, 50],
    shadowSize:   [50, 50],
    iconAnchor:   [0, 0],
    shadowAnchor: [0, 0],
    popupAnchor:  [25, 0]
});

//maker1
let marker1 = L.marker([60.73958103204708, 24.75605680821921], {icon:mascotIcon}, {alt:'alttext'}).addTo(map);

let popup1 = L.popup()
    .setContent('<b>Hello world!</b><br><img src="/static/map/testthumbnail.jpg" alt="thumbnail" style="height:125px;width:auto;max-width:220px;display:block;margin-left:auto;margin-right:auto;padding:5px;"><br>I am a popup. Click me twice to view a scene.');

marker1.bindPopup(popup1);

marker1.on('dblclick', OnMarkerClick);

//maker2
let marker2 = L.marker([60.73958103204708, 24.75605680821921], {icon:mascotIcon}, {alt:'alttext'}).addTo(map);

let popup2 = L.popup()
    .setContent('<b>Hello world!</b><br><img src="/static/map/testthumbnail.jpg" alt="thumbnail" style="height:125px;width:auto;max-width:220px;display:block;margin-left:auto;margin-right:auto;padding:5px;"><br>I am a popup. Click me twice to view a scene.');

marker2.bindPopup(popup2);

marker2.on('dblclick', OnMarkerClick);

//clicking function
function OnMarkerClick() {    
        window.open("/view/1")
};