
class SumSolution:
    
    def compute(self, x, y):
        """Return the result of sum x and y
            
            Args:
                x (int): Positive Integer between 0 and 100
                y (int): Positive Integer between 0 and 100.
            
            Returns:
                int: Sum of x and y.
                
        """
        
        if (isinstance(x,int) and x >= 0 and x <= 100) and (isinstance(y,int) and y >= 0 and y <= 100):
            return x + y
        else:
            raise ValueError("All imputs must be and integer between 0 and 100")
