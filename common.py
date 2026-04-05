import random

def line():
    print("="*20)

def select(num, add=[]):
    l = [str(i + 1) for i in range(num)]
    l += add
    ans = input("選択:")
    while ans not in l:
        ans = input("再選択:")
    return ans

def prob(num):
    return random.randint(1,100) <= num
