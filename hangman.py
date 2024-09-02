currentAlphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

wordsSet = [ "Bicycle" ]

# Starting the Program
def main():
    
    # SETUP
    print( "WELCOME TO HANGMAN" )

    numLetters = len( wordsSet[ 0 ] )

    current = ""

    for i in range( numLetters ):
        current += "_ "
        
    print( current )
    

if __name__ == "__main__":
    main()