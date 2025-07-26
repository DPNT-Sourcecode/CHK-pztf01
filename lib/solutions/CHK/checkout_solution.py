
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        sum = 0
        price_table = {"A": {"price" : 50, "special_offers" : {"units" : 3, "price" : 130}},
                "B": {"price" : 30, "special_offers" : {"units" : 2, "price" : 45}},
                "C": {"price" : 20},
                "D": {"price" : 15}}
        
        items_purchased = {}
        
        for i in skus:
            if i in items_purchased:
                items_purchased[i] = items_purchased[i] + 1
            else:
                items_purchased[i] = 1

        for i in items_purchased:
            quantity = items_purchased[i]
            
            if i in price_table:
                if "special_offers" in price_table[i]:
                    offer_unit = price_table[i]["special_offers"]["unit"]
                    offer_price = price_table[i]["special_offers"]["price"]
