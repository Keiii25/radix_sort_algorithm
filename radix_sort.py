import math
def radix_sort(new_list, base):
    '''
    Sorts a list on a column by column basis in a non decreasing order
    :param: new_list: An unsorted list of non-negative intergers
    :returns: A sorted list in a non decreasing order
    :time complexity: best & worst O(nk), where n = len(new_list) and k = greatest number of digit in any elements in new_list
    '''
    #if new_list is empty return new_list
    if len(new_list) == 0:
        return new_list
    
    #finds the maximum item in the list
    #O(n), where n = len(new_list)
    max_item = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] > max_item:
            max_item = new_list[i]
    
    #obtain the number of digits of the maximum number
    num_digit = max_item
    if num_digit > 0:
        num_digit = int(math.log(max_item, 10))+1

    #O(nk)
    #sorts the list by calling counting_sort_stable_col to sort the list column by column
    for i in range(num_digit):
        counting_sort_stable_col(new_list, i, base)
    return new_list
            
def column_digit(num, base, col):
    '''
    Obtain a single digit number at the column specified
    :param: num: A non negative integer
    :param: base: A non negative integer 
    :param: col: A non negative integer
    :return: A single non negative integer
    :time complexity: O(1)
    '''
    return (num//(base**col)) % base


def counting_sort_stable_col(new_list, col, base):
    '''
    Sorts a list based on the column given in a non decreasing order and maintain the relative order of elements of the same value
    :param: new_list: A list with non-negative integers 
    :return: A list where the integer at col is sorted
    time complexity: O(n+m), where n = length of new_list and m = max number in the list
    space complexity: O(m), where m = maximum number in the list
    '''
    #find the maximum
    max_item = column_digit(new_list[0], base, col)
    for item in new_list:
        item = column_digit(item, base, col)
        if item > max_item:
            max_item = item

    #initialise count array
    count_array = [0]*(max_item+1)
    for i in range(len(count_array)):
        count_array[i] = []

    #update input array
    index = 0
    for item in new_list:
        count_array[column_digit(item, base, col)].append(item)
    

    index = 0
    for i in range(len(count_array)):
        for j in range(len(count_array[column_digit(i, base, 0)])):
            new_list[index] = count_array[i][j]
            index += 1 
      
    #new list is sorted
    return new_list


def best_interval(transactions, t):
    '''
    Finds the interval of length t that contains the most transactions record
    :param: transactions: A list of transactions record with non-negative integers
    :param: t: the length of the transactions interval
    :return: Two element tuple(best_t, count), best_t is the time such that the interval starting at best_t and 
            ending at best_t + t contains more elements from transactions than any other interval of length t.
    :time complexity: O(nk), where n = len(transactions), k = greatest number of digit in any elements in transactions
    :space complexity: O(n), where n = len(transactions)
    '''
    #sorts the transactions list
    transactions = radix_sort(transactions, 10)

    #group similiar transactions time together with its frequency in the list
    frequency = 1
    temp = []
    for i in range(len(transactions)-1):
        if transactions[i] == transactions[i+1]:
            frequency += 1 
        else:
            temp += [(transactions[i], frequency)]
            frequency = 1
        if i+1 == len(transactions)-1:
            temp += [(transactions[i+1], frequency)]

    #Iterate the list to find the maximum length of interval with t time
    count = 0
    end = 0
    i = 0
    j = 0
    #if j = len(temp), the end of the list has been reached and the while loop will stop
    #O(n)
    while i < len(temp) and j < len(temp):    
        j = i + 1
        temp_count = temp[i][1]
        while (j < len(temp)) and (temp[j][0] - temp[i][0] <= t):
            temp_count += temp[j][1]
            j += 1
        i += 1
        
        if temp_count > count:
            count = temp_count
            end = temp[j-1][0]

    if (end - t) < 0:
        return 0, count
    return end-t, count
    

#Task 2
def counting_sort_string(input_str):
    '''
    Sorts a string using the ascii number of each alphabets in a non decreasing order
    :param: input_str: An unsorted string
    :returns: A non decreasing sorted string of input_str
    :best and worst time complexity: O(n+m), where n = len(input_str) and m = the maximum ascii value in the string
    :space complexity: O(m),  the greatest ascii value-97 of any alphabets in the string
    '''
    if len(input_str) == 0: 
        return input_str

    #find the maximum value of the alphabets in its ascii value-97
    max_item = ord(input_str[0])-97
    for item in input_str:
        item = (ord(item)-97)
        if item > max_item:
            max_item = item

    #initialise count array
    count_array = [0]*(max_item+1)

    #update input array
    for item in input_str:
        count_array[ord(item)-97] = count_array[ord(item)-97]+1


    string = ''
    for i in range(len(count_array)):
        for _ in range(count_array[i]):
            string += chr(i+97)
        
    return string


def radix_sort_alpha(new_list, base):
    '''
    Sorts a list of strings column by column in non decreasing order
    :param: new_list: An unsorted list of tuples consisting of a string and its sorted form 
    :return: A sorted list of tuples where the sorted string is sorted in a non decreasing order
    :time complexity: O(nk), where n = len(new_list) and k = greatest length of string in any elements in new_list
    '''
    if len(new_list) == 0:
        return new_list

    #find the greatest length of any strings in the list
    max_len = len(new_list[0])
    for i in range(1, len(new_list)):
        if len(new_list[i]) > max_len:
            max_len = len(new_list[i])
    
    for i in range(max_len):
        counting_sort_alpha(new_list, i, base)
    return new_list

def counting_sort_alpha(new_list, col, base):
    '''
    Sorts a list in a non decreasing order at the column given
    :param: new_list: A list of tuples consisting of a string and its sorted form
    :param: col: Column at which the sorted strings in the tuples should be sorted
    :return: A list of tuples which is sorted in a non decreasing order according to the second element(sorted string) in the tuple
    :time complexity: O(n+m), where n = len(new_list), m = maximum length of any string in the list
    '''
    if len(new_list) == 0:
        return new_list
    max_item = 0
    
    #checks if col has exceeded the maximum column of any string in the list
    for i in range(len(new_list)):
        if col > len(new_list[i][1])-1:
            return new_list 
    
    #find the maximum ascii value of any alphabets in the given column 
    max_item = column_digit(ord(new_list[0][1][col])-97,base, col)
    for item in new_list:
        item = column_digit(ord(item[1][col])-97, base, col)
        if item > max_item:
            max_item = item

    #initialise count array
    count_array = [0]*(max_item+1)
    for i in range(len(count_array)):
        count_array[i] = []

    #update input array
    index = 0
    for item in new_list:
        count_array[column_digit(ord(item[1][col])-97, base, col)].append(item)

    for i in range(len(count_array)):
        for j in range(len(count_array[column_digit(i, base, col)])):
            new_list[index] = count_array[i][j]
            index += 1
        
    #new list is sorted
    return new_list

def counting_sort_len(new_list):
    '''
    Sorts strings in a list according to the length of the strings in a non decreasing order
    :param: new_list: A list of tuples consisting strings
    :time complexity: O(n+m), where n = length of new_list, m = length of the longest string in the list
    :space complexity: O(m), m = length of the longest string in the list
    '''      
    if len(new_list) == 0:
        return new_list
    #find the maximum
    max_item = len(new_list[0][0])
    for item in new_list:
        item = len(item[0])
        if item > max_item:
            max_item = item

    #initialise count array
    count_array = [None]*(max_item+1)
    for i in range(len(count_array)):
        count_array[i] = []

    #update input array
    index = 0
    for item in new_list:
        count_array[len(item[0])].append(item)

    index = 0
    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            new_list[index] = count_array[i][j]
            index += 1 
     
    #new list is sorted
    return new_list        

def words_with_anagrams(list1, list2):
    '''
    Finds all words in the first list which have an anagram in the second list
    :param: list1: A list of non-duplicated strings
    :param: list2: A list of non-duplicated strings
    :return: A list of strings from list1 that has an anagram with string in the second list
    :time complexity: O(L1M1+L2M2), where L1 = len(list1), L2 = len(list2), M1 = number of characters in the longest string in list1,
    M2 = number of characters in the longest string in list2
    '''
    #sorting each string in the list and place the unsorted string and sorted string in a tuple
    #O(L1M1)
    for i in range(len(list1)):
       list1[i] =  [list1[i],counting_sort_string(list1[i])]
    
    #O(L2M2)
    for j in range(len(list2)):
        list2[j] = [list2[j],counting_sort_string(list2[j])]
    
    #sort all strings in alphabetical order
    #O(L1M1)
    radix_sort_alpha(list1, 26)
    #O(L2M2)
    radix_sort_alpha(list2, 26)

    #pre process the list by sorting the list according to the string length
    #O(L1)
    list1 = counting_sort_len(list1)
    #O(L2)
    list2 = counting_sort_len(list2)
    lst1 = []

    if len(list1) > 0:
        temp = [list1[0][0]]

    #grouping similiar strings together
    #O(L1M1)
    for i in range(len(list1)-1):
        if list1[i][1] == list1[i+1][1]:
            if list1[i][0] != list1[i+1][0]:
                temp += [list1[i+1][0]]
        else:
            lst1 += [(temp, list1[i][1])]
            temp = [list1[i+1][0]]
        if i+1 == len(list1)-1:
            lst1 += [([list1[i+1][0]], list1[i+1][1])]

    #O(L2M2)
    lst2 = []
    if len(list2) > 0:
        temp = [list2[0][0]]
    for i in range(len(list2)-1):
        if list2[i][1] == list2[i+1][1]:
            temp += [list2[i+1][0]]
        else:
            lst2 += [(temp, list2[i][1])]
            temp = [list2[i+1][0]]
        if i+1 == len(list2)-1:
            lst2 += [([list2[i+1][0]], list2[i+1][1])]


    #find anagrams in both lists by using pointers
    i = 0
    res = []
    last = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        j = last
        #both strings need to have the same length to run the loop
        while j < len(lst2) and j >= last and len(lst1[i][1]) == len(lst2[j][1]):
            if lst1[i][1] == lst2[j][1]:
                for k in range(len(lst1[i][0])):
                    res += [lst1[i][0][k]]
                last = j+1
                i += 1
                j += 1
                break
            else:
                j += 1
        else:
            if i >= len(lst1) or j >= len(lst2):
                break 
            if len(lst1[i][1]) > len(lst2[j][1]):
                j += 1
                last = j
            elif len(lst1[i][1]) < len(lst2[j][1]):
                i += 1

    return res


