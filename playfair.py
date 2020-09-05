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
        text_mat = []
        for e in text.upper():
            if e == ' ':
                pass
            elif e == 'J':
                text_mat.append('I')
            else:
                text_mat.append(e)
        if len(text_mat)%2==1:
            text_mat.append('X')
        self.text_mat = text_mat
        print(text_mat)
    
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

    def encrypt(self):
        for i in range(len(self.text_mat)/2):
            letter_1 = self.mg[i*2]
            letter_2 = self.mg[i*2 + 1]
            pos_1 = self.get_pos(letter_1)
            pos_2 = self.get_pos(letter_2)
            if pos_1[0] == pos_2[0]:
                # same row
                pass
            elif pos_1[1] == pos_2[1]:
                # same column
                pass
            else:
                pass

