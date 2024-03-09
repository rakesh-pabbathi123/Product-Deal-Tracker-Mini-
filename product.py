
# Define a class named Product
class Product:
  
  # Define a constructor method to initialize the object with provided attributes
  def __init__(self, name, price, deal_price, ratings):
    # Set the 'name' attribute of the object to the provided 'name' parameter
    self.name = name
    # Set the 'price' attribute of the object to the provided 'price' parameter
    self.price = price
    # Set the 'deal_price' attribute of the object to the provided 'deal_price' parameter
    self.deal_price = deal_price
    # Set the 'ratings' attribute of the object to the provided 'ratings' parameter
    self.ratings = ratings
    # Calculate the amount saved by subtracting 'deal_price' from 'price', and store it in 'you_save'
    self.you_save = price - deal_price

  # Define a method to display the details of the product
  def display_product_details(self):
      # Print the name of the product
      print("Product: {}".format(self.name))
      # Print the original price of the product
      print("Price: {}".format(self.price))
      # Print the deal price of the product
      print("Deal Price: {}".format(self.deal_price))
      # Print the amount saved on the deal
      print("You Saved: {}".format(self.you_save))
      # Print the ratings of the product
      print("Ratings: {}".format(self.ratings))
   
  # Define a method to get the deal price of the product
  def get_deal_price(self):
    # Return the deal price of the product
    return self.deal_price

# Define a class named ElectronicItem which inherits from the Product class
class ElectronicItem(Product):
   
  # Define a method to display the details of the electronic item
  def display_product_details(self):
    # Call the display_product_details method of the parent class (Product)
    super().display_product_details()
    # Print the warranty period of the electronic item
    print("Warranty {} months".format(self.warranty_in_months))
    
  # Define a method to set the warranty period of the electronic item
  def set_warranty(self, warranty_in_months):
    # Set the 'warranty_in_months' attribute of the object to the provided 'warranty_in_months' parameter
    self.warranty_in_months = warranty_in_months
    
  # Define a method to get the warranty period of the electronic item
  def get_warranty(self):
    # Return the warranty period of the electronic item
    return self.warranty_in_months

# Create an instance 'e' of the ElectronicItem class with specified attributes
e = ElectronicItem("Laptop",45000, 40000,3.5)
# Set the warranty period of the electronic item 'e' to 10 months
e.set_warranty(10)
# Display the details of the electronic item 'e'
e.display_product_details()


# This Python code defines two classes: `Product` and `ElectronicItem`. The `Product` class represents a generic product with attributes like name, price, deal price, and ratings, along with methods to display details and get the deal price. The `ElectronicItem` class inherits from the `Product` class and adds attributes specific to electronic items like warranty period, along with methods to set and get the warranty period and display the details. Finally, an instance of the `ElectronicItem` class is created, and its details are displayed.
# Output:
# Product: Laptop
# Price: 45000
# Deal Price: 40000
# You Saved: 5000
# Ratings: 3.5
# Warranty 10 months