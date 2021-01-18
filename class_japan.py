money = 5000

ORANGE = "오렌지"
COLA = "콜라"
MILK = "우유"

class japan():
    def __init__(self, *args):
        self.orange = 1500
        self.cola = 1000
        self.milk = 500

for bbang_one in str(money):
    arg = input("구매할 음료수를 선택하세요 (1 ~ 3)")
    ab = japan()

    if arg == "1":
        if money > ab.orange:
            money -= ab.orange
            print(f"{ORANGE}를 구매했습니다. 잔액: {money}원")
        else:
            print(f"님 음료수 살 돈도 없네요.. {ab.orange}원이에요..")
            break

    elif arg == "2":
        if money > ab.cola:
            money -= ab.cola
            print(f"{COLA}를 구매했습니다. 잔액: {money}원")
        else:
            print(f"님 음료수 살 돈도 없네요.. {ab.cola}원이에요..")
            break

    else:
        if money > ab.milk:
            money -= ab.milk
            print(f"{MILK}를 구매했습니다. 잔액: {money}원")
        else:
            print(f"님 음료수 살 돈도 없네요.. {ab.milk}원이에요..")
            break
