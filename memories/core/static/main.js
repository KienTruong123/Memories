$(function () {
  $('#ggmap').locationpicker({
    location: { latitude: 10.8230989, longitude: 106.6296638 },
    radius: 5,
    inputBinding: {
      latitudeInput: $('#lat'),
      longitudeInput: $('#lng'),
    },
    enableAutocomplete: true,
  });
});

// function getLocation() {
//   if (navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(showPosition);
//   }
// }

// function showPosition(position) {
//   document.getElementById("lat").value = position.coords.latitude;
//   document.getElementById("lng").value = position.coords.longitude;
// }
