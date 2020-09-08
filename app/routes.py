from flask import jsonify, request, render_template, redirect, url_for, abort
from .algorithms import vigenere as vigenere_cipher
from .algorithms import affine as affine_cipher
from .algorithms import hill as hill_cipher
from .algorithms import playfair as playfair_cipher
from flask_cors import cross_origin

from . import app



data = {}

@app.route('/api/input', methods=['POST'])
@cross_origin()
def search_keywords():
    if (not request.json or not ('type' in request.json and 'key' in request.json and 'text' in request.json)):
        abort(400)
    cipher = request.json['type']
    result = ''
    status = 200
    key = request.json['key']
    text = request.json['text']
    if cipher == 'vigenere':
        vig = vigenere_cipher.Vigenere()
        vig.input_key(key[0])
        vig.set_auto(True if request.json['variant'] == 'v_auto' else False)
        vig.set_extended(True if request.json['variant'] == 'v_extended' else False)
        vig.set_full(True if request.json['variant'] == 'v_full' else False)
        result = vig.encrypt(text)
    elif cipher == 'affine':
        af = affine_cipher.Affine()
        key_a = int(key[0])
        key_b = int(key[1])
        af.input_keys(key_a, key_b)
        if (af.check_coprime(af.key_a)):
            print('Keys are legal')
            result = af.encrypt(text, af.key_a, af.key_b)
        else:
            status = 400
            result = "Keys must be coprime with 26. Choose another value!"
    elif cipher == 'playfair':
        pf = playfair_cipher.Playfair()
        pf.set_key(key[0])
        pf.create_matrix()
        result = pf.encrypt(text)
    elif cipher == 'hill':
        mat = []
        for row in request.json['key']:
            mat.append(row)
        print(mat)
        hc = hill_cipher.Hill()
        encrypt = hc.encrypt(text, len(mat), mat)
        result = hc.matrix2string(encrypt)
        print(result)
    else:
        status = 400
    return jsonify({'result': result, 'status' : status})