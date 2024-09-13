import os
from concurrent.futures import ThreadPoolExecutor
import shutil

# Вказані директорії 
source_dir = "D:/Projects   IT/vscode-basics/web_module_03/pictures"
dist_dir = "D:/Projects   IT/vscode-basics/web_module_03/dist"

# Переміщаємося до обох каталогів
os.listdir(source_dir)
os.makedirs(dist_dir)

# Перебирає всі файли у директорії 
def copy_files(file_extension, source_dir, dist_dir):
   for file_extension in os.listdir(source_dir):
    if file_extension.endswith('.jpg'):
        os.makedirs(os.path.join(dist_dir, 'jpg'), exist_ok=True)
        for file in os.listdir(os.path.join(source_dir, file_extension)):
            shutil.copy(os.path.join(source_dir, file_extension, file), os.path.join(dist_dir, 'jpg', file))
    elif file_extension.endswith('.png'):
        os.makedirs(os.path.join(dist_dir, 'png'), exist_ok=True)
        for file in os.listdir(os.path.join(source_dir, file_extension)):
            shutil.copy(os.path.join(source_dir, file_extension, file), os.path.join(dist_dir, 'png', file))
    elif file_extension.endswith('.svg'):
        os.makedirs(os.path.join(dist_dir, 'svg'), exist_ok=True)
        for file in os.listdir(os.path.join(source_dir, file_extension)):
            shutil.copy(os.path.join(source_dir, file_extension, file), os.path.join(dist_dir, 'svg', file))
    else:
        print(f"Невідомий тип файлу: {file_extension}")

# Використати ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    executor.map(copy_files, os.listdir(source_dir))


