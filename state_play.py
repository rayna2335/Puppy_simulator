import puppy_state
import state_asleep

class StatePlay(puppy_state.Puppy_State):
    """Play State to implement puppy's reactions
    Attributes:
        N/A
    """
    def play(self, puppy):
        """puppy's reaction when user trys to play with the puppy"""
        puppy.inc_plays()
        if puppy.plays <= 2:
            return "You throw the ball again and the puppy excitedly chases it."
        else:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "You throw the ball again and the puppy excitedly chases it."\
            "\nPuppy played so much now it fell alseep!"
        
    def feed(self, puppy):
        """puppy's reaction when user trys to feed the puppy """
        return "The puppy is too busy playing with the ball to eat right now."
