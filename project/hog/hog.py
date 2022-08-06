"""CS 61A Presents The Game of Hog."""

import argparse
from email import message
from multiprocessing.spawn import old_main_modules
from sys import flags
from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    sum = 0
    one_flag = 0
    while num_rolls:
        dice_value = dice()
        if dice_value == 1:
            one_flag = 1
        else:
            sum += dice_value
        num_rolls -= 1 # we must 'num_rolls -= 1' from either condition
    if one_flag == 1:
        return 1       
    return sum
    # END PROBLEM 1


def digit_fn(digit):
    """Return the corresponding function for the given DIGIT.

    value:  The value which this function starts at.
    """
    # Error if DIGIT is not one of: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    assert isinstance(digit, int) and 0 <= digit < 10
    # List of pre-defined functions
    f0 = lambda value: value + 1
    f1 = lambda value: value ** 2
    f2 = lambda value: value * 3
    f3 = lambda value: value // 4
    f4 = lambda value: value - 5
    f5 = lambda value: value % 6
    f6 = lambda value: int((value % 7) * 8)
    f7 = lambda value: int(value * 8.8)
    f8 = lambda value: int(value / 99 * 15) + 10
    f9 = lambda value: value
    # Mapping from digit to function
    if digit == 0:
        return f0
    elif digit == 1:
        return f1
    elif digit == 2:
        return f2
    elif digit == 3:
        return f3
    elif digit == 4:
        return f4
    elif digit == 5:
        return f5
    elif digit == 6:
        return f6
    elif digit == 7:
        return f7
    elif digit == 8:
        return f8
    elif digit == 9:
        return f9


def hefty_hogs(player_score, opponent_score):
    """Return the points scored by player due to Hefty Hogs.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # return 1
    # if player choose roll zero 
    # and opponent_score == 0
    if opponent_score == 0:
        return 1 
    
    # return player_score by computing of nest functions
    # if player choose roll zero 
    # and opponent_score == digit
    while opponent_score:
        hefty_hogs_right_digit = opponent_score % 10
        player_score = digit_fn(hefty_hogs_right_digit)(player_score)
        opponent_score //= 10
    return player_score % 30
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided, goal=GOAL_SCORE):
    """Simulate a turn rolling NUM_ROLLS dice,
    which may be 0 in the case of a player using Hefty Hogs.
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    goal:            The goal score of the game.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert max(player_score, opponent_score) < goal, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # if play choose roll zero ,calling hefty_hogs
    if num_rolls == 0:
        return hefty_hogs(player_score, opponent_score)
    return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def hog_pile(player_score, opponent_score):
    """Return the points scored by player due to Hog Pile.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if player_score % 10 == opponent_score % 10:
            hog_pile_right_digit = opponent_score % 10
            return hog_pile_right_digit
    return 0
    # END PROBLEM 4


def next_player(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> next_player(0)
    1
    >>> next_player(1)
    0
    """
    return 1 - who


def silence(score0, score1, leader=None):
    """Announce nothing (see Phase 2)."""
    return leader, None


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call every turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    leader = None  # To be used in problem 7
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    "Players take turns rolling dice 'until' one of the players reaches the goal score." 
    "make sure you're only calling take_turn 'once' per turn!"
    # while score0 < goal and score1 < goal:
    #     # player0
    #     if who == 0: 
    #         roll_num0 = strategy0(score0, score1)
    #         turn_incr0 = take_turn(roll_num0, score0, score1, dice, goal)
    #         score0 += turn_incr0
    #         if score0 % 10 == score1 % 10:
    #             hog_pile_incr0 = hog_pile(score0, score1)
    #             score0 += hog_pile_incr0
    #     # player1
    #     if who == 1:
    #         roll_num1 = strategy1(score1, score0)       
    #         turn_incr1 = take_turn(roll_num1, score1, score0, dice, goal)
    #         score1 += turn_incr1          
    #         if score0 % 10 == score1 % 10:
    #             hog_pile_incr1 = hog_pile(score0, score1)
    #             score1 += hog_pile_incr1
    #     who = next_player(who)
    # END PROBLEM 5
    # (note that the indentation for the problem 7 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        # player0
        if who == 0: 
            roll_num0 = strategy0(score0, score1)
            turn_incr0 = take_turn(roll_num0, score0, score1, dice, goal)
            score0 += turn_incr0
            if score0 % 10 == score1 % 10:
                hog_pile_incr0 = hog_pile(score0, score1)
                score0 += hog_pile_incr0
        # player1
        if who == 1:
            roll_num1 = strategy1(score1, score0)       
            turn_incr1 = take_turn(roll_num1, score1, score0, dice, goal)
            score1 += turn_incr1          
            if score0 % 10 == score1 % 10:
                hog_pile_incr1 = hog_pile(score0, score1)
                score1 += hog_pile_incr1
        "If the message is not None and is not the empty string "", it should be printed."
        leader, message = say(score0, score1, leader)
        if message != None:
            print(message)
        who = next_player(who)

    # END PROBLEM 7
    return score0, score1

    # pass 05.py -> test_number=7964 (spent 3.5 hours)
    # It just a guess! why? what rule? I can't find it (I spent 3.5 hour to fix it)
    # I guess it is a old test from ald version, 
    # beacuse I pass all other tests (109 tests) when removing 'test_number=7964'
    # if score0 == 0 and player_roll_num0 == 0:
    #     score1 = score1 // 2 + 1

    # solution:
    # return 1 not return 1 + player_score
    # if player choose roll zero 
    # and opponent_score == 0

    # but, I can't understand two points
    # 1. player0 can continuosly rolls dices three times in 'test_number=7964' 
    # 2. why player1_score be changed by take_turn(roll_num=0, score1=12, score0=0, dice, 30)
    #    when player0 rolling during the first three times in 'test_number=7964'?
    # to tests the first condition of hefty_hogs?
    # if palyer0_score not change, we will let player1 do same rolls? 
    # I guess the reason come from 'tests.play_utils.describe_game'    


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1, player=None):
    """A commentary function that announces the score for each player."""
    message = f"Player 0 now has {score0} and now Player 1 has {score1}"
    return player, message


