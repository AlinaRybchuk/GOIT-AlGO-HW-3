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
def copy_file(file, source_dir, dist_dir):
    if file.endswith('.jpg'):
        target_dir = os.path.join(dist_dir, 'jpg')
    elif file.endswith('.png'):
        target_dir = os.path.join(dist_dir, 'png')
    elif file.endswith('.svg'):
        target_dir = os.path.join(dist_dir, 'svg')
    else:
        print(f"Unknown file type: {file}")
        return
    
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, file))
    print(f"Copied {file} to {target_dir}")

with ThreadPoolExecutor() as executor:
    files = os.listdir(source_dir)
    for file in files:
        executor.submit(copy_file, file, source_dir, dist_dir)
