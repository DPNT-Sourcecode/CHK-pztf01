
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        basket_total = 0
        price_table = {"A": {"price" : 50, "special_offers" : [{"units" : 5, "price" : 200}, {"units" : 3, "price" : 130}]},
                "B": {"price" : 30, "special_offers" : {"units" : 2, "price" : 45}},
                "C": {"price" : 20},
                "D": {"price" : 15},
                "E": {"price" : 40,  "multi_offer" : {"units" : 2, "free_product" : "B", "free_quantity" : 1}}}
        
        items_purchased = {}
        
        for i in skus:
            if i not in price_table:
                return -1
            if i in items_purchased:
                items_purchased[i] = items_purchased[i] + 1
            else:
                items_purchased[i] = 1

        for i in items_purchased:
            # i = A
            quantity = items_purchased[i] # 35
            offer_unit = 1
            offer_price = 0
            price = 0
            cost = 0
            if i in price_table:
                price = price_table[i]["price"] # 50
                if "special_offers" in price_table[i]:
                    j = 0
                    while j >= 0:
                        offer_unit = price_table[i]["special_offers"][j]["units"] # 5
                        offer_price = price_table[i]["special_offers"][j]["price"] # 200
                
                        quotient = quantity//offer_unit
                        remainder = quantity % offer_unit

                        cost = cost + (quotient * offer_price)

                        if remainder > 0 and j < len(price_table[i]["special_offers"]) - 1:
                            j = j + 1
                            quantity = remainder
                        else:
                            j = -1

                    item_total_cost = cost + (remainder * price)
                
                else:
                    item_total_cost = price * quantity
            basket_total = basket_total + item_total_cost
                
        return basket_total





