

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Race, Runner, FormLine
from course_mapping import get_course_characteristics
from datetime import datetime

app = Flask(**name**)
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
Get races with filtering
Query params: date (YYYY-MM-DD), course, going, distance, race_class, etc.
“””
# Get query parameters
date_str = request.args.get(‘date’)
course = request.args.get(‘course’)

```
# Start with all races
query = Race.query

# Apply filters
if date_str:
    try:
        race_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        query = query.filter_by(date=race_date)
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

if course:
    query = query.filter_by(course=course)

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

form_lines = query.order_by(FormLine.race_date.desc()).all()

return jsonify({
    'runner': runner.to_dict(include_form=False),
    'form': [form.to_dict() for form in form_lines]
})
```

@app.route(’/api/courses’, methods=[‘GET’])
def get_courses():
“””
Get list of all courses with their characteristics
“””
# Get unique courses from the database
courses = db.session.query(Race.course).distinct().all()
course_list = [course[0] for course in courses]

```
# Add characteristics
courses_with_chars = []
for course_name in course_list:
    chars = get_course_characteristics(course_name)
    courses_with_chars.append({
        'name': course_name,
        'characteristics': chars
    })

return jsonify({
    'count': len(courses_with_chars),
    'courses': courses_with_chars
})
```

@app.route(’/api/racecards’, methods=[‘GET’])
def get_racecards():
“””
Get race cards for a specific date with all runners
Query params: date (YYYY-MM-DD), course (optional)
“””
date_str = request.args.get(‘date’)
course = request.args.get(‘course’)

```
if not date_str:
    return jsonify({'error': 'Date parameter is required'}), 400

try:
    race_date = datetime.strptime(date_str, '%Y-%m-%d').date()
except ValueError:
    return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400

# Get races
query = Race.query.filter_by(date=race_date)
if course:
    query = query.filter_by(course=course)

races = query.all()

# Build race cards with runners
racecards = []
for race in races:
    runners = Runner.query.filter_by(race_id=race.id).all()
    racecards.append({
        'race': race.to_dict(),
        'runners': [runner.to_dict(include_form=False) for runner in runners]
    })

return jsonify({
    'date': date_str,
    'course': course,
    'count': len(racecards),
    'racecards': racecards
})
```

@app.route(’/api/filter-options’, methods=[‘GET’])
def get_filter_options():
“””
Get available filter options (goings, distances, classes, etc.)
“””
# Get unique values from races
goings = db.session.query(Race.going).distinct().all()
distances = db.session.query(Race.distance).distinct().all()
classes = db.session.query(Race.race_class).distinct().all()

```
# Get unique values from form lines
form_goings = db.session.query(FormLine.going).distinct().all()
form_distances = db.session.query(FormLine.distance).distinct().all()
form_classes = db.session.query(FormLine.race_class).distinct().all()

# Combine and deduplicate
all_goings = set([g[0] for g in goings if g[0]] + [g[0] for g in form_goings if g[0]])
all_distances = set([d[0] for d in distances if d[0]] + [d[0] for d in form_distances if d[0]])
all_classes = set([c[0] for c in classes if c[0]] + [c[0] for c in form_classes if c[0]])

return jsonify({
    'goings': sorted(list(all_goings)),
    'distances': sorted(list(all_distances)),
    'classes': sorted(list(all_classes))
})
```

@app.route(’/api/health’, methods=[‘GET’])
def health_check():
“”“Health check endpoint”””
return jsonify({‘status’: ‘healthy’})

@app.route(’/api/test-db’, methods=[‘GET’])
def test_db():
“”“Test database connection and show what races exist”””
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
