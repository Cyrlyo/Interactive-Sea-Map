import folium
from folium import Map
from folium.template import Template

def add_click_marker(sea_map: Map) -> None:
    folium.ClickForMarker().add_to(sea_map)
    
    
def custom_click_marker(sea_map: Map) -> None:
    template = Template(
        """
            {% macro script(this, kwargs) %}
                var markerCount = 0;  // compteur de marqueurs

                function newMarker(e) {
                    markerCount += 1;

                    var new_mark = L.marker().setLatLng(e.latlng).addTo({{ this._parent.get_name() }});
                    new_mark.dragging.enable();

                    // Supprimer le marqueur au double clic
                    new_mark.on('dblclick', function(e) {
                        {{ this._parent.get_name() }}.removeLayer(e.target);
                        markerCount -= 1;
                        updateMarkerCounter(); // met à jour le compteur après suppression
                    });

                    var lat = e.latlng.lat.toFixed(4),
                        lng = e.latlng.lng.toFixed(4);

                    new_mark.bindPopup("Marker: " + markerCount + "<br>Lat: " + lat + "<br>Lng: " + lng);

                    updateMarkerCounter();
                }

                // Met à jour un compteur visible dans la page
                function updateMarkerCounter() {
                    var counter = document.getElementById("marker-counter");
                    if (counter) {
                        counter.innerText = "Nombre de marqueurs : " + markerCount;
                    }
                }

                {{ this._parent.get_name() }}.on('click', newMarker);
            {% endmacro %}
            """
    )
    
    click_marker = folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}<b>Marker n°:</b> ${counter}")
    click_marker._template = template
    
    click_marker.add_to(sea_map)