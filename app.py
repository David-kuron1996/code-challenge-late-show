from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Routes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        result = episode.to_dict()
        result['appearances'] = [
            {
                'id': appearance.id,
                'rating': appearance.rating,
                'episode_id': appearance.episode_id,
                'guest_id': appearance.guest_id,
                'guest': {
                    'id': appearance.guest.id,
                    'name': appearance.guest.name,
                    'occupation': appearance.guest.occupation
                }
            }
            for appearance in episode.appearances
        ]
        return jsonify(result)
    else:
        return jsonify({'error': 'Episode not found'}), 404

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    
    # Check if required fields are present
    required_fields = ['rating', 'episode_id', 'guest_id']
    if not all(field in data for field in required_fields):
        return jsonify({'errors': ['Missing required fields']}), 400
    
    # Create new appearance
    appearance = Appearance(
        rating=data['rating'],
        episode_id=data['episode_id'],
        guest_id=data['guest_id']
    )
    
    # Validate appearance
    errors = appearance.validate()
    if errors:
        return jsonify({'errors': errors}), 400
    
    # Check if episode and guest exist
    episode = Episode.query.get(data['episode_id'])
    guest = Guest.query.get(data['guest_id'])
    
    if not episode or not guest:
        return jsonify({'errors': ['Episode or Guest not found']}), 404
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify(appearance.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)