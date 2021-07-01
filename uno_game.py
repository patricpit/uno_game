"""
Project 3: Uno Card Game
By Peter Ndiuwem Patrick
"""

from termcolor import colored, cprint
import random


def welcome():
    '''
    UNO game started...
    '''

    welcome_text = "welcome to game uno!".upper()
    text = colored(welcome_text, 'blue', attrs=['reverse', 'blink'])
    print(text)
    print("")


'''
Options
'''


def options():
    opt = question = "Select an Option: \n\n"
    option = "1) Game rules\n2) Play UNO\n\n"
    next_thing = input(question + option)
    if type(next_thing) == str and next_thing == "1":
        uno_rules()

    elif type(next_thing) == str and next_thing == "2":
        play_uno()

    else:
        options()
    return opt


def uno_rules():
    rules = """ UNO RULES
                Skip:
                The next player is "skipped".

                Reverse:
                Reverses the direction of play.

                Draw 2:
                The next player must draw 2 cards and lose a turn.

                Draw 4:
                Changes the current color plus the next player must draw 4 cards and lose a turn.

                Wild Card:
                Play this card to change the colour to be matched.

                Matching Cards:
                During play, matching(cards, colours or numbers) can be played.

                Force Play:
                If you have or draw a playable card, you have to play it for play to continue.

                Play Instructions:
                1. Input only numbers while playing.
                2. For game help, input 'help'

                Help:
                For uno rules and play instructions, type 'help'

        """
    cprint(rules, 'yellow')
    play_uno()
    return rules


