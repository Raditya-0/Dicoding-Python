"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.
def minimal(a, b):
    if a == b:
        return a  
    else:
        return a if a < b else b  


a = 10
b = 5

result = minimal(a, b)  
print(result) 
