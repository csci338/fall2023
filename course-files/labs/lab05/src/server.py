from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import aiohttp
import json

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/css/styles.css"></link>    
  </head>
  <body>
    <h1>Hello World!</h1>
    <script type="text/javascript" src="/js/main.js"></script>
  </body>
</html>
    """


@app.get("/items/{item_id}")
async def embed_data_in_url(item_id: int, query_param: str = None):
    # try querying with this url:
    # http://127.0.0.1:8000/items/123?query_param=456
    return {"item_id": item_id, "query_param": query_param}


@app.get("/data/yelp", response_class=HTMLResponse)
async def yelp(location: str = 'Asheville', term: str = None, limit: int = 10):
    url = f"https://www.apitutor.org/yelp/simple/v3/businesses/search?location={location}&limit={limit}"
    if term:
        url += f"&term={term}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            businesses = await response.json()
            # convert from list of dictionaries to a string:
            return json.dumps(businesses)


@app.get("/ui/yelp", response_class=HTMLResponse)
async def yelp(location: str = 'Asheville', term: str = None, limit: int = 10):
    url = f"https://www.apitutor.org/yelp/simple/v3/businesses/search?location={location}&limit={limit}"
    if term:
        url += f"&term={term}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            def to_card(business):
                return f'''
                    <section class="business">
                        <img src="{ business.get('image_url') }" />
                        <h2>{ business.get('name') }</h2>
                    </section>
                '''

            businesses = await response.json()
            return f'''
            <html>
            <head>
                <link rel="stylesheet" type="text/css" href="/css/styles.css"></link>    
            </head>
            <body>
                <h1>Hello World!</h1>
                <div class="businesses">
                    { ''.join(map(to_card, businesses)) }
                </div>
            </body>
        </html>
        '''


@app.get("/data/spotify", response_class=HTMLResponse)
async def spotify(q: str = 'Beyonce', type: str = 'track', limit: int = 2):
    url = f"https://www.apitutor.org/spotify/simple/v1/search?q={q}&type={type}&limit={limit}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            # convert from list of dictionaries to a string:
            return json.dumps(data)


@app.get("/ui/spotify", response_class=HTMLResponse)
async def spotify(q: str = 'Beyonce', type: str = 'track', limit: int = 2):
    return '''
    Your turn!
    '''

app.mount("/", StaticFiles(directory='ui'), name='ui')
