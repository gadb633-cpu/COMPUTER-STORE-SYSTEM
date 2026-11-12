from shaw_results_and_menus.shaw_product_menu import shaw_product_menu
from Helper_functions_and_validations.inputs import get_num
from product_management.add_product import add_product,save_product
from db.products import PRODUCTS

def product_management():
    status_loop = True
    while status_loop:
        shaw_product_menu()
        choice_product_menu= get_num("enter your choice")
        match choice_product_menu:
            case 1:
                new_product = add_product(PRODUCTS)
                save_product(new_product,PRODUCTS)
                print(new_product)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("choose only between 1-6")


    