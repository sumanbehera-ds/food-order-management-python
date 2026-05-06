class Fooditem:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items =[]
    def add_item(self,item):
        self.items.append(item)
    def total_price(self):
        # total = 0
        # for item in self.items:
        #     total = total +item
        return sum(item.price for item in self.items)
    
class FOODORDERNGAPP:
    def __init__(self):
        self.menu = {
            "brger":Fooditem("burger",80),
            "salad":Fooditem("salad",100),
            "chicken":Fooditem("chicken",150),
            "pizza":Fooditem("pizza",200)
        }
        self.current_order = Order()

    def display_menu(self):
        print("menu")
        for item_name ,food_item in self.menu.items():
            print(f"{item_name}: ₹{food_item.price}")

    def display_order(self):
        print("current order: ")
        for item in self.current_order.items:
            print(f"{item.name}: ₹{item.price}")
        
        print(f"total: ₹{self.current_order.total_price()}")

    def start(self):
        print("WELCOME TO FOOD ORDERING APP")

        while True:
            print("\n1. view menu")
            print("2. add item to order")
            print("3. view current order")
            print("4. place order")
            print("5. exit")

            choice = input("Enter your choice: ")
            if choice=="1":
                self.display_menu()
            elif choice=="2":
                item_name = input("enter what you want to order: ")
                if item_name in self.menu:
                    self.current_order.add_item(self.menu[item_name])
                    print(f"{item_name} added to order")
                else:
                    print("invalid items ")
                
            elif choice=="3":
                self.display_order()
            elif choice=="4":
                print("order placed thank you")
                break
            elif choice=="5":
                print("Thanks for visiting")
                break
            else:
                print("enter a valid choice.try again")

if __name__=="__main__":
    app = FOODORDERNGAPP()
    app.start()    