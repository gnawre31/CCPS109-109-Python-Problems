from itertools import combinations as comb
from functools import reduce
from statistics import median
import math
from itertools import cycle, islice


def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust



def is_ascending(items):
    if len(items) == 0:
        return True
    for i in range(1,len(items)):
        if items[i] <= items[i-1]:
            return False

    return True

def riffle(items, out = True):
    if len(items) > 0:
        half_cut = len(items) // 2
        deck = items[:half_cut]
        second_half = items[half_cut:]
        if out:
            starting_index = 1
        else:
            starting_index = 0
        for index, item in enumerate(second_half): 
            insert_index = index*2+starting_index      
            deck.insert(insert_index, item)
        return deck
    else:
        return items

def only_odd_digits(n):
    n = str(n)
    for number in n:
        if int(number) % 2 == 0:
            return False
            break
    return True


def is_cyclops(n):
    n = str(n)
    counter = 0
    for number in n:
        if number == "0":
            counter += 1
    if (len(n)) % 2 == 0:
        return False
    elif n[len(n) // 2] != '0':
        return False
    elif counter > 1:
        return False
    else:
        return True

def domino_cycle(tiles):
    if len(tiles) == 0:
            return True
    elif len(tiles) == 1:
        if tiles[0][0] == tiles[0][1]:
            return True
        else:
            return False
    else:
        answer = True
        last_value = tiles[0][1]
        first_value = 0 

        for i in range(1, len(tiles)):
            first_value = tiles[i][0]
            if first_value == last_value:
                last_value = tiles[i][1]
            else:
                answer = False
                break
        if tiles[0][0] != tiles[-1][1]:
            answer = False
        return answer



def count_dominators(items):
    ans = []
    inv = items[::-1]
    for i in range(len(inv)):
        if i == 0:
            ans.append(items[-1])
        if inv[i] > ans[-1]:
            ans.append(inv[i])
    return len(ans)



def extract_increasing(digits):
    if len(digits) == 1: return list(digits)
    else:
        final_list = [int(digits[0])]
        working_value = digits[1]
        digits = digits[2:]
        while len(digits) + 1 > 0:
            if int(working_value) < int(final_list[-1]) + 1:
                if len(digits) == 0:
                    break
                working_value = int(f"{working_value}{digits[0]}")
                digits = digits[1:]
            else:
                final_list.append(int(working_value))
                if len(digits) != 0:
                    working_value = digits[0]
                    digits = digits[1:]
        return final_list

def words_with_letters(words, letters):
    ans = []
    for word in words:
        i = 0
        j = 0
        while i < len(letters) and j < len(word):
            if letters[i] == word[j]:
                i += 1
            j += 1
        if i == len(letters): ans.append(word)
    return ans

def taxi_zum_zum(moves):
    direction = [1, 0, 0, 0]
    result = [0, 0]
    for i in range(len(moves)):
        if moves[i] == 'L':
            if direction.index(1) == 0:
                direction[0] = 0
                direction[3] = 1
            else:
                one_index = direction.index(1)
                direction[one_index - 1] = 1
                direction[one_index] = 0

        if moves[i] == 'R':
            if direction.index(1) == 3:
                direction[0] = 1
                direction[3] = 0
            else:
                one_index = direction.index(1)
                direction[one_index + 1] = 1
                direction[one_index] = 0

        if moves[i] == 'F':
            if direction.index(1) == 0: result[1] += 1
            elif direction.index(1) == 1: result[0] += 1
            elif direction.index(1) == 2: result[1] -= 1
            else: result[0] -= 1
    return tuple(result)
    
def give_change(amount, coins):
    answer = []
    for coin in coins:
        while coin <= amount:
            answer.append(coin)
            amount -= coin
    return answer

def pyramid_blocks(n, m, h):
    return int(h*m*n + (h-1)*h*(m+n)//2 + h*(h-1)*(2*h-1)//6)

def safe_squares_rooks(n, rooks):
    rcount = set()
    ccount = set()
    for i in range(len(rooks)):
        rcount.add(rooks[i][0])
        ccount.add(rooks[i][1])
    return (n - len(ccount)) * (n - len(rcount))

def pancake_scramble(text):
    for i in range(1,len(text)):
        res = []
        for j in range(i+1):
            res.insert(0,text[j])
        if(i+1 < len(text)):
            res.append(text[i+1:])

        text = ''.join(res)
    return text

def words_with_given_shape(words, shape):
    ans = []
    for word in words:
        counter = 0
        if len(word) == len(shape) + 1:
            for i in range(1, len(word)):
                if (shape[i-1] == -1 and word[i] < word[i-1]) or (shape[i-1] == 0 and word[i] == word[i-1]) or (shape[i-1] == 1 and word[i] > word[i-1]):
                    counter += 1
                else:
                    break
        if counter == len(shape):
            ans.append(word)
    return ans

def running_median_of_three(items):
    if len(items) < 3:
        return items
    else:
        ans = [items[0],items[1]]
        for i in range(2, len(items)):

            app = median((items[i], items[i-1], items[i-2]))
            ans.append(app)
        return ans

def create_zigzag(rows, cols, start = 1):
    temp = []
    ans = []
    for i in range(rows):
        for j in range(cols):
            if i > 0:
                app = ans[i-1][-1] +  j + 1
                temp.append(app)
            else:
                temp.append(start + j)
        ans.append(temp)
        temp = []
    for x in range(len(ans)):
        if x%2 == 1:
            ans[x].reverse()
    return ans

def detab(text, n = 8, sub = ' '):
    t = list(text)
    ans = []
    while len(t) > 0:
        if t[0] != '\t':
            ans.append(t[0])
            t.pop(0)
        elif t[0] == '\t':
            if len(ans)%n == 0:
                for i in range(n):
                    ans.append(sub)
            while len(ans)%n != 0:
                ans.append(sub)
            t.pop(0)
    ans = ''.join(ans)
    return ans

def knight_jump(knight, start, end):
    knight = list(knight)
    knight.sort()
    arr = []
    for i in range(len(start)):
        arr.append(abs(start[i]-end[i]))
    arr.sort()
    if arr == knight:
        return True
    else:
        return False


def longest_palindrome(text):
    p = text[0]
    for i in range(len(text)):
        idx = 1
        while idx <= i and i + idx < len(text):
            if text[i-idx] == text[i+idx]:
                idx += 1
            else:
                break
        if len(text[i-idx+1: i+idx]) > len(p):
            p = text[i-idx+1: i+idx]
        idx = 0
        while idx <= i and i+idx < len(text)-1:
            if text[i-idx] == text[i+1+idx]:
                idx += 1 
            else:
                break
        if len(text[i-idx+1: i+idx+1]) > len(p):
            p = text[i-idx+1:i+idx+1]
    return p


# # # #24 Last man standing - stuck
# # # def josephus(n, k):
# # #     arr = [i for i in range(1, n+1)]
# # #     ans = []

# # # print(josephus(4,2))

def recaman(n):
    check = set()
    ans = []
    for i in range(1, n+1):
        if ans == []:
            ans.append(i)
            check.add(i)
        elif ans[-1] - i <= 0 or (ans[-1] - i) in check:
            ans.append(ans[-1]+i)
            check.add(ans[-1])
        else:
            ans.append(ans[-1]-i)
            check.add(ans[-1])
    return ans


# # # 25 count growlers
# # # def count_growlers(animals):
# # #     growl_counter = 0 
# # #     #convert list to 1s and 0s (dog = 1, cat = 0)
# # #     animal_list = []
# # #     #convert list to 1s and 0s (left = 1, right = 0)
# # #     direction_list = []

# # #     for i in range(len(animals)):
# # #         if animals[i] == 'dog':
# # #             animal_list.append(1)
# # #             direction_list.append(1)
# # #         elif animals[i] == 'god':
# # #             animal_list.append(1)
# # #             direction_list.append(0)
# # #         elif animals[i] == 'cat':
# # #             animal_list.append(0)
# # #             direction_list.append(1)
# # #         else:
# # #             animal_list.append(0)
# # #             direction_list.append(0)

# # #     for i in range(len(animals)):
# # #         if direction_list[i] == 1:
# # #             if animal_list[:i].count(1) > animal_list[:i].count(0):
# # #                 growl_counter += 1
# # #         else:
# # #             if animal_list[i:].count(1) > animal_list[i:].count(0):
# # #                 growl_counter += 1
# # #     return growl_counter


def bulgarian_solitaire(piles, k):
    counter = 0
    total_sum = int(k*(k+1)//2)
    check_list = list(range(1, k+1))
    piles = [i for i in piles if i != 0]
    while True:
        if all(x in piles for x in check_list): break
        else:
            piles = [x - 1 for x in piles]
            piles = [i for i in piles if i != 0]
            appended_value = total_sum - sum(piles)
            piles.append(appended_value)
            counter +=1    
    return counter


def tukeys_ninthers(items):
    iterations = int(math.log(len(items), 3))
    arr = items
    working_arr = []
    for i in range(iterations):
        for j in range(0, len(arr), 3):
            working_arr.append(median([ arr[j], arr[j+1] , arr[j+2] ]))
        arr = working_arr
        working_arr = []
    return median(arr)

def is_zigzag(n):
    n = str(n)
    positive = None
    if len(n) == 1 or len(n) == 0:
        return True
    else:
        for i in range(2, len(n)):
            if (int(n[i]) - int(n[i - 1]) > 0 and int(n[i - 1]) - int(n[i - 2]) > 0) or (int(n[i]) - int(n[i - 1]) <= 0 and int(n[i - 1]) - int(n[i - 2]) <= 0):
                return False
        return True

def crag_score(dice):
    d = dict()
    low_straight,high_straight,odd_straight,even_straight = [1,2,3], [4,5,6], [1,3,5], [2,4,6]
    if sum(dice) == 13 and (dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]): 
        return 50
    elif sum(dice) == 13:
        return 26
    elif dice[0] == dice[1] == dice[2]:
        return 25
    elif all(x in dice for x in low_straight) or all(x in dice for x in high_straight) or all(x in dice for x in odd_straight) or all(x in dice for x in even_straight):
        return 20
    else:
        for die in dice:
            d[die] = d.get(die, 0) + 1
        x = [k*v for k,v in d.items()]
        return max(x)

def three_summers(items, goal):
    for i in range(0, len(items) -1):  
        s = set() 
        curr_sum = goal - items[i] 
        for j in range(i + 1, len(items)): 
            if (curr_sum - items[j]) in s: 
                return True
            s.add(items[j]) 
    return False

def count_distinct_sums_and_products(items):
    s = set()
    if len(items) == 0:
        return 0
    else:
        for i in range(len(items)):
            for j in range(len(items)):
                s.add(items[i] + items[j])
                s.add(items[i] * items[j])
        return len(s)


def count_carries(a, b):
    carry = 0
    counter = 0
    while a > 0 or b > 0:
        x = 0
        y = 0
        if len(str(a)) > 0:
            x = a % 10
            a = a // 10
        if len(str(b)) > 0:
            y = b % 10
            b = b // 10  
        sumABC = x + y + carry
        if sumABC > 9:
            carry = int(str(sumABC)[0])
            counter += 1
        else:
            carry = 0
    return counter


def duplicate_digit_bonus(n):
    n = str(n)
    x = n[0]
    ctr = 0
    answer = 0
    for i in range(1, len(n)):
        if n[i] == x:
            ctr += 1
        else:
            if ctr > 0:
                answer += 10**(ctr - 1)
                ctr = 0
        x = n[i]
    if ctr > 0:
        answer += 2 * (10**(ctr - 1))
    return answer


def squares_intersect(s1, s2):
    if (s1[0] + s1[2] < s2[0]) or (s1[1] + s1[2] < s2[1]) or (s2[0] + s2[2] < s1[0]) or (s2[1] + s2[2] < s1[1]):
        return False
    else: 
        return True

def double_until_all_digits(n, giveup = 1000):
    answer = -1
    check = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for i in range(giveup):
        val = set(str(n*2**i))
        if all(x in val for x in check):
            answer = i
            break
    return answer

def remove_after_kth(items, k = 1):
    d = {}
    ans = []
    for i in items:
        d[i] = d.get(i, 0) + 1
        if(d[i] <= k):
            ans.append(i)
    return ans


def first_preceded_by_smaller(items, k = 1):
    answer = None
    if k > len(items):
        return answer
    else:
        for i in range(k, len(items)):
            counter = 0
            for j in range(len(items[:i])):
                if items [j] < items[i]:
                    counter += 1
            if counter >= k:
                answer = items[i]
                break
        return answer

def eliminate_neighbours(items):
    mx = max(items)
    counter = 0
    while mx in items:
        mnInd = items.index(min(items))
        if mnInd == 0:
            del items[:mnInd + 2]
            counter += 1
        elif mnInd == len(items) - 1:
            del items[mnInd-1:]
            counter += 1
        else:
            if items[mnInd-1] > items[mnInd+1]:
                del items[mnInd-1:mnInd+1]
                counter += 1
            else:
                del items[mnInd:mnInd+2]
                counter += 1
            
    return counter


def count_and_say(digits):
    if digits == '':
        return digits
    
    currDigit, ans, count = digits[0], "", 0
    for digit in digits:
        if digit == currDigit:
            count += 1
        else:
            ans += str(count) + currDigit
            currDigit, count = digit, 1

    ans += str(count) + currDigit
    return ans

def safe_squares_bishops(n, bishops):
    count = 0
    for i in range(n):
        for j in range(n):
            safe = True
            for bishop in bishops:
                bisX, bisY = bishop[0],bishop[1]
                if abs(i - bisX) == abs(j - bisY):
                    safe = False
            if safe:
                count +=1
    return count

def reverse_vowels(text):
    temp = []
    ind = []
    check = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(text)):
        if text[i] in check:
            temp.append(text[i])
            ind.append(i)
    for i in range(len(temp)):
        if temp[i].isupper():
            text = text[:ind[i]] + temp[-i-1].upper() + text[ind[i]+1:] 
        else:
            text = text[:ind[i]] + temp[-i-1].lower() + text[ind[i]+1:] 
    return text


#55 Postfix interpreter ---------------------done
def postfix_evaluate(items):
    values = []
    for i in range(len(items)):
        if items[i] == '+':
            app = values[-2] + values[-1] 
            values.pop()
            values.pop()
            values.append(app)
        elif items[i] == '-':
            app = values[-2] - values[-1] 
            values.pop()
            values.pop()
            values.append(app)
        elif items[i] == '*':
            app = values[-2] * values[-1] 
            values.pop()
            values.pop()
            values.append(app)
        elif items[i] == '/':
            if values[-1] == 0:
                values.pop()
                values.pop()
                values.append(0)
            else:
                app = values[-2] // values[-1] 
                values.pop()
                values.pop()
                values.append(app)
        else:
            values.append(items[i])
    return values[0]



# # #59 ztalloc ecneuqes - it should work??
# # def ztalloc(shape):
# #     x = 1
# #     for i in reversed(range(len(shape))):
# #         if shape[i] == 'u' and x == 1:
# #             return None
# #             break
# #         elif shape[i] == 'd':
# #             x = x * 2
# #             if x%2 != 0:
# #                 return None
# #                 break
# #         else:
# #             x = (x-1)//3
# #             if x%2 == 0:
# #                 return None
# #                 break 
# #     return x

def reverse_ascending_sublists(items):
    arr = [items[0]]
    ans = []
    for i in range(1,len(items)):
        # print(arr)
        if items[i] > items[i - 1]:
            arr.append(items[i])
        else:
            if len(arr) == 1:
                ans.extend(arr)
                arr = [items[i]]
            else:
                arr.reverse()
                ans.extend(arr)
                arr = [items[i]]
    if len(arr) > 0:
        arr.reverse()
        ans.extend(arr)
        arr = []
    return ans

def brangelina(first, second):
    firstv, secondv, temp = [], [], []
    for ind, letter in enumerate(first):
        if letter in ('a', 'e', 'i', 'o', 'u'):
            temp.append(ind)
        else:
            if len(temp) > 0:
                firstv.append(temp)
                temp = []
    if len(temp) > 0:
                firstv.append(temp)
                temp = []
    if len(firstv) > 2:
        firstv = firstv[:-1]
        first = first[:int(firstv[-1][0])]
    else:
        first = first[:int(firstv[0][0])]
    
    while second[0] not in ('a', 'e', 'i', 'o', 'u'):
        second = second[1:]
            
    return first + second



# # # #63 Wythoff array - works but brute force takes way too long
# # def wythoff_array(n):
# #     arr = []
# #     f = [1,2]
# #     track = [1,2]
# #     while True:
# #         while True:
# #             # while True:
# #             app = f[-1] + f[-2]
# #             f.append(app)
# #             track.append(app)
# #             if app == n or (f[-1] > n and len(f) > 2):
# #                 break
# #         # print(app)
# #         print(f)
# #         arr.append(f)
# #         if n in track:
# #             break
# #         else:
# #             for i in range(1,n+1):
# #                 if i not in track:
# #                     f = [i]
# #                     track.append(i)
# #                     break
            
# #             if f[0]-arr[-1][0] == 2:
# #                 f.append(arr[-1][1]+3)
# #                 track.append(arr[-1][1]+3)
# #             else:
# #                 f.append(arr[-1][1]+5)
# #                 track.append(arr[-1][1]+5)
# #             if f[0] == n or f[1] == n:
# #                 arr.append(f)
# #                 break
# #             # print(f)
# #     print(arr)
# #     for j in range(len(arr[-1])):
# #         if n == arr[-1][j]:
# #             return (len(arr)-1,j)
# # print(wythoff_array(424242))

def seven_zero(n):
    d = 1
    ans = 0
    while True:
           
        if n%2 == 0 or n%5 == 0:
            k = 1
            while k <= d:
                val = int(k * '7' + (d-k) * '0')
                if val%n == 0:
                    ans = val
                    break
                k += 1
        else:
            val = int(d * '7')
            ans = val if val%n == 0 else 0 
        d += 1
        if ans > 0:
            return ans
            break


def autocorrect_word(word, words, df):
    closest = 26*len(word)
    smw = ''
    for w in words:
        arr = []
        if len(w) == len(word):
            s = 0
            for i in range(len(w)):
                s += df(w[i],word[i])
            if s < closest:
                closest = s
                smw = w
    return smw

            

def unscramble(words, word):
    ans = []
    check = dict()
    temp = dict()
    for i in word:
        check[i] = check.get(i, 0) + 1
    for w in words:
        if len(w) == len(word) and w[0] == word[0] and word[-1] == w[-1] and sum(map(ord,w)) == sum(map(ord,word)):
            for i in w:
                temp[i] = temp.get(i, 0) + 1
            if temp == check:
                ans.append(w)
            temp.clear()
    return ans


def fibonacci_sum(n):
    ans = []
    fib = [0, 1]
    while True:
        app = fib[-1] + fib[-2]
        if app > n:
            break
        fib.append(app)
    fib.reverse()
    for v in fib:
        if n >= v:
            n -= v 
            ans.append(v)
        if n == 0:
            break
    return ans

def possible_words(words, pattern):
    ans = []
    check = [i for i in pattern if i != "*"]
    for word in words:
        if len(word) == len(pattern):
            flag = True
            for i in range(len(pattern)):
                if (pattern[i] == '*' and word[i] in check) or (pattern[i] != '*' and word[i] != pattern[i]):
                    flag = False
            if flag:
                ans.append(word) 
    return ans

def prime_factors(n):
    i = 2
    ans = []
    while i <= n:
        if n%i == 0:
            ans.append(i)
            n /= i
        else:
            i += 1
    return ans
                    

def factoring_factorial(n):
    if n < 3:
        return [(n, 1)]
    else:
        count = dict()
        for i in range(1, n+1):
            f = prime_factors(i)
            for val in f:
                count[val] = count.get(val, 0) + 1
        ans = [(p,e) for p,e in count.items()]
        return ans


def reverse_reversed(items):
    if isinstance(items, list):
        return list(map(reverse_reversed, items[::-1]))
    else:
        return items

def frequency_sort(elems):
    ans = []
    elems.sort()
    count = dict()
    for elem in elems:
        count[elem] = count.get(elem, 0) + 1
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    k = [c[0] for c in count]
    v = [c[1] for c in count]

    for i in range(len(k)):
        for j in range(v[i]):
            ans.append(k[i])
    return ans

def expand_intervals(intervals):
    if intervals == '': 
        return []
    else:
        ans = []
        l = list(intervals.split(','))
        x = [x.split('-') for x in l]
        for i in range(len(x)):
            if len(x[i]) > 1:
                ans.extend([j for j in range(int(x[i][0]),int(x[i][1])+1)])
            else:
                ans.append(int(x[i][0]))
        return ans


def collapse_intervals(items):
    ans, lst, temp = [], [], [items[0]]
    for i in range(1,len(items)):
        if items[i] - items[i-1] == 1:
            temp.append(items[i])
        else:
            lst.append(temp)
            temp = [items[i]]
    if len(temp) > 0:
        lst.append(temp)    
    for l in lst:
        if len(l) > 1:
            ans.append(str(l[0]) + '-' + str(l[-1]))
        else:
            ans.append(str(l[0]))
    return ','.join(ans)


def count_consecutive_summers(n):
    count = 0
    for i in range(0, n): 
        d = n - i * (i + 1) // 2 
        if d <= 0: break
        if d % (i + 1) == 0: 
            count += 1
    return count


def count_divisibles_in_range(start, end, n):
    return (end - (start - n - start % n)) // n - 1 + (1 if start % n == 0 else 0)














    



































        










            















        











