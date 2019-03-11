import yaml


def analyze_file_values(file_path, data_title):
    file_path = "./data/" + file_path + ".yaml"
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.load(f)
        data_list = list()
        for i in data[data_title].values():
            data_list.append(i)
        return data_list


def analyze_file_keys(file_path, data_title):
    file_path = "./data/" + file_path + ".yaml"
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.load(f)
        keys_list = list()
        for i in data[data_title].values():
            keys_list.append(i)
        return keys_list
