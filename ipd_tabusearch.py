from abc import ABCMeta, abstractmethod
from collections import deque
from copy import deepcopy
from numpy import argmax
from opponent import *


class TabuSearch:
    """
    Conducts tabu search
    """
    __metaclass__ = ABCMeta

    cur_steps = None

    tabu_size = None
    tabu_list = None

    initial_state = None
    current = None
    best = None

    max_steps = None
    max_score = None

    def __init__(self, initial_state, tabu_size, max_steps, max_score=None):
        """
        :param initial_state: initial state, should implement __eq__ or __cmp__
        :param tabu_size: number of states to keep in tabu list
        :param max_steps: maximum number of steps to run algorithm for
        :param max_score: score to stop algorithm once reached
        """
        self.initial_state = initial_state

        if isinstance(tabu_size, int) and tabu_size > 0:
            self.tabu_size = tabu_size
        else:
            raise TypeError('Tabu size must be a positive integer')

        if isinstance(max_steps, int) and max_steps > 0:
            self.max_steps = max_steps
        else:
            raise TypeError('Maximum steps must be a positive integer')

        if max_score is not None:
            if isinstance(max_score, (int, float)):
                self.max_score = float(max_score)
            else:
                raise TypeError('Maximum score must be a numeric type')

    def __str__(self):
        return ('TABU SEARCH: \n' +
                'CURRENT STEPS: %d \n' +
                'BEST SCORE: %f \n' +
                'BEST MEMBER: %s \n\n') % \
               (self.cur_steps, self._score(self.best), str(self.best))

    def __repr__(self):
        return self.__str__()

    def _clear(self):
        """
        Resets the variables that are altered on a per-run basis of the algorithm
        :return: None
        """
        self.cur_steps = 0
        self.tabu_list = deque(maxlen=self.tabu_size)
        self.current = self.initial_state
        self.best = self.initial_state

    def __eq__(self, other):
        if isinstance(self, other):
            return self.initial_state == other

    @abstractmethod
    def _score(self, state):
        """
        Returns objective function value of a state
        :param state: a state
        :return: objective function value of state
        """
        score = 0
        opponent_state = random_bot()
        for i in range(len(state)):
            if state[i] == 'D':
                if opponent_state[i] == 'D':
                    score += 2
            elif state[i] == 'C':
                if opponent_state[i] == 'C':
                    score += 6
            else:
                score += 5
        return score

    @abstractmethod
    def _neighborhood(self):
        """
        Returns list of all members of neighborhood of current state, given current state
        :return: list of members of neighborhood
        """
        neighborhood = [[]]
        current_state = self.current
        n = len(current_state)
        for j in range(1000):
            neighbor = []
            for i in range(n):
                new_state = current_state
                if current_state[i] == 'C' or current_state[i] == 'D':
                    new_state = choice('CD')

                neighbor.append(new_state)
            neighborhood.append(neighbor)
        return neighborhood

    def _best(self, neighborhood):
        """
        Finds the best member of a neighborhood
        :param neighborhood: a neighborhood
        :return: the best member of neighborhood
        """
        return neighborhood[argmax([self._score(x) for x in neighborhood])]

    def run(self, verbose=True):
        """
        Conducts tabu search
        :param verbose: indicates whether to print progress regularly
        :return: best state and objective function value of best state
        """
        self._clear()
        for i in range(self.max_steps):
            self.cur_steps += 1

            if ((i + 1) % 100 == 0) and verbose:
                print(self)

            neighborhood = self._neighborhood()
            neighborhood_best = self._best(neighborhood)

            while True:
                if all([x in self.tabu_list for x in neighborhood]):
                    print("TERMINATING - NO SUITABLE NEIGHBORS")
                    return self.best, self._score(self.best)
                if neighborhood_best in self.tabu_list:
                    if self._score(neighborhood_best) > self._score(self.best):
                        self.tabu_list.append(neighborhood_best)
                        self.best = deepcopy(neighborhood_best)
                        break
                    else:
                        neighborhood.remove(neighborhood_best)
                        neighborhood_best = self._best(neighborhood)
                else:
                    self.tabu_list.append(neighborhood_best)
                    self.current = neighborhood_best
                    if self._score(self.current) > self._score(self.best):
                        self.best = deepcopy(self.current)
                    break

            if self.max_score is not None and self._score(self.best) > self.max_score:
                print("TERMINATING - REACHED MAXIMUM SCORE")
                return self.best, self._score(self.best)
        print("TERMINATING - REACHED MAXIMUM STEPS")
        print(self.best, self._score(self.best))
        print(self.__str__().replace("'", ''))


if __name__ == '__main__':
    ts = TabuSearch(initial_state=random_bot(), max_steps=150, tabu_size=128)
    ts.run()
