from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse  # Update this line
from fastapi.middleware.cors import CORSMiddleware
from app.v1.router.user_router import user_router

app = FastAPI(
    title='Tutorial API',
    description='Api paso a paso',
    version='0.0.1'
)
origins = [
    "http://localhost",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)


#API EJEMPLO

'''@app.get('/', tags=['inicio'])
def read_root():
    return HTMLResponse ('<h2> Hola </h2>')'''


