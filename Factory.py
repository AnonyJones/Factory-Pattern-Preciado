 # In this line it creates a burger class and it defines the constructor method for Burger class, set parameter to ingredients, also it print the ingredients
class Burger: 
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

#It create another class Burger factory, and there is 3 method below each method creates a unique Burger and returns it.
class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["Bun", "Cheese", "Beef-patty"]
        return Burger(ingredients)

    def createDeluxeCheeseBurger(self):
        ingredients = ["Bun", "Cheese", "Tomato", "Lettuce", "Beef-patty"]
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients = ["Bun", "Special Sauce", "Vegan-patty"]
        return Burger(ingredients)   

 # This creates an instance of the BurgerFactory class and assigns it to a variable called "burgerFactory".        
burgerFactory = BurgerFactory()


 # This prints a welcome message and a list of burger options, then prompts the user to enter a number corresponding to their desired burger.
def introduction():
    print("Hello Welcome to Jones Burger! What would you like to order?")
    print("1. Cheese Burger \n2. Deluxe Burger \n3. Vegan Burger")
    order = int (input("\nChoose a number: "))


# If the user entered "1", this code calls the "createCheeseBurger" method of the "burgerFactory" instance to create a cheeseburger, 
# prints out the ingredients, then prompts the user to confirm their order. 
# If the user confirms their order by typing "yes", it prints a message indicating that a cheeseburger has been ordered. 
# If the user types "no", it calls the "introduction" function again to restart the order process.
# If the user enters anything else, it prints a message indicating that their choice is not available.
    if(order == 1):
        print("\nThis is the Following Ingredients: ")
        burgerFactory.createCheeseBurger().print()

        print("Proceed with the order?")
        question = input()

        if(question == 'yes'): 
            print("Burger para sayo: CHEEEESEBURGER")
        elif(question == 'no'):
            return introduction(), 
        else:
            print("Choices not available")

    if(order == 2):
            print("\nThis is the Following Ingredients: ")
            burgerFactory.createDeluxeCheeseBurger().print()
            print("Proceed with the order?")
            question = input()

            if(question == 'yes'): 
                    print("Burger para sayo: DeluxeBurger")
            elif(question == 'no'):
                return introduction(), 
            else:
                print("Choices not available")

    if(order == 3): 
            print("\nThis is the Following Ingredients: ")
            burgerFactory.createVeganBurger().print()  
            print("Proceed with the order?")
            question = input()

            if(question == 'yes'): 
                    print("Burger para sayo: VeggieBurger")
            elif(question == 'no'):
                return introduction(), 
            else:
                print("your choices is not available")



introduction()