bal = {"Igor Ezerskiy": [1, 5, 7, 4],
       "Vasia Pupkin": [5, 1, 8, 2],
       "Oleg Fomenko": [1, 1, 2, 5],
       "Ilia Gorban": [1, 4, 5, 8]}

for k, v in bal.items():
    bal[k] = sum(v)/len(v)

print(f"{[(key, val) for key, val in bal.items() if val == max(bal.values())]}\n"
      f"{[(key, val) for key, val in bal.items() if val == min(bal.values())]}")
