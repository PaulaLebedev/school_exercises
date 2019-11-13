outcome = [8, 4, 5, 2, 8, 7]

outcome = list(dict.fromkeys(outcome))
outcome.sort()
print("Väljund: ", outcome[-2])