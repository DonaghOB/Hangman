currentAlphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

wordsSet = [ "Bicycle" ]
hintsSet = [ "A mode of transport" ]

name = ""

numGuesses = 6

currentWord = []

alreadyGuessed = []

def getName():
    
    global name
    
    name = input( "Please enter your name: " )

def printRules():
    
    print( "\nOkay,", name, "we have a few rules around here so pay attention!")
    print( "    1. You have", numGuesses, "guesses so think carefully.")
    print( "    2. Remember your previous guesses")
    print( "    3. You can have one hint by typing 'hint'")
    print( "    4. All of your guesses must be a letter - capital or lowercase")
    print( "    5. And finally...... Have Fun!\n")

    print( "Now that the rules are out of the way - here is your hangman:")
    print( "  O\n ---\n/ | \\\n  |\n ----\n /  \\\n |  |")
    print( "\nHis name is Steve - try to save him :)))")

    print( "\nTo start - Steve is free\n" )
    print( "  ______\n  |    |\n       |\n       |\n       |\n       |\n       |\n       |\n       |\n________" )

def guess():
    answer = input("Guess a letter that could be in the word: ")

    if answer == "hint":
        print(hintsSet[0])
    #TODO - Donagh this is for getInput
    return answer

     

def isValidLetter():
    
    #TODO Donagh

    return False

def drawHangman():
    
    print( "This is your current hangman:")
    
    if numGuesses == 6:
        print( "  ______\n  |    |\n       |\n       |\n       |\n       |\n       |\n       |\n       |\n________\n" )
    elif numGuesses == 5:
        print( "  ______\n  |    |\n  O    |\n       |\n       |\n       |\n       |\n       |\n       |\n________\n" )
    elif numGuesses == 4:
        print( "  ______\n  |    |\n  O    |\n ---   |\n  |    |\n  |    |\n ----  |\n       |\n       |\n________\n" )
    elif numGuesses == 3:
        print( "  ______\n  |    |\n  O    |\n ---   |\n/ |    |\n  |    |\n ----  |\n       |\n       |\n________\n" )
    elif numGuesses == 2:
        print( "  ______\n  |    |\n  O    |\n ---   |\n/ | \\  |\n  |    |\n ----  |\n       |\n       |\n________\n" )
    elif numGuesses == 1:
        print( "  ______\n  |    |\n  O    |\n ---   |\n/ | \\  |\n  |    |\n ----  |\n /     |\n |     |\n________\n" )
    elif numGuesses == 0:
        print( "  ______\n  |    |\n  O    |\n ---   |\n/ | \\  |\n  |    |\n ----  |\n /  \\  |\n |  |  |\n________\n" )
    

def keepScore( guess ):
    
    global numGuesses
    
    if guess in alreadyGuessed:
        print( "You already guessed this :(")
        numGuesses -= 1
    else:
        alreadyGuessed.append( guess )
        if guess in currentWord:
            for i in len( currentWord ):
                if currentWord[ i ] is guess:
                    currentWord[ i ] = '-'
        else:
            print( guess, "is not in the word")
            numGuesses -= 1
    

def play(): 
    
    global currentWord 

    finished = False

    print( "Okay your mystery word is: \n" )
    currentWord = wordsSet[ 0 ]
    current = ""

    for i in range( len( currentWord ) ):
        current += "_ "
        
    print( current )

    while not finished:
        keepScore( guess() )

        drawHangman()
        
    
# Starting the Program
def main():
    
    # SETUP
    print( "WELCOME TO HANGMAN!!" )
    print( "--------------------\n" )

    getName()
    guess()
    printRules()
    play()
    

if __name__ == "__main__":
    main()