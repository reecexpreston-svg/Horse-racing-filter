"""
Flask API for Horse Racing Data Filtering
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Race, Runner, FormLine
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Database configuration
# For Railway: Use DATABASE_URL environment variable
database_url = os.getenv('DATABASE_URL', 'sqlite:///racing.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/api/races', methods=['GET'])
def get_races():
    """
    Get races with optional filtering
    Query params: date, course, time
    """
    date_str = request.args.get('date')
    course = request.args.get('course')
    time = request.args.get('time')
    
    query = Race.query
    
    if date_str:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            query = query.filter_by(date=date_obj)
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    
    if course:
        query = query.filter_by(course=course)
    
    if time:
        query = query.filter_by(race_time=time)
    
    races = query.order_by(Race.date.desc(), Race.race_time).all()
    
    return jsonify({
        'races': [race.to_dict() for race in races],
        'count': len(races)
    })

@app.route('/api/races/<int:race_id>', methods=['GET'])
def get_race_detail(race_id):
    """
    Get detailed race card with all runners and their form
    """
    race = Race.query.get_or_404(race_id)
    runners = Runner.query.filter_by(race_id=race_id).all()
    
    return jsonify({
        'race': race.to_dict(),
        'runners': [runner.to_dict(include_form=True) for runner in runners]
    })

@app.route('/api/runners/<int:runner_id>/form', methods=['GET'])
def get_runner_form(runner_id):
    """
    Get filtered form for a specific runner
    Query params: going, distance, class, min_position, max_position
    """
    runner = Runner.query.get_or_404(runner_id)
    
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
        query = query.filter(FormLine.finishing_position >= min_position)
    
    max_position = request.args.get('max_position', type=int)
    if max_position:
        query = query.filter(FormLine.finishing_position <= max_position)
    
    # Order by date descending
    form_lines = query.order_by(FormLine.race_date.desc()).all()
    
    return jsonify({
        'runner': runner.to_dict(include_form=False),
        'form_lines': [fl.to_dict() for fl in form_lines],
        'count': len(form_lines)
    })

@app.route('/api/filter-stats', methods=['POST'])
def get_filter_stats():
    """
    Get statistics for runners based on form filters
    POST body: {
        "race_id": 123,
        "filters": {
            "going": "good",
            "distance": "1m4f",
            "class": "Class 2"
        }
    }
    """
    data = request.get_json()
    race_id = data.get('race_id')
    filters = data.get('filters', {})
    
    if not race_id:
        return jsonify({'error': 'race_id required'}), 400
    
    # Get all runners in the race
    runners = Runner.query.filter_by(race_id=race_id).all()
    
    results = []
    
    for runner in runners:
        # Query form lines with filters
        query = FormLine.query.filter_by(runner_id=runner.id)
        
        if filters.get('going'):
            query = query.filter_by(going=filters['going'])
        if filters.get('distance'):
            query = query.filter_by(distance=filters['distance'])
        if filters.get('class'):
            query = query.filter_by(race_class=filters['class'])
        
        form_lines = query.all()
        
        # Calculate stats
        if form_lines:
            total_runs = len(form_lines)
            wins = sum(1 for fl in form_lines if fl.finishing_position == 1)
            places = sum(1 for fl in form_lines if fl.finishing_position and fl.finishing_position <= 3)
            
            avg_position = sum(fl.finishing_position for fl in form_lines if fl.finishing_position) / total_runs if total_runs > 0 else None
            
            results.append({
                'runner': runner.to_dict(include_form=False),
                'stats': {
                    'total_runs': total_runs,
                    'wins': wins,
                    'places': places,
                    'win_rate': round(wins / total_runs * 100, 1) if total_runs > 0 else 0,
                    'place_rate': round(places / total_runs * 100, 1) if total_runs > 0 else 0,
                    'avg_position': round(avg_position, 1) if avg_position else None
                },
                'matching_form': [fl.to_dict() for fl in form_lines]
            })
        else:
            results.append({
                'runner': runner.to_dict(include_form=False),
                'stats': {
                    'total_runs': 0,
                    'wins': 0,
                    'places': 0,
                    'win_rate': 0,
                    'place_rate': 0,
                    'avg_position': None
                },
                'matching_form': []
            })
    
    return jsonify({
        'race_id': race_id,
        'filters': filters,
        'results': results
    })

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Get list of all courses in database"""
    courses = db.session.query(Race.course).distinct().all()
    return jsonify({
        'courses': [c[0] for c in courses]
    })

@app.route('/api/race-times', methods=['GET'])
def get_race_times():
    """
    Get available race times for a specific date and course
    Query params: date, course
    """
    date_str = request.args.get('date')
    course = request.args.get('course')
    
    if not date_str or not course:
        return jsonify({'error': 'date and course required'}), 400
    
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    
    times = db.session.query(Race.race_time).filter_by(
        date=date_obj,
        course=course
    ).order_by(Race.race_time).all()
    
    return jsonify({
        'times': [t[0] for t in times if t[0]]
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

@app.route('/api/test-db', methods=['GET'])
def test_db():
    try:
        races = Race.query.all()
        return jsonify({
            'status': 'success',
            'total_races': len(races),
            'races': [{
                'date': str(race.date),
                'course': race.course,
                'time': race.race_time,
                'name': race.race_name
            } for race in races[:5]]
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


