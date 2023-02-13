from random import *

# various strategies to compare and contrast in the genetic algorithm, also a random bot to initialize a random state


def tit_for_tat_bot(member):
    opponent_strategy = []
    for i in range(64):
        if member[-1:] == 'D' and i >= 1:
            opponent_strategy.append('D')
        else:
            opponent_strategy.append('C')
    return opponent_strategy


def random_bot():
    strategy = []
    for i in range(64):
        strategy.append(choice('CD'))
    return strategy


def suspicious_tit_for_tat_bot(member):
    opponent_strategy = []
    for i in range(64):
        if i == 0:
            opponent_strategy.append('D')
        if member[-1:] == 'C' and i >= 1:
            opponent_strategy.append('C')
        else:
            opponent_strategy.append('D')
    return opponent_strategy


def tit_for_two_tats_bot(member):
    opponent_strategy = []
    for i in range(64):
        if i == 0 and i == 1:
            opponent_strategy.append('C')
        if member[-2:] == ['D', 'D'] and i >= 2:
            opponent_strategy.append('D')
        else:
            opponent_strategy.append('C')
    return opponent_strategy


def defect_bot():
    strategy = []
    for i in range(64):
        strategy.append('D')
    return strategy


def coop_bot():
    strategy = []
    for i in range(64):
        strategy.append('C')


