import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
#from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
app = FastAPI()

#CORM inbuilt middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com', 'https://localhost:8000','https://127.0.0.1:8000', 'http://127.0.0.1:8000'
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)

#gzip inbuilt middleware
app.add_middleware(
    GZipMiddleware, minimum_size=1000
)

#custom middleware
class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        print(f'Request: {request.url.path} processed in {duration:.5f} seconds')
        return response


app.add_middleware(TimerMiddleware)

#httpsredirect inbuilt middleware
#app.add_middleware(HTTPSRedirectMiddleware)


# define endpoints
@app.get('/')
async def home():
    return {'message': 'welcome to my home page'}

@app.get('/hello')
async def hello():
    for _ in range(10000000):
        pass
    return {'message': 'Hello World!'}
