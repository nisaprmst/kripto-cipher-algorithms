""" import playfair as pf

PlayfairEngine = pf.Playfair()
key = str(input('Insert your key: '))
PlayfairEngine.set_key(key)
PlayfairEngine.create_matrix()
text = str(input('Insert your cipher text: '))
PlayfairEngine.set_cipher_text(text)
PlayfairEngine.print_key()
print(PlayfairEngine.get_pos(PlayfairEngine.text_mat[0]))
print(PlayfairEngine.get_pos(PlayfairEngine.text_mat[1]))

 """

""" import affine as affine_cipher
af = affine_cipher.Affine()
af.input_keys()
if (af.check_coprime(af.key_a)):
    print('Keys are legal')
    text = str(input('Input text to be encrypted: '))
    e_text = af.encrypt(text, af.key_a, af.key_b)
    d_text = af.decrypt(e_text, af.key_a, af.key_b)
else:
    print('\'a\' must be coprime with 26') """

import hill as hill_cipher
invertible_mat = [[6,24,1],[13,16,10],[20,17,14]]
inv_mat_2 = [[17,17,5], [21,18,21], [2,2,19]]
non_invertible_mat = [[9,6], [12,8]]
n2_mat = [[3,3],[2,5]]
input_text = "ARUNGAGAMANIBUD"
input2 = "HELP"
hc = hill_cipher.Hill()
encrypt = hc.encrypt(input_text, 3, inv_mat_2)
encrypted_text = hc.matrix2string(encrypt)
print(encrypted_text)
decrypted_text = hc.decrypt(encrypted_text, 3, inv_mat_2)
print(hc.matrix2string(decrypted_text))

""" import vigenere as vigenere_cipher
vig = vigenere_cipher.Vigenere()
vig.key = "SONY"
text = "thisplaintext"
e_text = vig.encrypt(text)
d_text = vig.decrypt(e_text) """
