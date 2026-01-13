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
