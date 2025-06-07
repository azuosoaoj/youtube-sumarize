from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from src.handlers.get_transcription import get_youtube_transcript
from src.handlers.ai import ai

app = Flask(__name__, static_folder='src', static_url_path='')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory('src', 'index.html')

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    link = data.get('link')
    language = data.get('language')
    additional_infos = data.get('additional_infos')
    
    transcription = get_youtube_transcript(link)
    print(transcription)
    summary = ai(transcription, language, additional_infos)
    
    return jsonify({'summary': summary}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5002)
