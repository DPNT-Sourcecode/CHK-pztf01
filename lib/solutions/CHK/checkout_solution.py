
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        sum = 0
        dict = {"A": {"price" : 50, "special_offers" : {"units" : 3, "price" : 130}},
                "B": {"price" : 30, "special_offers" : {"units" : 2, "price" : 45}},
                "C": {"price" : 20},
                "D": {"price" : 15}}
        

