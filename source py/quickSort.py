import time

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('#787A91')
        else:
            colorArray.append('#FFFFFF')

        if i == tail:
            colorArray[i] = '#1C6DD0'
        elif i == border:
            colorArray[i] = '#FF1700'
        elif i == currIdx:
            colorArray[i] = '#F9D371'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = '#34BE82'

    return colorArray