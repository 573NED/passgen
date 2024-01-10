import random
import string

def generate_simple_password():
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    
    password_length = (8)
    num_digits = random.randint(1, min(2, password_length - 1))
    num_lowercase = password_length - num_digits
    
    password = (
        ''.join(random.choice(lowercase_letters) for _ in range(num_lowercase)) +
        ''.join(random.choice(digits) for _ in range(num_digits))
    )

    return ''.join(random.sample(password, len(password)))

def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(random.randint(9, 12)))

def main():
    print("1. Простой пароль (8 символов, строчные буквы и 1-2 цифры)")
    print("2. Сложный пароль (9-12 символов с прописными, заглавными буквами, цифрами и спец символами)")

    choice = input("Введите номер выбора (1 или 2): ")

    if choice == "1":
        password = generate_simple_password()
    elif choice == "2":
        password = generate_strong_password()
    else:
        print("Неверный выбор. Пожалуйста, введите 1 или 2.")
        return

    print(f"Ваш пароль: {password}")

if __name__ == "__main__":
    main()
