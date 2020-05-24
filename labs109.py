from itertools import combinations as comb
from functools import reduce
from statistics import median
import math

# #1 calculate letter grades based on percentage grades
# def ryerson_letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return 'A+'
#     elif n > 84:
#         return 'A'
#     elif n > 79:
#         return 'A-'
#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         adjust = "-"
#     elif ones > 6:
#         adjust = "+"
#     else:
#         adjust = ""
#     return "DCB"[tens - 5] + adjust



# #2 Check if array is in ascending order
# def is_ascending(items):
#     previous_value = None

#     for item in items:
#         if previous_value and previous_value >= item:
#             return False

#         previous_value = item
#     return True

# #3 Riffle with either in or out shuffling
# def riffle(items, out = True):
#     if len(items) > 0:

#         #splitting the deck into 2
#         half_cut = len(items) // 2
#         deck = items[:half_cut]
#         second_half = items[half_cut:]

#         #determine the starting point
#         if out:
#             starting_index = 1
#         else:
#             starting_index = 0

#         #insert second half into deck with alternating indexes
#         for index, item in enumerate(second_half): 
#             insert_index = index*2+starting_index      
#             deck.insert(insert_index, item)
#         return deck

#     #return if items is empty
#     else:
#         return items

# #4 check if integer contains only odd digits
# def only_odd_digits(n):
#     n = str(n)
#     for number in n:
#         if int(number) % 2 == 0:
#             return False
#             break
#     return True

# #5 calculate total # of blocks in a pyramid given n rows, m columns, h layers
# def pyramid_blocks(n, m, h):
    # return int(h*m*n + (h-1)*h*(m+n)//2 + h*(h-1)*(2*h-1)//6)

# # 6 check if odd # of digits, middle is 0, no other 0s
# def is_cyclops(n):
#     #convert to string
#     n = str(n)
#     #count repeated 0s
#     counter = 0
#     for number in n:
#         if number == "0":
#             counter += 1

#     #check even digits
#     if (len(n)) % 2 == 0:
#         return False
#     #check if center is 0
#     elif n[len(n) // 2] != '0':
#         return False
#     #check if more than 1 zero
#     elif counter > 1:
#         return False
#     else:
#         return True

# # 7 check if end of tile matches start of subsequent tile
# def domino_cycle(tiles):
    
#     if len(tiles) == 0:
#             return True
#     elif len(tiles) == 1:
#         if tiles[0][0] == tiles[0][1]:
#             return True
#         else:
#             return False
#     else:
#         answer = True
#         last_value = tiles[0][1]
#         first_value = 0 

#         for i in range(1, len(tiles)):
#             first_value = tiles[i][0]
#             if first_value == last_value:
#                 last_value = tiles[i][1]
#             else:
#                 answer = False
#                 break
#         if tiles[0][0] != tiles[-1][1]:
#             answer = False

#         return answer



# # 8
# def count_dominators(items):
#     temp_list = items

#     if len(items) == 0:
#         counter = 0
#     elif len(items) == 1:
#         counter = 1
#     else:
#         counter = 1
#         for i in range(0, len(items) - 1):
#             temp_list = items[i+1:]
#             temp_list.sort(reverse=True)
#             if items[i] > temp_list[0]:
#                 counter +=1
#     return counter



# # 9 convert string of digits to list of ascending numbers
# def extract_increasing(digits):
#     #return if string has a length of 1
#     if len(digits) == 1:
#         final_list = [digits[0]]

#     else:
#         #extract first digit
#         final_list = [int(digits[0])]
#         #second digit becomes the first to be examined
#         working_value = digits[1]
#         #delete the first 2 digits because they have been extracted
#         digits = digits[2:]
        
#         # +1 to while loop to do a final check
#         while len(digits) + 1 > 0:
#             if int(working_value) < int(final_list[-1]) + 1:

#                 #to avoid out of index error
#                 if len(digits) == 0:
#                     break

#                 #concat working value (placeholder) with the first digit
#                 working_value = int(f"{working_value}{digits[0]}")

#                 #delete the first digit so that the next digit becomes the first
#                 digits = digits[1:]

#             else:
#                 #append and reset working value if it is not the last digit
#                 final_list.append(int(working_value))
#                 if len(digits) != 0:
#                     working_value = digits[0]
#                     digits = digits[1:]
#     return final_list

# # 10 words that contain given letter sequence
# # def words_with_letters(words, letters):

