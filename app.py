from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.map_modificator import add_click_marker
from src.map_generator import generate_marine_map

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_map(request: Request):
    # Créer une carte centrée sur Concarneau
    m = generate_marine_map(location=[47.8722, -3.9216], map_name="sea_map")
    add_click_marker(m)
    
    # Sauvegarder dans un fichier temporaire HTML (embeddable)
    map_html = m.get_root().render()

    return templates.TemplateResponse("map.html", {
        "request": request,
        "map_html": map_html
    })
