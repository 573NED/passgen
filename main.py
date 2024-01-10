import random
import string

def generate_simple_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(8))

def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(random.randint(9, 12)))

def main():
    print("Выберите тип пароля:")
    print("1. Простой пароль (8 символов, только прописные буквы и цифры)")
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
