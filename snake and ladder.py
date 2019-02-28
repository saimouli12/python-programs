import

d = 0
p = 0
while true:
    r = input("press r to roll,q to quit :")
    if r == 'r':
       d = random.randint(1,6)
       print("you got :",d)
       if d==6:
           print("congratulations, you can play now.")
           