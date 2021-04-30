


class House():
  """A class to model a house that is for sale"""

  def __init__(self,style,sq_footage, year_built, price):
    """Initialize attributes"""
    self.style = style
    self.sq_footage = sq_footage
    self.year_built = year_built
    self.price = price
    
    self.sold = False
    self.weeks_on_mrket= 0
  
  def display_info(self):
    print(f"Style :{self.style.title()}\n Sq_footage : {self.sq_footage}\n Year Built : {self.year_built}\n Price : {self.price} \n Sold : {self.sold}\n Weeks on market : {self.weeks_on_mrket}" )