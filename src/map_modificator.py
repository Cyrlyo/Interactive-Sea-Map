import folium
from folium import Map
from folium.template import Template

def add_click_marker(sea_map: Map) -> None:
    folium.ClickForMarker().add_to(sea_map)
    
    
def custom_click_marker(sea_map: Map) -> None:
    template = Template(
        """
        {% macro script(this, kwargs) %}
            var markerCount = 0;

            function newMarker(e) {
                markerCount += 1;

                var new_mark = L.marker().setLatLng(e.latlng, { draggable: true }).addTo({{ this._parent.get_name() }});
                new_mark.dragging.enable();

                // Display coordinates in the popup
                function updatePopup(marker) {
                    var lat = marker.getLatLng().lat.toFixed(4);
                    var lng = marker.getLatLng().lng.toFixed(4);
                    marker.bindPopup("Marker: " + markerCount + "<br>Lat: " + lat + "<br>Lng: " + lng).openPopup();
                }

                updatePopup(new_mark); // afficher dès l'ajout

                // Update the pupop when the marker moves
                new_mark.on('dragend', function(e) {
                    updatePopup(e.target);
                });

                // Delete when double click
                new_mark.on('dblclick', function(e) {
                    {{ this._parent.get_name() }}.removeLayer(e.target);
                    markerCount -= 1;
                    updateMarkerCounter();
                });

                updateMarkerCounter();
            }

            function updateMarkerCounter() {
                var counter = document.getElementById("marker-counter");
                if (counter) {
                    counter.innerText = "Number of markers : " + markerCount;
                }
            }

            {{ this._parent.get_name() }}.on('click', newMarker);
        {% endmacro %}
        """
    )
    
    click_marker = folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}<b>Marker n°:</b> ${counter}")
    click_marker._template = template
    
    click_marker.add_to(sea_map)