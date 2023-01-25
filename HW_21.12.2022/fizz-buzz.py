print("Task \"fizz-buzz\"")

fizz = int(input("Input fizz: "))
buzz = int(input("Input buzz: "))
max = int(input("Input max number: "))
i = 1
reply = []

while i <= max:
    if (fizz < 1) or (buzz < 1):
        print(f"+--------ERROR--------+\n"
              f"|Fizz {fizz} or Buzz {buzz} < 0 |\n"
              f"+------Try again------+")
        break
    if (i % fizz == 0) and (i % buzz == 0):
        reply.append("FB ")
    elif i % fizz == 0:
        reply.append("F ")
    elif i % buzz == 0:
        reply.append("B ")
    else:
        reply.append(str(i)+" ")
    i += 1
if reply:
    print(f"Reply:\n"
          f"{''.join(map(str, reply))}")