def announce_lead_changes(score0, score1, last_leader=None):
    """A commentary function that announces when the leader has changed.

    >>> leader, message = announce_lead_changes(5, 0)
    >>> print(message)
    Player 0 takes the lead by 5
    >>> leader, message = announce_lead_changes(5, 12, leader)
    >>> print(message)
    Player 1 takes the lead by 7
    >>> leader, message = announce_lead_changes(8, 12, leader)
    >>> print(leader, message)
    1 None
    >>> leader, message = announce_lead_changes(8, 13, leader)
    >>> leader, message = announce_lead_changes(15, 13, leader)
    >>> print(message)
    Player 0 takes the lead by 2
    """
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    if score0 == score1:
        return None, None
    elif score0 > score1:
        leader = 0
        lead_score = score0 - score1
    elif score1 > score0:
        leader = 1
        lead_score = score1 - score0

    if leader == last_leader:
        return leader, None
    
    # use str() convert int to string, otherwise the following info will be printed
    # TypeError: can only concatenate str (not “int“) to str
    # or use format f"..."
    message = f"Player {leader} takes the lead by {lead_score}"
    # message = 'Player ' + str(leader) + ' takes the lead by ' + str(lead_score)
    return leader, message
    # END PROBLEM 6


def both(f, g):
    """A commentary function that says what f says, then what g says.

    >>> say_both = both(say_scores, announce_lead_changes)
    >>> player, message = say_both(10, 0)
    >>> print(message)
    Player 0 now has 10 and now Player 1 has 0
    Player 0 takes the lead by 10
    >>> player, message = say_both(10, 8, player)
    >>> print(message)
    Player 0 now has 10 and now Player 1 has 8
    >>> player, message = say_both(10, 17, player)
    >>> print(message)
    Player 0 now has 10 and now Player 1 has 17
    Player 1 takes the lead by 7
    """
    def say(score0, score1, player=None):
        f_player, f_message = f(score0, score1, player)
        g_player, g_message = g(score0, score1, player)
        if f_message and g_message:
            return g_player, f_message + "\n" + g_message
        else:
            return g_player, f_message or g_message
    return say


#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, total_samples=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    "I FORGET roll_dice() return 1 when meeting dice_dot equal 1"
    "Python-style: PASS '*args', NOT PASS 'args'"
    # I can't understand averaged_func() just repeatedly calls orgfunc()
    # and *args as arguments of orgfunc()
    # before I compute it
    def averaged_func(*args):
        cnt = total_samples
        sum = 0
        while cnt:
            sum += original_function(*args)
            cnt -= 1
        average = sum / total_samples
        return average
    return averaged_func
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    
    "If two numbers of rolls are tied for the maximum average score, return the lower number."

    "I don't pay attention to the following illustration(waste 1 hour)"
    # In order to pass all of our tests, please make sure that you are testing dice rolls
    # starting from 1 going up to 10, rather than starting from 10 to 1.
    max_num_dice = 1
    another_num_dice = 2

    averaged_roll_dice = make_averaged(roll_dice, total_samples)
    max_aver = averaged_roll_dice(max_num_dice, dice)
    
    while another_num_dice <= 10:
        another_aver = averaged_roll_dice(another_num_dice, dice)
        if another_aver > max_aver:
            max_num_dice = another_num_dice
            max_aver = another_aver
        another_num_dice += 1
    return max_num_dice
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)
    print('always_roll(6) win rate:', average_win_rate(always_roll(6)))

    #print('always_roll(8) win rate:', average_win_rate(always_roll(8)))
    #print('hefty_hogs_strategy win rate:', average_win_rate(hefty_hogs_strategy))
    print('hog_pile_strategy win rate:', average_win_rate(hog_pile_strategy))
    #print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def hefty_hogs_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice if that gives at least THRESHOLD points, and
    returns NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    if hefty_hogs(score, opponent_score) >= threshold:
        return 0
    return num_rolls
    # return 6  # Remove this line once implemented.
    # END PROBLEM 10


def hog_pile_strategy(score, opponent_score, threshold=8, num_rolls=6):
    """This strategy returns 0 dice when this would result in Hog Pile taking
    effect. It also returns 0 dice if it gives at least THRESHOLD points.
    Otherwise, it returns NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    # hefty_hogs_strategy must be at the forefront,
    # beacuse 'line:473' let score increase
    if hefty_hogs_strategy(score, opponent_score, threshold, num_rolls) == 0:
        return 0
    incr = hefty_hogs(score, opponent_score)
    score += incr
    "I don't pay attention to the following illustration(waste 1 hour)"
    "This strategy returns 0 dice when this would result in Hog Pile taking effect."
    if hog_pile(score, opponent_score) > 0:
        return 0
    return num_rolls
    # return 6  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
