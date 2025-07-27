
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        basket_total = 0
        price_table = {
                "A": {"price" : 50, "special_offers" : [{"units" : 5, "price" : 200}, {"units" : 3, "price" : 130}]},
                "B": {"price" : 30, "special_offers" : [{"units" : 2, "price" : 45}]},
                "C": {"price" : 20},
                "D": {"price" : 15},
                "E": {"price" : 40,  "multi_offer" : {"units" : 2, "free_product" : "B", "free_quantity" : 1}},
                "F": {"price" : 10,  "multi_offer" : {"units" : 2, "free_product" : "F", "free_quantity" : 1}},
                "G": {"price" : 20,},
                "H": {"price" : 10, "special_offers" : [{"units" : 10, "price" : 80}, {"units" : 5, "price" : 45}]},
                "I": {"price" : 35},
                "J": {"price" : 60},
                "K": {"price" : 80,  "special_offers" : [{"units" : 2, "price" : 150}]},
                "L": {"price" : 90},
                "M": {"price" : 15},
                "N": {"price" : 40, "multi_offer" : {"units" : 3, "free_product" : "M", "free_quantity" : 1}},
                "O": {"price" : 10},
                "P": {"price" : 50, "special_offers" : [{"units" : 5, "price" : 200}]},
                "Q": {"price" : 30, "special_offers" : [{"units" : 3, "price" : 80}]},
                "R": {"price" : 50, "multi_offer" : {"units" : 3, "free_product" : "Q", "free_quantity" : 1}},
                "S": {"price" : 30},
                "S": {"price" : 30},
                "N": {"price" : 40, "multi_offer" : {"units" : 3, "free_product" : "M", "free_quantity" : 1}},
                "A": {"price" : 50, "special_offers" : [{"units" : 5, "price" : 200}, {"units" : 3, "price" : 130}]},
                "S": {"price" : 20},
                "T": {"price" : 20},
                "U": {"price" : 40, "multi_offer" : {"units" : 3, "free_product" : "U", "free_quantity" : 1}},
                "V": {"price" : 50, "special_offers" : [{"units" : 3, "price" : 130}, {"units" : 2, "price" : 90}]},
                "W": {"price" : 20},
                "X": {"price" : 17},
                "Y": {"price" : 20},
                "Z": {"price" : 21},
                }
        
        group_offers = {"G1" : {"group" : ["Z", "Y", "S", "T", "X"], "group_quantity" : 3, "group_price" : 45}}
        
        items_purchased = {}
        items_group={}

        for i in skus:
            if i not in price_table:
                return -1
            if i in items_purchased:
                items_purchased[i]["item_count"] = items_purchased[i]["item_count"] + 1
                for j in group_offers:
                    if i in group_offers[j]["group"]:
                        items_purchased[i]["item_group"]="G1"
                        if i in items_group:
                            items_group[i] = items_group[i] + 1
                        else:
                            items_group[i] = 1 
            else:
                items_purchased[i] = {"item_count": 1}

        for i in items_purchased:
            quantity = items_purchased[i]["item_count"]
            if i in price_table:
                if "multi_offer" in price_table[i]:
                    units = price_table[i]["multi_offer"]["units"]
                    free_product = price_table[i]["multi_offer"]["free_product"]
                    free_quantity = price_table[i]["multi_offer"]["free_quantity"]

                    quotient = quantity//units

                    if free_product == i:
                        frees = ((free_quantity * quantity)//(units + free_quantity))
                        items_purchased[i]["item_count"] = items_purchased[i]["item_count"] - frees
                    else:
                        if free_product in items_purchased:
                            items_purchased[free_product]["item_count"] = items_purchased[free_product]["item_count"] - quotient
                            if items_purchased[free_product]["item_count"] < 0:
                                items_purchased[free_product]["item_count"] = 0

        for i in items_purchased:
            # i = A
            quantity = items_purchased[i]["item_count"] # 35
            if quantity ==0:
                pass

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

                        if remainder > 0:
                            quantity = remainder
                            if j < len(price_table[i]["special_offers"]) - 1:
                                j = j + 1
                            else:
                                j = -1
                        else:
                            j = -1

                    item_total_cost = cost + (remainder * price)
                
                else:
                    item_total_cost = price * quantity
            basket_total = basket_total + item_total_cost
                
        return basket_total




