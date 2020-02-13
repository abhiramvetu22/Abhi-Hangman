letter = a
secret = "bloaa"




def test():
    "'tests if letter in secret, if true updates updatedWord displays, updatedWord, calls ifWon, if false displays updatedWord, calls getLetter'"
    global updatedWord
    if letter in secret:
        updatedword.append(letter)
        ifwon()
    else:
        print(updatedWord)
        print("No silly, this letter is not part of the secret word")
        getLetter() 
   
    print updatedWord
    
def testtester():
    fail = 0
    global val
    secret = "bruhbruh"
    updateword = []
    for i in range (0,len(secret) + 1)
        print(updateword[i], end = "")
    Letter = (str(input("what is your guess myguy? "))
    val = secret.find(Letter)
    if val == -1:
        return "wrong letter"
        fail = fail + 1
    else:
        del updateword[vl]
        updateword.insert(val, Letter)
        for i in range (0,len(secret) + 1)
        print(updateword[i], end = "")
        
    
        