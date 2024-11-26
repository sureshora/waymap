from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


app = Flask(__name__)
CORS(app)

@app.route('/api/config', methods=['GET'])
def get_config():
    api_key = os.getenv("GCP_API_KEY")
    return jsonify({"api_key": api_key})


# Directory where your audio files are stored
AUDIO_DIR = os.path.join(os.path.dirname(__file__), 'audio')


# Add this route for the root URL
@app.route('/')
def home():
    return render_template('wonders.html')

@app.route('/3dmap1')
def map1():
    return render_template('3dmap1.html')

@app.route('/3dmap3')
def map3():
    return render_template('3dmap3.html')


# Route to serve audio files
@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

# Wonders of the World API data
@app.route('/api/wonders', methods=['GET'])
def wonders():
    wonders_data = [
{
            "id": 1,
            "title": "Great Wall of China",
            "description": "A historic landmark in China.",
            "location": { "lat": 40.4319, "lng": 116.5704 },
            "audio": "http://104.197.173.36:5000/audio/badaling.mp3",
            "length": "21,196 km",
        },
        {
            "id": 2,
            "title": "Eiffel Tower",
            "description": "An iconic tower in Paris.",
            "location": { "lat": 48.8584, "lng": 2.2945 },
            "audio": "http://104.197.173.36:5000/audio/eiffel.mp3",
            "length": "324 meters",
        },
        {
            "id": 3,
            "title": "Taj Mahal",
            "description": "A symbol of love in Agra, India.",
            "location": { "lat": 27.1751, "lng": 78.0421 },
            "audio": "http://104.197.173.36:5000/audio/tajmahal.mp3",
            "length": "73 meters height",
        },
        {
            "id": 4,
            "title": "Christ the Redeemer",
            "description": "A massive statue in Rio de Janeiro.",
            "location": { "lat": -22.9519, "lng": -43.2105 },
            "audio": "http://104.197.173.36:5000/audio/christredeemer.mp3",
            "length": "30 meters",
        },
        {
            "id": 5,
            "title": "Machu Picchu",
            "description": "An ancient Incan city in Peru.",
            "location": { "lat": -13.1631, "lng": -72.5450 },
            "audio": "http://104.197.173.36:5000/audio/machupicchu.mp3",
            "length": "7 sq km area",
        },
        {
            "id": 6,
            "title": "Colosseum",
            "description": "A historic amphitheater in Rome.",
            "location": { "lat": 41.8902, "lng": 12.4922 },
            "audio": "http://104.197.173.36:5000/audio/colosseum.mp3",
            "length": "188 meters long",
        },
        {
            "id": 7,
            "title": "Petra",
            "description": "An archaeological city in Jordan.",
            "location": { "lat": 30.3285, "lng": 35.4444 },
            "audio": "http://104.197.173.36:5000/audio/petra.mp3",
            "length": "264,000 sq meters",
        },
        {
            "id": 8,
            "title": "Statue of Liberty",
            "description": "A gift of freedom in New York City.",
            "location": { "lat": 40.6892, "lng": -74.0445 },
            "audio": "http://104.197.173.36:5000/audio/statueofliberty.mp3",
            "length": "93 meters",
        },
        {
            "id": 9,
            "title": "Pyramids of Giza",
            "description": "Ancient Egyptian wonders.",
            "location": { "lat": 29.9792, "lng": 31.1342 },
            "audio": "http://104.197.173.36:5000/audio/gizapyramids.mp3",
            "length": "138.8 meters (Great Pyramid)",
        },
        {
            "id": 10,
            "title": "Chichen Itza",
            "description": "A Mayan archaeological site in Mexico.",
            "location": { "lat": 20.6843, "lng": -88.5678 },
            "audio": "http://104.197.173.36:5000/audio/chichenitza.mp3",
            "length": "30 meters height",
        },
        {
            "id": 11,
            "title": "Angkor Wat",
            "description": "A vast temple complex in Cambodia.",
            "location": { "lat": 13.4125, "lng": 103.8670 },
            "audio": "http://104.197.173.36:5000/audio/angkorwat.mp3",
            "length": "162.6 hectares",
        },
        {
            "id": 12,
            "title": "Sydney Opera House",
            "description": "An architectural marvel in Australia.",
            "location": { "lat": -33.8568, "lng": 151.2153 },
            "audio": "http://104.197.173.36:5000/audio/sydneyopera.mp3",
            "length": "183 meters",
        },
        {
            "id": 13,
            "title": "Mount Everest",
            "description": "The highest mountain in the world.",
            "location": { "lat": 27.9881, "lng": 86.9250 },
            "audio": "http://104.197.173.36:5000/audio/mounteverest.mp3",
            "length": "8,849 meters height",
        },
        {
            "id": 14,
            "title": "Niagara Falls",
            "description": "A natural wonder straddling Canada and the USA.",
            "location": { "lat": 43.0962, "lng": -79.0377 },
            "audio": "http://104.197.173.36:5000/audio/niagarafalls.mp3",
            "length": "51 meters height",
        },
        {
            "id": 15,
            "title": "Stonehenge",
            "description": "A prehistoric monument in England.",
            "location": { "lat": 51.1789, "lng": -1.8262 },
            "audio": "http://104.197.173.36:5000/audio/stonehenge.mp3",
            "length": "33 meters diameter (outer circle)",
        },
        {
            "id": 16,
            "title": "Golden Gate Bridge",
            "description": "A suspension bridge in San Francisco.",
            "location": { "lat": 37.8199, "lng": -122.4783 },
            "audio": "http://104.197.173.36:5000/audio/goldengate.mp3",
            "length": "2.7 km",
        },
        {
            "id": 17,
            "title": "Burj Khalifa",
            "description": "The tallest skyscraper in Dubai.",
            "location": { "lat": 25.1972, "lng": 55.2744 },
            "audio": "http://104.197.173.36:5000/audio/burjkhalifa.mp3",
            "length": "828 meters height",
        },
        {
            "id": 18,
            "title": "Victoria Falls",
            "description": "A massive waterfall in Africa.",
            "location": { "lat": -17.9243, "lng": 25.8572 },
            "audio": "http://104.197.173.36:5000/audio/victoriafalls.mp3",
            "length": "1,708 meters width",
        },
    ]
    return jsonify(wonders_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
