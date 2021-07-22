# radix_sort_algorithm
### Question 1:
Consider a large dataset of transaction records. Given a number t, we wish to determine which
interval of length t contains the most transactions. All times in this question are measured in
whole seconds after midnight 1/1/1970, i.e. they are non-negative integers.

To solve this problem, a function `best_interval(transactions, t)` is written.

**Input**  
`transactions` is a unsorted list of non-negative integers. Each integer in transactions represents the time that some transaction occurred. 
`t` is a non-negative integer, representing a length of time in seconds. 
        <br>
        
**Output**
An interval is a set of numbers that contains all numbers lying between some starting number and some larger ending number (inclusive). These two numbers are called             the endpoints of the interval. The length of an interval is the absolute difference between the two endpoints.

<br>
Consequently, and interval starting at a and ending at b has length b-a. Conversley, an interval starting at a of length d will end at a+d. best_interval returns a two element tuple, `(best_t, count)`. `best_t` is the time such that the interval starting at `best_t` and ending at `best_t` + `t` contains more elements from `transactions` than any other interval of length `t`.
<br>

If there are multiple such intervals, return the interval with minimal start time. Note that this may mean the interval begins at a time which is not in transactions            (see the example).
<br> 
         
`count` is the number of elements in the interval of length `t` starting at `best_t`.
          
<br>

**Complexity** 
O(nk), where n is the number of elements in transactions and k is the greatest number of digits in any element in transactions
<br>
   

**Example:**
```
t = 5
transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]
>>> best_interval(transaction, t)
(0, 5)
```

### Question 2 
Consider the following problem: Given two lists of words, we wish to find all words in the first list which have an anagram in the second list.
Strings r and s are anagrams of one another if the characters in s can be permuted to form r. Trivially, if r = s, then they are anagrams of one another.
To solve this problem, a function `words_with_anagrams(list1, list2)` is written. 

<br>
**Input**
Both arguments, `list1` and `list2`, are lists of strings, which may be empty. All characters are lowercase a-z. Neither list contains duplicate strings, but there may          be strings which appear in both lists. <br>

<br>
**Output**
A list of strings (in no particular order) from `list1` which have at least one anagram appearing in `list2`. Note that it is possible for two different strings in `list1` to share an anagram in `list2`. <br>

<br>
**Complexity**
O(L1M1 + L2M2), where L1 is the number of elements in list1, L2 is the number of elements in list2, M1 is the number of characters in the longest string in list1, M2             is the number of characters in the longest string in list2. <br>

<br>
**Example:** 
```
list1 = [spot, tops, dad, simple, dine, cats]
list2 = [pots, add, simple, dined, acts, cast]
>>> words_with_anagrams(list1, list2)
[cats, dad, simple, spot, tops]
```

          
    
   
