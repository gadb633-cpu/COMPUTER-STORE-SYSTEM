
def val_not_empty(name):
    if name =="":
        return False
    return True
def is_positive(num):
    if num > 0:
        return True
    return False
def is_name_exist(name,products):
    for product in products:
        if product["name"] ==name:
            return False
    return True    
def check_is_category(search_by):
    if search_by in ["id","name","category","active","price"]:
        return True
    return False