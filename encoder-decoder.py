import base64
import sys

def to_binary(text):
    binary = []
    for i in text:
        binary.append(format(ord(i), '08b'))
    return ' '.join(binary)

def from_binary(binary):
    chars = binary.strip().split()
    text = ''
    for i in chars:
        text += chr(int(i, 2))
    return text

def to_hex(text):
    hex_list = []
    for i in text:
        hex_list.append(format(ord(i), '02x'))
    return ' '.join(hex_list)

def from_hex(hex_text):
    hex_values = hex_text.strip().split()
    text = ''
    for i in hex_values:
        text += chr(int(i, 16))
    return text

def to_base64(text):
    encoded = base64.b64encode(text.encode())
    return encoded.decode()

def from_base64(b64):
    decoded = base64.b64decode(b64)
    return decoded.decode()

def to_ascii_decimal(text):
    decimals = []
    for i in text:
        decimals.append(str(ord(i)))
    return ' '.join(decimals)

def from_ascii_decimal(decimal_string):
    numbers = decimal_string.strip().split()
    text = ''
    for i in numbers:
        text += chr(int(i))
    return text

def caesar_cipher(text, shift):
    result = ''
    for i in text:
        if i.isalpha():
            base = ord('A') if i.isupper() else ord('a')
            shifted = (ord(i) - base + shift) % 26
            result += chr(shifted + base)
        else:
            result += i
    return result

def xor_cipher(text, key):
    result = ''
    for i, c in enumerate(text):
        result += chr(ord(c) ^ ord(key[i % len(key)]))
    return result

def print_menu():
    print("""
          **************************
          |                        |
          |    ENCODER & DECODER   |
          |                        |
          **************************
          """)
    print("1. Codifica")
    print("2. Decodifica")
    print("3. Cifra")
    print("4. Decifra")
    print("0. Esci")

def print_menu_encode():
    print("1. Binario")
    print("2. Hex")
    print("3. Base64")
    print("4. ASCII decimale")

def print_menu_cipher():
    print("1. Cesare")
    print("2. XOR")

def main():
    print_menu()
    choice = input("Scelta: ")

    if choice == "1":
        text = input("Testo da codificare: ")
        print_menu_encode()
        t = input("Tipo: ")
        if t == "1":
            print(to_binary(text))
        elif t == "2":
            print(to_hex(text))
        elif t == "3":
            print(to_base64(text))
        elif t == "4":
            print(to_ascii_decimal(text))
        else:
            print("Tipo non valido.")

    elif choice == "2":
        print_menu_encode()
        t = input("Tipo: ")
        if t == "1":
            binary = input("Binario: ")
            print(from_binary(binary))
        elif t == "2":
            hex_text = input("Hex: ")
            print(from_hex(hex_text))
        elif t == "3":
            b64 = input("Base64: ")
            print(from_base64(b64))
        elif t == "4":
            decimals = input("ASCII decimale: ")
            print(from_ascii_decimal(decimals))
        else:
            print("Tipo non valido.")

    elif choice == "3":
        text = input("Testo da cifrare: ")
        print_menu_cipher()
        c = input("Tipo: ")
        if c == "1":
            shift = int(input("Shift: "))
            print(caesar_cipher(text, shift))
        elif c == "2":
            key = input("Chiave: ")
            encrypted = xor_cipher(text, key)
            print("Cifrato (base64):", base64.b64encode(encrypted.encode()).decode())
        else:
            print("Tipo non valido.")

    elif choice == "4":
        text = input("Testo da decifrare: ")
        print_menu_cipher()
        c = input("Tipo: ")
        if c == "1":
            shift = int(input("Shift: "))
            print(caesar_cipher(text, -shift))
        elif c == "2":
            key = input("Chiave (qualsiasi testo): ")
            try:
                encrypted_bytes = base64.b64decode(text)
                encrypted_text = encrypted_bytes.decode()
                decrypted = xor_cipher(encrypted_text, key)
                print("Decifrato:", decrypted)
            except Exception as e:
                print("Errore nella decifratura:", str(e))
        else:
            print("Tipo non valido.")

    elif choice == "0":
        print("Uscita...")
        sys.exit()

    else:
        print("Scelta non valida.")
        sys.exit()

if __name__ == "__main__":
    main()
