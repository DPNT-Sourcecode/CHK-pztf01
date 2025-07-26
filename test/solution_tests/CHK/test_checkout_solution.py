from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestChk():
    def test_checkout_1(self):
        assert CheckoutSolution().checkout("AAABBCD") == 210

    def test_checkout_2(self):
        assert CheckoutSolution().checkout("AACD") == 135

    def test_checkout_3(self):
        assert CheckoutSolution().checkout("G") == -1

    def test_checkout_4(self):
        assert CheckoutSolution().checkout("DCBA") == 115

    def test_checkout_5(self):
        assert CheckoutSolution().checkout("") == 0