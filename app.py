from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)

PLAYERS_FILE = "players_data.json"
TEAMS = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]

HARDCODED_PLAYERS = [
    {"name": "Rhianna Arevalo", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    {"name": "Atashya Lacerna", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    {"name": "Noleen Pangilinan", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    {"name": "Yumi Tubangi", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    {"name": "Marcus De Leon", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    {"name": "Art Villanueva", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    {"name": "John Ken Morishita", "grade": 10, "section": "Emerald", 
     "team": "Green Hornets"},
    {"name": "Anthea Alavado", "grade": 10, "section": "Ruby", 
     "team": "Green Hornets"},
    {"name": "Julianne Carpio", "grade": 10, "section": "Ruby", 
     "team": "Green Hornets"},
    {"name": "Sittie Dida Agun", "grade": 10, "section": "Ruby", 
     "team": "Green Hornets"},
    {"name": "Jakob Estapia", "grade": 10, "section": "Ruby", 
     "team": "Green Hornets"},
    {"name": "Anxela Aventajado", "grade": 10, "section": "Ruby", 
     "team": "Green Hornets"},
    {"name": "Nikolo De Leon", "grade": 10, "section": "Ruby", 
     "team": "Green Hornets"},
    {"name": "Chelsea De Peralta", "grade": 10, "section": "Ruby", 
     "team": "Green Hornets"},
    {"name": "Kayla Casul", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "Sophie Jimenez", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "Arabella Quinto", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "JC Vida", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "Max Ancheta", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "Cade Chua", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "Ethan Francia", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "Kleiser Fermocil", "grade": 10, "section": "Sapphire", 
     "team": "Green Hornets"},
    {"name": "Cassandra David", "grade": 10, "section": "Emerald", 
     "team": "Yellow Tigers"},
    {"name": "Ava Lavilla", "grade": 10, "section": "Emerald", 
     "team": "Yellow Tigers"},
    {"name": "Sebastian Atienza", "grade": 10, "section": "Emerald", 
     "team": "Yellow Tigers"},
    {"name": "Andrew De Luna", "grade": 10, "section": "Emerald", 
     "team": "Yellow Tigers"},
    {"name": "Gabe Sta. Maria", "grade": 10, "section": "Emerald", 
     "team": "Yellow Tigers"},
    {"name": "Amber Francisco", "grade": 10, "section": "Emerald", 
     "team": "Yellow Tigers"},
    {"name": "Maiah Arenal", "grade": 10, "section": "Ruby", 
     "team": "Yellow Tigers"},
    {"name": "Caiomey Cenon", "grade": 10, "section": "Ruby", 
     "team": "Yellow Tigers"},
    {"name": "Caitlyn Sannino", "grade": 10, "section": "Ruby", 
     "team": "Yellow Tigers"},
    {"name": "Anika Magpantay", "grade": 10, "section": "Ruby", 
     "team": "Yellow Tigers"},
    {"name": "Nathan Abaca", "grade": 10, "section": "Ruby", 
     "team": "Yellow Tigers"},
    {"name": "Hans Ulit", "grade": 10, "section": "Ruby", 
     "team": "Yellow Tigers"},
    {"name": "Pio Ramos", "grade": 10, "section": "Ruby", 
     "team": "Yellow Tigers"},
    {"name": "Athena Catapang", "grade": 10, "section": "Sapphire", 
     "team": "Yellow Tigers"},
    {"name": "Solei Magday", "grade": 10, "section": "Sapphire", 
     "team": "Yellow Tigers"},
    {"name": "Jadin Sarao", "grade": 10, "section": "Sapphire", 
     "team": "Yellow Tigers"},
    {"name": "Alonso Asuncion", "grade": 10, "section": "Sapphire", 
     "team": "Yellow Tigers"},
    {"name": "Zyan Eusebio", "grade": 10, "section": "Sapphire", 
     "team": "Yellow Tigers"},
    {"name": "Javi Mabilog", "grade": 10, "section": "Sapphire", 
     "team": "Yellow Tigers"},
    {"name": "Curt Fernando", "grade": 10, "section": "Sapphire", 
     "team": "Yellow Tigers"},
    {"name": "Stephanie De Guzman", "grade": 10, "section": "Emerald", 
     "team": "Red Bulldogs"},
    {"name": "Megan Ortega", "grade": 10, "section": "Emerald", 
     "team": "Red Bulldogs"},
    {"name": "Jasie Santiaguel", "grade": 10, "section": "Emerald", 
     "team": "Red Bulldogs"},
    {"name": "Christian Cubillas", "grade": 10, "section": "Emerald", 
     "team": "Red Bulldogs"},
    {"name": "Rye Deinla", "grade": 10, "section": "Emerald", 
     "team": "Red Bulldogs"},
    {"name": "Lucas Urrutia", "grade": 10, "section": "Emerald", 
     "team": "Red Bulldogs"},
    {"name": "Ezra Lazo", "grade": 10, "section": "Ruby", 
     "team": "Red Bulldogs"},
    {"name": "Chloe Galope", "grade": 10, "section": "Ruby", 
     "team": "Red Bulldogs"},
    {"name": "Jelo Gurango", "grade": 10, "section": "Ruby", 
     "team": "Red Bulldogs"},
    {"name": "Andre Tecson", "grade": 10, "section": "Ruby", 
     "team": "Red Bulldogs"},
    {"name": "Xander Panuncialman", "grade": 10, "section": "Ruby", 
     "team": "Red Bulldogs"},
    {"name": "Radhika Evangelio", "grade": 10, "section": "Sapphire", 
     "team": "Red Bulldogs"},
    {"name": "Yanna Moya", "grade": 10, "section": "Sapphire", 
     "team": "Red Bulldogs"},
    {"name": "Enzo Battung", "grade": 10, "section": "Sapphire", 
     "team": "Red Bulldogs"},
    {"name": "Brianna Sy", "grade": 10, "section": "Sapphire", 
     "team": "Red Bulldogs"},
    {"name": "AC Mactal", "grade": 10, "section": "Sapphire", 
     "team": "Red Bulldogs"},
    {"name": "Victor Buenvenida", "grade": 10, "section": "Sapphire", 
     "team": "Red Bulldogs"},
    {"name": "Ceska Ganal", "grade": 10, "section": "Emerald", 
     "team": "Blue Bears"},
    {"name": "Shanti Luna", "grade": 10, "section": "Emerald", 
     "team": "Blue Bears"},
    {"name": "Brooke Solis", "grade": 10, "section": "Emerald", 
     "team": "Blue Bears"},
    {"name": "Joaquin Dela Paz", "grade": 10, "section": "Emerald", 
     "team": "Blue Bears"},
    {"name": "John Rony Elevazo", "grade": 10, "section": "Emerald", 
     "team": "Blue Bears"},
    {"name": "Eyl Valeroso", "grade": 10, "section": "Emerald", 
     "team": "Blue Bears"},
    {"name": "Gabriella Buhain", "grade": 10, "section": "Ruby", 
     "team": "Blue Bears"},
    {"name": "Uriel Galura", "grade": 10, "section": "Ruby", 
     "team": "Blue Bears"},
    {"name": "Samantha Prowel", "grade": 10, "section": "Ruby", 
     "team": "Blue Bears"},
    {"name": "Jarret Dumlao", "grade": 10, "section": "Ruby", 
     "team": "Blue Bears"},
    {"name": "Jacob Liwag", "grade": 10, "section": "Ruby", 
     "team": "Blue Bears"},
    {"name": "Jourcey Del Barrio", "grade": 10, "section": "Ruby", 
     "team": "Blue Bears"},
    {"name": "Arron Guevarra", "grade": 10, "section": "Ruby", 
     "team": "Blue Bears"},
    {"name": "Mara Fado", "grade": 10, "section": "Sapphire", 
     "team": "Blue Bears"},
    {"name": "Charlotte Sy", "grade": 10, "section": "Sapphire", 
     "team": "Blue Bears"},
    {"name": "Luis Nazareno", "grade": 10, "section": "Sapphire", 
     "team": "Blue Bears"},
    {"name": "Inigo Romero", "grade": 10, "section": "Sapphire", 
     "team": "Blue Bears"},
    {"name": "Kyler Santos", "grade": 10, "section": "Sapphire", 
     "team": "Blue Bears"}
]


def load_registered_players():
    if os.path.exists(PLAYERS_FILE):
        with open(PLAYERS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_registered_players(players):
    with open(PLAYERS_FILE, 'w') as f:
        json.dump(players, f, indent=2)


def get_all_players():
    hardcoded = HARDCODED_PLAYERS
    registered = load_registered_players()
    
    all_players = hardcoded[:]
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


@app.route('/api/register', methods=['POST'])
def register_player():
    data = request.json
    
    required_fields = ['firstName', 'lastName', 'grade', 'section']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify(
                {'error': 'All fields are required'}
            ), 400
    
    first_name = data['firstName'].strip()
    last_name = data['lastName'].strip()
    grade = int(data['grade'])
    section = data['section'].strip()
    
    if grade < 7 or grade > 10:
        return jsonify(
            {'error': 'Grade must be between 7 and 10'}
        ), 400
    
    team = assign_team(grade, section)
    if not team:
        return jsonify(
            {'error': 'Invalid section'}
        ), 400
    
    full_name = f"{first_name} {last_name}"
    
    registered = load_registered_players()
    for player in registered:
        if (player['name'].lower() == full_name.lower() and
            player['grade'] == grade and
            player['section'].lower() == section.lower()):
            return jsonify(
                {'error': 'Player already registered'}
            ), 409
    
    new_player = {
        'name': full_name,
        'grade': grade,
        'section': section,
        'team': team,
        'registered_at': datetime.now().isoformat()
    }
    
    registered.append(new_player)
    save_registered_players(registered)
    
    return jsonify({
        'message': 'Registration successful',
        'player': new_player
    }), 201


@app.route('/api/check-team', methods=['POST'])
def check_team():
    data = request.json
    
    if not data.get('firstName') or not data.get('lastName'):
        return jsonify(
            {'error': 'Name is required'}
        ), 400
    
    if not data.get('grade') or not data.get('section'):
        return jsonify(
            {'error': 'Grade and section are required'}
        ), 400
    
    if data.get('registered') != 'yes':
        return jsonify(
            {'error': 
             'Must be registered to participate'}
        ), 400
    
    if data.get('medical') != 'yes':
        return jsonify(
            {'error': 
             'Must have medical clearance'}
        ), 400
    
    first_name = data['firstName'].strip()
    last_name = data['lastName'].strip()
    full_name = f"{first_name} {last_name}"
    grade = int(data['grade'])
    section = data['section'].strip()
    
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


@app.route('/api/search-player', methods=['POST'])
def search_player():
    data = request.json
    
    if not data.get('firstName') or not data.get('lastName'):
        return jsonify(
            {'error': 'Name is required'}
        ), 400
    
    if not data.get('grade') or not data.get('section'):
        return jsonify(
            {'error': 'Grade and section are required'}
        ), 400
    
    first_name = data['firstName'].strip()
    last_name = data['lastName'].strip()
    full_name = f"{first_name} {last_name}"
    grade = int(data['grade'])
    section = data['section'].strip()
    
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
            'error': 'Player not found in the system'
        }), 404


@app.route('/api/players', methods=['GET'])
def get_players():
    all_players = get_all_players()
    return jsonify({
        'players': all_players,
        'total': len(all_players)
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
