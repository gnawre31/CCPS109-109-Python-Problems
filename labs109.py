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


