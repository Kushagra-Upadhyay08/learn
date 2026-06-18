# Names & Ages Manager

A simple web service to manage names and ages with a backend API and frontend UI.

## Setup

### Backend
```bash
cd backend
npm install
npm start
```
Backend runs on `http://localhost:5000`

### Frontend
Open `frontend/index.html` in your browser or use a local server:
```bash
# Using Python
python -m http.server 3000 --directory frontend

# Or using Node.js
npx http-server frontend -p 3000
```
Frontend runs on `http://localhost:3000`

## Features
- ✅ Add names and ages
- ✅ View all entries
- ✅ Search by name or age
- ✅ Delete entries
