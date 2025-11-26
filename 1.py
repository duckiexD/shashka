import hashlib

def calculate_file_hash(file_path):
    """Вычисляет SHA-256 хеш файла"""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            # Читаем файл по частям для обработки больших файлов
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def verify_file_integrity():
    """Проверяет целостность файла"""
    file_path = input("Путь к файлу: ").strip()
    known_hash = input("Известный хеш: ").strip().lower()
    
    # Вычисляем хеш файла
    file_hash = calculate_file_hash(file_path)
    
    if file_hash is None:
        return
    
    print(f"Вычисленный хеш: {file_hash}")
    print(f"Известный хеш:   {known_hash}")
    
    # Сравниваем хеши
    if file_hash == known_hash:
        print("✅ Файл целостен!")
    else:
        print("❌ Файл поврежден или изменен!")