# # 11 taxi zum zum
# def taxi_zum_zum(moves):
#     # in order top, right, bottom, left
#     direction = [1, 0, 0, 0]
#     # in order x, y
#     result = [0, 0]

#     for i in range(len(moves)):

#         if moves[i] == 'L':
#             if direction.index(1) == 0:
#                 direction[0] = 0
#                 direction[3] = 1

#             else:
#                 one_index = direction.index(1)
#                 direction[one_index - 1] = 1
#                 direction[one_index] = 0

#         if moves[i] == 'R':
#             if direction.index(1) == 3:
#                 direction[0] = 1
#                 direction[3] = 0
#             else:
#                 one_index = direction.index(1)
#                 direction[one_index + 1] = 1
#                 direction[one_index] = 0
        
#         if moves[i] == 'F':
#             if direction.index(1) == 0:
#                 result[1] += 1
#             elif direction.index(1) == 1:
#                 result[0] += 1
#             elif direction.index(1) == 2:
#                 result[1] -= 1
#             else:
#                 result[0] -= 1
#     return tuple(result)
    

# #12 count growlers
# def count_growlers(animals):
#     growl_counter = 0 
#     #convert list to 1s and 0s (dog = 1, cat = 0)
#     animal_list = []
#     #convert list to 1s and 0s (left = 1, right = 0)
#     direction_list = []

#     for i in range(len(animals)):
#         if animals[i] == 'dog':
#             animal_list.append(1)
#             direction_list.append(1)
#         elif animals[i] == 'god':
#             animal_list.append(1)
#             direction_list.append(0)
#         elif animals[i] == 'cat':
#             animal_list.append(0)
#             direction_list.append(1)
#         else:
#             animal_list.append(0)
#             direction_list.append(0)

#     for i in range(len(animals)):
#         if direction_list[i] == 1:
#             if animal_list[:i].count(1) > animal_list[:i].count(0):
#                 growl_counter += 1
#         else:
#             if animal_list[i:].count(1) > animal_list[i:].count(0):
#                 growl_counter += 1
#     return growl_counter


# #13 Bulgarian solitaire
# def bulgarian_solitaire(piles, k):
#     counter = 0
#     total_sum = int(k*(k+1)//2)
#     #generate list to check
#     check_list = list(range(1, k+1))
#     #remove initial 0s
#     piles = [i for i in piles if i != 0]
#     #loop until piles matches the check list
#     while True:
#         if all(x in piles for x in check_list):
#             break
#         else:
#             piles = [x - 1 for x in piles]
#             piles = [i for i in piles if i != 0]
#             appended_value = total_sum - sum(piles)
#             piles.append(appended_value)
#             counter +=1    
#     return counter

# # 14 Scylla or Charybdis?
# def scylla_or_charybdis(sequence, n):

#15 arithmetic progression - no idea
# def arithmetic_progression(elems):
#     arr = []
#     dict_count = {}
#     for i in range(len(elems)):
#         temp_arr = []
#         for j in reversed(range(len(elems[:i]))):
#             difference = elems[i] - elems[j]
#             temp_arr.append(difference)
#             if not difference in dict_count:
#                 dict_count[difference] = 1
#             else:
#                 dict_count[difference] +=1 
#         arr.append(temp_arr)
    
#     print(arr)
#     print(dict_count)
# arithmetic_progression([2, 4, 6, 7, 8, 12, 17])

# #16 tukeys ninther - not sure why this doesnt work
# import math
# def tukeys_ninthers(items):
#     iterations = int(math.log(len(items), 3))
#     arr = items
#     working_arr = []
#     for i in range(iterations):
#         for j in range(0, len(arr), 3):
#             working_arr.append(median([ arr[j], arr[j+1] , arr[j+2] ]))
#         arr = working_arr
#         working_arr = []
#     return median(arr)

# #17 is zigzag
# def is_zigzag(n):
#     n = str(n)
#     positive = None
#     if len(n) == 1 or len(n) == 0:
#         return True
#     else:
#         for i in range(2, len(n)):
#             if (int(n[i]) - int(n[i - 1]) > 0 and int(n[i - 1]) - int(n[i - 2]) > 0) or (int(n[i]) - int(n[i - 1]) <= 0 and int(n[i - 1]) - int(n[i - 2]) <= 0):
#                 return False
#         return True

# #18 crack the crag - showing correct answer, not sure what's wrong
# def crag_score(dice):
#     low_straight = [1,2,3]
#     high_straight = [4,5,6]
#     odd_straight = [1,3,5]
#     even_straight = [2,4,6]
    
