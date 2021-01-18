
number = 0

while number != 10:
    a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
    arg = input('뭐로 계산하고 싶나염 기호로 표시하세염 +, -, *, /: ')
    number += 1
    if arg == "+":
        print(a+b)
    elif arg == "-":
        print(a + b)
    elif arg == "*":
        print(a * b)
    elif arg == "/":
        print(a / b)
    else:
        print("그런거 안 넣음")
        break
#--------------------------------------------------------

#def plus(a, b):
#    return int(a)+int(b)

#a = input("숫자를 입력하세요")
#b = input("두번째 자를 입력하세요")

#print(plus(a,b))

#---------------------------------------------------------
