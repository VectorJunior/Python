# Początek programu
import time
time_out_y = 3

for x in range(time_out_y,0,-1):
    print(x)
    time.sleep(1)

question1 = input("jaka jest stolica Polski? ")
question2 = input("jaka jest stolica Francji? ")
question3 = input("jaka jest stolica Niemiec? ")

answer1 = "Warszawa"
answer2 = "Paryż"
answer3 = "Berlin"

time_out_x = 5
for x in range(time_out_x,0,-1):
    print(x)
    time.sleep(1)



if question1 == answer1:
    print("TO jest poprawna odpowiedz")

    print(answer1)
else:
    print("zła odpowiedz")

if question2 == answer2:
    print("TO jest poprawna odpowiedz")

    print(answer2)
else:
    print("zła odpowiedz")
if question3 == answer3:
    print("TO jest poprawna odpowiedz")

    print(answer3)
else:
    print("zła odpowiedz")



