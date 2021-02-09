f = open("reservations.csv")

for reservation in f:
    name, number = reservation.split(",")
    try:
    chairs_per_person = 50 // int(number)
    except ValueError:
        print("The number should be an integer and not a number")

    except ZeroDivisionError:
        print("You cannot reserve 0 chairs. dumbdumb")
        
    print("{} will get {} chairs per person".format(name, chairs_per_person))
