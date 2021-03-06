"""

random_walker_bot_v2.1.py

This bot attacks any enemies that are close by or otherwise moves
around randomly.

Add in call to random.seed() to make choice of motion random.


"""

import random

import rg

class Robot:

    def act(self, game):
        # If there are enemies around, attack them.
        for loc, bot in game.robots.iteritems():
            if bot.player_id != self.player_id:
                if rg.dist(loc, self.location) <= 1:
                    return ['attack', loc]

        # Otherwise find possible moves around the bot and then
        # randomly pick one.
        moves = rg.locs_around(self.location,
                               filter_out=('invalid', 'obstacle'))

        random.seed()
        if len(moves) > 0:
            return ['move', random.choice(moves)]

        # If no moves available just guard
        return ['guard']
