############################################
# FILE: ex7.py
# WRITER: OREN SULTAN, orens, 201557972
# EXERCISE: intro2cs ex7 2015-2016
# DESCRIPTION: Implementation of recursive functions and some help functions
# In addition, implementation of hanoi game by using "hanoi_game.py"
############################################


# definitions of constants

SMALLEST_DIVISOR = 2


def print_to_n(n):
    """
    :param n:
    :return: all numbers from 1 to n in ascending order
    """
    if n < 1:
        # invalid input for n
        return None
    if n == 1:
        # base case: if n == 1 print 1
        print(1)
    else:
        # recursive call: I assume we have solution for print numbers from
        # 1 to n-1, all I have to do is to print the number n
        print_to_n(n-1)
        print(n)


def print_reversed_n(n):
    """
    :param n:
    :return: all numbers from n to 1 in descending order
    """
    if n < 1:
        # invalid input for n
        return None
    if n == 1:
        # base case: if n == 1 print 1
        print(1)
    else:
        # first print n, then, recursive call
        print(n)
        print_reversed_n(n-1)


def has_divisor_smaller_than(n, i):
    """
    :param n:
    :param i:
    :return: boolean, True if n has smaller divisor than i,
     otherwise, False
    """

    if i <= SMALLEST_DIVISOR:
        # if i == 1 or i == 2 so of course there is no smaller divisor
        # (the divisor should be different than 1 and of course different
        # than 0)
        return False
    else:
        # if i-1 is a divisor or there is a divisor among the numbers
        # which are smaller than i-1, so, return True
        return n % (i-1) == 0 or has_divisor_smaller_than(n, i-1)


def is_prime(n):
    """
    :param n:
    :return: if n is prime or not by using has_divisor_smaller_than
     recursive function
    """
    if n <= 1:
        # if n == 1 or n == 0 or n is negative so n is not a prime number
        # return False
        return False
    # if n has no smaller divisor than n, return True
    # that is mean n has no divisor at all, so, it is prime number
    return not has_divisor_smaller_than(n, n)


def divisor(n, i, divisors_lst):
    """
    :param n:
    :param i:
    :param divisors_lst:
    :return: divisors_lst from i to n / 2
    for example: for n = 12 the list will be:
    1, 2, 4, 6
    """
    if n % i == 0:
        # append the divisor
        divisors_lst.append(i)
    i += 1
    if n / i < 2:
        # stop condition
        return divisors_lst
    # recursive call
    divisor(n, i, divisors_lst)
    return divisors_lst


def divisors(n):
    """
    :param n:
    :return: divisors_lst with all divisors of n
    from 1 to n in ascending order.
    by calling divisor recursive function and adding
    n to the returned divisor list
    """
    divisors_lst = []
    # take care of negative number
    # for example for n = -6 the return value will be
    # [1,2,3,6] like for n = 6
    n = abs(n)
    if n == 0:
        return []
    if n == 1:
        divisors_lst.append(1)
        return divisors_lst
    divisors_lst = divisor(n, 1, divisors_lst)
    # if divisors_lst is None, we want to return None
    # else append n to lst and return the lst
    if divisors_lst is not None:
        divisors_lst.append(n)
    return divisors_lst


def factorial(n):
    """
    :param n:
    :return: n!
    """
    if n <= 1:
        # base case: 0! = 1 and 1! = 1 by definition
        return 1
    else:
        # recursive call: n! = (n-1)! * n
        return factorial(n-1) * n


def pow_x_n(x, n):
    """
    :param x:
    :param n:
    :return: x ^ n
    """
    if n == 0 or x == 1:
        # base case: x ^ 0 = 1 and 1 ^ n = 1 by definition
        return 1
    else:
        # recursive call: x ^ n = x * x ^ n-1
        return x * pow_x_n(x, n-1)


def exp_n_x(n, x):
    """
    :param n:
    :param x:
    :return: exp_n_x
    """
    if n == 0:
        # base case: x ^ 0 / 0! = 1 / 1 = 1
        return 1
    else:
        # recursive call: exp_n_x(n-1,x) + x ^ n / n!
        return exp_n_x(n-1, x) + (pow_x_n(x, n) / factorial(n))


def play_hanoi(hanoi, n, src, dest, temp):
    """
    :param hanoi:
    :param n:
    :param src:
    :param dest:
    :param temp:
    :return: result of hanoi game from src to dest with n disks
    """
    if n <= 0:
        # nothing to do with n == 0 or negative so just return
        return
    if n == 1:
        # base case: if only one disk, so move the disk from src to dest
        hanoi.move(src, dest)
    else:
        # recursive call
        # move n-1 disks from src to temp
        play_hanoi(hanoi, n-1, src, temp, dest)
        # move 1 (the biggest) disk from src to dest
        hanoi.move(src, dest)
        # recursive call
        # move n-1 disks from temp to dest
        play_hanoi(hanoi, n-1, temp, dest, src)


