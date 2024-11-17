import string

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        decrypted_text.append(chr(value + 65))
    
    return "".join(decrypted_text)

def brute_force_vigenere(ciphertext, max_key_length, dictionary):
    for key_length in range(1, max_key_length + 1):
        for key in generate_keys(key_length):
            decrypted_text = vigenere_decrypt(ciphertext, key)
            if is_valid_text(decrypted_text, dictionary):
                print(f"Found valid key: {key} -> {decrypted_text}")

def generate_keys(length):
    characters = string.ascii_uppercase
    if length == 1:
        return characters
    else:
        return [a + b for a in generate_keys(1) for b in generate_keys(length - 1)]

def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = set(word.strip().upper() for word in file)
    return words

def is_valid_text(text, dictionary):
    words = text.split()
    return all(word in dictionary for word in words)

def main():
    ciphertext = input("Introduce la palabra cifrada con Vigenere: ").upper()
    max_key_length = int(input("Introduce la longitud máxima de la clave: "))
    dictionary = load_dictionary('dictionary.txt')
    brute_force_vigenere(ciphertext, max_key_length, dictionary)

if __name__ == "__main__":
    main()