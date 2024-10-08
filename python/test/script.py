import os
import shutil
import datetime

def backup(source_dir, dest):
    today = datetime.date.today().strftime("%Y-%m-%d")
    dest_dir = os.path.join(dest, today)
    
    # Проверяем, существует ли директория
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    try:
        shutil.copytree(source_dir, dest_dir, dirs_exist_ok=True)
        print(f"Backup successful to {dest_dir}")
    except Exception as e:
        print(f"Error during backup: {e}")

source = input("Input source: ")
dest = input("Input destination: ")
backup(source, dest)
