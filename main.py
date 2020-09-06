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

import affine as affine_cipher
import vigenere as vigenere_cipher
# af = affine_cipher.Affine()
# af.input_keys()
# if (af.check_coprime(af.key_a)):
#     print('Keys are legal')
#     text = str(input('Input text to be encrypted: '))
#     e_text = af.encrypt(text, af.key_a, af.key_b)
#     d_text = af.decrypt(e_text, af.key_a, af.key_b)
# else:
#     print('\'a\' must be coprime with 26')

vig = vigenere_cipher.Vigenere()
vig.key = "SONY"
vig.set_full(True)
vig.set_auto(True)
vig.set_extended(True)
vig.set_extended(False)
vig.set_full(False)
vig.set_auto(False)
text = "thisplaintext"
e_text = vig.encrypt(text)
d_text = vig.decrypt(e_text)