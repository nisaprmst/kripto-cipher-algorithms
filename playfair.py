import numpy as np

class Playfair():
    def __init__(self):
        self.matrix = []
        self.keyword = ""
        self.has_keyword = False
        pass
    
    def set_key(self, key):
        matrix = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for e in key.upper():
            if e not in matrix:
                if e == 'J':
                    matrix.append('I')
                else:
                    matrix.append(e)
        for e in alphabet:
            if e not in matrix:
                matrix.append(e)
        self.has_keyword = True
        self.matrix = matrix

    def print_key(self):
        print("========KEY MATRIX========")
        print(self.mg[0])
        print(self.mg[1])
        print(self.mg[2])
        print(self.mg[3])
        print(self.mg[4])
        print("==========================")
    
    def set_cipher_text(self, text):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        text_mat = []
        for e in text.upper():
            if e == 'J':
                text_mat.append('I')
            elif e not in alphabet:
                pass
            else:
                text_mat.append(e)
        cnt = 0
        text_bigram = []
        while cnt < len(text_mat):
            if cnt+1 == len(text_mat):
                text_bigram.append([text_mat[cnt], 'X'])
                cnt += 1
                continue
            if text_mat[cnt] != text_mat[cnt+1]:
                text_bigram.append([text_mat[cnt], text_mat[cnt+1]])
                cnt += 2
            else:
                if text[cnt] == 'X':
                    text_bigram.append([text_mat[cnt], 'Z'])
                else:
                    text_bigram.append([text_mat[cnt], 'X'])
                cnt += 1
        self.text_bigram = text_bigram
        print(text_bigram)    
    def create_matrix(self):
        if self.has_keyword:
            mg = [[],[],[],[],[]]
            mg[0] = self.matrix[0:5]
            mg[1] = self.matrix[5:10]
            mg[2] = self.matrix[10:15]
            mg[3] = self.matrix[15:20]
            mg[4] = self.matrix[20:25]
            self.mg = mg
            print(self.mg)

        else:
            print('Assign key first by using set_key() method')
    
    def get_pos(self, letter):
        l = letter.upper()
        x = 0
        y = 0
        for i in range(5):
            for j in range(5):
                if self.mg[i][j] == l:
                    x = i
                    y = j
                    break
        return (x,y)

    def encrypt(self, text: str):
        self.set_cipher_text(text)
        ciphertext = ""
        for i in range(len(self.text_bigram)):
            letter_1 = self.text_bigram[i][0]
            letter_2 = self.text_bigram[i][1]
            pos_1 = self.get_pos(letter_1)
            pos_2 = self.get_pos(letter_2)
            if pos_1[0] == pos_2[0]:
                # same row
                ciphertext += self.mg[pos_1[0]][(pos_1[1]+1)%5]
                ciphertext += self.mg[pos_2[0]][(pos_2[1]+1)%5]
            elif pos_1[1] == pos_2[1]:
                # same column
                ciphertext += self.mg[(pos_1[0]+1)%5][pos_1[1]]
                ciphertext += self.mg[(pos_2[0]+1)%5][pos_2[1]]
            else:
                ciphertext += self.mg[pos_1[0]][pos_2[1]]
                ciphertext += self.mg[pos_2[0]][pos_1[1]]
        print(ciphertext)
        return ciphertext

    def decrypt(self, text: str):
        self.set_cipher_text(text)
        plaintext = ""
        for i in range(len(self.text_bigram)):
            letter_1 = self.text_bigram[i][0]
            letter_2 = self.text_bigram[i][1]
            pos_1 = self.get_pos(letter_1)
            pos_2 = self.get_pos(letter_2)
            if pos_1[0] == pos_2[0]:
                # same row
                plaintext += self.mg[pos_1[0]][(pos_1[1]-1)%5]
                plaintext += self.mg[pos_2[0]][(pos_2[1]-1)%5]
            elif pos_1[1] == pos_2[1]:
                # same column
                plaintext += self.mg[(pos_1[0]-1)%5][pos_1[1]]
                plaintext += self.mg[(pos_2[0]-1)%5][pos_2[1]]
            else:
                plaintext += self.mg[pos_1[0]][pos_2[1]]
                plaintext += self.mg[pos_2[0]][pos_1[1]]
        print(plaintext)
        return plaintext