#     if sum(dice) == 13 and (dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]):
#         answer = 50
#     elif sum(dice) == 13:
#         answer = 26
#     elif dice[0] == dice[1] == dice[2]:
#         answer = 25
#     elif all(x in dice for x in low_straight) or all(x in dice for x in high_straight) or all(x in dice for x in odd_straight) or all(x in dice for x in even_straight):
#         answer = 20
#     else:
#         answer = max(dice) * dice.count(max(dice))
#     return answer

# # 19 three summers ago
# def three_summers(items, goal):
#     for i in range(0, len(items) -1):  
#         s = set() 
#         curr_sum = goal - items[i] 
#         for j in range(i + 1, len(items)): 
#             if (curr_sum - items[j]) in s: 
#                 return True
#             s.add(items[j]) 
#     return False

# #20 count all sums and products
# def count_distinct_sums_and_products(items):
#     s = set()
#     if len(items) == 0:
#         return 0
#     else:
#         for i in range(len(items)):
#             for j in range(len(items)):
#                 s.add(items[i] + items[j])
#                 s.add(items[i] * items[j])
#         return len(s)

# # 21 sum of two squares - attempt 1 too slow, attempt 2 not sure why doesnt work
# def sum_of_two_squares(n): 
    # #find max value
    # max_value = math.floor(math.sqrt(n - 1))
    # for i in range(max_value):
    #     first_val = (max_value - i) ** 2
    #     for j in range(max_value):
    #         second_val = (j + 1) ** 2
    #         if n - first_val - second_val == 0:
    #             return tuple([int(math.sqrt(first_val)), int(math.sqrt(second_val))])
      
#     #attempt #2
#     answer = []
#     s = dict() 
#     for i in range(n): 
#         if i * i > n: 
#             break
#         # store square value in hashmap 
#         s[i * i] = 1
#         if (n - i * i) in s.keys(): 
#             answer.append( [i, int((n - i * i)**(1 / 2))])
#     if len(answer) > 0:
#         return tuple(answer[-1])
# print(sum_of_two_squares(2))

# #22 try a spatula
# def pancake_scramble(text):
#     for i in range(1,len(text)):
#         res = []
#         for j in range(i+1):
#             res.insert(0,text[j])
#         if(i+1 < len(text)):
#             res.append(text[i+1:])

#         text = ''.join(res)
#     return text

# 23 carry on pythonista
# def count_carries(a, b):
#     longest = b
#     ctr = 0
#     carry_val = 0 
#     if(a == 0 and b == 0):
#         return 0
     
#     for i in range(len(str(longest))):
#         carry_val = a%10 + b%10 + carry_val
#         if carry_val > 9:
#             carry_val = 1
#         else:
#             carry_val = 0
#         ctr += carry_val
#         a //= 10
#         b //= 10
        
#     return ctr

# #24 word dominators - need to figure out count dominators first
# def count_word_dominators(words):

# #25 duplicate digit bonus - done
# def duplicate_digit_bonus(n):
#     n = str(n)
#     x = n[0]
#     ctr = 0
#     answer = 0
    
#     for i in range(1, len(n)):
#         if n[i] == x:
#             ctr += 1
#         else:
#             if ctr > 0:
#                 answer += 10**(ctr - 1)
#                 ctr = 0
#         x = n[i]
#     if ctr > 0:
#         answer += 2 * (10**(ctr - 1))
#     return answer

#26 nearest smallest element
# def nearest_smaller(items):
    # note the number and its index for bot



# nearest_smaller([1,99,12,77,234,123])

# #27 interesting intersecting
# def squares_intersect(s1, s2):
#     if (s1[0] + s1[2] < s2[0]) or (s1[1] + s1[2] < s2[1]) or (s2[0] + s2[2] < s1[0]) or (s2[1] + s2[2] < s1[1]):
#         return False
#     else: 
#         return True

# #28 keep doubling - done
# def double_until_all_digits(n, giveup = 1000):
#     answer = -1
#     check = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
#     for i in range(giveup):
#         val = set(str(n*2**i))
#         if all(x in val for x in check):
#             answer = i
#             break
#     return answer

# #29 Remove each item after its k:th occurrence - done
# def remove_after_kth(items, k = 1):
#     result = []
#     if k == 0:
#         return []
#     else:
#         count = dict()
#         for item in items:
#             count[item] = count.get(item, 0) + 1
#             if count[item] < k + 1:
#                 result.append(item)
#         return result


