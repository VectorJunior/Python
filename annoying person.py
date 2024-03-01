# Początek programu

import time

while True:
    time_out = 2

    for time_out in range(time_out, 0, -1):
        print(time_out)
        time.sleep(1)

    input1 = input("kto cię denerwuje w kalsie? ")
    person1 = "Oliwier"
    person2 = "Mikołaj"

    if input1 == person1:
        time_out = 2

        for time_out in range(time_out, 0, -1):
            print(time_out)
            time.sleep(1)

        print("Zgadłeś,wygałeś 6+")
        print(person1)
        break

    if input1 == person2:
        time_out = 2

        for time_out in range(time_out, 0, -1):
            print(time_out)
            time.sleep(1)

        print("Zgadłeś,wygałeś 6+")
        print(person2)
        break

    else:
        print("OJ bardzo żle próbuj ponownie")

# koniec programu