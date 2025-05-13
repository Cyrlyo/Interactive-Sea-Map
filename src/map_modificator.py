import folium
from folium import Map

def add_click_marker(sea_map: Map) -> Map:
    folium.ClickForMarker().add_to(sea_map)