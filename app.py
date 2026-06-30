import os
import webbrowser
from threading import Timer
import requests
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="CyberMap API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "templates", "index.html")

class get_data:
    @staticmethod
    def get_location(ip=None):
        try:
            url = f"http://ip-api.com/json/{ip}?fields=61439" if ip else "http://ip-api.com/json/?fields=61439"
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching location: {e}")
            return None

@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        with open(INDEX_PATH, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Frontend template not found</h1>", status_code=404)

@app.get("/api/location")
def get_location_endpoint(ip: str = Query(None)):
    result = get_data.get_location(ip)
    if not result:
        return {"status": "fail", "message": "Could not fetch location info"}
    return result

def open_browser():
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    Timer(1.5, open_browser).start()
    print("Starting server at http://127.0.0.1:8000 ...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