def print_binary_sequences_with_prefix(prefix, n):
    """
    :param prefix:
    :param n:
    :return: print combination of n characters from "1" and "0" after
    a specific prefix
    """
    if n == 0:
        # base case: if n == 0 so print only the prefix
        print(prefix)
        return
    # recursive call: assume that there is a solution for n-1
    # characters after prefix. all we have to do is to print "0" or "1"
    # one time with "0" in the end
    print_binary_sequences_with_prefix(prefix + "0", n-1)
    # second time with "1" in the end
    print_binary_sequences_with_prefix(prefix + "1", n-1)


def print_binary_sequences(n):
    """
    :param n:
    :return: print all combinations of "0" and "1"
    for sequence of n characters.
    by using print_binary_sequences_with_prefix
    which is a recursive function
    """
    if n == 0:
        # base case: if 0 characters, print empty string
        print("")
        return
    # two calls for print_binary_sequences_with_prefix
    # first call with prefix "1" and second call with prefix "0"
    # print_binary_sequences_with_prefix should create combination of
    # "1" and "0" with n characters with prefix
    print_binary_sequences_with_prefix("1", n-1)
    print_binary_sequences_with_prefix("0", n-1)


def remove_duplicates(char_list):
    """
    :param char_list:
    :return: char_list without duplicates of chars
    """
    new_char_list = []
    for char in char_list:
        if char not in new_char_list:
            # create new list with unique characters
            new_char_list.append(char)
    return new_char_list


def print_sequences_with_prefix(prefix, char_list, n):
    """
    :param prefix:
    :param char_list:
    :param n:
    :return: print sequence of n characters from characters of
    char_list after a specific prefix
    """
    if n == 0:
        # base case: if n == 0, print only prefix
        print(prefix)
        return
    for char in char_list:
        # assume that there is solution for prefix + n-1 characters
        # all I have to do is adding a char from char_list
        # for each solution I should add different char from char_list
        print_sequences_with_prefix(prefix + char, char_list,  n-1)


def print_sequences(char_list, n):
    """
    :param char_list:
    :param n:
    :return: print sequences of n characters from char_list
    by using print_sequences_with_prefix
    """

    # if empty list or n==0
    if n == 0 or len(char_list) == 0:
        print("")
        return
    # eliminate duplicates in the list
    char_list = remove_duplicates(char_list)
    for char in char_list:
        # print_sequences_with_prefix function will return
        # solution of n-1 characters, for each solution we will add
        # different char from char_list
        print_sequences_with_prefix(char, char_list, n-1)


def print_sequences_with_prefix_no_repetition(prefix, char_list, n):
    """
    :param prefix:
    :param char_list:
    :param n:
    :return: print sequence of n characters from characters of
    char_list after a specific prefix without repetition of characters
    """
    if n == 0:
        # base case: if n == 0 print only prefix
        print(prefix)
        return
    for char in char_list:
        # recursive call: we assume we have solution for prefix + n-1
        # characters and add for each solution different char from char_list
        # only if the char is not exist in the prefix
        if char not in prefix:
            print_sequences_with_prefix_no_repetition(prefix + char, char_list, n-1)


def print_no_repetition_sequences(char_list, n):
    """
    :param char_list:
    :param n:
    :return: print sequences of n characters from char_list
    without repetition, by using recursive function:
    print_sequences_with_prefix_no_repetition
    """

    if n == 0 or len(char_list) == 0:
        print("")
        return
    char_list = remove_duplicates(char_list)
    for char in char_list:
        # print_sequences_with_prefix_no_repetition function will return
        # solution of n-1 characters, for each solution we will add
        # different char from char_list
        print_sequences_with_prefix_no_repetition(char, char_list, n-1)


def sequences_with_prefix_no_repetition(prefix, char_list, new_list, n):
    """
    :param prefix:
    :param char_list:
    :param new_list:
    :param n:
    :return: list with sequences of n characters after a prefix, without
    repetition of characters
    """
    if n == 0:
        # if n == 0 append to list only prefix and return the list
        new_list.append(prefix)
        return new_list
    for char in char_list:
        # recursive call: assuming there is a solution for prefix and n-1
        # characters after the prefix. all we have to do is to add for each
        # solution a char from char_list, only if the char is not in prefix
        if char not in prefix:
            sequences_with_prefix_no_repetition(prefix + char, char_list, new_list, n-1)
    return new_list


def no_repetition_sequences_list(char_list, n):
    """
    :param char_list:
    :param n:
    :return: new list of sequences of n characters from char_list
     without repetition. by using sequences_with_prefix_no_repetition
    """

    if n == 0 or len(char_list) == 0:
        # empty list or n == 0
        return ['']
    # eliminate duplicates in char_list
    char_list = remove_duplicates(char_list)
    new_list = []
    for char in char_list:
        # add to new_list a char from char_list
        # new list is the list from sequences_with_prefix_no_repetition function
        # so it is a list with all sequences of n-1 characters with no repetition
        new_list = sequences_with_prefix_no_repetition(char, char_list, new_list, n-1)
    return new_list

