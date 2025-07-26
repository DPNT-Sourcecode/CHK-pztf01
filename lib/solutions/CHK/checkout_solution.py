
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        basket_total = 0
        price_table = {"A": {"price" : 50, "special_offers" : {"units" : 3, "price" : 130}},
                "B": {"price" : 30, "special_offers" : {"units" : 2, "price" : 45}},
                "C": {"price" : 20},
                "D": {"price" : 15}}
        
        items_purchased = {}
        
        if len(skus) == 0:
            return -1
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
            if i in price_table:
                if "special_offers" in price_table[i]:
                    offer_unit = price_table[i]["special_offers"]["units"] # 3
                    offer_price = price_table[i]["special_offers"]["price"] # 130
            
                price = price_table[i]["price"] # 50

            
            quotient = quantity//offer_unit
            remainder = quantity % offer_unit

            item_total_cost = (quotient * offer_price) + (remainder * price)
            
            basket_total = basket_total + item_total_cost
                
        return basket_total




