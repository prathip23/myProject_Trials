import math
class SquareRoot:
  def __init__(self, value):
    self.value = value
    self.approx_value = math.isqrt(int(value))

  def calculate_square_root(self):
      # Divide this by n an approximate root of N
    quotient = int(self.value) / self.approx_value
      #Mean of the quotient Formula (n+N/n)/2
    mean = (self.approx_value + quotient) / 2
    #print("Mean of the quotient", mean)
    if round(quotient, 6) == round(mean, 6):
        print("Square root of",self.value, "is", mean)
        return mean
    else:
        self.approx_value = mean
        return self.calculate_square_root()

Num = input('Enter an integer: ')
sqrt = SquareRoot(Num)
sqrt.calculate_square_root()