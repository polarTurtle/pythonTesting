def returnOne():
    return 1


def basic_bar(results):
    listForm = []
    for key, value in results.items():
        temp = [key, value]
        listForm.append(temp)
    listForm.sort(key=lambda x: (-x[1], x[0]))
    finalString = ""
    for quater, amount in listForm:
        if amount == 0:
            temp = quater + "|" + "0" + "\n"
        else:
            temp = quater + "|" + "#"*int(amount/50) + " " + str(amount) + "\n"
        finalString += temp
    return finalString.strip("\n")


def short_bar(results):
    listForm = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    finalString = ""
    for quater, amount in listForm:
        if amount == 0:
            temp = quater + "|" + "0" + "\n"
        else:
            temp = quater + "|" + "#"*int(amount/50) + " " + str(amount) + "\n"
        finalString += temp
    return finalString.strip("\n")


sampleDict = {'Q4': 0, 'Q3': 100, 'Q2': 0, 'Q1': 600}
# print(basic_bar(sampleDict))
print(short_bar(sampleDict))

# "Q1|############ 600\nQ3|## 100\nQ2|0\nQ4|0"
