from tkinter import *
from random import random, randint

colorUp = []
EndOfGame = 0
tries = 0
count = 0
NumberOfButton2 = 1
NumberOfButton1 = 1

def game():

    #Активация кнопки
    def FaceUp(number):
        find = 0
        if count == 0:
            global NumberOfButton1
            NumberOfButton1 = number
        elif count == 1:
            global NumberOfButton2
            NumberOfButton2 = number
        for i in range (0, 1):
            bg = buttons[number]["activebackground"]
            buttons[number].configure(bg = bg)
            for i in colorUp:
                if i == bg:
                    find+= 1
                    break
            if NumberOfButton1 == NumberOfButton2:
                find += 1
        if find == 0:
            CheckAnotherBTN(buttons[number], number)

    #Раздача цветов (не живых)
    def FaceDown():
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for i in range(0, 16, 2):
            bg = color[randint(0, len(color) - 1)]
            BtnNum1 = nums[randint(0, len(nums) - 1)]
            buttons[BtnNum1].configure(activebackground = bg)
            nums.remove(BtnNum1)
            BtnNum2 = nums[randint(0, len(nums) - 1)]
            buttons[BtnNum2].configure(activebackground = bg)
            color.remove(bg)
            nums.remove(BtnNum2)

    #Проверка на совместимость
    def CheckAnotherBTN(button, num):
        global count
        if count == 0:
            global ColorOfBtn1
            ColorOfBtn1 = button["activebackground"]
            global NumberOfButton1
            NumberOfButton1 = num
            buttons[NumberOfButton1].configure(state = "disabled")
            count += 1
        elif count == 1:
            global ColorOfBtn2
            ColorOfBtn2 = button["activebackground"]
            global NumberOfButton2
            NumberOfButton2 = num
            count = 0
            if ColorOfBtn1 == ColorOfBtn2:
                global EndOfGame
                EndOfGame += 1
                colorUp.append(button["activebackground"])
                buttons[NumberOfButton2].configure(state ="disabled")
                if EndOfGame == 8:
                    frame.pack_forget()
                    for i in range (16):
                        buttons[i].pack_forget()
                    Newframe = Frame(root,
                                  width=3,
                                  height=5,
                                  bg="white",
                                  bd=180)
                    label = Label(Newframe,
                                  text="You Win!",
                                  compound="center",
                                  width = 20,
                                  height = 10,
                                  bg = "white",
                                  font = "Arial",
                                  padx = 15)
                    Newframe.pack()
                    label.pack()
            else:
                buttons[NumberOfButton1].configure(state = "normal")
                buttons[NumberOfButton1].configure(bg="lightgreen")
                buttons[NumberOfButton2].configure(bg="lightgreen")
                global tries
                tries += 1


    frame = Frame(root,
                  width=2000,
                  height=650,
                  bg="white",
                  bd=30)

    # Создание кнопок
    buttons = []
    for i in range(16):
        Btn = Button(frame,
                     width=12,
                     height=6,
                     bg="lightgreen",
                     bd=1)
        buttons.append(Btn)

    ColorOfBtn1 = buttons[0]
    ColorOfBtn2 = buttons[0]


    """frame.grid(row=1, column=0)
    """
    frame.pack()
    a = 1
    j = 1
    # Вывод кнопок
    for i in buttons:
        i.grid(row=a, column=j)
        if j == 4:
            a += 1
            j = 1
        else:
            j += 1

    color = ['red', 'yellow', 'green', 'blue', 'black', 'orange', 'white', 'brown']
    FaceDown()


    buttons[0].bind("<Button-1>", lambda event: FaceUp(0))
    buttons[1].bind("<Button-1>", lambda event:FaceUp(1))
    buttons[2].bind("<Button-1>", lambda event:FaceUp(2))
    buttons[3].bind("<Button-1>", lambda event:FaceUp(3))
    buttons[4].bind("<Button-1>", lambda event:FaceUp(4))
    buttons[5].bind("<Button-1>", lambda event:FaceUp(5))
    buttons[6].bind("<Button-1>", lambda event:FaceUp(6))
    buttons[7].bind("<Button-1>", lambda event:FaceUp(7))
    buttons[8].bind("<Button-1>", lambda event:FaceUp(8))
    buttons[9].bind("<Button-1>", lambda event:FaceUp(9))
    buttons[10].bind("<Button-1>", lambda event:FaceUp(10))
    buttons[11].bind("<Button-1>", lambda event:FaceUp(11))
    buttons[12].bind("<Button-1>", lambda event:FaceUp(12))
    buttons[13].bind("<Button-1>", lambda event:FaceUp(13))
    buttons[14].bind("<Button-1>", lambda event:FaceUp(14))
    buttons[15].bind("<Button-1>", lambda event:FaceUp(15))


#Стартовая кнопка
def start():
    def clearAndGo(some):
        Btn.pack_forget()
        frame.pack_forget()


    frame = Frame(root,
                  width=3,
                  height=5,
                  bg="white",
                  bd=140)
    Btn = Button(frame,
                 width = 30,
                 height = 10,
                 bd = 2,
                 bg = "yellow",
                 activebackground = "black",
                 text = "Press Start button")
    frame.pack()
    Btn.pack()
    res = Btn.bind("<Button-1>", clearAndGo)
    return 1

#Расположение экрана по центру
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

if __name__ == '__main__':
    root = Tk()
    root.title("Find and Match")
    root.geometry("428x455")
    root.resizable(width=False, height=False)
    center(root)

res = start()
if res == 1:
    res1 = game()

root.mainloop()
