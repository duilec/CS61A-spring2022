from cats import match, time, word_at
def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(match["times"]))  # contains an *index* for each player
    word_indices = range(len(match["words"]))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    
    # print(match_string(match))


    sort_player = []
    for player_num in player_indices:
        sort_player += [[]]

    fastest_player_num = 0
    for word_index in word_indices:
        fastest_word_index = 0
        min_time = time(match, fastest_player_num, word_index)
        for player_num in player_indices:
            min_time = min(min_time, time(match, player_num, word_index))
            # use the first min_time if it is same situation
            if min_time == time(match, fastest_player_num, fastest_word_index):
                continue
            if min_time == time(match, player_num, word_index):
                fastest_player_num = player_num
                fastest_word_index = word_index
        sort_player[fastest_player_num] += [word_at(match, fastest_word_index)]
    return sort_player

p0 = [2, 2, 3]
p1 = [6, 1, 3]
fastest_words(match(['What', 'great', 'luck'], [p0, p1]))