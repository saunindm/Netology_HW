import os

BASE_PATH = os.getcwd()
SORTED_DIR_NAME = 'files to sort'
SORTED_FILE_NAME = 'sorted.txt'
sorted_file_path = os.path.join(BASE_PATH, SORTED_FILE_NAME)
catalog_path = os.path.join(BASE_PATH, SORTED_DIR_NAME)
files_list = os.listdir(catalog_path)

lines_quantity = []
files_dict = {}

for file in files_list:
    with open(os.path.join(catalog_path, file), 'r', encoding='utf-8') as file_obj:
        raw_data = file_obj.read()
    with open(os.path.join(catalog_path, file), 'r', encoding='utf-8') as file_obj:
        lines = file_obj.readlines()
        lines = [line.strip() for line in lines if line != '\n']
        files_dict[file] = (len(lines), raw_data)
        sorted_files_tup = sorted(files_dict.items(), key=lambda x: x[1])

with open(sorted_file_path, 'a', encoding='utf-8') as file_obj:
    for el in sorted_files_tup:
        result = (
            f"{el[0]}\n"
            f"{el[1][0]}\n"
            f"{el[1][1]}\n\n"
        )
        file_obj.write(result)