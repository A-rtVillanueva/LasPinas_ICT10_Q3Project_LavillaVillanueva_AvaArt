# Quick Start Guide - OBMC Intramurals Python Backend

## What's New

Your project now has a **Python Flask backend** that replaces the JavaScript localStorage approach. The frontend HTML files remain unchanged (CSS/animations perfect!), but now they communicate with a Python server backend.

## ⚡ Fastest Way: Use Startup Script

### Mac/Linux Users
Double-click `run.sh` in your project folder, or in Terminal:
```bash
./run.sh
```

### Windows Users
Double-click `run.bat` in your project folder

The script will:
✅ Check if Python is installed  
✅ Install dependencies automatically  
✅ Start Flask server  
✅ Tell you what to do next  

---

## Manual Setup (if startup script doesn't work)

## Step-by-Step Instructions

### 1. Verify Installation
Open Terminal and navigate to your project folder:
```bash
cd /Users/artvillanueva/Downloads/Project/LasPinas_ICT10_Q3Project_LavillaVillanueva_AvaArt
```

### 2. Install Python Dependencies (One-time)
```bash
pip install -r requirements.txt
```

This installs Flask and Flask-CORS needed for the server.

### 3. Start the Flask Server
```bash
python app.py
```

You'll see:
```
 * Running on http://127.0.0.1:5000
```

**Leave this terminal window open** while using the app.

### 4. Open the Website
In your web browser, open:
- **index.html** for Registration
- **team-checker.html** for Team Checker  
- **players.html** for Player List

The HTML files will communicate with the Flask server running on localhost:5000.

## Key Python Concepts Implemented

### 1. **if/elif/else Statements** (Team Assignment)
```python
if grade < 7 or grade > 10:
    return None
elif section_lower not in sections:
    return None
else:
    team_idx = (grade_idx + section_idx) % len(TEAMS)
    return TEAMS[team_idx]
```

### 2. **for Loops** (Data Searching)
```python
for reg_player in registered:
    for existing in all_players:
        if (matching_criteria):
            found = True
            break
```

### 3. **Functions with Clear Logic**
- `get_all_players()` - Merges hardcoded and registered players
- `assign_team()` - Uses if/elif/else for team assignment
- `register_player()` - Validates input, saves to JSON
- `check_team()` - Verifies eligibility
- `search_player()` - Finds player in database

### 4. **PEP 8 Standards**
- Proper spacing and indentation
- Descriptive variable names
- No inline comments (clean code)
- Functions separated by purpose
- Consistent naming conventions

## Files Created/Modified

| File | Status | Purpose |
|------|--------|---------|
| **app.py** | ✨ NEW | Python Flask backend with all business logic |
| **requirements.txt** | ✨ NEW | Python dependencies (Flask, Flask-CORS) |
| **PYTHON_BACKEND.md** | ✨ NEW | Detailed documentation |
| **index.html** | 🔄 UPDATED | Now calls /api/register endpoint |
| **team-checker.html** | 🔄 UPDATED | Now calls /api/check-team endpoint |
| **players.html** | 🔄 UPDATED | Now calls /api/search-player endpoint |

## Data Flow

```
HTML (Frontend)
    ↓ fetch() POST request
Flask Backend (Python)
    ↓ Processes with if/elif/else/loops
JSON File (players_data.json)
    ↓ Stored registrations
``````

## Python Code Highlights

### Team Assignment (if/elif/else)
Grades 7-10 + Section name → Teams distributed evenly:
- Blue Bears
- Red Bulldogs  
- Yellow Tigers
- Green Hornets

### Data Persistence
- **Hardcoded Players:** 81 original student roster
- **Registered Players:** Saved in JSON file when users register
- **Auto-merge:** Backend combines both sources

## Stopping the Server

Press `Ctrl + C` in the Terminal running Flask.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Connection refused" | Make sure Flask is running with `python app.py` |
| "Port 5000 already in use" | Kill the process: `lsof -i :5000` then `kill -9 <PID>` |
| Import errors | Run `pip install -r requirements.txt` again |
| Player not found | Check exact name/grade/section match |

## Architecture Benefits

✅ **Server-side validation** - No way to bypass checks  
✅ **Data persistence** - Registrations saved permanently  
✅ **Scalable** - Easy to add database (SQLite/PostgreSQL) later  
✅ **RESTful API** - Can serve mobile apps in future  
✅ **Python learning** - Demonstrates if/elif/loops/functions  

## Next Steps (Optional)

Want to add more features? The backend can be extended to:
- Add SQLite database instead of JSON
- Email notifications
- Team statistics dashboard
- Admin panel for moderators
- API rate limiting

Let me know if you need help with any of these! 🚀
