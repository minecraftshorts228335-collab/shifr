import math

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Обратного элемента для ключа a={a} не существует.")

def affine_encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError(f"Ошибка: ключ a={a} не взаимно прост с 26.")
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            x = ord(char) - ord('a')
            encrypted_x = (a * x + b) % 26
            result.append(chr(ord('a') + encrypted_x))
        elif 'A' <= char <= 'Z':
            x = ord(char) - ord('A')
            encrypted_x = (a * x + b) % 26
            result.append(chr(ord('A') + encrypted_x))
        else:
            result.append(char)
    return ''.join(result)

def affine_decrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError(f"Ошибка: ключ a={a} не взаимно прост с 26.")
    a_inv = mod_inverse(a, 26)
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            x = ord(char) - ord('a')
            decrypted_x = (a_inv * (x - b)) % 26
            result.append(chr(ord('a') + decrypted_x))
        elif 'A' <= char <= 'Z':
            x = ord(char) - ord('A')
            decrypted_x = (a_inv * (x - b)) % 26
            result.append(chr(ord('A') + decrypted_x))
        else:
            result.append(char)
    return ''.join(result)