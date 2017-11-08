#Zachary Zawaideh
#Commputer Programming
#10/12/17
s=0.0
d=''
PLANET=""
NAME=""
pc=""
QUIT=""


def startup():
    global NAME
    print("The objective of this game is to get your ship off of Earth and venture out of other planets.")
    print("When you are ready to quit there will be an option in between each planet.")
    print("Enjoy!")
    NAME = input("What is your name?: ")
    the_menu()


    
def the_menu():
    global d
    print("Menu: ")
    print("1. Start Game")
    print("2. Load Game")
    c = input("choice: ")

    if c == '1':
        global PLANET
        global w
        global s
        global pc

        PLANET = ("Earth")
        w = input("What is the wieght of your ship in pounds?: ")
        s = float(input("What is the speed of your ship in km/s?: "))
        d = input("What planet do you want to go to?: ").lower()
        print((NAME)+", you are on " +(PLANET)+ " and want to go to " +(d)+ ", the wieght of your ship is " +(w)+ " pounds.")
        escape_earth()

    if c == '2':
        pc= input("What is the planet code for the last planet you were on?: ")
        if pc=='marsbars':
            escape_mars()
        elif pc=='tinydot':
            escape_pluto
        elif pc=='hothothot':
            escape_sun()
        elif pc=='thermostat':
            escape_mercury()
        elif pc=='whereami':
            escape_venus()
        elif pc=='man_on_the_moon':
            escape_moon()
        elif pc=='red':
            escape_jupiter()
        elif pc=='green':
            escape_saturn()
        elif pc=='blue':
            escape_uranus()
        elif pc=='seagod':
            escape_neptune()
        else:
            print("Not a planet code!")
            the_menu()
        
        
    
    

def escape_earth():
    global s
    global d
    if s >= 11 and s <= 14:
        if d=='mars':
            escape_mars()
        elif d=='pluto':
            escape_pluto()
        elif d=='sun':
            escape_sun()
        elif d=='mercury':
            escape_mercury()
        elif d=='venus':
            escape_venus()
        elif d=='moon':
            escape_moon()
        elif d=='jupiter':
            escape_jupiter()
        elif d=='saturn':
            escape_saturn()
        elif d=='uranus':
            escape_uranus()
        elif d=='neptune':
            escape_neptune()
        else:
            print('not a destination')
            the_menu()

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()
        
def escape_mars():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Mars, what is your next destination?: ").lower()
    print("Your password code for mars is: marsbars")
    pc == "marsbars"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 4 and s <= 6:
        the_points()
        if d=='mars':
            escape_mars()
        elif d=='pluto':
            escape_pluto()
        elif d=='sun':
            escape_sun()
        elif d=='mercury':
            escape_mercury()
        elif d=='venus':
            escape_venus()
        elif d=='moon':
            escape_moon()
        elif d=='jupiter':
            escape_jupiter()
        elif d=='saturn':
            escape_saturn()
        elif d=='uranus':
            escape_uranus()
        elif d=='neptune':
            escape_neptune()
            
        else:
            print("Not a destination.")
            the_menu()
        
    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_pluto():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Pluto, what is your next destination?: ").lower()
    print("Your password code for pluto is: tinydot")
    pc == "tinydot"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 1 and s <= 3:
        the_points()
        if d=='mars':
            escape_mars()
        elif d=='pluto':
            escape_pluto()
        elif d=="sun":
            escape_sun()
        elif d=='mercury':
            escape_mercury()
        elif d=='venus':
            escape_venus()
        elif d=='moon':
            escape_moon()
        elif d=='jupiter':
            escape_jupiter()
        elif d=='saturn':
            escape_saturn()
        elif d=='uranus':
            escape_uranus()
        elif d=='neptune':
            escape_neptune()
        else:
            print("Not a destination.")
            the_menu()
    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_sun():
    global d
    global s
    global pc
    d = input("Yay you made it to the Sun, what is your next destination?: ").lower()
    print("Your password code for the sun is: hothothot")
    pc == "hothothot"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 616 and s <= 618:
       the_points()
       if d=='mars':
            escape_mars()
       elif d=='pluto':
            escape_pluto()
       elif d=='sun':
            escape_sun()
       elif d=='mercury':
            escape_murcury()
       elif d=='venus':
            escape_venus()
       elif d=='moon':
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
       elif d=='neptune':
            escape_neptune() 
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_mercury():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Mercury, what is your next destination?: ").lower()
    print("Your password code for mercury is: thermostat")
    pc == "thermostat"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 3 and s <= 6:
       the_points()
       if d=='mars':
            escape_mars()
       elif d=='pluto':
            escape_pluto()
       elif d=='sun':
            escape_sun()
       elif d=='mercury':
            escape_mercury()
       elif d=='venus':
            escape_venus()
       elif d=='moon':
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
       elif d=='neptune':
            escape_neptune()
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_venus():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Venus, what is your next destination?: ").lower()
    print("Your password code for venus is: whereami")
    pc == "whereami"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 9 and s <= 11:
       the_points()
       if d=='mars':
            escape_mars()
       elif d=='pluto':
            escape_pluto()
       elif d=='sun':
            escape_sun()
       elif d=='mercury':
            escape_mercury()
       elif d=='venus':
            escape_venus()
       elif d=='moon':
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
       elif d=='neptune':
            escape_neptune()
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_moon():
    global d
    global s
    global pc
    d = input("Yay you made it to the Moon, what is your next destination?: ").lower()
    print("Your password code for the moon is: man_on_the_moon")
    pc == "man_on_the_moon"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 1 and s <= 3:
       the_points()
       if d=='mars':
            escape_mars()
            escape_mars()
       elif d=='pluto':
            escape_pluto()
            escape_pluto()
       elif d=='sun':
            escape_sun()
            escape_sun()
       elif d=='mercury':
            escape_mercury()
            escape_mercury()
       elif d=='venus':
            escape_venus()
            escape_venus()
       elif d=='moon':
            escape_moon()
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
            escape_uranus()
       elif d=='neptune':
            escape_neptune()
            escape_neptune()
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_jupiter():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Jupiter, what is your next destination?: ").lower()
    print("Your password code for jupiter is: red")
    pc == "red"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 59 and s <= 61:
       the_points()
       if d=='mars':
            escape_mars()
       elif d=='pluto':
            escape_pluto()
       elif d=='sun':
            escape_sun()
       elif d=='mercury':
            escape_mercury()
       elif d=='venus':
            escape_venus()
       elif d=='moon':
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
       elif d=='neptune':
            escape_neptune()
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_saturn():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Saturn, what is your next destination?: ").lower()
    print("Your password code for saturn is: green")
    pc == "green"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 35 and s <= 37:
       the_points()
       if d=='mars':
            escape_mars()
       elif d=='pluto':
            escape_pluto()
       elif d=='sun':
            escape_sun()
       elif d=='mercury':
            escape_mercury()
       elif d=='venus':
            escape_venus()
       elif d=='moon':
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
       elif d=='neptune':
            escape_neptune()
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You made a sad-turn and blew up.")
        the_menu()

