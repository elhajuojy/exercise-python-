TimeInSeconds=int(input("donner le temps :"))
H=TimeInSeconds//3600
Rest=TimeInSeconds%3600
M=Rest//60
Seconds=Rest%60
print(f"Time is :{H}:{M}:{Seconds}")


