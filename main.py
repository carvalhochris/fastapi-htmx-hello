from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return """
    <html>
    <head>
    <title>Hello...</title>
    <script src="https://unpkg.com/htmx.org@1.9.5" integrity="sha384-xcuj3WpfgjlKF+FXhSQFQ0ZNr39ln+hwjN3npfM9VBnUskLolQAcN80McRIVOPuO" crossorigin="anonymous"></script>
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
    </body>
    </html>
    """

@app.get("/world", response_class=HTMLResponse)
async def world():
    return """
        <title>...world</title>
        <h1>...world</h1>
    """


