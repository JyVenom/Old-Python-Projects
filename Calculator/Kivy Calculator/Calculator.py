while 1:
    equation = input("What would you like me to solve?")
    process = equation
    for operation in range(0, 4):
        last = len(process) - 1
        for place in range(1, last):
            previous_place = place - 1
            next_place = place + 1
            part = process[previous_place] + process[place] + process[next_place]
            if process[place] == "*":
                answer = str(eval(part))
                process.replace(part, answer, 1)
        for place in range(1, last):
            previous_place = place - 1
            next_place = place + 1
            part = process[previous_place] + process[place] + process[next_place]
            if process[place] == "/":
                answer = str(eval(part))
                process.replace(part, answer, 1)
        for place in range(1, last):
            previous_place = place - 1
            next_place = place + 1
            part = process[previous_place] + process[place] + process[next_place]
            if process[place] == "+":
                answer = str(eval(part))
                process.replace(part, answer, 1)
        for place in range(1, last):
            previous_place = place - 1
            next_place = place + 1
            part = process[previous_place] + process[place] + process[next_place]
            if process[place] == "-":
                answer = str(eval(part))
                process.replace(part, answer, 1)
    print (process)
    repeat = input("Would you like me to solve another one? (Y/N)")
    repeat = repeat.lower()
    if repeat == "n":
        break
