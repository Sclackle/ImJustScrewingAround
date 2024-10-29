#Samuel Clackler
#UWYO COSC 1010
#Submission Date: 10/29/24
#HW 02
#Lab Section 11
#Sources: ChatGPT

morse = {
    'a':'.- ',
    'b':'-... ',
    'c':'-.-. ',
    'd':'-.. ',
    'e':'. ',
    'f':'..-. ',
    'g':'--. ',
    'h':'.... ',
    'i':'.. ',
    'j':'.--- ',
    'k':'-.- ',
    'l':'.-.. ',
    'm':'-- ',
    'n':'-. ',
    'o':'--- ',
    'p':'.--. ',
    'q':'--.- ',
    'r':'.-. ',
    's':'... ',
    't':'- ',
    'u':'..- ',
    'v':'...- ',
    'w':'.-- ',
    'x':'-..- ',
    'y':'-.-- ',
    'z':'--.. ',
    ' ':'  '
    }

usr_inpt = input("write what you would like to be converted to morse code: ").lower()

morse_output = ''.join(morse[char] for char in usr_inpt if char in morse)
 
print(morse_output)