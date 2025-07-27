from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestChk():
    def test_checkout_1(self):
        assert CheckoutSolution().checkout("AAAAAAAAABBCD") == 460

    def test_checkout_2(self):
        assert CheckoutSolution().checkout("AACD") == 135

    def test_checkout_3(self):
        assert CheckoutSolution().checkout("G") == 20

    def test_checkout_4(self):
        assert CheckoutSolution().checkout("DCBA") == 115

    def test_checkout_5(self):
        assert CheckoutSolution().checkout("") == 0

    def test_checkout_6(self):
        assert CheckoutSolution().checkout("ABCDE") == 155

    def test_checkout_7(self):
        assert CheckoutSolution().checkout("AAAAAAED") == 305

    def test_checkout_8(self):
        assert CheckoutSolution().checkout("AAAABC") == 230

    def test_checkout_9(self):
        assert CheckoutSolution().checkout("EEEEEB") == 200

    def test_checkout_10(self):
        assert CheckoutSolution().checkout("FFFFFFF") == 50

    def test_checkout_11(self):
        assert CheckoutSolution().checkout("AAFF") == 120

    def test_checkout_12(self):
        assert CheckoutSolution().checkout("AAAAABBBEEFFF") == 345