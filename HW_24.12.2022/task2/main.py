from random import randint

print("Task \"fizz-buzz\"")


def fizzbuzz(fizz_def: str, buzz_def: str, maximum_def: str):
    i = 1
    reply = []
    out = ""
    while i <= int(maximum_def):
        if (int(fizz_def) < 1) or (int(buzz_def) < 1) or (int(buzz_def) == 0):
            out = "+--------ERROR--------+" + "\n"
            return out
            break
        if (i % int(fizz_def) == 0) and (i % int(buzz_def) == 0):
            reply.append("FB ")
        elif i % int(fizz_def) == 0:
            reply.append("F ")
        elif i % int(fizz_def) == 0:
            reply.append("B ")
        else:
            reply.append(str(i) + " ")
        i += 1
    if reply:
        """out.join(map(str, reply)) + "\n"""""
        # out = str(reply)
    return reply


fizz = ""
buzz = ""
maximum = ""
j = 1

# list generator
f = open("fizzbuzz.txt", "w")

while j <= 20:
    list_to_text = ""
    for listID in range(0, 3):
        if listID == 0:
            data = randint(0, 10)
            list_to_text += str(data) + " "
        elif listID == 1:
            data = randint(0, 10)
            list_to_text += str(data) + " "
        else:
            data = randint(0, 50)
            list_to_text += str(data) + "\n"
    f.writelines(list_to_text)
    j += 1
f.close()

# fizz-buzz
f = open("fizzbuzz.txt", "r")

for line in f:
    whitespace_counter = 0
    for item in line:
        if item == " ":
            whitespace_counter += 1
        if whitespace_counter == 0:
            fizz += str(item)
        elif whitespace_counter == 1:
            buzz += str(item)
        elif whitespace_counter == 2:
            maximum += str(item)
    # print(fizzbuzz(fizz, buzz, maximum))
    lines_to_file = fizzbuzz(fizz, buzz, maximum)
    if type(lines_to_file) is list:
        print("".join(str(names) for names in lines_to_file)+"\n")
    else:
        print(lines_to_file)
    fizz = ""
    buzz = ""
    maximum = ""
f.close()
