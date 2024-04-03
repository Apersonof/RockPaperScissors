def RockPaperScissors():
    print("one player or two players (1 or 2)")
    option = input("1 or 2 : ")
    if int(option) == 1:
        singleplayerRPS()
    elif int(option) == 2:
        multiplayerRPS()
    else:
        print("invalid imput: please start again")
        RockPaperScissors()

def singleplayerRPS():
    import random
    robotwin = 0
    humanwin = 0
    while True:
        n = 0
        while n==0:
            print("input rock paper or scissor")
            human = input("here: ")
            if human == "rock" or human == "paper" or human == "scissor":
                n = 1
                
            else:
                print("not an input buddy")

        
        if human == "rock":
            humanity = 1
        elif human == "paper":
            humanity = 2
        elif human == "scissor":
            humanity = 3
        
            print("not an option")
        RobOfDOOM = random.randint(1,3)
        if humanity == RobOfDOOM:
            print("draw 🫠 go again")
            pass
        elif humanity == 1:
            if RobOfDOOM == 2:
                robotwin = robotwin + 1 
                print(f"robots win {robotwin}, humans win {humanwin}")   
            else:
                humanwin = humanwin + 1 
                print(f"robots win {robotwin}, humans win {humanwin}")
        elif humanity == 2:
            if RobOfDOOM == 1:
                humanwin = humanwin + 1 
                print(f"robots win {robotwin}, humans win {humanwin}")   
            else:
                robotwin = robotwin + 1 
                print(f"robots win {robotwin}, humans win {humanwin}")
        elif humanity == 3:
            if RobOfDOOM == 2:
                humanwin = humanwin + 1 
                print(f"robots win {robotwin}, humans win {humanwin}")   
            else:
                robotwin = robotwin + 1 
                print(f"robots win {robotwin}, humans win {humanwin}")
        n = 0
def multiplayerRPS():
    human1wins = 0
    human2wins = 0
    something = 'y'
    while something == 'y':
        n = 0
        while n==0:
            print("input rock paper or scissor player one")
            player1 = input("here: ")
            if player1 == "rock" or player1 == "paper" or player1 == "scissor":
                n = 1      
            else:
                print("not an input buddy")

                
            if player1 == "rock":
                    personofinterestone = 1
            elif player1 == "paper":
                    personofinterestone = 2
            elif player1 == "scissor":
                    personofinterestone = 3
            k = 0
            while k==0:
                print("input rock paper or scissor player two")
                player2 = input("here: ")
                if player2 == "rock" or player2 == "paper" or player2 == "scissor":
                    k = 1      
                else:
                    print("not an input buddy")
            
            if player2 == "rock":
                personofinteresttwo = 1
            elif player2 == "paper":
                personofinteresttwo = 2
            elif player2 == "scissor":
                personofinteresttwo = 3
            
            if personofinterestone == personofinteresttwo:
                print("draw 🫠 go again")
                pass
            elif personofinterestone == 1:
                if personofinteresttwo == 2:
                    human2wins = human2wins + 1 
                    print(f"player two win {human2wins}, player one win {human1wins}")   
                else:
                    human1win = human1win + 1 
                    print(f"player two win {human2wins}, player one win {human1wins}")
            elif personofinterestone == 2:
                if personofinteresttwo == 1:
                        human1win = human1win + 1 
                        print(f"player two win {human2wins}, player one win {human1wins}")   
                else:
                        human2wins = human2wins + 1 
                        print(f"player two win {human2wins}, player one win {human1wins}")
            elif personofinterestone == 3:
                if personofinteresttwo == 2:
                    human1win = human1win + 1 
                    print(f"player two win {human2wins}, player one win {human1wins}")                       
                else:
                    human2wins = human2wins + 1 
                    print(f"player two win {human2wins}, player one win {human1wins}")
        something = input("want to go again (y/n)? ")
        k=0
        n=0

RockPaperScissors()