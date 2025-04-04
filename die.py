import random
class Die:
    """A general class representing a die
    """
    
    def __init__(self, sides=6):
        """Creates a instance of a die with a not set side

        Args:
            sides (int): number of sides. Defaults to 6.
        """
        self.sides = sides

    def roll_die(self):
        """Rolls the created die 

        Returns:
            Int: The number the die lands on
        """
        rolled_die = random.randint(1,self.sides)
        return rolled_die

def main():
    die1 = Die()
    for num in range(10):
        res1 = die1.roll_die()
        print(f"Die 1 rolled: {res1}")
    print()
    die2 = Die(10)
    for num in range(10):    
        res2 = die2.roll_die() 
        print(f"Die 2 rolled: {res2}") 
    print()
    die3 = Die(20)
    for num in range(10):    
        res3 = die3.roll_die() 
        print(f"Die 3 rolled: {res3}") 

if __name__ == '__main__':
    main()