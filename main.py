from shaw_results_and_menus.shaw_main_menu import shaw_main_menu
from Helper_functions_and_validations.inputs import get_num,get_str
from shaw_results_and_menus.shaw_product_menu import shaw_product_menu
from product_management.main_product import product_management

def main():
    status_loop = True
    while status_loop:
        shaw_main_menu()
        choice_main_menu = get_num("Choose an option")
        match choice_main_menu:
            case 1:
                product_management()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                status_loop = False
            case _:
                print("choice only between 1-5")

if __name__ == "__main__":
    main()