from flask import jsonify, request, render_template, redirect, url_for, abort
from .algorithms import vigenere as vigenere_cipher
from .algorithms import affine as affine_cipher
from .algorithms import hill as hill_cipher
from .algorithms import playfair as playfair_cipher
from .algorithms import supercipher as supercipher
from flask_cors import cross_origin

from . import app

data = {}

vig = vigenere_cipher.Vigenere()

@app.route('/api/process', methods=['POST'])
@cross_origin()
def process():
    if (not request.json or not ('type' in request.json and 'key' in request.json and 'text' in request.json)):
        abort(400)
    cipher = request.json['type']
    result = ''
    status = 200
    is_encrypt = request.json['command']
    key = request.json['key']
    text = request.json['text']
    if cipher == 'vigenere':
        print(len(text))
        vig.input_key(key[0])
        vig.set_auto(True if request.json['variant'] == 'v_auto' else False)
        vig.set_extended(True if request.json['variant'] == 'v_extended' else False)
        vig.set_full(True if request.json['variant'] == 'v_full' else False)
        #if request.json['variant'] == 'v_extended':
            #text = ''.join([chr(i) for i in text])
        if is_encrypt:
            if request.json['variant'] != 'v_extended':
                print("yeyyyyy")
                result = vig.encrypt_extended(text)
                result = ''.join([chr(x) for x in result])
                print(len(result))
            else:
                print("lho")
                result = vig.encrypt(text)

        else:
            if request.json['variant'] != 'v_extended':
                result = vig.decrypt_extended(text)
                result = ''.join([chr(x) for x in result])
                print(len(result))
            else:
                result = vig.decrypt(text)

    elif cipher == 'affine':
        af = affine_cipher.Affine()
        key_a = int(key[0])
        key_b = int(key[1])
        af.input_keys(key_a, key_b)
        if (af.check_coprime(af.key_a)):
            print('Keys are legal')
            if is_encrypt:
                result = af.encrypt(text, af.key_a, af.key_b)
            else:
                result = af.decrypt(text, af.key_a, af.key_b)
        else:
            status = 400
            result = "Keys must be coprime with 26. Choose another value!"
    elif cipher == 'playfair':
        pf = playfair_cipher.Playfair()
        pf.set_key(key[0])
        pf.create_matrix()
        if is_encrypt:
            result = pf.encrypt(text)
        else:
            result = pf.decrypt(text)
    elif cipher == 'hill':
        mat = []
        invertible_mat = [[6,24,1],[13,16,10],[20,17,14]]
        for row in request.json['key']:
            mat.append(row)
        print(mat)
        hc = hill_cipher.Hill()
        res = None
        if is_encrypt:
            res = hc.encrypt(text, len(mat), mat)
            # res = hc.encrypt(text, 3, invertible_mat)
        else:
            res = hc.decrypt(text, len(mat), mat)
            # res = hc.decrypt(text, 3, invertible_mat)
        print(res)
        result = hc.matrix2string(res)
        print(result)
    elif cipher == 'supercipher':
        sc = supercipher.Superencrypt()
        vg = vigenere_cipher.Vigenere()
        vg.input_key(key[0])
        if is_encrypt:
            result = sc.transpose(vg.encrypt(text))
        else:
            result = vg.decrypt(sc.transpose(text))
        print(result)
    else:
        status = 400
    return jsonify({'result': result, 'status' : status})