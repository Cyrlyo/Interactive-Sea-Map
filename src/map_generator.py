import folium
from typing import Optional, Sequence

class MapGenerator:
    def __init__(
        self, 
        location: Optional[Sequence[float]] = None,
        zoom_start: int = 13,
        map_name: Optional[str] = None,
    ):
        if location is None:
            location = [47.8722, -3.9216]  # Concarneau, par défaut

        self.location = location
        self.map_name = map_name or "Map"
        
        # Création de la carte
        self.map = folium.Map(location=self.location, zoom_start=zoom_start)

        # Ajouter un fond spécifique (OpenSeaMap)
        folium.TileLayer(
            tiles='https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png',
            attr='Map data: © OpenSeaMap contributors',
            name='OpenSeaMap',
            overlay=True,
            control=True
        ).add_to(self.map)

        folium.LayerControl().add_to(self.map)

    def add_click_marker(self):
        # Fonction qui active le mode d'ajout de marqueurs via clic
        folium.ClickForMarker(popup='Nouveau marqueur').add_to(self.map)

    def get_map_html(self):
        # Retourner la carte en HTML pour l'intégrer dans le template
        return self.map._repr_html_()

def generate_marine_map(
    location: Optional[Sequence[float]] = None,
    map_name: Optional[str] = None,
    zoom_start: int = 13,
    ) -> folium.Map:
    
    if location is None:
        location = [47.8722, -3.9216]
    else:
        location = location
        
    name = map_name or "Map"
    
    sea_map = folium.Map(location=location, zoom_start=zoom_start)
    
    folium.TileLayer(
            tiles='https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png',
            attr='Map data: © OpenSeaMap contributors',
            name='OpenSeaMap',
            overlay=True,
            control=True
        ).add_to(sea_map)
    
    folium.LayerControl().add_to(sea_map)
    
    return sea_map