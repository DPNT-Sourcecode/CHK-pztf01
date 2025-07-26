
class SumSolution:
    
    def compute(self, x, y):
        """Return the result of sum a and b
            
            Args:
                a (int): Positive Integer between 0 and 100
                b (int): Positive Integer between 0 and 100.
            
            Returns:
                int: Sum of a and b.
                
            """
        if (isinstance(a,int) and a > 0 and a < 100) and (isinstance(b,int) and b > 0 and b < 100):
            return a + b
        else:
            raise ValueError("All imputs must be and integer between 0 and 100")

