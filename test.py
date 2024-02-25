# Początek programu
import time

question1 = input("jaka jest stolica Polski? ")
question2 = input("jaka jest stolica Francji ")
question3 = input("jaka jest stolica Niemiec ")

answer1 = "Warszawa"
answer2 = "Paryż"
answer3 = "Berlin"

if question1 == answer1:
    print("TO jest poprawna odpowiedz")
    print(answer1)
    for x in range(question1):
        print(x)
        time.sleep(5)
else:
    print("zła odpowiedz")

if question2 == answer2:
    print("TO jest poprawna odpowiedz")
    print(answer2)
    for y in range(question2):
        print(y)
        time.sleep(5)

else:
    print("zła odpowiedz")
if question3 == answer3:
    print("TO jest poprawna odpowiedz")
    print(answer3)
    for z in range(question3):
        print(z)
        time.sleep(5)
else:
    print("zła odpowiedz")



