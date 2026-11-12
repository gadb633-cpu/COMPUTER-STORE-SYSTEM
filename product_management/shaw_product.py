from Helper_functions_and_validations.inputs import get_str,get_num
from Helper_functions_and_validations.validation import check_is_category
def get_info_to_search():
    search_by = get_str("enter search_by[id,name,category]")
    if search_by =="id":
        search_value = get_num("enter id")
    else:
        search_value = get_str(f"enter {search_by}")
    return [search_by,search_value]
def search_product_by_id(products,search_value):
    for product in products:
        if product["id"] == search_value:
            return [product]
    print("not found!")
    return [] 
def search_product(products,search_by,search_value):
    result = []
    if check_is_category(search_by)==False:
        print("it's not correct!")
        return result
    for product in products:
        if str(search_value).lower() in str(product[search_by]).lower():
            result.append(product)
    if result ==[]:
        print("not found!")
        return result
    return result

def display_products(results):
    for result in results:
        print(result)