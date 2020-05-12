#1 calculate letter grades based on percentage grades
def ryerson_letter_grade(pct):
    if pct < 50:
        return 'F'
    elif pct < 53:
        return 'D-'
    elif pct < 57:
        return 'D'
    elif pct < 60:
        return 'D+'
    elif pct < 63:
        return 'C-'
    elif pct < 67:
        return 'C'
    elif pct < 70:
        return 'C+'
    elif pct < 73:
        return 'B-'
    elif pct < 77:
        return 'B'
    elif pct < 80:
        return 'B+'
    elif pct < 85:
        return 'A-'
    elif pct < 90:
        return 'A'
    else:
        return 'A+'


#2 Check if array is in ascending order
def is_ascending(items):
    previous_value = None

    for item in items:
        if previous_value and previous_value >= item:
            return False

        previous_value = item
    return True

#3 Riffle with either in or out shuffling
def riffle(items, out = True):
    if len(items) > 0:

        #splitting the deck into 2
        half_cut = len(items) // 2
        deck = items[:half_cut]
        second_half = items[half_cut:]

        #determine the starting point
        if out:
            starting_index = 1
        else:
            starting_index = 0

        #insert second half into deck with alternating indexes
        for index, item in enumerate(second_half): 
            insert_index = index*2+starting_index      
            deck.insert(insert_index, item)
        return deck

    #return if items is empty
    else:
        return items

#4 check if integer contains only odd digits
def only_odd_digits(n):
    n = str(n)
    for number in n:
        if int(number) % 2 == 0:
            return False
            break
    return True

#5 calculate total # of blocks in a pyramid given n rows, m columns, h layers
def pyramid_blocks(n, m, h):
    count = 0
    for i in range(0,h):
        increment = n * m
        count += increment
        n += 1 
        m += 1
    return count

#6 check if odd # of digits, middle is 0, no other 0s
def is_cyclops(n):
    #convert to string
    n = str(n)
    #count repeated 0s
    counter = 0
    for number in n:
        if number == "0":
            counter += 1

    #check even digits
    if (len(n)) % 2 == 0:
        return False
    #check if center is 0
    elif n[len(n) // 2] != '0':
        return False
    #check if more than 1 zero
    elif counter > 1:
        return False
    else:
        return True

#7 






        

