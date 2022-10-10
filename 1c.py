def count_occurences(input_string):
    items = input_string.split(', ')
    itemCounts = {}

    for item in items:
        if item in itemCounts:
            itemCounts[item] += 1
        else:
            itemCounts[item] = 1

    maxCount = max(itemCounts.values())

    result = []

    for item, count in itemCounts.items():
        if (count == maxCount):
            result.append([item, maxCount])

    return result
