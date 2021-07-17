//Reading in tour json
//Testing using local data
fetch("tour_data_json.json")
.then(response => {
   return response.json();
})
.then(data => console.log(data))
.then((response) => {
   const concerts = response.name;

   const layerGroup = L.featureGroup().addTo(map);

   concerts.forEach(({ lat, lng, name, City }) => {
     layerGroup.addLayer(
       L.marker([lat, lng], { icon }).bindPopup(
         `Name: ${name}, Venue: ${Venue}, Date: ${Date}`
       )
     );
   });

   map.fitBounds(layerGroup.getBounds());
 });

//Function to determine the marker size based upon the revenue
function markerSize (revenue) {
   return revenue/100000
};

var locations = []


