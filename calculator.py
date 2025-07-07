
from tkinter import *

win = Tk()
win.title('Calculator')
win.geometry('400x340')
win.resizable(width=False, height=False)

# ****************************************
resultCalc = StringVar()
#*****************************************
tempString = " "
def add_to_field(input):
    global tempString
    tempString += str(input)
    resultCalc.set(tempString)

# ****************************************
def calculate():
    global tempString
    print(type(eval(tempString)))
    result = str(eval(tempString))
    print(type(result))
    resultCalc.set(result)

# ****************************************
def clear():
    global tempString
    tempString = ""
    resultCalc.set(tempString)

# *****************************************

zeroFrame = Frame(win, width=400, height=85 ,bg='')
zeroFrame.pack(side=TOP)
firstFrame = Frame(win, width=400, height=55, bg='')
firstFrame.pack(side = TOP)
secondFrame = Frame(win, width=400, height=55, bg='')
secondFrame.pack(side = TOP)
thirdFrame = Frame(win, width=400, height=55, bg='')
thirdFrame.pack(side = TOP)
fourthFrame = Frame(win, width=400, height=55, bg='')
fourthFrame.pack(side = TOP)
fifthtFrame = Frame(win, width=400, height=55, bg='')
fifthtFrame.pack(side=TOP)
#zeroFrame
myfont = ('clabri', 18)
entryResult = Entry(zeroFrame, fg='black', bg='darkgray' ,font= myfont ,width= 300,textvariable=resultCalc)
entryResult.pack(side=LEFT, padx= 10 , pady= 6)
# button, firstFrame
btnSeven = Button(firstFrame, text='7', command= lambda : add_to_field('7'),fg='black', bg='white', width= 8, height= 2)
btnSeven.pack(side=LEFT, padx= 10 , pady= 6)
btnEight = Button(firstFrame, text='8', command= lambda : add_to_field('8'),fg='black', bg='white', width= 8, height= 2)
btnEight.pack(side=LEFT, padx= 10 , pady= 6)
btnNine = Button(firstFrame, text='9', command= lambda : add_to_field('9'),fg='black', bg='white', width= 8, height= 2)
btnNine.pack(side=LEFT, padx= 10 , pady= 6)
btnDivide = Button(firstFrame, text='/', command= lambda : add_to_field('/'),fg='black', bg='white', width= 8, height= 2)
btnDivide.pack(side=LEFT, padx= 10 , pady= 6)
# button, secondFrame
btnFourth = Button(secondFrame, text='4', command= lambda : add_to_field('4'),fg='black', bg='white', width= 8, height= 2)
btnFourth.pack(side=LEFT, padx= 10 , pady=6)
btnFive = Button(secondFrame, text='5', command= lambda : add_to_field('5'),fg='black', bg='white', width= 8, height= 2)
btnFive.pack(side=LEFT, padx= 10 , pady=6)
btnSix = Button(secondFrame, text='6', command= lambda : add_to_field('6'),fg='black', bg='white', width= 8, height= 2)
btnSix.pack(side=LEFT, padx= 10 , pady=6)
btnMulty = Button(secondFrame, text='*', command= lambda : add_to_field('*'),fg='black', bg='white', width= 8, height= 2)
btnMulty.pack(side=LEFT, padx= 10 , pady= 6)
# button, thirdFrame
btnOne = Button(thirdFrame,text='1', command= lambda : add_to_field('1'),fg='black', bg='white', width= 8, height= 2)
btnOne.pack(side=LEFT, padx= 10 , pady=6)
btnSecond = Button(thirdFrame, text='2', command= lambda : add_to_field('2'),fg='black', bg='white', width= 8, height= 2)
btnSecond.pack(side=LEFT, padx= 10 , pady=6)
btnThird = Button(thirdFrame, text='3', command= lambda : add_to_field('3'),fg='black', bg='white', width= 8, height= 2)
btnThird.pack(side=LEFT, padx= 10 , pady=6)
btnMinus = Button(thirdFrame, text='-', command= lambda : add_to_field('-'),fg='black', bg='white', width= 8, height= 2)
btnMinus.pack(side=LEFT, padx= 10 , pady=6)
# button, fourthFrame
btnEqual = Button(fourthFrame, text='-/+', command= lambda : add_to_field('00'),fg='black', bg='white', width= 8, height= 2)
btnEqual.pack(side=LEFT, padx= 10 , pady=6)
btnZero = Button(fourthFrame, text='0', command= lambda : add_to_field('0'),fg='black', bg='white', width= 8, height= 2)
btnZero.pack(side=LEFT, padx= 10 , pady=6)
btnPercent = Button(fourthFrame, text='.', command= lambda : add_to_field('.'),fg='black', bg='white', width= 8, height= 2)
btnPercent.pack(side=LEFT, padx= 10 , pady=6)
btnPlus = Button(fourthFrame, text='+', command= lambda : add_to_field('+'),fg='black', bg='white', width= 8, height= 2)
btnPlus.pack(side=LEFT, padx= 10 , pady=6)
#button, fifthFrame
btnEqual = Button(fifthtFrame, text='=', command= lambda : calculate(),fg='black', bg='white', width= 25, height= 2)
btnEqual.pack(side=LEFT, padx= 14 , pady=6)
btnDivide = Button(fifthtFrame, text='CE', command= lambda : clear(),fg='black', bg='white', width= 14, height= 2)
btnDivide.pack(side=LEFT, padx= 12 , pady= 6)


win.mainloop()