def escape_uranus():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Uranus, what is your next destination?: ").lower()
    print("Your password code for uranus is: blue")
    pc == "blue"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 20 and s <= 22:
       the_points()
       if d=='mars':
            escape_mars()
       elif d=='pluto':
            escape_pluto()
       elif d=='sun':
            escape_sun()
       elif d=='mercury':
            escape_mercury()
       elif d=='venus':
            escape_venus()
       elif d=='moon':
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
       elif d=='neptune':
            escape_neptune()
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def escape_neptune():
    global d
    global s
    global pc
    d = input("Yay you made it to planet Neptune, what is your next destination?: ").lower()
    print("Your password code for neptune is: seagod")
    pc == "seagod"
    x= input("Yes or no; are you ready to quit?: ").lower()
    if x=="yes":
        the_menu()
    s = float(input("How fast do you want to get there in km/s?: "))
    if s >= 22 and s <= 24:
       the_points()
       if d=='mars':
            escape_mars()
       elif d=='pluto':
            escape_pluto()
       elif d=='sun':
            escape_sun()
       elif d=='mercury':
            escape_mercury()
       elif d=='venus':
            escape_venus()
       elif d=='moon':
            escape_moon()
       elif d=='jupiter':
            escape_jupiter()
       elif d=='saturn':
            escape_saturn()
       elif d=='uranus':
            escape_uranus()
       elif d=='neptune':
            escape_neptune()
       else:
            print("Not a destination.")
            the_menu

    else:
        print("You were not going the correct speed and blew up.")
        the_menu()

def the_points():
    global d
    if d=='mars':
            print("Yay you got a point")
            escape_mars()
    elif d=='pluto':
            print("Yay you got a point")
            escape_pluto()
    elif d=='sun':
            print("Yay you got a point")
            escape_sun()
    elif d=='mercury':
            print("Yay you got a point")
            escape_mercury()
    elif d=='venus':
            print("Yay you got a point")
            escape_venus()
    elif d=='moon':
            print("Yay you got a point")
            escape_moon()
    elif d=='jupiter':
            print("Yay you got a point")
            escape_jupiter()
    elif d=='saturn':
            print("Yay you got a point")
            escape_saturn()
    elif d=='uranus':
            print("Yay you got a point")
            escape_uranus()
    elif d=='neptune':
            print("Yay you got a point")
            escape_neptune()
    else:
            print("Not a destination.")
            the_menu

def point_s():
    if d=='mars':
        print("Yay you got 2 points")
        escape_mars()
    elif d=='pluto':
        print("Yay you got 2 points")
        escape_pluto()
    elif d=='sun':
            print("Yay you got 2 points")
            escape_sun()
    elif d=='mercury':
            print("Yay you got 2 points")
            escape_mercury()
    elif d=='venus':
            print("Yay you got 2 points")
            escape_venus()
    elif d=='moon':
            print("Yay you got 2 points")
            escape_moon()
    elif d=='jupiter':
            print("Yay you got 2 points")
            escape_jupiter()
    elif d=='saturn':
            print("Yay you got 2 points")
            escape_saturn()
    elif d=='uranus':
            print("Yay you got 2 points")
            escape_uranus()
    elif d=='neptune':
            print("Yay you got 2 points")
            escape_neptune()
    else:
        print("Not a destination.")
        the_menu

            








        
    
        

        

 
    
    
startup()




          
        
    

