# 🌐 CyberMap - Interactive IP Geolocation Dashboard

An elegant, real-time IP Geolocation dashboard built with **FastAPI** (Python) and **Leaflet.js** (JavaScript). This application lets you lookup any IPv4 or IPv6 address, display comprehensive network/location metadata in a clean card layout, and pinpoint the coordinates on a responsive, light-themed map with custom animations.

## ✨ Features

- **Real-time lookup**: Resolves hostnames or raw IP addresses using a secure, performant local API bridge.
- **Dynamic Data Grid**: Automatically renders all metadata returned by the geolocation API (ISP, ASN, Country, City, Region, Zip Code, Timezone, and exact coordinates).
- **Interactive Map**: Renders coordinates using Leaflet.js with high-contrast **CartoDB Voyager** light cartography.
- **Custom Pulse Beacon**: Highlights the target location with a glowing, animated CSS beacon marker.
- **Auto-Detect**: Instantly locates the current system's IP address upon application startup.
- **Modern Light UI**: Sleek, elegant light-theme aesthetic using Inter and Space Grotesk typography, soft shadows, and clean borders.
- **Instant Browser Access**: Automatically opens your default web browser to the dashboard URL on startup.

---

## 🛠️ Tech Stack

- **Backend**: FastAPI, Uvicorn, Python Requests
- **Frontend**: Vanilla HTML5, CSS3, Modern JavaScript (ES6+ Fetch API)
- **Map & Geospatial**: Leaflet.js, CartoDB Voyager Tile Service

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have Python 3.8+ installed along with the required libraries:
```bash
pip install fastapi uvicorn requests
```

### 2. Running the Application
Launch the server from the root of the `ip_checker` folder:
```bash
python app.py
```

### 3. Usage
Once started:
- Your default web browser will automatically open to `http://127.0.0.1:8000`.
- Leave the search field blank and click **Locate** (or click **Use My IP**) to locate your current system.
- Enter any custom IP address (e.g., `8.8.8.8`) to instantly fly to its location on the map.
