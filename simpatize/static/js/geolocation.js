function checkNearbyPlacesSelected() {
  radioButtonLocation = document.getElementById("nearby_places_yes");

  if(radioButtonLocation.checked){
    getLocation();
  } else {
    setEmptyPositionOnHTMLElements();
  }
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(setPositionOnHTMLElements);
  }
}

function setEmptyPositionOnHTMLElements() {
  var elementLatitude = document.getElementById("currentLatitude");
  elementLatitude.value = "";

  var elementLongitude = document.getElementById("currentLongitude");
  elementLongitude.value = "";
}

function setPositionOnHTMLElements(position) {
  var elementLatitude = document.getElementById("currentLatitude");
  elementLatitude.value = position.coords.latitude;

  var elementLongitude = document.getElementById("currentLongitude");
  elementLongitude.value = position.coords.longitude;
}