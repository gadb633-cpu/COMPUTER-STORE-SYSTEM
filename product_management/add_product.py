from Helper_functions_and_validations.inputs import get_num,get_str

def add_product(products:list):
    id_num = len(products +1)
    name_product = get_str("enter name product")
    category = get_str("enter category")
    price = float(get_num("enter price"))
    amount = get_num("enter amount")
    return {"id": id_num,    
               "name": name_product,    
               "category": category,    
               "price": price,    
               "stock": amount,    
               "active": True}
    

def save_product(product,products:list):
    products.append(product)
    print("Saved successfully!")