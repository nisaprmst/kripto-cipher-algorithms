from flask import jsonify, request, render_template, redirect, url_for, abort
from .algorithms import vigenere as vigenere_cipher
from flask_cors import CORS, cross_origin

app = Flask(__name__, template_folder="static")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

data = {}

@app.route('/api/input', methods=['POST'])
@cross_origin()
def search_keywords():
    if (not request.json or not ('type' in request.json and 'key' in request.json and 'text' in request.json)):
        abort(400)
    cipher = request.json['type']
    result = ''
    key = request.json['key']
    text = request.json['text']
    if cipher == 'vigenere':
        vig = vigenere_cipher.Vigenere()
        vig.input_key(key[0])
        vig.set_auto(request.json['auto'])
        vig.set_extended(request.json['extended'])
        vig.set_full(request.json['full'])
        result = vig.encrypt(text)
    return jsonify({'result': result})