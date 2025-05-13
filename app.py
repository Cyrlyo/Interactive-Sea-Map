from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.map_modificator import add_click_marker, custom_click_marker
from src.map_generator import generate_marine_map

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def show_map(request: Request):
    m = generate_marine_map(location=[47.8722, -3.9216], map_name="sea_map")

    custom_click_marker(m)
    
    map_html = m.get_root().render()

    m.save("templates/generated_map.html")
    
    return templates.TemplateResponse("map.html", {
        "request": request,
        "map_html": map_html
    })
