menu={"jira rice":130,"shevbhaji":120,"paneer tikka":250,"kajukari": 180,"tandur roti":35,"biryani":300,"veg pulav":160,"palak paneer":190,"mix veg":180,"soyabin chilli":250}


print("Welcome to FAUJI hotel")
print("here our menu:")
print("jira rice      : 130\nshevbhaji      : 120\npaneer tikka   : 250\nkajukari       : 180\ntandur  roti   : 35\nbiryani        : 300\nveg pulav      : 160\npalak paneer   : 190\nmix veg        : 180\nsoyabin chilli : 250")

total=0

item=(input("Enter item you want to order:"))
if item in menu:
   total= total + menu [item]
   print(f"{item } is added to your order")
else:
    print(f"{item} is not available")

another=(input("Do yo want to add another item (yes/no):"))   
if another=="yes":
    item_2=(input("Enter item name:"))
    if item_2 in menu :
        total = total + menu [item_2]
        print(f"{item_2} is added to your order")
    else:
        print(f"sorry {item_2} not available")

print("Total amount to pay:",total)
    