import random

nr = random.randint(1, 100)
loop = 1
times = 0

print("Arva ära number 1-100")

while loop == 1:
    guess = int(input("Sisesta arv: "))
    
    if guess == nr:
        times += 1
        print("Tubli, pakkumisi kokku: ", times)
        loop = 0
    elif guess <nr:
        times += 1
        print("Sinu pakutud arv on liiga väike")
    else:
        times += 1
        print("Sinu pakutud arv on liiga suur")