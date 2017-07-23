import re

datesArray = []
amountArray = []
jsonData = []

def createJSON(dateCount, day, month, year, individualTotals):
    dictionary = {}
    dictionary = {'date': {'day': day, 'month': month, 'year': year}, 'NoOfMessages': dateCount, 'individual': individualTotals}
    jsonData.append(dictionary)

def checkDate(date):
    if re.match('[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]', date):
        return True
    else:
        return False

def extractDate(line):
    date = ""
    for i in range (0,len(line)):
        if line[i] == ",":
            return date
        else:
            date += line[i]

def extractName(line):
    name = ""
    colonCount = 0
    for letter in line:
        if letter == ':':
            colonCount += 1
        if colonCount == 3:
            name += letter
        if colonCount == 4:
            return name[2:]

def extractDay(date):
    slashCount = 0
    day = ""
    for part in date:
        if part == '/':
            slashCount += 1
        if slashCount < 1:
            day += str(part)
        elif slashCount == 1:
            return day

def extractMonth(date):
    slashCount = 0
    month = ""
    for part in date:
        if part == '/':
            slashCount += 1
        if slashCount == 1:
            month += str(part)
        elif slashCount == 2:
            return int(month[1:])

def extractYear(date):
    slashCount = 0
    year = ""
    for part in date:
        if part == '/':
            slashCount += 1
        if slashCount == 2:
            year += str(part)
    return int(year[1:])

def individualAmounts(nameArray, totalNames):
    totalArray = []
    for name in nameArray:
        total = totalNames.count(name)
        totalAmount = {'name': name, 'amount': total}
        totalArray.append(totalAmount)
    return totalArray


def getCount(chat):
    nameArray = []
    totalNames = []
    dateCount = 0
    nameCount = 0
    line = chat.readline()
    date = extractDate(line)

    if date != None and checkDate(date) != False:
        while extractDate(line) == date:
            name = extractName(line)
            if name not in nameArray and name != None:
                nameArray.append(name)
            totalNames.append(name)
            lastPos = chat.tell()
            line = chat.readline()
            dateCount +=1

        if len(datesArray)!=0:
            if datesArray[-1] == date:
                amountArray[-1] += dateCount
            else:
                amountArray.append(dateCount)
                datesArray.append(date)
        else:
            amountArray.append(dateCount)
            datesArray.append(date)

        line = chat.seek(lastPos)
        individualTotals = individualAmounts(nameArray,totalNames)
        day = extractDay(date)
        month = extractMonth(date)
        year = extractYear(date)
        createJSON(dateCount, day, month, year, individualTotals)

def readChat():
    chat = open("chat.txt")
    numLines = sum(1 for line in open('chat.txt'))
    lineCount = 0
    while lineCount != numLines:
        num = getCount(chat)
        lineCount += 1

    return jsonData
