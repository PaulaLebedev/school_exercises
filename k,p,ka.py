import random
replay = "yes"
while replay == "yes":
    
    player_c = input("Vali kas kivi, paber, käärid: ")
    cpu = ('kivi', 'paber', 'käärid')
    cpu_c = random.choice(cpu)

    if player_c == cpu_c:
        print("Viik")
    elif player_c == "kivi" and cpu_c == "paber" or player_c == "käärid" and cpu_c == "kivi" or player_c == "paber" and cpu_c == "käärid":
        print("Loser")
    else:
        print("Winner")
    
    replay = input("Mängid edasi? ")
    