import os
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

port = 8000
host = "0.0.0.0"
root_dir = os.path.dirname(__file__)

app = FastAPI()

def cors_headers(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, HEAD, OPTIONS"
    return response 

@app.head("/data/")
@app.get("/data/")
async def get_headers(response: Response):
    cors_headers(response)
    return {"message": "Hello World"}

# Mount the static files directory
app.mount("/", StaticFiles(directory=root_dir), name="root")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=host, port=port, server_header=False)