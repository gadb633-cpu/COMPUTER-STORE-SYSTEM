from Helper_functions_and_validations.validation import val_not_empty,is_positive
def get_str(msg):
    status_loop = True
    while status_loop:
        name = input(f"{msg}:").strip()
        if val_not_empty(name) == False:
            continue
        status_loop = False
        return name
        
def get_num(msg):
    status_loop = True
    while status_loop:
        try:
            num = int(input(f"{msg}:").strip())
            if is_positive(num) == False:
                print("enter positive num")
                continue
            status_loop = False
            return num
        except ValueError as error:
            print(f"{error},try again!!")
            



