# Python Code Examples - Implementation Details

## Overview

Your Flask backend (`app.py`) demonstrates core Python concepts for a student project.

## 1. If/Elif/Else Statements

### Team Assignment Function
```python
def assign_team(grade, section):
    if grade < 7 or grade > 10:
        return None
    
    section_lower = section.lower()
    grade_idx = grade - 7
    
    sections = ["amethyst", "beryl", "crystal", "diamond", 
                "emerald", "garnet", "ruby", "sapphire", "topaz"]
    
    if section_lower not in sections:
        return None
    
    section_idx = sections.index(section_lower)
    team_idx = (grade_idx + section_idx) % len(TEAMS)
    
    return TEAMS[team_idx]
```

**Demonstrates:**
- `if` condition checking range
- `if` checking membership in list
- `else` implied (return None)
- Multiple validation steps

### Eligibility Validation
```python
required_fields = ['firstName', 'lastName', 'grade', 'section']
for field in required_fields:
    if field not in data or not data[field]:
        return jsonify(
            {'error': 'All fields are required'}
        ), 400

if grade < 7 or grade > 10:
    return jsonify(
        {'error': 'Grade must be between 7 and 10'}
    ), 400

if not team:
    return jsonify(
        {'error': 'Invalid section'}
    ), 400
```

**Demonstrates:**
- Multiple `if` statements for validation
- Early return pattern
- Conditional error handling

## 2. For Loops

### Data Merging (Combining Lists)
```python
def get_all_players():
    hardcoded = HARDCODED_PLAYERS
    registered = load_registered_players()
    
    all_players = hardcoded[:]  # Copy list
    for reg_player in registered:
        found = False
        for existing in all_players:
            if (existing['name'].lower() == 
                reg_player['name'].lower() and
                existing['grade'] == reg_player['grade'] and
                existing['section'].lower() == 
                reg_player['section'].lower()):
                found = True
                break
        if not found:
            all_players.append(reg_player)
    
    return all_players
```

**Demonstrates:**
- Nested loops (loop within loop)
- Conditional logic inside loops
- `break` statement to exit loop
- List.append() to add elements

### Duplicate Checking
```python
registered = load_registered_players()
for player in registered:
    if (player['name'].lower() == full_name.lower() and
        player['grade'] == grade and
        player['section'].lower() == section.lower()):
        return jsonify(
            {'error': 'Player already registered'}
        ), 409
```

**Demonstrates:**
- Loop with conditional
- Multiple comparison operators (`and`)
- Case-insensitive comparison (.lower())

### Player Search (Finding in List)
```python
all_players = get_all_players()

found_player = None
for player in all_players:
    if (player['name'].lower() == full_name.lower() and
        player['grade'] == grade and
        player['section'].lower() == section.lower()):
        found_player = player
        break

if found_player:
    return jsonify({
        'success': True,
        'player': found_player
    }), 200
else:
    return jsonify({
        'error': 'Player not found'
    }), 404
```

**Demonstrates:**
- Loop to find single item
- Break when found
- Conditional response based on result

## 3. Data Structures & Operations

### Dictionaries (Key-Value Pairs)
```python
new_player = {
    'name': full_name,
    'grade': grade,
    'section': section,
    'team': team,
    'registered_at': datetime.now().isoformat()
}

registered.append(new_player)
```

**Demonstrates:**
- Dictionary creation
- Adding to list

### List Slicing & Copying
```python
all_players = hardcoded[:]  # Create copy
```

## 4. Flask Decorators (PEP 8 Pattern)

```python
@app.route('/api/register', methods=['POST'])
def register_player():
    data = request.json
    # ... function body
```

**Demonstrates:**
- Function decorators
- Route mapping
- HTTP method specification

## 5. File I/O with JSON

### Load Data
```python
def load_registered_players():
    if os.path.exists(PLAYERS_FILE):
        with open(PLAYERS_FILE, 'r') as f:
            return json.load(f)
    return []
```

**Demonstrates:**
- File existence check
- Context manager (`with` statement)
- JSON parsing

### Save Data
```python
def save_registered_players(players):
    with open(PLAYERS_FILE, 'w') as f:
        json.dump(players, f, indent=2)
```

**Demonstrates:**
- File writing
- JSON serialization
- Indentation for readability

## 6. String Methods (PEP 8)

```python
first_name = data['firstName'].strip()
last_name = data['lastName'].strip()
section = data['section'].strip()

full_name = f"{first_name} {last_name}"
```

**Demonstrates:**
- String.strip() method
- f-strings for formatting
- Input validation

## 7. CORS Configuration

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

**Demonstrates:**
- Importing modules
- Decorator pattern application
- Cross-Origin Resource Sharing

## Constants (PEP 8 Style)

```python
PLAYERS_FILE = "players_data.json"
TEAMS = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

HARDCODED_PLAYERS = [
    {"name": "Rhianna Arevalo", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    # ... more players
]
```

**Demonstrates:**
- UPPERCASE naming for constants
- List of dictionaries
- Organized data structure

## HTTP Status Codes (RESTful Standards)

```python
return jsonify({'message': 'Registration successful'}), 201  # Created
return jsonify({'error': 'Player already registered'}), 409  # Conflict
return jsonify({'error': 'Player not found'}), 404            # Not Found
return jsonify({'success': True, 'player': found}), 200       # OK
return jsonify({'error': 'All fields are required'}), 400     # Bad Request
```

## Testing the API (Terminal)

### Using curl to test registration:
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"firstName":"Test","lastName":"User","grade":10,"section":"Emerald"}'
```

### Using Python requests library:
```python
import requests

response = requests.post(
    'http://localhost:5000/api/register',
    json={
        'firstName': 'Test',
        'lastName': 'User',
        'grade': 10,
        'section': 'Emerald'
    }
)

print(response.json())
```

## Summary of Python Concepts Used

| Concept | Location | Purpose |
|---------|----------|---------|
| **if/elif/else** | `assign_team()`, validation | Decision making |
| **for loops** | `get_all_players()`, search | Iteration |
| **Dictionary** | Player data | Store key-value pairs |
| **List** | Players array | Store multiple players |
| **String methods** | `.lower()`, `.strip()` | String manipulation |
| **File I/O** | `load/save data` | Persistence |
| **JSON** | Database format | Data serialization |
| **Functions** | All routes | Code organization |
| **Decorators** | `@app.route` | Flask routing |
| **Context managers** | `with open()` | Resource management |

This demonstrates core CS concepts while building a real application! 🎓
