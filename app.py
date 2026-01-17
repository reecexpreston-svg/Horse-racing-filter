

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Race, Runner, FormLine
from course_mapping import get_course_characteristics
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Database configuration

database_url = os.getenv(‘DATABASE_URL’)
if database_url and database_url.startswith(‘postgres://’):
database_url = database_url.replace(‘postgres://’, ‘postgresql://’, 1)

app.config[‘SQLALCHEMY_DATABASE_URI’] = database_url
app.config[‘SQLALCHEMY_TRACK_MODIFICATIONS’] = False

db.init_app(app)

# Create tables

with app.app_context():
db.create_all()

@app.route(’/api/races’, methods=[‘GET’])
def get_races():
“””
Get races with optional filtering
Query params: date, course, going, distance, race_class
“””
date_str = request.args.get(‘date’)
course = request.args.get(‘course’)
going = request.args.get(‘going’)
distance = request.args.get(‘distance’)
race_class = request.args.get(‘race_class’)

```
# Start with all races
query = Race.query

# Apply filters
if date_str:
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        query = query.filter_by(date=date_obj)
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

if course:
    query = query.filter_by(course=course)

if going:
    query = query.filter_by(going=going)
    
if distance:
    query = query.filter_by(distance=distance)
    
if race_class:
    query = query.filter_by(race_class=race_class)

races = query.all()

return jsonify({
    'count': len(races),
    'races': [race.to_dict() for race in races]
})
```

@app.route(’/api/races/<int:race_id>’, methods=[‘GET’])
def get_race_detail(race_id):
“””
Get detailed race card with all runners and their form
“””
race = Race.query.get_or_404(race_id)
runners = Runner.query.filter_by(race_id=race_id).all()

```
return jsonify({
    'race': race.to_dict(),
    'runners': [runner.to_dict(include_form=True) for runner in runners]
})
```

@app.route(’/api/runners/<int:runner_id>/form’, methods=[‘GET’])
def get_runner_form(runner_id):
“””
Get filtered form for a specific runner
Query params: going, distance, class, min_position, max_position
“””
runner = Runner.query.get_or_404(runner_id)

```
# Start with all form lines for this runner
query = FormLine.query.filter_by(runner_id=runner_id)

# Apply filters
going = request.args.get('going')
if going:
    query = query.filter_by(going=going)

distance = request.args.get('distance')
if distance:
    query = query.filter_by(distance=distance)

race_class = request.args.get('class')
if race_class:
    query = query.filter_by(race_class=race_class)

min_position = request.args.get('min_position', type=int)
if min_position:
    query = query.filter(FormLine.position >= min_position)

max_position = request.args.get('max_position', type=int)
if max_position:
    query = query.filter(FormLine.position <= max_position)

# Order by date descending (most recent first)
form_lines = query.order_by(FormLine.date.desc()).all()

return jsonify({
    'runner': runner.to_dict(include_form=False),
    'form': [form.to_dict() for form in form_lines]
})
```

@app.route(’/api/courses’, methods=[‘GET’])
def get_courses():
“””
Get list of all courses
“””
courses = db.session.query(Race.course).distinct().order_by(Race.course).all()
return jsonify({
‘courses’: [course[0] for course in courses]
})

@app.route(’/api/courses/<course_name>’, methods=[‘GET’])
def get_course_info(course_name):
“””
Get course characteristics
“””
characteristics = get_course_characteristics(course_name)

```
if characteristics:
    return jsonify({
        'course': course_name,
        'characteristics': characteristics
    })
else:
    return jsonify({
        'error': 'Course not found'
    }), 404
```

@app.route(’/api/goings’, methods=[‘GET’])
def get_goings():
“””
Get list of all going descriptions
“””
goings = db.session.query(Race.going).distinct().order_by(Race.going).all()
return jsonify({
‘goings’: [going[0] for going in goings if going[0]]
})

@app.route(’/api/distances’, methods=[‘GET’])
def get_distances():
“””
Get list of all distances
“””
distances = db.session.query(Race.distance).distinct().order_by(Race.distance).all()
return jsonify({
‘distances’: [distance[0] for distance in distances if distance[0]]
})

@app.route(’/api/classes’, methods=[‘GET’])
def get_classes():
“””
Get list of all race classes
“””
classes = db.session.query(Race.race_class).distinct().order_by(Race.race_class).all()
return jsonify({
‘classes’: [cls[0] for cls in classes if cls[0]]
})

@app.route(’/api/racecards’, methods=[‘GET’])
def get_racecards():
“””
Get race cards (races with runners) for a specific date
Query params: date (required)
“””
date_str = request.args.get(‘date’)

```
if not date_str:
    return jsonify({'error': 'Date parameter is required'}), 400

try:
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
except ValueError:
    return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

races = Race.query.filter_by(date=date_obj).order_by(Race.race_time).all()

racecards = []
for race in races:
    runners = Runner.query.filter_by(race_id=race.id).all()
    racecards.append({
        'race': race.to_dict(),
        'runners': [runner.to_dict(include_form=False) for runner in runners]
    })

return jsonify({
    'date': date_str,
    'count': len(racecards),
    'racecards': racecards
})
```

@app.route(’/api/health’, methods=[‘GET’])
def health_check():
“”“Health check endpoint”””
return jsonify({‘status’: ‘healthy’})

@app.route(’/api/test-db’, methods=[‘GET’])
def test_db():
“”“Test database connection and show what races are in the database”””
try:
races = Race.query.all()
return jsonify({
‘status’: ‘success’,
‘total_races’: len(races),
‘races’: [{
‘date’: str(race.date),
‘course’: race.course,
‘time’: race.race_time,
‘name’: race.race_name
} for race in races[:5]]
})
except Exception as e:
return jsonify({‘status’: ‘error’, ‘message’: str(e)}), 500

if **name** == ‘**main**’:
port = int(os.environ.get(‘PORT’, 5000))
app.run(host=‘0.0.0.0’, port=port)
