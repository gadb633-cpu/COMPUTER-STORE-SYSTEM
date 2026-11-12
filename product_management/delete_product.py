from Helper_functions_and_validations.inputs import get_num,get_str

def delete_product(products):
    num_id = get_id_to_delete()
    if get_allowed() == "no":
        return
    elif get_allowed() =="yes":
        for product in products:
            if product["id"] == num_id:
                products.remove(product)
                return "Successfully deleted"

def get_allowed():
    while True:
        allowed = get_str("Are you sure? [y/n]")
        if allowed.lower() not in ["yes","no"]:
            print("only [y/n]!")
            continue
        return allowed

def get_id_to_delete():
    num_id = get_num("enter id to delete")
    return num_id