def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    stringToReturn = ''

    for char in phrase:
        if char.lower() == to_swap.lower():
            stringToReturn += char.swapcase()
        else:
            stringToReturn += char

    return stringToReturn

    #return "".join([ l.swapcase() for l in list(phrase) if l.lower() == to_swap.lower() ])
