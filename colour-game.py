from tkinter import * #Importing tkinter package
import tkinter.font as font #Importing font and random library
import random as r

#Creating a window
root = Tk()

colors = ["Red", "Orange", "White", "Green", "Blue", "Brown", "Purple", "Yellow", "Pink"]
timer = 30      #Initialising the timer to thirty seconds
score = 0       #Initialising the score to zero
displayedcolour = ''    

#This function will be called when start button is clicked
def start():
    global displayedcolour
    if(timer == 30):
        countdown()     #Calls function countdown to start the countdown
        displayedcolour = r.choice(colors).lower()  #For the interface to pick the colour of text randomly from the list
        display_words.config(text=r.choice(colors), fg=displayedcolour) #Binding the displayed colour along with random colour name to a Label created
        colourentry.bind('<Return>', nextword)  #It calls the nextword function when the enter/return button is pressed

#This function is to reset the game
def reset():
    global timer, score, displayedcolour
    timer = 30 #Initialises the timer
    score = 0 #Initialises the score
    gamescore.config(text = "Score : " + str(score))
    display_words.config(text =displayedcolour) #Rechoicing the colour to be displayed
    time_left.config(text="Time Left: ")
    colourentry.delete(0, END) #deletes the previous entry after the game is reset
    
#This function controls the timer for the game
def countdown():   
    global timer
    if(timer >= 0):
        time_left.config(text = "Time left: " + str(timer) + "s")
        timer -= 1
        time_left.after(1000,countdown)
        if (timer == -1):
            time_left.config(text="---Game Over---")
            colourentry.delete(0, END)
            
#This function checks for the correctness of answer and displays the next word
def nextword(event):
    global displayedcolour
    global score
    if(timer > 0):
        if(displayedcolour == colourentry.get().lower()):
            score += 1
            gamescore.config(text = "Score : " + str(score))
        colourentry.delete(0, END)
        displayedcolour = r.choice(colors).lower()
        display_words.config(text = r.choice(colors), fg = displayedcolour)

#Title of the window
root.title("Color Game")

#Window background 
root['bg'] = 'gray10'

#Creating a game description of the interface
game_desp = "Game Description: Enter the color of the words displayed below. \n Not the word text itself!"
game_description = Label(root, text = game_desp, fg= "cyan2", bg= 'gray10',font = font.Font(family='mv boli', size = 14))
game_description.pack()

#Displaying the score obtained
gamescore = Label(root, text = "Score : " + str(score), font = (font.Font(family = 'bodoni mt',size=28)), fg = "lawn green", bg= 'gray10')
gamescore.pack()

#Displays the words for the game
display_words = Label(root , font = (font.Font(family = 'comic sans ms',size=30)), pady = 15, bg='gray10')
display_words.pack()

#Displaying the time left
time_left = Label(root, text = "Time left: ", font = (font.Font(family = 'bodoni mt',size=24)), fg = "violetred1",bg='gray10')
time_left.pack(pady=15)

#Entry box for entering the answer
colourentry = Entry(root, width = 40)
colourentry.pack(ipady = 7)

#To keep Buttons below in a frame
btn_frame = Frame(root, width= 100, height = 30, bg= 'gold')
btn_frame.pack(side = BOTTOM)

#Start button
start_button = Button(btn_frame, text = "START", width = 10, fg = "gray20", bg = "gold", bd = 2,padx = 30, pady = 10 , command = start,font = (font.Font(family='showcard gothic', size=18)))
start_button.grid(row=0, column= 0)

#Restart button
reset_button = Button(btn_frame, text = "RESET", width = 10, fg = "gray20", bg = "olive drab", bd = 2,padx = 30, pady = 10 , command = reset ,font = (font.Font(family='showcard gothic',size=18)))
reset_button.grid(row=0, column= 1)

#window width and height
root.geometry('700x400')
root.mainloop()
