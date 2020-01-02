file = open("hours.txt")
for line in file:
    tokens = line.split()
    id = tokens[0]
    name = tokens[1]

    hours = 0.0 # cumulative sum of employee's hours
    days = 0
    for token in tokens[2:]:
        hours += float(token)
        days += 1

    average = hours / days
    above = 0 # compute number of days above average
    for token in tokens[2:]:
        if float(token) > average:
            above += 1
    print (name, "worked", hours, "hours ", average, "/ day,", above, "days above average")
