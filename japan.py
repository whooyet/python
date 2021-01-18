money = 5000

orange = 1000
cola = 1000
milk = 500

ORANGE = "오렌지"
COLA = "콜라"
MILK = "우유"

def japan():
    arg = input("구매할 음료수를 선택하세요 (1 ~ 3)")

    global money

    if arg == "1":
        if money > orange:
            money -= orange
            print(f"{ORANGE}를 구매했습니다. 잔액: ({money - orange}원)")
        else:
            print(f"님 음료수 살 돈도 없네요.. {orange}원이에요..")

    elif arg == "2":
        if money > cola:
            money -= cola
            print(f"{COLA}를 구매했습니다. 잔액: ({money - cola}원)")
        else:
            print(f"님 음료수 살 돈도 없네요.. {cola}원이에요..")

    else:
        if money > milk:
            money -= milk
            print(f"{MILK}를 구매했습니다. 잔액: ({money - milk}원)")
        else:
            print(f"님 음료수 살 돈도 없네요.. {milk}원이에요..")
    japan()

japan()
