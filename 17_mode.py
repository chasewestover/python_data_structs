def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    mostCommonDictionary = {}

    for num in nums:
        if num not in mostCommonDictionary:
            mostCommonDictionary[num] = 1
        else:
            mostCommonDictionary[num] += 1

    maxKey = 0
    maxVal = 0
    for k in mostCommonDictionary:
        if mostCommonDictionary[k] > maxVal:
            maxKey = k
            maxVal = mostCommonDictionary[k]

    return maxKey



if __name__ == "__main__":
    import doctest
    doctest.testmod()