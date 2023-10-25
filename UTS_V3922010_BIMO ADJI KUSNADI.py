def generate_key(text, keyword):
    keyword = keyword.upper()
    key_length = len(keyword)
    key_string = ""

    for i in range(len(text)):
        key_string += keyword[i % key_length]

    return key_string

def vigenere_encrypt(text, key):
    encrypted_text = ""
    text = text.upper()

    for i in range(len(text)):
        char_num = (ord(text[i]) - 65 + ord(key[i]) - 65) % 26
        char = chr(char_num + 65)
        encrypted_text += char

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    encrypted_text = encrypted_text.upper()

    for i in range(len(encrypted_text)):
        char_num = (ord(encrypted_text[i]) - 65 - (ord(key[i]) - 65)) % 26
        char = chr(char_num + 65)
        decrypted_text += char

    return decrypted_text

def affine_encrypt(text, a, b):
    encrypted_text = ""
    text = text.upper()

    for char in text:
        char_num = (a * (ord(char) - 65) + b) % 26
        char = chr(char_num + 65)
        encrypted_text += char

    return encrypted_text

def affine_decrypt(cipher, a, b):
    decrypted_text = ""
    mod_inverse = pow(a, -1, 26)

    for char in cipher:
        char_num = (mod_inverse * (ord(char) - 65 - b)) % 26
        char = chr(char_num + 65)
        decrypted_text += char

    return decrypted_text

def combined_encrypt(text, affine_key_a, affine_key_b, vigenere_key):
    affine_encrypted_text = affine_encrypt(text, affine_key_a, affine_key_b)
    vigenere_encrypted_text = vigenere_encrypt(affine_encrypted_text, vigenere_key)
    return vigenere_encrypted_text

def combined_decrypt(text, affine_key_a, affine_key_b, vigenere_key):
    vigenere_decrypted_text = vigenere_decrypt(text, vigenere_key)
    affine_decrypted_text = affine_decrypt(vigenere_decrypted_text, affine_key_a, affine_key_b)
    return affine_decrypted_text

# Program Utama
string = "Success is not final, failure is not fatal, it is the courage to continue that counts"
keyword_vigenere = "BIMO"
keyword_affine_a = 7
keyword_affine_b = 3

string = ''.join(filter(str.isalpha, string)).upper()
keyword_vigenere = ''.join(filter(str.isalpha, keyword_vigenere)).upper()

key_vigenere = generate_key(string, keyword_vigenere)
encrypt_text_vigenere = vigenere_encrypt(string, key_vigenere)

print("Hasil Enkripsi menggunakan Vigenere Cipher:", encrypt_text_vigenere)

encrypted_text = affine_encrypt(encrypt_text_vigenere, keyword_affine_a, keyword_affine_b)
print("Hasil Enkripsi menggunakan Vigenere Cipher dan Affine Cipher:", encrypted_text)

combined_encrypted_text = combined_encrypt(string, keyword_affine_a, keyword_affine_b, key_vigenere)
print("Hasil Enkripsi menggunakan Kombinasi Affine Cipher dan Vigenere Cipher:", combined_encrypted_text)

combined_decrypted_text = combined_decrypt(combined_encrypted_text, keyword_affine_a, keyword_affine_b, key_vigenere)
print("Hasil Deskripsi menggunakan Kombinasi Affine Cipher dan Vigenere Cipher:", combined_decrypted_text)