def play_uno():
    '''
    Build card deck
    '''

    def buildDeck():
        deck = []
        colours = ["Blue", "Yellow", "Green", "Red"]
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
        wilds = ["Wild", "Wild Draw Four"]
        for colour in colours:
            for value in values:
                cardVal = "{} {}".format(colour, value)
                deck.append(cardVal)
                if value != 0:
                    deck.append(cardVal)
        for i in range(4):
            deck.append(wilds[0])
            deck.append(wilds[1])
        return deck

    """
    Shuffles deck
    """

    def shuffleDeck(deck):
        for cardPos in range(len(deck)):
            randPos = random.randint(0, 107)
            deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
        return deck

    """
    Draw card function
    """

    def drawCards(numCards):
        cardsDrawn = []
        for x in range(numCards):
            cardsDrawn.append(unoDeck.pop(0))
        return cardsDrawn

    unoDeck = buildDeck()
    unoDeck = shuffleDeck(unoDeck)
    unoDeck = shuffleDeck(unoDeck)
    discards = []
    # print(unoDeck)

    '''
    Player Class
    '''

    class Player:
        count = 0

        def __init__(self, name):
            self.name = name.upper()
            self.hand = []
            Player.count = Player.count + 1

        def playerHand(self):
            return self.hand

        def display(self):
            print(self.name + " 's Hand", self.hand)

    try:
        uno_players = []
        numPlayers = int(input("How many Players? \n"))
        while numPlayers < 2 or numPlayers > 4:
            numPlayers = int(input("Invalid. Please enter a number between 2-4.  How many players? \n"))
        for player in range(numPlayers):
            if numPlayers == 2:
                name = input("Player1, what's your name? \n")
                P1 = Player(name)
                P1.playerHand()
                P1.display()
                uno_players.append(P1.name)
                print("")

                name = input("Player2, what's your name?  \n")
                P2 = Player(name)
                P2.playerHand()
                P2.display()
                uno_players.append(P2.name)
                print("")
                break

            elif numPlayers == 3:
                name = input("Player1, what's your name?  \n")
                P1 = Player(name)
                P1.playerHand()
                P1.display()
                uno_players.append(P1.name)
                print("")

                name = input("Player2, what's your name?  \n")
                P2 = Player(name)
                P2.playerHand()
                P2.display()
                uno_players.append(P2.name)
                print("")

                name = input("Player3, what's your name?  \n")
                P3 = Player(name)
                P3.playerHand()
                P3.display()
                uno_players.append(P3.name)
                print("")
                break

        else:
            name = input("Player1, what's your name?  \n")
            P1 = Player(name)
            P1.playerHand()
            P1.display()
            uno_players.append(P1.name)
            print("")

            name = input("Player2, what's your name?  \n")
            P2 = Player(name)
            P2.playerHand()
            P2.display()
            uno_players.append(P2.name)
            print("")

            name = input("Player3, what's your name?  \n")
            P3 = Player(name)
            P3.playerHand()
            P3.display()
            uno_players.append(P3.name)
            print("")

            name = input("Player4, what's your name?  \n")
            P4 = Player(name)
            P4.playerHand()
            P4.display()
            uno_players.append(P4.name)
            print("")

        print('uno_players =', uno_players)

        def showHand(uno_players, playerHand):
            if playerTurn == 0:
                print(f"{P1.name}'s Turn".format(uno_players + 1))
                print("Your Hand")
                print("------------------")
                y = 1
                for card in playerHand:
                    print("{}) {}".format(y, card))
                    y += 1
                print("")

            elif playerTurn == 1:
                print(f"{P2.name}'s Turn".format(uno_players + 1))
                print("Your Hand")
                print("------------------")
                y = 1
                for card in playerHand:
                    print("{}) {}".format(y, card))
                    y += 1
                print("")


            elif playerTurn == 2:
                print(f"{P3.name}'s Turn".format(uno_players + 1))
                print("Your Hand")
                print("------------------")
                y = 1
                for card in playerHand:
                    print("{}) {}".format(y, card))
                    y += 1
                print("")


            else:
                print(f"{P4.name}'s Turn".format(uno_players + 1))
                print("Your Hand")
                print("------------------")
                y = 1
                for card in playerHand:
                    print("{}) {}".format(y, card))
                    y += 1
                print("")

        def canPlay(colour, value, playerHand):
            for card in playerHand:
                if "Wild" in card:
                    return True
                elif colour in card or value in card:
                    return True
            return False

        players = []
        playerTurn = 0
        colours = ["Blue", "Yellow", "Green", "Red"]
        numPlayers = len(uno_players)
        playDirection = 1
        playing = True
        discards.append(unoDeck.pop(0))
        splitCard = discards[0].split(" ", 1)
        currentColour = splitCard[0]
        if currentColour != "Wild":
            cardVal = splitCard[1]
        else:
            cardVal = "Any"

        for player in uno_players:
            cprint(player, 'red')

        for player in range(numPlayers):
            players.append(drawCards(5))
        print("")

        while playing:
            showHand(playerTurn, players[playerTurn])
            print("Card on top of discard pile: {}".format(discards[-1]))
            if canPlay(currentColour, cardVal, players[playerTurn]):
                cardChosen = int(input("Which card do you want to play? "))
                main_menu()

                while not canPlay(currentColour, cardVal, [players[playerTurn][cardChosen - 1]]):
                    cardChosen = int(input("Not a valid card. Which card do you want to play? "))
                print("You played {}".format(players[playerTurn][cardChosen - 1]))
                discards.append(players[playerTurn].pop(cardChosen - 1))

                # Check if player won
                if len(players[playerTurn]) == 0:
                    playing = False
                    winner = "Player{}".format(playerTurn + 1)
                else:
                    # Check for special cards
                    splitCard = discards[-1].split(' ', 1)
                    currentColour = splitCard[0]
                    if len(splitCard) == 1:
                        cardVal = "Any"
                    else:
                        cardVal = splitCard[1]

                    if currentColour == "Wild":
                        for x in range(len(colours)):
                            print("{}) {}".format(x + 1, colours[x]))
                        newColour = int(input("What colour would you like to chose? "))
                        while newColour < 1 or newColour > 4:
                            newColour = int(input("Invalid option. What colour would you like to chose? "))
                        currentColour = colours[newColour - 1]
                    if cardVal == "Reverse":
                        playDirection = playDirection * -1
                    elif cardVal == "Skip":
                        playerTurn += playDirection
                        if playerTurn >= numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1
                    elif cardVal == "Draw Two":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(2))
                        playerTurn += playDirection
                        if playerTurn >= numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1
                    elif cardVal == "Draw Four":
                        playerDraw = playerTurn + playDirection
                        if playerDraw == numPlayers:
                            playerDraw = 0
                        elif playerDraw < 0:
                            playerDraw = numPlayers - 1
                        players[playerDraw].extend(drawCards(4))
                        playerTurn += playDirection
                        if playerTurn >= numPlayers:
                            playerTurn = 0
                        elif playerTurn < 0:
                            playerTurn = numPlayers - 1
                    print("")


            else:
                print("You can't play. You have to draw a card.")
                players[playerTurn].extend(drawCards(1))
            print("")

            playerTurn += playDirection
            if playerTurn >= numPlayers:
                playerTurn = 0
            elif playerTurn < 0:
                playerTurn = numPlayers - 1

        print("{} is the winneR!".format(winner))

        player_hands = []
        for winner in players:
            if players[0] == []:
                print("The Winner is: ")
                cprint(P1.name, "red")
                P1.hand.append(players[0])
                player_hands.append(P1.hand)
                break

            elif players[1] == []:
                print("The Winner is: ")
                cprint(P2.name, "red")
                P2.hand.append(players[1])
                player_hands.append(P2.hand)
                break

            elif players[2] == []:
                print("The Winner is: ")
                cprint(P3.name, "red")
                P3.hand.append(players[2])
                player_hands.append(P3.hand)
                break

        else:
            print("The Winner is: ")
            cprint(P4.name, "red")
            P4.hand.append(players[3])
            player_hands.append(P4.hand)

        print("uno_players =", uno_players)
        print('player_hands =')
        cprint(players, 'yellow')



    except ValueError:
        print("Invalid Option: ")
        print("*** Kindly input number ***")

    except IndexError:
        print("Invalid Option: ")
        print("*** Play number within range of cards in player's hand ***")
    # except UnboundLocalError:
    #     pass
    finally:
        print("*** Game Over!")
        print("")


def uno_game():
    welcome()
    options()


def uno_rules2():
    rules = """ UNO RULES
                Skip:
                The next player is "skipped".

                Reverse:
                Reverses the direction of play.

                Draw 2:
                The next player must draw 2 cards and lose a turn.

                Draw 4:
                Changes the current color plus the next player must draw 4 cards and lose a turn.

                Wild Card:
                Play this card to change the colour to be matched.

                Matching Cards:
                During play, matching(cards, colours or numbers) can be played.

                Force Play:
                If you have or draw a playable card, you have to play it for play to continue.

                Play Instructions:
                1. Input only numbers while playing.
                2. For game help, input 'help'

                Help:
                For uno rules and play instructions, type 'help'

        """
    cprint(rules, 'yellow')
    main_menu()
    return rules


def main_menu():
    menu_text = "Type '--help' for Uno rules or '--resume' to continue, or '--quit' to resign. \n"
    menu_text2 = "Enter choice: \n"
    option1 = input(menu_text + menu_text2)
    text = colored(menu_text + menu_text2, 'blue', attrs=['reverse', 'blink'])
    text2 = colored(menu_text2, 'blue', attrs=['reverse', 'blink'])

    cprint(option1, "blue")
    if option1 == 'help':
        uno_rules2()
    elif option1 == 'resume':
        option1
    elif option1 == 'quit':
        exit()
    else:
        main_menu()

    return

uno_game()