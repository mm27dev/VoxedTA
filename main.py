import time
import os
cyan = "\033[96m"
end = "\033[0m"
global coins
coins = 0
global buying_one
buying_one = False
items = {
    "Health Potion": "Increases 40 health when used. Can be used during, before, or after battle. Costs 5 coins each.",
    "Wooden Sword": "The most basic sword. Deals 10 damage per hit.Costs 15 coins.",
    "Wooden Shield": "The most basic shield. Blocks 10 damage per hit.Costs 25 coins.",
    "Full set of leather armor": "The most basic armor. Grants user 2 armor points .Grants .Costs 45 coins.",
    "Individual piece of leather armor": "The most basic armor. Armor points vary. Cost will also vary",
    "Snacks": "A delicious snack to help you fuel up on energy. Can be used during, before, or after battle. Costs 5 coins each. "
}
leather_armor_piece = {
    "Cap": "The most basic armor. Grants user 0.4 armor points . Costs 8 coins.",
    "Tunic": "The most basic armor. Grants user 0.8 armor points . Costs 16 Coins",
    "Pants": "The most basic armor. Grants user 0.5 armor points. Costs 14 coins",
    "Boots": "The most basic armor. Grants user 0.3 armor points. Costs 7 Coins"

}
item_costs = {
    "Health Potion": 5,
    "Wooden Sword": 15,
    "Wooden Shield": 25,
    "Full set of leather armor":45,
    "Cap": 8,
    "Tunic": 16,
    "Pants": 14,
    "Boots": 7,
    "Snacks": 5
}
global health_pot_num
health_pot_num = 0
global wood_sword_num
wood_sword_num = 0
global wood_shield_num
wood_shield_num = 0
global cap_num
cap_num = 0
global pants_num
pants_num = 0
global boots_num
boots_num = 0
global tunic_num
tunic_num  = 0
global snacks_num
snacks_num = 0
global inventory
inventory = {
    "Health Potion": health_pot_num,
    "Wooden Sword": wood_sword_num,
    "Wooden Shield": wood_shield_num,
    "Cap": cap_num,
    "Tunic": tunic_num,
    "Pants": pants_num,
    "Boots": boots_num,
    "Snacks": snacks_num

}
global wood_sword_state
wood_sword_state = "Not Equipped"
global wood_shield_state
wood_shield_state = "Not Equipped"
global cap_state
cap_state = "Not Equipped"
global tunic_state
tunic_state = "Not Equipped"
global pants_state
pants_state = "Not Equipped"
global boots_state
boots_state = "Not Equipped"
item_state = {
    "Wooden Sword": wood_sword_state,
    "Wooden Shield": wood_shield_state,
    "Cap":cap_state,
    "Tunic": tunic_state,
    "Pants":pants_state,
    "Boots": boots_state,
}


def leave_inv_for_story_continue():
    os.system("cls")
    print(cyan + "Well, thats it, you've got the hang of the mechanics. Now go conquer the world, adventurer!"+"\x1b[0m")
    print("\n\nEnd of Demo. Full version releasing soon.")
    print("Credits:")
    print("Main Head & Production: Mithun Mani")
    print("Created in 2024")

