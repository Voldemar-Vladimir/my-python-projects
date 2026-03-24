import os
from pathlib import Path

def get_files(folder_path):
    # возвращает список файлов (не папок)
    senior=[]
    junior_list=os.listdir(folder_path)
    for i in junior_list:
        p_path = os.path.join(folder_path, i)
        if os.path.isfile(p_path):
            senior.append(i)
        else:
            continue
    return senior
def create_folders(folder_path):
    # создаёт Images, Docs, Music, Archives, Other
    os.mkdir(os.path.join(folder_path, "Images"))
    os.mkdir(os.path.join(folder_path, "Docs"))
    os.mkdir(os.path.join(folder_path, "Archives"))
    os.mkdir(os.path.join(folder_path, "Music"))
    os.mkdir(os.path.join(folder_path, "Other"))
def move_files(folder_path):
    # проходит по файлам и перемещает
    files = get_files(folder_path)
    for s in files:
        s_path = Path(folder_path) / s
        if s_path.suffix == '.jpg' or s_path.suffix == '.jpeg' or s_path.suffix == '.png' or s_path.suffix == '.gif':
            old_path = Path(folder_path) / s
            new_folder = Path(folder_path) / "Images"
            new_path = new_folder / s
            new_folder.mkdir(exist_ok=True)
            old_path.rename(new_path)
        elif s_path.suffix == '.txt' or s_path.suffix == '.docx' or s_path.suffix == '.pdf' or s_path.suffix == '.xlsx':
            old_path = Path(folder_path) / s
            new_folder = Path(folder_path) / "Docs"
            new_path = new_folder / s
            new_folder.mkdir(exist_ok=True)
            old_path.rename(new_path)
        elif s_path.suffix == '.mp3' or s_path.suffix == '.wav' or s_path.suffix == '.flac':
            old_path = Path(folder_path) / s
            new_folder = Path(folder_path) / "Music"
            new_path = new_folder / s
            new_folder.mkdir(exist_ok=True)
            old_path.rename(new_path)
        elif s_path.suffix == '.zip' or s_path.suffix == '.rar' or s_path.suffix == '.7z':
            old_path = Path(folder_path) / s
            new_folder = Path(folder_path) / "Archives"
            new_path = new_folder / s
            new_folder.mkdir(exist_ok=True)
            old_path.rename(new_path)
        else:
            old_path = Path(folder_path) / s
            new_folder = Path(folder_path) / "Other"
            new_path = new_folder / s
            new_folder.mkdir(exist_ok=True)
            old_path.rename(new_path)
def main():
    path = input("Введи путь к папке (Enter — текущая): ").strip()
    if not path:
        path = os.getcwd()
    print(f"Работаем в {path}")
    
    create_folders(path)          # создаём папки
    move_files(path)               # перемещаем файлы
    print("Готово!")


if __name__ == "__main__":
    main()