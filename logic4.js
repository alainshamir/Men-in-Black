// Creating map object
var map = L.map("map", {
  center: [38.9072, -77.0369],
  zoom: 11
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(map);

// var link = "http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/" +
// "35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson";

var link = "https://opendata.arcgis.com/datasets/f6c703ebe2534fc3800609a07bad8f5b_17.geojson";

// Function that will determine the color of a neighborhood based on the borough it belongs to
// function chooseColor(borough) {
//   switch (borough) {
//   case "Brooklyn":
//     return "yellow";
//   case "Bronx":
//     return "red";
//   case "Manhattan":
//     return "orange";
//   case "Queens":
//     return "green";
//   case "Staten Island":
//     return "purple";
//   default:
//     return "black";
//   }
// }
// function chooseColor(NBH_NAMES) {
//   switch (NBH_NAMES) {
//   case "Congress Heights, Bellevue, Washington Highlands":
//     return "yellow";
//   case "Shaw, Logan Circle":
//     return "red";
//   case "Manhattan":
//     return "orange";
//   case "Queens":
//     return "green";
//   case "Staten Island":
//     return "purple";
//   default:
//     return "black";
//   }
// }



function chooseColor(NBH_NAMES) {
  switch (NBH_NAMES) {
  case "Kalorama Heights, Adams Morgan, Lanier Heights":
    return "yellow";
  case "Columbia Heights, Mt. Pleasant, Pleasant Plains, Park View":
    return "red";
  case "Howard University, Le Droit Park, Cardozo/Shaw":
    return "orange";
  case "Georgetown, Burleith/Hillandale":
    return "green";
  case "West End, Foggy Bottom, GWU":
    return "purple";
  case "Dupont Circle, Connecticut Avenue/K Street":
    return "purple";
  case "Shaw, Logan Circle":
    return "purple";
  case "Downtown, Chinatown, Penn Quarters, Mount Vernon Square, North Capitol Street":
    return "purple";
  case "Southwest Employment Area, Southwest/Waterfront, Fort McNair, Buzzard Point":
    return "purple";
  case "Hawthorne, Barnaby Woods, Chevy Chase":
    return "purple";
  case "Friendship Heights, American University Park, Tenleytown":
    return "purple";
  case "North Cleveland Park, Forest Hills, Van Ness":
    return "purple";
  case "Spring Valley, Palisades, Wesley Heights, Foxhall Crescent, Foxhall Village, Georgetown Reservoir":
    return "purple";
  case "Cathedral Heights, McLean Gardens, Glover Park":
    return "purple";
  case "Cleveland Park, Woodley Park, Massachusetts Avenue Heights, Woodland-Normanstone Terrace":
    return "purple";
  case "Colonial Village, Shepherd Park, North Portal Estates":
    return "purple";
  case "Takoma, Brightwood, Manor Park":
    return "purple";
  case "Brightwood Park, Crestwood, Petworth":
    return "purple";
  case "Lamond Riggs, Queens Chapel, Fort Totten, Pleasant Hill":
    return "purple";
  case "North Michigan Park, Michigan Park, University Heights":
    return "purple";
  case "Edgewood, Bloomingdale, Truxton Circle, Eckington":
    return "purple";
  case "Brookland, Brentwood, Langdon":
    return "purple";
  case "Ivy City, Arboretum, Trinidad, Carver Langston":
    return "purple";
  case "Woodridge, Fort Lincoln, Gateway":
    return "purple";
  case "NoMa, Union Station, Stanton Park, Kingman Park":
    return "purple";
  case "Capitol Hill, Lincoln Park":
    return "purple";
  case "Near Southeast, Navy Yard":
    return "purple";
  case "Historic Anacostia":
    return "purple";
  case "Eastland Gardens, Kenilworth":
    return "purple";
  case "Mayfair, Hillbrook, Mahaning Heights":
    return "purple";
  case "Deanwood, Burrville, Grant Park, Lincoln Heights, Fairmont Heights":
    return "purple";
  case "River Terrace, Benning, Greenway, Fort Dupont":
    return "purple";
  case "Capitol View, Marshall Heights, Benning Heights":
    return "purple";
  case "Twining, Fairlawn, Randle Highlands, Penn Branch, Fort Davis Park, Dupont Park":
    return "purple";
  case "Fairfax Village, Naylor Gardens, Hillcrest, Summit Park":
    return "purple";
  case "Woodland/Fort Stanton, Garfield Heights, Knox Hill":
    return "purple";
  case "Sheridan, Barry Farm, Buena Vista":
    return "purple";
  case "Douglass, Shipley Terrace":
    return "purple";
  case " Congress Heights, Bellevue, Washington Highlands":
    return "purple";
  default:
    return "black";
  }
}



// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  // Creating a geoJSON layer with the retrieved data
  L.geoJson(data, {
    // Style each feature (in this case a neighborhood)
    style: function(feature) {
      return {
        color: "white",
        // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
        fillColor: chooseColor(feature.properties.borough),
        fillOpacity: 0.5,
        weight: 1.5
      };
    },
    // Called on each feature
    onEachFeature: function(feature, layer) {
      // Set mouse events to change map styling
      layer.on({
        // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.9
          });
        },
        // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
        mouseout: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.5
          });
        },
        // When a feature (neighborhood) is clicked, it is enlarged to fit the screen
        click: function(event) {
          map.fitBounds(event.target.getBounds());
        }
      });
      // Giving each feature a pop-up with information pertinent to it
      layer.bindPopup("<h1>" + feature.properties.NBH_NAMES + "</h1> <hr> <h2>" + feature.properties.NBH_NAMES + "</h2>");


    }
  }).addTo(map);
});
