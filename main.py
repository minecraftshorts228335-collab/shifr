from caesar import caesar_cipher
from affine import affine_encrypt, affine_decrypt
from atbash import atbash_cipher

def main():
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ: ШИФРЫ НА PYTHON ===")
        print("1. Шифр Цезаря")
        print("2. Аффинный шифр")
        print("3. Шифр Атбаш")
        print("4. Выход")
        
        choice = input("Выберите пункт меню (1-4): ").strip()
        
        if choice == '1':
            text = input("Введите текст: ")
            try:
                shift = int(input("Введите шаг сдвига (целое число): "))
                encrypted = caesar_cipher(text, shift)
                decrypted = caesar_cipher(encrypted, -shift)
                print(f"\n[Результат]")
                print(f"Зашифровано: {encrypted}")
                print(f"Расшифровано: {decrypted}")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")
                
        elif choice == '2':
            text = input("Введите текст: ")
            try:
                a = int(input("Введите ключ a (взаимно простой с 26, например 5): "))
                b = int(input("Введите ключ b (например 8): "))
                encrypted = affine_encrypt(text, a, b)
                decrypted = affine_decrypt(encrypted, a, b)
                print(f"\n[Результат]")
                print(f"Зашифровано: {encrypted}")
                print(f"Расшифровано: {decrypted}")
            except ValueError as e:
                print(f"Ошибка: {e}")
                
        elif choice == '3':
            text = input("Введите текст: ")
            encrypted = atbash_cipher(text)
            decrypted = atbash_cipher(encrypted)
            print(f"\n[Результат]")
            print(f"Зашифровано: {encrypted}")
            print(f"Расшифровано: {decrypted}")
            
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

if __name__ == "__main__":
    main()