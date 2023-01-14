from random import choice
from settings import rps_throws

def player_throw():
    """
    """

    throw = input("> ")

    return throw

def rps_throw():
    """
    """

    rps_choice = choice(rps_throws)
    return rps_choice

def main():
    """
    """

    throw1 = player_throw()
    throw2 = rps_throw()

    if throw1 in rps_throws:
    
        if throw1 == "paper":
    
            if throw2 == throw1:
                print("it's a draw")
        
            elif throw2 == "rock":
                throw2 = "scissors"
                print(f"{throw2} beats {throw1}")
        
            elif throw2 == "scissors":
                print(f"{throw2} beats {throw1}")
        
            else:
                print("error")
    
        elif throw1 == "rock":
    
            if throw2 == throw1:
                print("it's a draw")
        
            elif throw2 == "scissors":
                throw2 = "paper"
                print(f"{throw2} beats {throw1}")
        
            elif throw2 == "paper":
                print(f"{throw2} beats {throw1}")
        
            else:
                print("error")
        
        elif throw1 == "scissors":
    
            if throw2 == throw1:
                print("it's a draw")
    
            elif throw2 == "paper":
                throw2 = "rock"
                print(f"{throw2} beats {throw1}")
    
            elif throw2 == "rock":
                print(f"{throw2} beats {throw1}")
    
            else:
                print("error")
    
        else:
            print("error")
    
    else:
        print("that's not an option")

if __name__ == "__main__":
    main()
