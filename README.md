# 🌐 CivicTrack - Community Issue Reporting Platform

**CivicTrack** is a full-stack civic engagement platform that enables citizens to report, track, and resolve local community issues like potholes, broken streetlights, water leaks, and more. It features an interactive map interface, smart filtering, and detailed status tracking.

---

## 🔧 Features

- 🗺️ **Live Map with Issue Markers**
- 📋 **Report Issues via Modal Form**
- 📍 **Location-Based Filtering**
- 📊 **Categorized Issue Cards with Status**
- 📡 **FastAPI Backend for Data Handling**
- 💾 **SQLite Database for Storage**
- ⚡ **Responsive UI with Leaflet.js**
- 🔐 **Anonymous Reporting Supported**

---

## 📁 Project Structure

```bash
CivicTrack/
│
├── frontend/               # Contains index.html and static assets
│   └── index.html          # Full-featured UI with embedded JS + CSS
│
├── backend/                # FastAPI backend
│   ├── main.py             # API routes
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── database.py         # DB connection setup
│   └── civictrack.db       # SQLite DB (auto-created)
│
└── README.md               # You're here!
