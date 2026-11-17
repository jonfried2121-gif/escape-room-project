

def dict_printer(dictionary:dict):
    for key, val in dictionary.items():
        print(f"{key} : {val}")
    print("-----------")
    return

def list_printer(list_all):
    for dictionary in list_all:
        dict_printer(dictionary)
    return