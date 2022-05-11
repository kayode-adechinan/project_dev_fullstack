var map = L.map("map").setView([8.541389, 39.268889], 12);

const autoRefresh = async () => {
  setInterval(async () => {
    map.eachLayer((layer) => {
      if (!layer._url) {
        layer.remove();
      }
    });

    const { data } = await axios.get(`/coordinates`);

    var locations = data.coordinates.map((i) => {
      return [
        `LOCATION_${i.id}`,
        parseFloat(i.latitude),
        parseFloat(i.longitude),
      ];
    });

    mapLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
    L.tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "&copy; " + mapLink + " Contributors",
      maxZoom: 18,
    }).addTo(map);

    for (var i = 0; i < locations.length; i++) {
      marker = new L.marker([locations[i][1], locations[i][2]])
        .bindPopup(locations[i][0])
        .addTo(map);
    }
  }, 1000);
};

const initMap = async () => {
  map.eachLayer((layer) => {
    if (!layer._url) {
      layer.remove();
    }
  });

  const { data } = await axios.get(`/coordinates`);

  var locations = data.coordinates.map((i) => {
    return [
      `LOCATION_${i.id}`,
      parseFloat(i.latitude),
      parseFloat(i.longitude),
    ];
  });

  var tiles = L.tileLayer(
    "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
    {
      maxZoom: 18,
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      id: "mapbox/streets-v11",
      tileSize: 512,
      zoomOffset: -1,
    }
  ).addTo(map);

  for (var i = 0; i < locations.length; i++) {
    marker = new L.marker([locations[i][1], locations[i][2]])
      .bindPopup(locations[i][0])
      .addTo(map);
  }
};

const refreshMap = async () => {
  map.eachLayer((layer) => {
    if (!layer._url) {
      layer.remove();
    }
  });

  const { data } = await axios.get(`/coordinates`);

  console.log(data);

  var locations = data.coordinates.map((i) => {
    return [
      `LOCATION_${i.id}`,
      parseFloat(i.latitude),
      parseFloat(i.longitude),
    ];
  });

  var tiles = L.tileLayer(
    "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
    {
      maxZoom: 18,
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      id: "mapbox/streets-v11",
      tileSize: 512,
      zoomOffset: -1,
    }
  ).addTo(map);

  for (var i = 0; i < locations.length; i++) {
    marker = new L.marker([locations[i][1], locations[i][2]])
      .bindPopup(locations[i][0])
      .addTo(map);
  }
};

initMap();
const element = document.getElementById("refresh");
element.addEventListener("click", function () {
  refreshMap();
});
