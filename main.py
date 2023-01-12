from random import choice

throw = input("> ")
assert isinstance(throw, str) # should be a string

def main(throw):
    """
    """

    rps_throws = [
        "paper",
        "rock",
        "scissors"
    ]

    rps_choice = choice(rps_throws)
    assert rps_choice in rps_throws # should be either paper, rock, or scissors

    if throw in rps_throws:
    
        if throw == "paper":
    
            if rps_choice == throw:
                print("it's a draw")
        
            elif rps_choice == "rock":
                rps_choice = "scissors"
                print(f"{rps_choice} beats {throw}")
        
            elif rps_choice == "scissors":
                print(f"{rps_choice} beats {throw}")
        
            else:
                print("error")
    
        elif throw == "rock":
    
            if rps_choice == throw:
                print("it's a draw")
        
            elif rps_choice == "scissors":
                rps_choice = "paper"
                print(f"{rps_choice} beats {throw}")
        
            elif rps_choice == "paper":
                print(f"{rps_choice} beats {throw}")
        
            else:
                print("error")
        
        elif throw == "scissors":
    
            if rps_choice == throw:
                print("it's a draw")
    
            elif rps_choice == "paper":
                rps_choice = "rock"
                print(f"{rps_choice} beats {throw}")
    
            elif rps_choice == "rock":
                print(f"{rps_choice} beats {throw}")
    
            else:
                print("error")
    
        else:
            print("error")
    
    else:
        print("that's not an option")

if __name__ == "__main__":
    main(throw)
