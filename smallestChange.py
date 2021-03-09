def fillArray(coins, amount, array):
    minNo = min(array)
    if minNo == 9999:
        return False
    minIndex = array.index(minNo)
    for i in coins:
        if minIndex + i == amount:
            return minNo + 1
        if minIndex + i < amount:
            if array[minIndex+i] > minNo+1:
                array[minIndex+i] = minNo+1
    array[minIndex] = 9999
    return fillArray(coins, amount, array)


def ownWay(coins, amount):
    array = [9999 for i in range(amount)]
    array[0] = 0
    return fillArray(coins, amount, array)


print(ownWay([2], 3))
