import hashlib

def hash_password(password):
    """Вычисляет SHA-256 хеш пароля"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def brute_force_password():
    """Находит пароль по его хешу методом брутфорса"""
    target_hash = input("Хеш: ").strip().lower()
    
    # Получаем список паролей
    passwords_input = input("Список паролей (через запятую): ").strip()
    passwords = [p.strip().strip("'\"[]") for p in passwords_input.split(',')]
    
    print(f"\nИщем пароль для хеша: {target_hash}")
    print(f"Проверяемые пароли: {passwords}")
    print("-" * 50)
    
    found_password = None
    
    for password in passwords:
        # Вычисляем хеш текущего пароля
        current_hash = hash_password(password)
        
        print(f"Пароль: '{password}' -> Хеш: {current_hash}")
        
        # Сравниваем с целевым хешем
        if current_hash == target_hash:
            found_password = password
            print(f"✅ СОВПАДЕНИЕ! Найден пароль: '{password}'")
            break
    
    if found_password:
        print(f"\n🎉 Пароль найден: '{found_password}'")
    else:
        print(f"\n❌ Пароль не найден в предоставленном списке")

# Альтернативная версия с предопределенным списком паролей
def brute_force_password_predefined():
    """Версия с предопределенными данными для тестирования"""
    target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6a88a4b5021eea1b7e7d9f1b"
    passwords = ['password', '123456', 'hello', 'secret', 'letmein']
    
    print(f"Ищем пароль для хеша: {target_hash}")
    
    for password in passwords:
        current_hash = hash_password(password)
        if current_hash == target_hash:
            print(f"✅ Найден пароль: '{password}'")
            return password
    
    print("❌ Пароль не найден")
    return None
