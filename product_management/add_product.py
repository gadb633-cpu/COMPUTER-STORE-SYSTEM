from Helper_functions_and_validations.inputs import get_num,get_str
from Helper_functions_and_validations.validation import is_name_exist
def add_product(products:list):
    id_num = len(products)+1
    status_loop = True
    while status_loop:
        name_product = get_str("enter name product")
        if is_name_exist(name_product,products) == False:
            continue
        category = get_str("enter category")
        price = float(get_num("enter price"))
        amount = get_num("enter amount")
        status_loop = False
    return {"id": id_num,    
            "name": name_product,    
            "category": category,    
            "price": price,    
            "stock": amount,    
            "active": True}
    
def save_product(product,products:list):
    products.append(product)
    print("Saved successfully!")