from lib2to3.pgen2.literals import evalString


HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos < 10:
        return int(pos == 8)
    else:
        return int(pos % 10 == 8) + num_eights(pos // 10) 

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    # we can create a helper func that have more than one agrument
    # flag = 1 => down; flag = 0 => up
    def helper(ping ,pong, flag):
        if ping == n:
            return pong
                
        if flag == 0 and (num_eights(ping) or ping % 8 == 0):
            return helper(ping + 1, pong - 1, flag = 1)
        elif flag == 1 and (num_eights(ping) or ping % 8 == 0):
            return helper(ping + 1, pong + 1, flag = 0)

        if ping < 8:
            return helper(ping + 1, pong + 1, flag)
        elif flag == 0:
            return helper(ping + 1, pong + 1, flag)
        else:
            return helper(ping + 1, pong - 1, flag)
    return helper(1 ,1, 0)
    
"use loop"
    # ping = 1
    # pong = 1
    # flag = 0 # flag = 1 => down; flag = 0 => up
    # while(n != ping):
    #     if flag == 0 and (num_eights(ping) or ping % 8 == 0):
    #         flag = 1
    #     elif flag == 1 and (num_eights(ping) or ping % 8 == 0):
    #         flag = 0 

    #     if ping < 8:
    #         pong += 1
    #     elif flag == 0:
    #         pong += 1
    #     else:
    #         pong -= 1      
  
    #     ping += 1
    # return pong

"reference answer"
    # flag = 1 => up; flag = -1 => down
    # def helper(pong, ping, flag):
    #     if ping == n:
    #         return pong
    #     elif ping % 8 == 0 or num_eights(ping):
    #         return helper(pong - flag, ping + 1, -flag)
    #     else:
    #         return helper(pong + flag, ping + 1, flag)
    # return helper(1, 1, 1)

def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def get_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> get_smaller_coin(25)
    10
    >>> get_smaller_coin(10)
    5
    >>> get_smaller_coin(5)
    1
    >>> get_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    # "refer to count_partitions(n, m)"
    def get_max_cent_coin(change):
        if change == 1:
            return 1
        elif change < 5:
            return 1
        elif change < 10: # if change == 5, its max_cent_coin also is 5
            return 5
        elif change < 25: # if change == 10, its max_cent_coin also is 10
            return 10
        else:
            return 25 # if change == 25, its max_cent_coin also is 25
    def helper(change, max_cent_coin):
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif max_cent_coin == 1 :
            return 1
        else:
            with_max = helper(change - max_cent_coin, max_cent_coin)
            without_max = helper(change, get_smaller_coin(max_cent_coin))
        return with_max + without_max
    return helper(change, get_max_cent_coin(change))


# def count_partitions(n, m):
#     """
#     >>> count_partitions(6, 4)
#     9
#     """
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0
#     elif m == 0:
#         return 0
#     else:
#         with_m = count_partitions(n-m, m)
#         without_m = count_partitions(n, m-1)
#         return with_m + without_m

"reference answer"
    # def constrained_count(change, smallest_coin):
    #     if change == 0:
    #         return 1
    #     if change < 0:
    #         return 0
    #     if smallest_coin == None:
    #         return 0
    #     without_coin = constrained_count(change, get_larger_coin(smallest_coin))
    #     with_coin = constrained_count(change - smallest_coin, smallest_coin)
    #     return without_coin + with_coin
    # return constrained_count(change, 1)

    # def constrained_count_small(change, largest_coin):
    #     if change == 0:
    #         return 1
    #     if change < 0:
    #         return 0
    #     if largest_coin == None:
    #         return 0
    #     without_coin = constrained_count_small(change, get_smaller_coin(largest_coin))
    #     with_coin = constrained_count_small(change - largest_coin, largest_coin)
    #     return without_coin + with_coin
    # return constrained_count_small(change, 25)

