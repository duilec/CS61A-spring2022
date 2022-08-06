"""Typing test implementation"""
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    select_paragraphs = [p for p in paragraphs if select(p)]
    if len(select_paragraphs) <= k:
        return ''
    return select_paragraphs[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def match_topic(sentence):
            sentence = lower(sentence)
            sentence = remove_punctuation(sentence)
            sentence = split(sentence)
            # eg. 'Cute Dog!' => [cute, dog]
            for word1 in sentence:
                for word2 in topic:
                    if word1 == word2:
                        return True
            return False
    return match_topic
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    lenght_typed = len(typed_words)
    lenght_reference = len(reference_words)

    
    if lenght_typed == 0 and lenght_reference == 0:
        return 100.0
    elif lenght_reference == 0:
        return 0.0
    elif lenght_typed == 0:
        return 0.0

    hit_cnt = 0
    typed_cnt = 0
    reference_cnt = 0

    for typed_word in typed_words:
        for reference_word in reference_words:
            if typed_word == reference_word and typed_cnt == reference_cnt:
                hit_cnt += 1
                break
            reference_cnt += 1
        typed_cnt += 1
        reference_cnt = 0  # reset reference_cnt
    return float((hit_cnt / lenght_typed) * 100) # compute the percentage only by lenght_typed
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 * (60 / elapsed)
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing reference words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"

    # same word
    diff_vals = []
    for word in word_list:
        if typed_word == word:
            return typed_word        
        diff_vals += [diff_function(typed_word, word, limit)]
    
    cnt = 0
    min_diff_val = diff_vals[0]
    for diff_val in diff_vals:  
        min_diff_val = min(min_diff_val, diff_val)
        if min_diff_val == diff_val:
            last_min_diff_index = cnt
        cnt += 1
    
    # surpass limit
    if diff_function(typed_word, word_list[last_min_diff_index], limit) > limit:
        return typed_word

    # multiple lowest difference words: we return the first word in multiple lowest difference words
    #    
    # If typed_word is not contained inside word_list, 
    # and multiple strings have the same lowest difference 
    # from typed_word according to the diff_function, 
    # autocorrect should return the string that appears first 
    # in word_list.
    #
    # NOT the first word in word_list, the first word in multiple lowest difference words
    first_min_diff_index = 0
    for diff_val in diff_vals:
        if diff_val == min_diff_val:
            return word_list[first_min_diff_index]
        first_min_diff_index += 1
    
    # END PROBLEM 5


def sphinx_swaps(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_swaps("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_swaps("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_swaps("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_swaps("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_swaps("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    if limit < 0:
        return 0
    elif len(start) == 0:
        return len(goal) # get rest lenght of goal
    elif len(goal) == 0:
        return len(start) # get rest lenght of start
    elif start[0] == goal[0]: 
        return sphinx_swaps(start[1:], goal[1:], limit) # 'limit' only limit operation(substitute)
    else:
        return  1 + sphinx_swaps(start[1:], goal[1:], limit - 1)
    # END PROBLEM 6

    "old version but right answer"
    # assert False, 'Remove this line'
    # def reach_limit(start, goal, limit, cnt):
    #     # If the number of characters that must change is greater than limit, 
    #     # then sphinx_swaps should return 
    #     # any number larger than limit 
    #     # and should minimize the amount of computation needed to do so.
    #     # NOTE:it is 'greater than'!!
    #     if cnt > limit:
    #         return 0
    #     elif len(start) == 0:
    #         return len(goal) # get rest lenght of goal
    #     elif len(goal) == 0:
    #         return len(start) # get rest lenght of start
    #     else:
    #         diff_flag = int(start[0] != goal[0])
    #         if diff_flag:
    #             cnt += 1
    #         return diff_flag + reach_limit(start[1:], goal[1:], limit, cnt)
    # return reach_limit(start, goal, limit, 0)    


def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 1s0
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    # assert False, 'Remove this line'

    # if ______________:  # Fill in the condition
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # elif ___________:  # Feel free to remove or add additional cases
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END

    # else:
    #     add = ...  # Fill in these lines
    #     remove = ...
    #     substitute = ...
    #     # BEGIN
    #     "*** YOUR CODE HERE ***"
    #     # END
    
    # # surpass limit
    if limit < 0:
        return 0
    # the rest length represent times of operation
    elif len(start) == 0:
        return len(goal) 
    elif len(goal) == 0:
        return len(start)
    # 'limit' only limit operations(add, remove or substitute)
    elif start[0] == goal[0]:
        return minimum_mewtations(start[1:], goal[1:], limit)
    # we just count times of operation operation but don't care how to operate it
    # and we should refer to sphinx_swaps(start, goal, limit) by 'important'
    else:
        add = minimum_mewtations(start, goal[1:], limit - 1)
        remove = minimum_mewtations(start[1:], goal, limit - 1)
        substitute = minimum_mewtations(start[1:], goal[1:], limit - 1)
        return min(add, remove, substitute) + 1

    "old version and wrong answer"
    # def match(start, goal):
    #     if len(start) == 0 or len(goal) == 0:
    #         return 0
    #     return int(start[0] == goal[0]) + match(start[1:], goal[1:])    
    # match_lenght = match(start, goal)
    # goal_lenght = len(goal)
    # start_lenght = len(start)

    # if goal_lenght == match_lenght == start_lenght:
    #     return 1
    # elif start_lenght == 0:
    #     return 0
    # else:
    #     def get_diff_index_val(start, goal):
    #         cnt_lenght = min(start_lenght, goal_lenght)
    #         index = 0
    #         while(cnt_lenght):
    #             if start[index] != goal[index]:
    #                 return index, goal[index]
    #             index += 1
    #             cnt_lenght -= 1
    #         if start_lenght < goal_lenght:
    #             return start_lenght, ''
    #         else:
    #             return goal_lenght, ''    
    #     diff_index, diff_val = get_diff_index_val(start, goal)

    #     add_str = start[:diff_index] + diff_val + start[diff_index:]
    #     remove_str = start[:diff_index] + start[diff_index + 1:]
    #     subtitute_str = start[:diff_index] + diff_val + start[diff_index + 1:]

    #     match_add_lenght = match(add_str, goal)
    #     match_remove_lenght = match(remove_str, goal)
    #     match_subtitute_lenght = match(subtitute_str, goal)
    #     if len(add_str) == match_add_lenght == match_add_lenght \
    #         or len(remove_str) == match_remove_lenght == match_remove_lenght \
    #         or len(subtitute_str) == match_subtitute_lenght == match_subtitute_lenght:
    #         return 1
    #     else:
    #         return 1 + min(minimum_mewtations(add_str, goal, limit) ,\
    #             minimum_mewtations(remove_str, goal, limit) ,\
    #             minimum_mewtations(subtitute_str, goal, limit))

def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(sofar, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # count the time of match sofar value and prompt value
    def match_equal(sofar, prompt):
        if len(sofar) == 0 or len(prompt) == 0:
            return 0
        elif sofar[0] != prompt[0]:
            return 0
        else:
            return 1 + match_equal(sofar[1:], prompt[1:])
    ratio = match_equal(sofar, prompt) / max(len(sofar), len(prompt))
    upload({'id': user_id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # Specifically, times[i][j] indicates how long it took player i to type words[j].
    
    times = []
    player_index = 0
    while(player_index < len(times_per_player)):
        time_index = 0
        player_count = len(times_per_player[player_index]) - 1
        while(time_index < player_count):
            times_per_player[player_index][time_index]  \
            = times_per_player[player_index][time_index + 1] \
              - times_per_player[player_index][time_index]
            time_index += 1
        # a list as an element of times
        times += [times_per_player[player_index][:player_count]] 
        player_index += 1
    return {'words':words, 'times':times}

    # 'for' loop version:(it is right!)
    # times = []
    # player_index = 0
    # for player in times_per_player:
    #     time_index = 0
    #     for time in player:
    #         if time == player[len(player) - 1]:
    #             break
    #         player[time_index] = player[time_index + 1] - player[time_index]
    #         time_index += 1
    #     times += [player[:(len(player) - 1)]]
    #     player_index += 1
    # return {'words':words, 'times':times}  

    # END PROBLEM 9


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
    # we should use helper function by reference
    sort_player = []
    for player_num in player_indices:
        sort_player += [[]]

    for word_index in word_indices:
        fastest_player_num = 0 # the first player: player_0
        fastest_word_index = word_index # this column of word
        fastest_time = time(match, fastest_player_num, fastest_word_index)
        for player_num in player_indices:
            current_time = time(match, player_num, word_index)
            fastest_time = min(fastest_time, current_time)
            # use the first fastest_time if this column has same time
            if fastest_time == time(match, fastest_player_num, fastest_word_index):
                continue
            if fastest_time == current_time:
                fastest_player_num = player_num
                fastest_word_index = word_index
        sort_player[fastest_player_num] += [word_at(match, fastest_word_index)]
    return sort_player

    # old version but wrong idea

    # times = match["times"]
    # words = match["words"]
    # time_indices = range(len(times[0]))
    # sort_player_num = []
    # for time_index in time_indices:
    #     min_player_num = 0
    #     for player_num in player_indices:
    #         fastest_time = min(times[player_num][time_index], times[min_player_num][time_index])
    #         if fastest_time == times[min_player_num][time_index]:
    #             continue
    #         if fastest_time == times[player_num][time_index]:
    #             min_player_num = player_num
    #     sort_player_num += [min_player_num]

    # while(time_index < len(player_indices[player_index])):
    #     fastest_time = min(player_indices[player_index][min_time_index], \
    #                    player_indices[player_index][time_index])
    #     if fastest_time == player_indices[player_index][time_index]:
    #         min_time_index = time_index
    #     time_index += 1
        



    return 
    # END PROBLEM 10


def match(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def word_at(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(match["words"]), "word_index out of range of words"
    return match["words"][word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match["words"]), "word_index out of range of words"
    assert player_num < len(match["times"]), "player_num out of range of players"
    return match["times"][player_num][word_index]


def match_string(match):
    """A helper function that takes in a match dictionary and returns a string representation of it"""
    return f"match({match['words']}, {match['times']})"


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