def re_open_demo_inv():
    time.sleep(1)
    global inventory
    os.system("cls")
    print("This is your inventory")
    for equip_check_a in inventory:
        print(equip_check_a + ": " + str(inventory[equip_check_a]))
    print(cyan + "Now, you have two options. You can equip/use an item(u), "
                 "un-equip; not for consumables(x), or exit your inventory(e) " + end)
    inv_action = input(">  ")
    if inv_action == "u":
        os.system("cls")
        print("Which Item would you like to equip/use? :")
        for equip_check_b in inventory:
            if inventory[equip_check_b] > 0:
                print(equip_check_b)
        use_item = input(">  ")
        for inven_check_a in inventory:
            if inventory[inven_check_a] > 0:
                if use_item == inven_check_a:
                    for equip_check_c in item_state:
                        if item_state[equip_check_c] == "Not Equipped" and use_item == equip_check_c:
                            print("Equipped/Used: " + inven_check_a)
                            item_state[equip_check_c] = "Equipped"
                            re_open_demo_inv()
                        elif item_state[equip_check_c] == "Equipped" and use_item == equip_check_c:
                            print("This item has already been equipped")
                            re_open_demo_inv()
    if inv_action == "x":
        os.system("cls")
        print("Which Item would you like to unequip :")
        for equip_check_d in inventory:
            if inventory[equip_check_d] > 0:
                if equip_check_d == "Wooden Sword" or equip_check_d == "Wooden Shield" or equip_check_d == "Cap" or equip_check_d == "Tunic" or equip_check_d == "Pants" or equip_check_d == "Boots":
                    print(equip_check_d)
        print(cyan + "If the above space is empty, that mean you have no gear, or your gear is already equipped.")
        print("If that is true, then answer 'q' to the next prompt. Or else, just answer with the name of the item."+end)

        unuse_item = input(">  ")
        if unuse_item == "q":
            re_open_demo_inv()
        if unuse_item != "q":
            for inven_check_d in inventory:
                if inven_check_d == "Wooden Sword" or inven_check_d == "Wooden Shield" or inven_check_d == "Cap" or inven_check_d == "Tunic" or inven_check_d == "Pants" or inven_check_d == "Boots":
                    if inventory[inven_check_d] > 0:

                        if unuse_item == inven_check_d:
                            for equip_check_e in item_state:
                                if unuse_item == equip_check_e and item_state[equip_check_e] == "Equipped":
                                    print("Un-equipped: " + unuse_item)
                                    item_state[equip_check_e] = "Not Equipped"
                                    re_open_demo_inv()
                                elif item_state[equip_check_e] == "Not Equipped" and unuse_item == equip_check_e:
                                    print("Item has already been Unequipped")
                                    re_open_demo_inv()

    if inv_action == "e":
        leave_inv_for_story_continue()


def demo_inventory():
    global inventory
    os.system("cls")
    print("This is your inventory")
    for equip_check_f in inventory:
        print(equip_check_f + ": "+str(inventory[equip_check_f]))
    print(cyan+ "Now, you have two options. You can equip/use an item(u), "
                "un-equip; not for consumables(x), or exit your inventory(e) " + end)
    inv_action = input(">  ")
    if inv_action == "e":
        leave_inv_for_story_continue()
    if inv_action == "u":
        os.system("cls")
        print("Which Item would you like to equip/use? :")
        for inven_check_f in inventory:
            if inventory[inven_check_f] > 0:
                print(inven_check_f)
        use_item = input(">  ")
        for equip_check_g in inventory:
            if inventory[equip_check_g] > 0:
                if use_item == equip_check_g:
                    for inven_check_h in item_state:
                        if item_state[inven_check_h] == "Not Equipped" and use_item == inven_check_h:
                            print("Equipped/Used: " + equip_check_g)
                            item_state[inven_check_h] = "Equipped"
                            re_open_demo_inv()
                        elif item_state[inven_check_h] == "Equipped" and use_item == inven_check_h:
                            print("This item has already been equipped")
                            re_open_demo_inv()
    if inv_action == "x":
        os.system("cls")
        print("Which Item would you like to unequip :")
        for inven_check_i in inventory:
            if inventory[inven_check_i] > 0:

                if inven_check_i == "Wooden Sword" or inven_check_i == "Wooden Shield" or inven_check_i =="Cap" or inven_check_i =="Tunic" or inven_check_i =="Pants" or inven_check_i =="Boots":
                    print(inven_check_i)
        print(cyan+"If the above space is empty, that mean you have no gear, or your gear is already equipped.")
        print("If that is true, then answer 'q' to the next prompt. Or else, just answer with the name of the item."+ end)


        unuse_item = input(">  ")
        if unuse_item == "q":
            re_open_demo_inv()
        if unuse_item != "q":
            for inven_check_j in inventory:
                if inven_check_j == "Wooden Sword" or inven_check_j == "Wooden Shield" or inven_check_j == "Cap" or inven_check_j == "Tunic" or inven_check_j == "Pants" or inven_check_j == "Boots":
                    if inventory[inven_check_j] > 0:

                        if unuse_item == inven_check_j:
                            for equip_check_h in item_state:
                                if unuse_item == equip_check_h and item_state[equip_check_h] == "Equipped":
                                    print("Un-equipped: "+unuse_item)
                                    item_state[equip_check_h] = "Not Equipped"
                                    re_open_demo_inv()
                                elif item_state[equip_check_h] == "Not Equipped" and unuse_item == equip_check_h:
                                    print("Item has already been Unequipped")
                                    re_open_demo_inv()








def leave_shop_for_story_continue():
    print("The villager wishes you a good day as you leave the shop.")
    print(cyan+"Remember, you can always access the shop whenever you'd like. During a prompt, answer 's' to access the shop")
    print(cyan +"Now, If you have purchased something, lets open up your inventory to access the item you have purchased")
    print("Answer 'e' to the next prompt to open up your inventory" + end)
    demo_inv = input(">  ")
    while demo_inv != "e":
        print("Invalid answer")
        demo_inv = input(">  ")
    if demo_inv == "e":
        demo_inventory()

def buy_action():
    global inventory
    global boots_num
    global pants_num
    global tunic_num
    global cap_num
    global coins
    global piece_key
    piece_key = 0
    global item_key
    item_key = 0
    global full_armor_key
    full_armor_key = 0
    for keyski in leather_armor_piece:
        if keyski == buying_one:
            piece_key = keyski
            print("Are you sure you would like to buy item: " + piece_key+"(y/n)?")

    if buying not in inventory:
        full_armor_key = "Full set of leather armor"
        print("Are you sure you would like to buy item: " + full_armor_key+"(y/n)?")


    for key1 in item_costs:
        if key1 == buying and buying != "Full set of leather armor":
            item_key = key1
            print("Are you sure you would like to buy item: " + item_key + "(y/n)?")

    for keyhoooooi in item_costs:
        if piece_key == keyhoooooi or item_key == keyhoooooi and (keyhoooooi == buying_one or keyhoooooi == buying) :
            print("This item will cost " + str(item_costs[keyhoooooi]) + " coins!")
            will_buy = input(">  ")
            if will_buy == "y":
                global coins
                if coins >= item_costs[keyhoooooi] :
                    coins -= item_costs[keyhoooooi]

                    for keyrooofg in inventory:
                        if keyrooofg == piece_key or keyrooofg == item_key:
                            inventory[keyrooofg] += 1
                    time.sleep(2)
                    print("Succesfully bought! You now have " + str(coins)+" coins left.")
                    create_regular_shop()
                else:
                    print("You cant afford this item!")
                    create_regular_shop()
            elif will_buy == "n":
                create_regular_shop()
    if full_armor_key == "Full set of leather armor":
        print("This item will cost 45 coins!")
        will_buy = input(">  ")
        if will_buy == "y":

            if coins >= 45:
                coins -= 45
                for keybro in inventory:
                    if keybro == "Cap":
                        inventory[keybro] += 1
                    elif keybro == "Tunic":
                        inventory[keybro] += 1
                    if keybro == "Pants":
                        inventory[keybro] += 1
                    if keybro == "Boots":
                        inventory[keybro] += 1

                print("Succesfully bought! You now have " + str(coins) + " coins left.")
                create_regular_shop()
            else:
                print("You cant afford this item!")
                create_regular_shop()
        elif will_buy == "n":
            create_regular_shop()

def create_regular_shop():
    time.sleep(2)
    print("Here are the items I am currently selling:")
    print("Health Potion")
    print("Wooden Sword")
    print("Wooden Shield")
    print("Full set of leather armor")
    print("Individual piece of leather armor")
    print("Snacks")
    time.sleep(1)
    print("What would you like to buy? Type in the exact name of the item to view it!(Or enter 'q' to leave the shop)")
    global buying
    buying = input(">  ")
    if buying == "q":
        leave_shop_for_story_continue()
    else:
        global key
        for key in items:

            if buying == key:
                if key == "Individual piece of leather armor":
                    global buying_one
                    buying_one = key
                    print("Here are the individual armor pieces I am selling:")
                    print("1.Cap")
                    print("2.Tunic")
                    print("3.Pants")
                    print("4.Boots")
                    print("What would you like to buy? Type in the exact name of the item to view it!")

                    buying_one = input(">  ")
                    for keyhe in leather_armor_piece:
                        if keyhe == buying_one:
                            print("Item you are viewing: " + key)
                            time.sleep(2)
                            print("Description:")
                            print(leather_armor_piece[keyhe])
                            buy_action()
                else:
                    print("Item you are viewing: " + key)
                    time.sleep(2)
                    print("Description:")
                    print(items[key])
                    buy_action()


