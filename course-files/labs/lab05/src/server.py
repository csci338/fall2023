from fastapi import FastAPI
from fastapi.responses import Response, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/yelp", response_class=HTMLResponse)
async def root():
    return """
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="/styles.css"></link>    
 </head>
 <body>
  <h1>Hello World!</h1>
  <script type="text/javascript" src="/js/main.js"></script>
 </body>
</html>
    """

@app.get("/js/main.js")
async def js_main_js():
    js: str = """
async function main() {
    console.log("Hello from JavaScript!")
}

window.onload = main;
    """
    return Response(content=js, media_type="text/javascript")

app.mount("/", StaticFiles(directory='ui'), name='ui')