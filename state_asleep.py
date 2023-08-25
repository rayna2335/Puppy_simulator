import puppy_state
import state_eat


class StateAsleep(puppy_state.Puppy_State):
    """Asleep State to implement puppy's reactions
    Attributes:
        N/A
    """
    def play(self, puppy):
        """puppy's reaction when user trys to play with the puppy"""
        return "The puppy is asleep. It doesn't want to play right now."


    def feed(self, puppy):
        """puppy's reaction when user trys to feed the puppy """
        puppy.change_state(state_eat.StateEat())
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat"