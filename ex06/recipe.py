class col:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


sandwich = {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
            "meal": "lunch",
            "prep_time": 10
            }
cake = {"ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
        }
salad = {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
         "meal": "lunch",
         "prep_time": 15
         }
cookbook = {}
cookbook.update({'sandwich': sandwich})
cookbook.update({'cake': cake})
cookbook.update({'salad': salad})


def display_help():
    print(col.OKBLUE, end="")
    print("Please select an option by typing the corresponding number:")
    print("1. Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\033[0m")


def cookbook_add(name, ing, meal, time):
    recipe = {
        "ingredients": ing,
        "meal": meal,
        "prep_time": time
        }
    cookbook.update({name: recipe})


def cookbook_del(ssel):
    if ssel in cookbook:
        cookbook.pop(ssel)
    else:
        print(col.FAIL)
        print("Recipe for ", ssel, " does not exist.", col.ENDC, sep="")
    print()


def cookbook_display(ssel):
    if ssel in cookbook:
        print("Recipe for ", ssel, ":", sep="")
        print("Ingredients list:", cookbook[ssel]["ingredients"])
        print("To be eaten for ", cookbook[ssel]["meal"], ".", sep="")
        print("Takes", cookbook[ssel]["prep_time"], "minutes of cooking.")
    else:
        print(col.FAIL, end="")
        print("Recipe for ", ssel, " does not exist.", col.ENDC, sep="")
    print()


def cookbook_display_all():
    for ssel in cookbook:
        cookbook_display(ssel)
    display_help()


display_help()
while(1):
    sel = input()
    print()
    if (sel == "1"):
        name = input("Please enter the recipe's name to add:\n")
        ing = []
        print("Please enter the recipe's ingredients:")
        print("(Use ""exit"" when you are done)")
        while (1):
            in_ing = input()
            if (in_ing == "exit"):
                break
            ing.append(in_ing)
        meal = input("Please enter the recipe's type:\n")
        time = input("Please enter the recipe's preparation time in min:\n")
        cookbook_add(name, ing, meal, time)
        display_help()
    elif (sel == "2"):
        ssel = input("Please enter the recipe's name to delete it:\n")
        cookbook_del(ssel)
        display_help()
    elif (sel == "3"):
        ssel = input("Please enter the recipe's name to get its details:\n")
        print()
        cookbook_display(ssel)
        display_help()
    elif (sel == "4"):
        cookbook_display_all()
    elif (sel == "5"):
        print("Cookbook closed.")
        break
    else:
        print(col.FAIL, end="")
        print("This option does not exist, ", end="")
        print("please type the corresponding number.", col.ENDC)
        print("To exit, enter 5.")
