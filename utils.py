import json
import os


def load_data(file_name: str) -> list:
    """
    load data from local file
    :param file_name: name of import file
    :return: list of dictionaries
    """
    path_file = os.path.join(os.getcwd(), "data", file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data

print(load_data("operations.json"))