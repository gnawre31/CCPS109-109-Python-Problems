def extract_increasing(digits):
    #extract first digit
    final_list = [int(digits[0])]
    #second digit becomes the first to be examined
    working_value = digits[1]
    #delete the first 2 digits from string because they have been extracted
    digits = digits[2:]
    
    # +1 to while loop to include a final check
    while len(digits) + 1 > 0:
        if int(working_value) < int(final_list[-1]) + 1:

            #to avoid out of index error
            if len(digits) == 0:
                break

            #concat working value with the first digit of from string
            working_value = int(f"{working_value}{digits[0]}")

            #delete the first digit from string so that the next digit becomes the first
            digits = digits[1:]

        else:
            #append and reset working value if it is not the last digit in string
            final_list.append(int(working_value))
            if len(digits) != 0:
                working_value = digits[0]
                digits = digits[1:]
    print(final_list)

extract_increasing('0')