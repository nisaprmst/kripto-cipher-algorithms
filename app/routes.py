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
        vig.set_auto(request.json['auto'])
        vig.set_extended(request.json['extended'])
        vig.set_full(request.json['full'])
        result = vig.encrypt(text)
    elif cipher == 'affine':
        af = affine_cipher.Affine()
        key_a = key[0]
        key_b = key[1]
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
        inv_mat_2 = [[17,17,5], [21,18,21], [2,2,19]]
        hc = hill_cipher.Hill()
        encrypt = hc.encrypt(text, 3, inv_mat_2)
        result = hc.matrix2string(encrypt)
        print(result)
    else:
        status = 400
    return jsonify({'result': result, 'status' : status})