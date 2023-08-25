
import state_asleep

class Puppy:
    """ Object that the user interact with
    Attributes:
        _plays (int): plays with the puppy
        _feeds (int): feeds the puppy
        _state : puppy's state
    """
    def __init__(self):
        """ initializes the state to asleep state and the number of feeds and plays"""
        self._state = state_asleep.StateAsleep()
        self._feeds = 0
        self._plays = 0

    #getter method for plays
    @property
    def plays(self):
        """Accesses play"""
        return self._plays

    @property
    def feeds(self):
        """Accesses feeds"""
        return self._feeds
        
    def change_state(self, new_state):
        """updates the puppy's state to the new state"""
        self._state = new_state

    def throw_ball(self):
        """calls the play method"""
        return self._state.play(self)

    def give_food(self):
        """calls the feed method"""
        return self._state.feed(self)

    def inc_feeds(self):
        """increments the number of times the puppy has been fed"""
        self._feeds += 1
        

    def inc_plays(self):
        """increments the number of times the puppy has been played with"""
        self._plays += 1

    def reset(self):
        """reinitialize the feeds and play"""
        self._feeds = 0
        self._plays = 0
    