from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def checkout_test1(self):
        assert CheckoutSolution().checkout("AAABBCD") == 210

    def checkout_test2(self):
        assert CheckoutSolution().checkout("AACD") == 135

    def checkout_test3(self):
        assert CheckoutSolution().checkout("G") == -1

    def checkout_test4(self):
        assert CheckoutSolution().checkout("DCBA") == 115

    def checkout_test(self):
        assert CheckoutSolution().checkout("") == -1