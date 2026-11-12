from product_management.shaw_product import search_product_by_id,get_info_to_search
from Helper_functions_and_validations.validation import check_is_category
from Helper_functions_and_validations.inputs import get_num,get_str
def update_product(products,search_value,search_by,change_value):
    production = search_product_by_id(products,search_value)
    if check_is_category(search_by) == False:
        return "it's not correct!"
    for product in production:
        product[search_by] = change_value 
    return "Updated successfully"

def get_info_to_update():
    search_value = get_num("enter id")
    search_by = get_str("enter what you want to search [price,name,category,active]")
    if search_by == "price":
        change_value = float(get_num("enter new price"))
    else:    
        change_value = get_str("enter item to change")
    if search_by =="active":
        bool(change_value)
    return [search_value,search_by,change_value]


