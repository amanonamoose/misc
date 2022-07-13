import cplex
import docplex
from cplex.exceptions import CplexSolverError
import random
import math

NUM_PRISONERS = 100
NUM_GUESSES = math.floor(NUM_PRISONERS / 2)
NUM_ITERATIONS = 1000

boxes = []

def get_random_array(length, number_of_items = -1):
    if number_of_items < 0:
        number_of_items = length

    items = list(range(length))
    random.shuffle(items)
    return items[0:math.floor(number_of_items)]

def try_brute_force():
    results = []
    for i in range(NUM_PRISONERS):
        guesses = get_random_array(NUM_PRISONERS, NUM_PRISONERS / 2)
        is_success = False
        for guess in guesses:
            if boxes[guess] == i:
                # success!
                is_success = True
                break

        results.append(is_success)

    # print results
    everyone_won = True
    output = ''
    num_successes = 0
    for result in results:
        output += 'Y' if result else 'N'
        if not result:
            everyone_won = False
        else:
            num_successes += 1

    print('BRUTE FORCE - Individual winning: ' + output)
    print('BRUTE FORCE - Ratio of winners: ' + str(num_successes / NUM_PRISONERS))
    print('BRUTE FORCE - Everyone won: ' + str(everyone_won))

    return everyone_won

def try_own_boxes():
    results = []
    for i in range(NUM_PRISONERS):
        # first guess is our own box
        next_guess = i
        num_guesses = 0
        is_success = False

        while num_guesses < NUM_GUESSES:
            result = boxes[next_guess]
            if result == i:
                is_success = True
                break

            next_guess = result
            num_guesses += 1

        results.append(is_success)

    # print results
    everyone_won = True
    output = ''
    num_successes = 0
    for result in results:
        output += 'Y' if result else 'N'
        if not result:
            everyone_won = False
        else:
            num_successes += 1

    print('OWN_BOXES - Individual winning: ' + output)
    print('OWN_BOXES - Ratio of winners: ' + str(num_successes / NUM_PRISONERS))
    print('OWN_BOXES - Everyone won: ' + str(everyone_won))

    return everyone_won

if __name__ == '__main__':
    assert(NUM_PRISONERS % 2 == 0)
    num_brute_force_winners = 0
    num_own_boxes_winners = 0
    for i in range(NUM_ITERATIONS):
        boxes = get_random_array(NUM_PRISONERS)
        if try_brute_force():
            num_brute_force_winners += 1

        if try_own_boxes():
            num_own_boxes_winners += 1

    print("Ratio of brute force winnings: " + str(num_brute_force_winners / NUM_ITERATIONS))
    print("Ratio of own boxes winnings: " + str(num_own_boxes_winners / NUM_ITERATIONS))
