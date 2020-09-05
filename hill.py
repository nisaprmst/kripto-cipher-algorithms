import numpy as np
ord_A = ord('A')
class Hill():
    def create_matrix(self, mat):
        pass

    def modInverse(self, a, m) : 
        a = a % m; 
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1

    def cofactor(self, mat):
        
        pass

    def cofactor_matrix(self, mat):
        pass

    def adj_mat(self, mat):
        numpy_mat = np.matrix(mat)
        print((numpy_mat * np.linalg.det(mat))%26)
        return numpy_mat.getH()


    def split_text(self, text: str, n):
        mat = []
        im_mat = []
        for i in range(len(text)):
            if i != len(text) - 1:
                if len(im_mat) == n:
                    mat.append(im_mat)
                    im_mat = []
                im_mat.append(text[i].upper())
            else:
                if len(im_mat) < n:
                    im_mat.append(text[i].upper())
                    n_iter = n - len(im_mat)
                    for i in range(n_iter):
                        im_mat.append('X')
                    mat.append(im_mat)
                else:
                    mat.append(im_mat)
                    im_mat = []
                    im_mat.append(text[i].upper())
                    n_iter = n - len(im_mat)
                    for i in range(n_iter):
                        im_mat.append('X')
                    mat.append(im_mat)
        self.text_mat = mat
        return mat

    def mat_char2ord(self, mat):
        res = []
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[i])):
                temp.append(ord(mat[i][j]) - ord_A)
            res.append(temp)
        return res
    
    def mat_ord2char(self, mat):
        res = []
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[i])):
                temp.append(chr(mat[i][j] + ord_A))
            res.append(temp)
        return res

    def verify_matrix(self, mat):
        is_invertible = False
        try:
            np.linalg.inv(mat)
            is_invertible = True
        except:
            pass
        return is_invertible

    def encrypt(self, text, n, mat):
        x_shape,y_shape = np.shape(mat)
        if x_shape != y_shape:
            print("Non-square matrix. Aborting")
            return None
        if x_shape != n:
            print("Incompatible matrix dimension and text grouping. Aborting")
            return None
        if self.verify_matrix(mat) == False:
            print("Non-invertible matrix. Aborting")
            return None
        text_arr = self.split_text(text, n)
        text_arr = self.mat_char2ord(text_arr)
        key_mat = np.array(mat)
        res_mat = []
        for parts in text_arr:
            mult = np.array(parts)
            mult = key_mat.dot(mult)
            mult %= 26
            res_mat.append(list(mult))
        return self.mat_ord2char(res_mat)
        

    def decrypt(self, text, n, mat):
        x_shape,y_shape = np.shape(mat)
        if x_shape != y_shape:
            print("Non-square matrix. Aborting")
            return None
        if x_shape != n:
            print("Incompatible matrix dimension and text grouping. Aborting")
            return None
        if self.verify_matrix(mat) == False:
            print("Non-invertible matrix. Aborting")
            return None
        text_arr = self.split_text(text, n)
        text_arr = self.mat_char2ord(text_arr)
        det_inv = self.modInverse(np.linalg.det(mat)%26, 26)
        decrypt_key_mat = (det_inv * self.adj_mat(mat))%26
        # print(decrypt_key_mat)
        pass