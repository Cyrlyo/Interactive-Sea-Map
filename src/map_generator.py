import folium
from typing import Optional, Sequence

class MapGenerator(folium.Map):
    
    def __init__(
        self, 
        location: Optional[Sequence[float]] = None,
        map_name: Optional[str] = None,
        zoom_start: int = 13,
        ):
        super().__init__()
        
        if location is None:
            self.location = [47.8722, -3.9216]
        else:
            self.location = location
            
        self._name = map_name or "Map"
            
        self.map = folium.Map(location=self.location, zoom_start=zoom_start)
        
        folium.TileLayer(
            tiles='https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png',
            attr='Map data: © OpenSeaMap contributors',
            name='OpenSeaMap',
            overlay=True,
            control=True
        ).add_to(self.map)
        
        folium.LayerControl().add_to(self.map)

def generate_marine_map(
    location: Optional[Sequence[float]] = None,
    map_name: Optional[str] = None,
    zoom_start: int = 13,
    ):
    
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