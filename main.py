


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
    """Display information on the house"""
    print("\n ......House for Sale......")
    print(f"Style :{self.style.title()}\n Sq_footage : {self.sq_footage}\n Year Built : {self.year_built}\n Price : {self.price} \n Sold : {self.sold}\n Weeks on market : {self.weeks_on_mrket}" )

  def sell_house(self):
    """Sell the house"""
   if self.sold == False :
     print(f"Congrats! Your house sold for {self.price}")
     self.sold == True
    else:
      print("Sorry,this house is no longer for sale")
richards_house = House("bungalow",1200,1918,100000)

richards_house.display_info()
