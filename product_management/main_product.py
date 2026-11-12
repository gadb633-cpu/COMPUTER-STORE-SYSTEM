from shaw_results_and_menus.shaw_product_menu import shaw_product_menu
from Helper_functions_and_validations.inputs import get_num
from product_management.add_product import add_product,save_product
from db.products import PRODUCTS
from product_management.shaw_all_products import shaw_all_products
from product_management.shaw_product import search_product,get_info_to_search,display_products,search_product_by_id
from product_management.update_product import update_product,get_info_to_search,get_info_to_update
def product_management():
    status_loop = True
    while status_loop:
        shaw_product_menu()
        choice_product_menu= get_num("enter your choice")
        match choice_product_menu:
            case 1:
                new_product = add_product(PRODUCTS)
                save_product(new_product,PRODUCTS)
            case 2:
                shaw_all_products(PRODUCTS)
            case 3:
                info = get_info_to_search()
                if info[0] == "id":
                    display_products(search_product_by_id(PRODUCTS,info[1]))
                else:
                    display_products(search_product(PRODUCTS,info[0],info[1]))
            case 4:
                info_to_update = get_info_to_update()
                print(update_product(PRODUCTS,info_to_update[0],info_to_update[1],info_to_update[2]))
            case 5:
                pass
            case 6:
                break
            case _:
                print("choose only between 1-6")