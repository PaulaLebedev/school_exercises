number = int(input("Sisestage mingi arv: "))

double = []
for num in range(0, number):
    double.append(num * num)

print (str(double)[1:-1])