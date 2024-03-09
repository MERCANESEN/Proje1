import random
NUM_DIGITS= 3
MAX_GUESSES= 10

def main():
    print('''Bagels, tümdengelimli bir mantik oyunu.

Tekrarlanan basamaklari olmayan {} basamakli bir sayi düşünüyorum.
Ne olduğunu tahmin etmeye çalisin. Işte bazi ipuçlari:
Dedigimde: Bu su anlama geliyor:
Pico       Bir hane dogru ancak yanlis konumda.
Fermi      Bir rakam dogru ve dogru konumda.
Bagels     Hicbir rakam dogru degil.

Ornegin gizli numara 248 ve tahmininiz 843 ise,
ipuçlari Fermi Pico olabilir.'''.format(NUM_DIGITS))
    
    while True:
        secretNum=getSecretNum()
        print('Bir sayi düşündüm.')
        print(' Bunu elde etmek için {} tahmininiz var.'.format(MAX_GUESSES))
        
        numGuesses=1
        while numGuesses <= MAX_GUESSES:
            guess=''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print ('Guess {}'.format(numGuesses))
                guess=input('> ')
                
                clues=getClues(guess,secretNum)
                print(clues)
                numGuesses += 1
                
                if guess== secretNum:
                    break
                if numGuesses > MAX_GUESSES:
                    print('Tahminleriniz bitti.')
                    print('Cevap {} idi.'.format(secretNum))
        print('Yeniden oynamak ister misin? (Evet veya hayır)') 
        if not input('> ').lower().startswith('e'):
            break
        print('Oynadiginiz için tesekkurler!')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Devam et!'
    
    clues = []
    
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
            
        elif guess[i] in secretNum:
            clues.append('Pico')
            
    if len(clues) == 0:
        return 'Bagels'
    else:
            clues.sort()
            return ' '.join(clues)

if __name__ == '__main__':
    main()