# #30 First item that is preceded by k smaller items - done but takes 15 sec
# def first_preceded_by_smaller(items, k = 1):
#     answer = None
#     if k > len(items):
#         return answer
#     else:
#         for i in range(k, len(items)):
#             ctr = 0
#             for j in range(len(items[:i])):
#                 if items [j] < items[i]:
#                     ctr += 1
#             if ctr >= k:
#                 answer = items[i]
#                 break
#         return answer

# #31 pull down your neighbour - stuck
# def eliminate_neighbours(items):
#     max_val = max(items)
#     ctr = 0
    
#     for i in range(len(items)//2):
#         ctr +=1
#         min_val = min(items)
#         min_index = items.index(min_val)
#         if min_index == 0:
#             r1 = items[min_index+1]
#         elif min_index == len(items):
#             r1 = items[min_index-1]
#         else:
#             r1 = items[min_index+1] if items[min_index+1] > items[min_index-1] else items[min_index-1]
#         if r1 == max_val:
#             break
#         items.remove(min_val)
#         items.remove(r1)
#     return ctr
# print(eliminate_neighbours([8, 5, 3, 1, 7, 2, 6, 4]))


# #32 What do you hear, what do you say? - stuck
# def count_and_say(digits):
#     count = dict()
#     result = []
#     if len(digits) == 0:
#         return '' 
#     else:
#         val = digits[0]
#         ctr = 0
#         result = []
#         for i in range(0, len(digits)):
#             val2 = digits[i]
#             if val == val2:
#                 ctr += 1
            
#             else:
#                 result.append(ctr)
#                 result.append(digits[i-1])
#                 ctr = 1
#             if i == len(digits):
#                 result.append(1)
#                 result.append(digits[i])
#             val = digits[i]
        
#         return str("".join(str(x) for x in result))

# print(count_and_say('123456789'))

#33 All your fractions are belong to base - what
# def group_and_skip(n, out, in):

# #34 Rooks on a rampage - done
# def safe_squares_rooks(n, rooks):
#     rcount = set()
#     ccount = set()
#     for i in range(len(rooks)):
#         rcount.add(rooks[i][0])
#         ccount.add(rooks[i][1])
#     return (n - len(ccount)) * (n - len(rcount))

#35 Bishops on a binge - stuck on intersection
# def safe_squares_bishops(n, bishops):
#     for i in range(len(bishops)):
#         top_left = min(bishops[i][0], bishops[i][1]) - 1
#         bot_left = n - max(bishops[i][0], n+1-bishops[i][1])  
#         bot_right = n - max(bishops[i][0], bishops[i][1]) 
#         top_right = min(bishops[i][0], n+1-bishops[i][1]) -1
#         total = top_left + bot_left + top_right + bot_right + 1
#     return 

# #36 Up for the count
# def counting_series(n):
#     skip = int('9' + '0'*(len(str(n)) - 2))
#     iterations = n - skip
#     start = len(str(skip))
#     skip2 = 0
#     iter2 = 0
#     while len(str(skip2)) < len(str(n)) - 1:
#         skip2 = skip2 + (iter2+1)*9*(10**iter2)
#         iter2 += 1

# counting_series(1000000000)

# #37 Revorse the vewels - done
# def reverse_vowels(text):
#     temp = []
#     ind = []
#     check = ['a','e','i','o','u','A','E','I','O','U']
#     for i in range(len(text)):
#         if text[i] in check:
#             temp.append(text[i])
#             ind.append(i)
#     for i in range(len(temp)):
#         if temp[i].isupper():
#             text = text[:ind[i]] + temp[-i-1].upper() + text[ind[i]+1:] 
#         else:
#             text = text[:ind[i]] + temp[-i-1].lower() + text[ind[i]+1:] 
#     return text

# #38 Everybody do the Scrooge Shuffle - wtf
# def spread_the_coins(piles, left, right):

# #39 Boustrophedon - done :D 
# def create_zigzag(rows, cols, start = 1):
#     temp = []
#     ans = []
#     for i in range(rows):
#         for j in range(cols):
#             if i > 0:
#                 app = ans[i-1][-1] +  j + 1
#                 temp.append(app)
#             else:
#                 temp.append(start + j)

#         ans.append(temp)
#         temp = []
#     for x in range(len(ans)):
#         if x%2 == 1:
#             ans[x].reverse()

#     return ans
































        










            















        











