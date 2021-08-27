from tkinter import *
import math
from pygame import mixer
import speech_recognition

mixer.init()


def click(value):
    v = entryField.get()  # i.e store pressed number eg:123
    answer = ''

    try:

        if value == 'C':
            v = v[0:len(v)-1]           # slice last number
            entryField.delete(0, END)    # clear screen
            entryField.insert(0, v)      # return rest eg:12
            return

        elif value == 'CE':
            entryField.delete(0, END)
            return

        elif value == '√':
            answer = math.sqrt(eval(v))  # eval is used to evaluate string value and convert inti int,float as req.

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(v)))    # evaluate v then convert into angle using radian()

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(v)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(v)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(v))

        elif value == 'tanh':
            answer = math.tanh(eval(v))

        elif value == 'sinh':
            answer = math.sinh(eval(v))

        elif value == chr(8731):                    # cube root
            answer = eval(v) ** (1 / 3)

        elif value == 'x\u02b8':                    # 7**2 x power y
            entryField.insert(END, '**')            # insert ** at the end
            return

        elif value == 'x\u00B3':                    # cube
            answer = eval(v) ** 3

        elif value == 'x\u00B2':                    # square
            answer = eval(v) ** 2

        elif value == 'ln':                         # log to the base e
            answer = math.log2(eval(v))

        elif value == 'deg':                        # covert no. to degree
            answer = math.degrees(eval(v))

        elif value == "rad":                        # convert no. to angle
            answer = math.radians(eval(v))

        elif value == 'e':                          # get value of exponent
            answer = math.e

        elif value == 'log₁₀':                      # log to base 10
            answer = math.log10(eval(v))

        elif value == 'x!':                         # factorial
            answer = math.factorial(v)

        elif value == chr(247):                    # Division 7/2=3.5
            entryField.insert(END, "/")            # insert ** at the end
            return                                 # using so as control should not go to entryField.delete(0, END)

        elif value == '=':
            answer = eval(v)                       # evaluate value and return answer

        else:
            entryField.insert(END, value)         # when need to click 2 values then at the end insert 2nd pressed value
            return                                # using so as control should not go to entryField.delete(0, END)

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def mod(a, b):
    return a % b


def lcm(a, b):
    lc = math.lcm(a, b)
    return lc


def gcd(a, b):
    h = math.gcd(a, b)
    return h


# Creating voice operation dictionary
operation = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
             'SUBTRACTION': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
             'PRODUCT': mul, 'MULTIPLICATION': mul, 'MULTIPLY': mul,
             'DIVISION': div, 'DIV': div, 'DIVIDE': div,
             'LCM': lcm, 'HCF': gcd,
             'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod}


def findnumbers(t):
    l = []
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l


def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()    # to recognize speech using object sr
    with speech_recognition.Microphone()as microphn:            # created obj for microphone as micrphn
        try:
            sr.adjust_for_ambient_noise(microphn, duration=0.2)  # i.e if 0.2s silence b/w 2sentence treat as next line
            voice = sr.listen(microphn)          # listen to voice via microphone obj and store in var
            voitext = sr.recognize_google(voice)  # decode voice to text and store in var to print in EntryField
            mixer.music.load('music2.mp3')
            mixer.music.play()
            # split text received into list and pull usefull item using some function eg add(),sub()
            text_list = voitext.split('')
            for word in text_list:
                if word.upper() in operation.keys():
                    l = findnumbers(text_list)      # fn. to find no. from speech
                    result = operation[word.upper()](l[0], l[1])  # pass find no. to operation function
                    entryField.delete(0, END)
                    entryField.insert(END, result)
                else:                               # counter moves here if spoken word outside dictionary
                    pass
        except:
            pass


root = Tk()                            # setting window for calci

root.title('Scientific Calculator')   # providing title to window
root.config(bg='dodgerblue3')         # setting windows bg color
root.geometry('680x486+100+100')      # setting window size in pixels and location of window to load on screen

            # Calci Logo:
logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

            # Input Field:
entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief='sunken', width=30)
entryField.grid(row=0, column=0, columnspan=8)  # set entryfield at 0,0 of window loc

            # Mic Btn:
micImage = PhotoImage(file='microphone.png')
micBtn = Button(root, image=micImage, bg='dodgerblue3', bd=0, command=audio())
micBtn.grid(row=0, column=7, columnspan=10)

        # create btn list
button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]

rowvalue = 1
colvalue = 0

for i in button_text_list:
    button = Button(root, width=5, height=2, bd=2, relief='sunken', text=i, bg='dodgerblue3', fg='white', font=('arial',
                    18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))  # cmd= lambda
                    # used to write one line fn.here assign pressed btn value to btn var & pass that var to fn. click.
    button.grid(row=rowvalue, column=colvalue, pady=1)
    colvalue += 1
    if colvalue > 7:
        rowvalue += 1
        colvalue = 0


root.mainloop()              # to make window stable
