import puppy_state
import state_asleep
import state_play
class StateEat(puppy_state.Puppy_State):
    """Eat State to implement puppy's reactions
    Attributes:
        N/A
    """
    def play(self, puppy):
        """puppy's reaction when user trys to play with the puppy"""
        puppy.change_state(state_play.StatePlay())
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."
        
    def feed(self, puppy):
        """puppy's reaction when user trys to feed the puppy """
        puppy.inc_feeds()
        if puppy.feeds <= 2:
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."
        else:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "The puppy continues to eat as you add another scoop of kibble to its bowl."\
            "\nThe puppy ate too much and now fall alseep."
            