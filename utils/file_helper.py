import pickle
from tkinter import filedialog as fd


def save_test_cases_into_file(test_cases):
    file_path = call_file_save_dialog()

    with open(file_path, 'w+b') as file:
        pickle.dump(test_cases, file)

    print("Test cases were saved")

def deserialization_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = pickle.load(file)
            return files
    except AttributeError as ex:
        print("Deserialization file is not supported.")
        raise ex

    except Exception as ex:
        print("Please use correct serialized file.")
        raise ex

def load_file(file_path) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError as ex:
        print(f"File {file_path} not found.")
        raise ex

def call_file_save_dialog():
    file_path = fd.asksaveasfilename(filetypes=[("Test Cases", ".data")], defaultextension=".data")
    return file_path

def call_file_open_dialog():
    file_path = fd.askopenfilename()
    return file_path