import os
import webbrowser
from threading import Timer
import requests
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="ShadowTrace API")

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
def get_location_endpoint(request: Request, ip: str = Query(None)):
    if not ip:
        # Extract original client IP behind proxy headers (Render uses x-forwarded-for)
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            ip = forwarded.split(",")[0].strip()
        else:
            ip = request.headers.get("x-real-ip")
        
        # Fallback to connection ip
        if not ip:
            ip = request.client.host
            
        # Don't pass loopback addresses to ip-api
        if ip in ("127.0.0.1", "localhost", "::1", "testclient"):
            ip = None

    result = get_data.get_location(ip)
    if not result:
        return {"status": "fail", "message": "Could not fetch location info"}
    return result

def open_browser():
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    # Render sets the PORT environment variable dynamically
    port = int(os.environ.get("PORT", 8000))
    
    # Check if we are running in a production or headless environment
    is_render = "RENDER" in os.environ
    
    if is_render:
        print(f"Starting production server on 0.0.0.0:{port}...")
        uvicorn.run(app, host="0.0.0.0", port=port)
    else:
        # Local development auto-launch
        Timer(1.5, open_browser).start()
        print(f"Starting local server at http://127.0.0.1:{port}...")
        uvicorn.run(app, host="127.0.0.1", port=port)

