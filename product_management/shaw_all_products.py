def shaw_all_products(products):
    for product in products:
        if product["active"] == True:
            print(product)