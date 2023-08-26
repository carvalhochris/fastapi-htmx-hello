from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return """
    <html>
    <head>
    <title>Hello...</title>
    </head>
    <body>
    <div id="parent-div">
    <h1>Hello...</h1>
    </div>
    <button 
        hx-get="/world"
        hx-trigger="click"
        hx-target="#parent-div"
        hx-swap="innerHTML"
        >Click Me!
    </button>    
    <script src="/static/htmx.min.js"></script>
    </body>
    </html>
    """

@app.get("/world", response_class=HTMLResponse)
async def world():
    return """
        <title>...world</title>
        <h1>...world</h1>
    """