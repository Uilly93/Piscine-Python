from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__():
        pass

    def die():
        pass
# your code here


class Stark(Character):
    """Your docstring for Class"""
    first_name = Character
    is_alive = True

    def __init__(self, name, alive=None):
        # """init the object with 2 parameters
        # name: str
        # alive: bool (optionnal)"""
        """Your docstring for Constructor"""
        self.first_name = name
        self.is_alive = True
        if alive is not None:
            self.is_alive = alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False

# your code here


def main():
    try:
        # hodor = Character("hodor")
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
