from fastapi import FastAPI, Request
from src.map_generator import MapGenerator
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_map(request: Request):
    # Créer une carte centrée sur Concarneau
    # m = folium.Map(location=[47.8722, -3.9216], zoom_start=13)
    m = MapGenerator(location=[47.8722, -3.9216])

    # Sauvegarder dans un fichier temporaire HTML (embeddable)
    map_html = m._repr_html_()

    return templates.TemplateResponse("map.html", {
        "request": request,
        "map_html": map_html
    })
