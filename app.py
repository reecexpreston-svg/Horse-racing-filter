from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Race, Runner, FormLine
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

database_url = os.getenv('DATABASE_URL', 'sqlite:///racing.db')
if database_url and database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({'message': 'Horse Racing API', 'status': 'running'})

@app.route('/api/health')
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/races', methods=['GET'])
def get_races():
    date_str = request.args.get('date')
    course = request.args.get('course')
    query = Race.query
    
    if date_str:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            query = query.filter_by(date=date_obj)
        except:
            return jsonify({'error': 'Invalid date'}), 400
    
    if course:
        query = query.filter_by(course=course)
    
    races = query.order_by(Race.date.desc()).all()
    return jsonify({'races': [race.to_dict() for race in races], 'count': len(races)})

@app.route('/api/races/<int:race_id>')
def get_race(race_id):
    race = Race.query.get_or_404(race_id)
    runners = Runner.query.filter_by(race_id=race_id).all()
    return jsonify({
        'race': race.to_dict(),
        'runners': [runner.to_dict(include_form=True) for runner in runners]
    })

@app.route('/api/filter-stats', methods=['POST'])
def filter_stats():
    data = request.get_json()
    race_id = data.get('race_id')
    filters = data.get('filters', {})
    
    if not race_id:
        return jsonify({'error': 'race_id required'}), 400
    
    runners = Runner.query.filter_by(race_id=race_id).all()
    results = []
    
    for runner in runners:
        query = FormLine.query.filter_by(runner_id=runner.id)
        
        if filters.get('going'):
            query = query.filter_by(going=filters['going'])
        if filters.get('distance'):
            query = query.filter_by(distance=filters['distance'])
        if filters.get('class'):
            query = query.filter_by(race_class=filters['class'])
        
        form_lines = query.all()
        
        if form_lines:
            total = len(form_lines)
            wins = sum(1 for fl in form_lines if fl.finishing_position == 1)
            places = sum(1 for fl in form_lines if fl.finishing_position and fl.finishing_position <= 3)
            
            results.append({
                'runner': runner.to_dict(include_form=False),
                'stats': {
                    'total_runs': total,
                    'wins': wins,
                    'places': places,
                    'win_rate': round(wins / total * 100, 1) if total > 0 else 0,
                    'place_rate': round(places / total * 100, 1) if total > 0 else 0
                },
                'matching_form': [fl.to_dict() for fl in form_lines]
            })
        else:
            results.append({
                'runner': runner.to_dict(include_form=False),
                'stats': {'total_runs': 0, 'wins': 0, 'places': 0, 'win_rate': 0, 'place_rate': 0},
                'matching_form': []
            })
    
    return jsonify({'race_id': race_id, 'filters': filters, 'results': results})

@app.route('/api/courses')
def get_courses():
    courses = db.session.query(Race.course).distinct().all()
    return jsonify({'courses': [c[0] for c in courses]})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
