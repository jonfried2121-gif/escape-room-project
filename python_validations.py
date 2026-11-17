

def number_validation(number):
    try:
        num = int(number)
        if num <= 0:
            print("please enter a valid number")
            return
        return number
    except ValueError:
        print("enter  only integer")
        return
    
def is_empty(string:str):
    if string.strip() == "":
        return True
    return

