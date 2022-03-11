print('Hello there! I have a cute little story about a mouse on the farm. I can not wait to tell you.')
print('I have a few questions to ask you first.')
print('After typing you answer, please press the enter key.')
input('Please press enter...')

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    veg = input('\nWhat is your favorite vegetable? ')
    while (len(veg) ==0):
        veg = input('Please enter a vegetable:')

    num = input('\nWhat is your favorite number: ')
    while not num.isdigit():
        num = input('Value not recognized. Please enter a numeric value: ')

    room = input('A room in a house: ')
    while (len(room) == 0):
        room = input('Please enter a room in a house: ')

    fruit = input('A type of fruit: ')
    while (len(fruit) == 0):
        fruit = input('Please enter a type of fruit:')

    fav_food = input('What is your favorite food? ')
    while (len(fav_food) == 0):
        fav_food = input('Please enter a favorite food:')

    user_name = input('What is your name? ')
    while (len(user_name) == 0):
        user_name = input('Please enter your name:')

    input('Please press enter to continue')

    print('\nNow we can start our story.')

    print('\nThere was once a little mouse named', user_name, '.')
    print(user_name, 'was a curious little mouse that lived on', veg, 'farm.')
    print('It was early in the morning when', user_name, 'decided to explore', veg, 'farm.')
    print(user_name, 'also wanted to collect some food for home.')
    print('As', user_name, 'was exploring, it saw Farmer', fruit, 'feeding the chickens.')
    print('The corn looked so good and', user_name, 'knew their mom could make good food with it.')
    print('Should the mouse get some corn?')

    corn = input('Please type yes or no\n')
    while corn.lower() != 'yes' and corn.lower() != 'no':
        corn = input('Please type yes or no:')


    if corn == 'no':
        print('\nThe mouse knew chickens liked chasing mice.')
        print(user_name, 'was mostly scared of', fav_food, '.')
        print(fav_food, 'is the biggest and fastest chicken in the lot.')
        print(user_name, 'had to feel it\'s best to outrun', fav_food, '.')
        print(user_name, 'did not feel good today, so it walked away before', fav_food, 'saw it.')
        print(user_name, 'was happy it walked away because it saw a friend that almost got caught by', fav_food, 'before.')

    else:
        print('\nWhen', user_name, 'saw', fav_food, 'it was scared.')
        print(fav_food, 'was the fastest chicken in the lot and', user_name, 'knew this.')
        print('Fortunately', user_name, 'was a fast mouse.')
        print('It had outrun', fav_food, 'several times.')
        print(user_name, 'ran into the chicken lot when', fav_food, 'was not looking.')
        print('It was able to grab', num, 'kernals of corn before', fav_food, 'saw it.')
        print(user_name, 'ran as fast as it could and escaped the lot right before', fav_food, 'caught it.')
        print('It put the corn in a bag and continued the exploring the farm.')

    print('\nLater in the day,', user_name, 'went into the', room, '.')
    print(user_name, 'discovered something when it went in the', room, '.')
    print('What did', user_name, 'discover?')
    discov = input('Was it a box or cheese?\n')
    while discov.lower() != "box" and discov.lower() != "cheese":
        discov = input('Please type box or cheese:')


    if discov == 'box':
        print('As', user_name, 'enterned the', room, 'it smelled something really good.')
        print('It had never smelled anything like it before.')
        print(user_name, 'came across a little black box.')
        print('It sniffed the opening of the box.')
        print(user_name, 'thought it smelled so good.')
        print('It slowly snuck in the box, unsure of what it was.')
        print('As', user_name, 'got to the back of the box, it saw a little green block.')
        print(user_name, 'had seen something like this before.')
        print('One of', user_name + '\'s friends brought this home before and everyone in the house got sick.')
        print(user_name, 'backed out of the box, and ran back home.')

    else:
        print(user_name, 'smell something familiar.')
        print('When it found the smell, it noticed a big piece of cheese.')
        print('The problem was that it was sitting on a mouse trap.')
        print(user_name, 'was a fast little mouse.')
        print('It had beat this thing several times before.')
        print(user_name, 'slowly walked close to the mouse trap and grabbed the cheese really fast.')
        print('It was so happy that not only did it get the cheese but the trap was not even triggered.')


    if corn == 'no' and discov == 'box':
        print('\nAfter searching all day for food', user_name, 'was too scared and went back home with no extra food for the family.')
        print('It was just happy that other family members were able to find food for the day.')
        print(user_name, 'was just happy that it made it home safe.')



    elif(corn == 'yes' and discov == 'box'):
        print(user_name, 'was able to come home with', num, 'kernels of corn.')
        print('They had so much corn that', user_name + '\'s', 'was able to make corn stew and cornbread for the whole family.')
    
    elif(corn == 'no' and discov == 'cheese'):
        print('When', user_name, 'came home with cheese, its mother was so happy.')
        print(user_name + '\'s', 'mother was able to make cheesecae for everyone.')

    elif(corn == 'yes' and discov == 'cheese'):
        print('When', user_name, 'came home, the family was surprised.')
        print(user_name, 'brought home', num, 'kernals of corn and a big piece of cheese.')
        print('The little mouse family held a big celebration that night, under the', room, '.')


    print('Every day that all of', user_name + '\'s family makes it home is a good day, because Farmer', fruit, 'is working hard to stop mice from being at', veg, 'farm.')
    print('It is a good thing Farmer', fruit, 'doesn\'t know that the whole mouse family lives under the', room + '.')
    print('\n The End')

    keepPlaying = input('\nDo you want to read the story again?' )
    while keepPlaying.lower() != 'yes' and keepPlaying.lower() != 'no':
        keepPlaying = input('Please type yes or no:')



