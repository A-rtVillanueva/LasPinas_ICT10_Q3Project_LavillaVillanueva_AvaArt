# OBMC Intramurals - Python Flask Backend

This project now includes a Python Flask backend that replaces the JavaScript localStorage logic with server-side data persistence.

## Features Implemented

### Python Backend (app.py)
- **Flask web framework** for REST API endpoints
- **Team assignment algorithm** using if/elif/else logic based on grade + section
- **Data persistence** with JSON file storage (players_data.json)
- **CORS support** for frontend-backend communication
- **PEP 8 compliant** code with proper spacing, naming conventions, and structure
- **Four API endpoints**:
  - `POST /api/register` - Register a new player
  - `POST /api/check-team` - Check team assignment
  - `POST /api/search-player` - Search for a player
  - `GET /api/players` - Get all players

### Python Concepts Used
- **if/elif/else statements** in team assignment logic
- **for loops** for data searching and matching
- **List comprehensions** and data filtering
- **Dictionaries** for player data structures
- **Functions** with clear separation of concerns
- **Error handling** with try/except patterns

## Running the Backend

### Easiest Way: Use Startup Script

**Mac/Linux:** Double-click `run.sh` or run `./run.sh`  
**Windows:** Double-click `run.bat`

The script handles everything:
- ✅ Checks Python installation
- ✅ Installs dependencies
- ✅ Starts Flask server
- ✅ Clear instructions on next steps

---

### Or Do It Manually:

### 1. Install Dependencies
```bash
cd /Users/artvillanueva/Downloads/Project/LasPinas_ICT10_Q3Project_LavillaVillanueva_AvaArt
pip install -r requirements.txt
```

### 2. Start the Flask Server
```bash
python app.py
```

The server will start on `http://localhost:5000`

You should see output like:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 3. Open the Web Application
In your browser, open:
- Registration: `file:///Users/artvillanueva/Downloads/Project/LasPinas_ICT10_Q3Project_LavillaVillanueva_AvaArt/index.html`
- Team Checker: `file:///Users/artvillanueva/Downloads/Project/LasPinas_ICT10_Q3Project_LavillaVillanueva_AvaArt/team-checker.html`
- Players List: `file:///Users/artvillanueva/Downloads/Project/LasPinas_ICT10_Q3Project_LavillaVillanueva_AvaArt/players.html`

**Keep the Flask server running** in the terminal while using the application.

## File Structure

```
LasPinas_ICT10_Q3Project_LavillaVillanueva_AvaArt/
├── app.py                          # Python Flask backend
├── requirements.txt                # Python dependencies
├── index.html                      # Registration page
├── team-checker.html               # Team eligibility checker
├── players.html                    # Player roster search
├── players_data.json               # Registered players (auto-created)
└── PYTHON_BACKEND.md               # This file
```

## How It Works

### Backend Architecture

The Flask backend implements PEP 8 standards with:

1. **Team Assignment Logic** (if/elif/else)
   ```python
   def assign_team(grade, section):
       if grade < 7 or grade > 10:
           return None
       if section_lower not in sections:
           return None
       # Uses modulo arithmetic to assign teams
       team_idx = (grade_idx + section_idx) % len(TEAMS)
       return TEAMS[team_idx]
   ```

2. **Data Merging** (loops and list operations)
   ```python
   def get_all_players():
       # Combines hardcoded roster with registered players
       # Loops through to avoid duplicates
       for reg_player in registered:
           for existing in all_players:
               if (matching criteria):
                   found = True
   ```

3. **RESTful Endpoints**
   - Each endpoint handles POST requests with JSON data
   - Returns JSON responses with player info or error messages
   - Uses CORS for cross-origin requests from HTML files

### Frontend Integration

The HTML files now use `fetch()` API to communicate with the backend:

```javascript
fetch('http://localhost:5000/api/register', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
})
.then(response => response.json())
.then(data => {
    // Handle response
})
```

## Data Storage

### players_data.json
Registered players are stored in JSON format:
```json
[
    {
        "name": "John Doe",
        "grade": 10,
        "section": "Emerald",
        "team": "Green Hornets",
        "registered_at": "2025-02-22T10:30:00"
    }
]
```

### Hardcoded Players
The backend includes 81 hardcoded players from the original roster. When a student registers, they are added to the JSON file.

## API Endpoints

### 1. Register Player
**Endpoint:** `POST /api/register`
**Request:**
```json
{
    "firstName": "Jane",
    "lastName": "Smith",
    "grade": 10,
    "section": "Ruby"
}
```
**Response (Success):**
```json
{
    "message": "Registration successful",
    "player": {
        "name": "Jane Smith",
        "grade": 10,
        "section": "Ruby",
        "team": "Blue Bears"
    }
}
```

### 2. Check Team Eligibility
**Endpoint:** `POST /api/check-team`
**Request:**
```json
{
    "firstName": "Art",
    "lastName": "Villanueva",
    "grade": 10,
    "section": "Emerald",
    "registered": "yes",
    "medical": "yes"
}
```
**Response (Success):**
```json
{
    "success": true,
    "player": {
        "name": "Art Villanueva",
        "grade": 10,
        "section": "Emerald",
        "team": "Green Hornets"
    }
}
```

### 3. Search Player
**Endpoint:** `POST /api/search-player`
**Request:**
```json
{
    "firstName": "Marcus",
    "lastName": "De Leon",
    "grade": 10,
    "section": "Emerald"
}
```

## Troubleshooting

### "Connection refused" Error
- Make sure Flask server is running: `python app.py`
- Check that server is on port 5000

### "Player not found"
- Verify name, grade, and section match exactly (case-sensitive for section)
- Check players_data.json for registered players

### CORS Errors
- Flask-CORS is already configured in app.py
- Make sure you're running Flask (not just opening HTML files)

## Requirements

- Python 3.7+
- Flask 2.3.2
- Flask-CORS 4.0.0

See `requirements.txt` for exact versions.
