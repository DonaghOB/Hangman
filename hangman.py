import time


currentAlphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

wordsSet = [ "BICYCLE" ]
hintsSet = [ "A mode of transport" ]
WordNumber = 0

name = ""

numGuesses = 6

currentWord = []

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

    time.sleep( 2 )
    
    print( "Now that the rules are out of the way - here is your hangman:")
    print( "  O\n ---\n/ | \\\n  |\n ----\n /  \\\n |  |")
    print( "\nHis name is Steve - try to save him :)))")

    time.sleep( 2 )

    print( "\nTo start - Steve is free\n" )
    print( "  ______\n  |    |\n       |\n       |\n       |\n       |\n       |\n       |\n       |\n________" )

def guess():
    answer = input("\nGuess a letter that could be in the word: ")

    if answer == "hint":
        print( hintsSet[0] )
    elif isValidLetter( answer ):
        return answer
    else: 
        print( "Please guess again" )

     
def isValidLetter( answer ):
    if str.isupper( answer ) and len( answer ) == 1:
        return True   
        
    print("WRONG INPUT!")

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
    
    if guess not in currentAlphabet:
        print( "You already guessed this :(")
        numGuesses -= 1
    else:
        currentAlphabet.remove( guess )
        if guess in currentWord:
            current = ""

            for i in range( len( currentWord ) ):
                if currentWord[ i ] == "_":
                    current = wordsSet[ 0 ][ i ] 
                else:
                    current += "_ "
        
                print( current )
        else:
            print( guess, "is not in the word" )
            numGuesses -= 1
    

def play(): 
    
    global currentWord 

    finished = False

    print( "Okay your mystery word is: \n" )
    currentWord = list( wordsSet[ 0 ] )
    current = ""

    for i in range( len( currentWord ) ):
        if currentWord[ i ] == "_":
            current = wordsSet[ 0 ][ i ] 
            print( wordsSet[ 0 ] )
        else:
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
    printRules()
    #guess()
    
    play()
    

if __name__ == "__main__":
    main()