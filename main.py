import random
import string

def generate_simple_password():
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    
    num_lowercase = 6
    num_digits = 2
    
    password = (
        ''.join(random.choice(lowercase_letters) for _ in range(num_lowercase)) +
        ''.join(random.choice(digits) for _ in range(num_digits))
    )

    return ''.join(random.sample(password, len(password)))

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "/.,_"
    return ''.join(random.choice(characters) for _ in range(random.randint(9, 12)))

def main():
    first_time = True

    while True:
        if first_time:
            print("Выберите тип пароля:")
            print("1. Простой пароль (8 символов, строчные буквы и 2 цифры)")
            print("2. Сложный пароль (9-12 символов с прописными и строчными буквами, цифрами, спец символами: /, ., , или _)")
            print("0. Выйти")
            first_time = False

        choice = input("Введите номер выбора (0, 1 или 2): ")

        if choice == "0":
            print("Выход из программы.")
            break
        elif choice == "1":
            password = generate_simple_password()
        elif choice == "2":
            password = generate_strong_password()
        else:
            print("Неверный выбор. Пожалуйста, введите 0, 1 или 2.")
            continue

        print(f"Ваш пароль: {password}")

if __name__ == "__main__":
    main()
