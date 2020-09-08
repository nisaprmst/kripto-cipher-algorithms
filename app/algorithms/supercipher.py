import math
class Superencrypt():
    ''' This transpose function just swap the  '''
    def transpose(self, text: str):
        string_arr = [];
        string_len = len(text)
        for i in text:
            print(i)
            string_arr.append(i)
        print(len(text))
        print(len(string_arr))
        print(string_len//2)
        for i in range(string_len//2):
            string_arr[i], string_arr[string_len-i-1] = string_arr[string_len-i-1], string_arr[i]
        return ''.join(string_arr)
    pass