def create_demo_shop():
    print("Welcome to my shop!")
    print("Feel free to take a look around!")
    time.sleep(4)
    os.system("cls")
    print("Here are the items I am currently selling:")
    print("Health Potion")
    print("Wooden Sword")
    print("Wooden Shield")
    print("Full set of leather armor")
    print("Individual piece of leather armor")
    print("Snacks")
    time.sleep(1)
    print(cyan + "For demo purposes, lets buy something. I have supplied you with 50 coins that you can use for anything you'd like. Enjoy!" + end)
    time.sleep(4)
    global coins
    coins = 50
    print("What would you like to buy? Type in the exact name of the item to view it!(Or enter 'q' to leave the shop)")
    global buying
    buying = input(">  ")
    if buying == "q":
        leave_shop_for_story_continue()

    else:
        global key
        for key in items:

            if buying == key:
                if key == "Individual piece of leather armor":
                    global buying_one
                    buying_one = key
                    print("Here are the individual armor pieces I am selling:")
                    print("1.Cap")
                    print("2.Tunic")
                    print("3.Pants")
                    print("4.Boots")
                    print("What would you like to buy? Type in the exact name of the item to view it!")

                    buying_one = input(">  ")
                    os.system("cls")
                    for keyeee in leather_armor_piece:
                        if keyeee == buying_one:
                            print("Item you are viewing: " + keyeee)
                            time.sleep(2)
                            print("Description:")
                            print(leather_armor_piece[keyeee])
                            buy_action()
                else:
                    print("Item you are viewing: " + key)
                    time.sleep(2)
                    print("Description:")
                    print(items[key])
                    buy_action()




def instructions():
    time.sleep(1)
    print("Hello.I am your guide. Whenever you need to learn something, I will talk to you about it. \nYou will know when I am talking when you see Cyan text "+ cyan  + "like this" + end )
    print("Instructions:")
    time.sleep(0.5)
    print("1. Complete the map to win.")
    print("2. Collect coins from chests and battles and spend them at the shop!")
    print("3. ALWAYS remember to export a save at the end of each session!")
    print("4. Read each prompt carefully so you know what to type in the next time an input box comes!")
    print("5. You have an armor, health, and energy bar. Use snacks and health potions to fill up your energy and health bar, and equip armor to increase the amount of points in your armor bar.")
    print("6. The health and energy bar have 100 points, while the armor bar has 10 points. ")
    print("7. HAVE FUN!")
    print("Good luck, "+ name)
    time.sleep(20)
def start_new():
    print("Loading game....")
    time.sleep(2)
    print("Tip: You can take your chances at opening chests for coins, but there may be be a monster hiding inside!")
    time.sleep(5)
    print("Game Ready!")
    time.sleep(2)
    os.system("cls")
    time.sleep(2)
    print("You wake up to another sunny morning. Its another perfect day for coin hunting in your village! ")
    time.sleep(3)
    print()
    print("The village shopkeeper says hello to you. He beckons you to his shop. You accept and take a look around his shop")
    time.sleep(5)
    os.system("cls")
    create_demo_shop()



print("Welcome to Voxed.")
time.sleep(2)
print("Tip: For a better experience, make the console bigger")
name = input("Enter your name\n>")
print("Hello, "+name+".Loading experience....")

time.sleep(3)
os.system('cls')

print("-")
time.sleep(0.2)
os.system('cls')

print("\\")
time.sleep(0.2)
os.system('cls')

print("|")
time.sleep(0.2)
os.system('cls')

print("/")
time.sleep(0.2)
os.system('cls')
print("-")
time.sleep(0.2)
os.system('cls')

print("-")
time.sleep(0.2)
os.system('cls')

print("\\")
time.sleep(0.2)
os.system('cls')

print("|")
time.sleep(0.2)
os.system('cls')

print("/")
time.sleep(0.2)
os.system('cls')
print("-")
time.sleep(0.2)
os.system('cls')

print("-")
time.sleep(0.2)
os.system('cls')

print("\\")
time.sleep(0.2)
os.system('cls')

print("|")
time.sleep(0.2)
os.system('cls')

print("/")
time.sleep(0.2)
os.system('cls')
print("-")
time.sleep(0.2)
os.system('cls')

print("-")
time.sleep(0.2)
os.system('cls')

print("\\")
time.sleep(0.2)
os.system('cls')

print("|")
time.sleep(0.2)
os.system('cls')

print("/")
time.sleep(0.2)
os.system('cls')
print("-")
time.sleep(0.2)
os.system('cls')


# -\|/-

#Initialize Home screen
print("-"*20)
print()
print("Welcome! Would you like to start a new game(n) or load a save (s)")
action = input(">")
if action == "n":
    print("New game successfully started")
    instructions()

    start_new()

    os.system("cls")
    #create_demo_shop()
    leave_inv_for_story_continue()
