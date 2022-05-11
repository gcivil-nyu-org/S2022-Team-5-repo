function initMap() {
    // The location of Uluru
    const uluru = { lat: latitude, lng: longitude };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 18,
      center: uluru,
    });
    // The marker, positioned at Uluru
    const infoWindow = new google.maps.InfoWindow();
    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
      title: listing_name,
    });
    marker.addListener("click", () => {
      infoWindow.close();
      infoWindow.setContent(marker.getTitle());
      infoWindow.open(marker.getMap(), marker);
    });
  }