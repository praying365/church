balance = 100
def add(balance, x):
    global balance
    balance = balance + x
    return balance
a = int(input('a:'))
add(100, a)
print(f"{balance}+{a}={balance}")

