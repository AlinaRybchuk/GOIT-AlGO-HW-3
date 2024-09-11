import os
import shutil

# Аргументи командного рядка
source_dir = "D:\ALINA\picture"
destination_dir = "D:\ALINA\dist"

# Задаємо замовчування для шляху до категорії
destination_dir = destination_dir if destination_dir else "dist"

# Переміщаємося до обох каталогів
os.chdir(source_dir)
os.makedirs(destination_dir, exist_ok=True)

# Сортуємо файли за типом
for file_extension in os.listdir(source_dir):
    if file_extension.endswith('.jpg'):
        os.makedirs(os.path.join(destination_dir, 'jpg'), exist_ok=True)
        for file in os.listdir(os.path.join(source_dir, file_extension)):
            shutil.copy(os.path.join(source_dir, file_extension, file), os.path.join(destination_dir, 'jpg', file))
    elif file_extension.endswith('.png'):
        os.makedirs(os.path.join(destination_dir, 'png'), exist_ok=True)
        for file in os.listdir(os.path.join(source_dir, file_extension)):
            shutil.copy(os.path.join(source_dir, file_extension, file), os.path.join(destination_dir, 'png', file))
    elif file_extension.endswith('.svg'):
        os.makedirs(os.path.join(destination_dir, 'svg'), exist_ok=True)
        for file in os.listdir(os.path.join(source_dir, file_extension)):
            shutil.copy(os.path.join(source_dir, file_extension, file), os.path.join(destination_dir, 'svg', file))
    else:
        print(f"{file_extension}")