import math

ord_A = ord('A')
legal_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Affine():
    def input_keys(self):
        self.key_a = int(input('Insert key a: '))
        self.key_b = int(input('Insert key b: '))

    def set_keys(self, a, b):
        self.key_a = a
        self.key_b = b

    def check_coprime(self, a):
        return (True if math.gcd(a,26) == 1 else False)
    
    def encrypt(self, text: str, a, b):
        print('Encrypting...')
        res = ""
        if self.check_coprime(a):
            for e in text.upper():
                if e == ' ':
                    pass
                elif e in legal_alphabet:
                    e_ = self.encrypt_func(ord(e), a,b)
                    res += e_
                    print('{} is legal and transformed to {}'.format(e, e_))
            print("Final text is: {}".format(res))
            self.encrypted = res
            return res
        else:
            print('Key \'a\' must be coprime with 26. Choose another value!')
            return ""
    
    def decrypt(self, text: str, a:int, b:int):
        print('Decrypting...')
        res = ""
        if self.check_coprime(a):
            for e in text.upper():
                if e == ' ':
                    pass
                elif e in legal_alphabet:
                    e_ = self.decrypt_func(ord(e), a,b)
                    res += e_
                    # print('{} is legal and transformed to {}'.format(e, e_))
            print("Final text is: {}".format(res))
            self.decrypted = res
            return res
        else:
            print('Key \'a\' must be coprime with 26. Choose another value!')
            return ""
        pass

    def encrypt_func(self, letter, a, b):
        transformed_letter_ord = letter - ord_A
        transformed_letter_ord *= a
        transformed_letter_ord += b
        transformed_letter_ord %= 26
        return chr(transformed_letter_ord + ord_A)
    
    def decrypt_func(self, letter:int, a:int, b:int):
        decrypted = letter - ord_A
        decrypted = self.modInverse(a, 26) * (decrypted - b)
        decrypted %= 26
        return chr(decrypted + ord_A)

    def modInverse(self, a, m) : 
        a = a % m; 
        for x in range(1, m) : 
            if ((a * x) % m == 1) : 
                return x 
        return 1



