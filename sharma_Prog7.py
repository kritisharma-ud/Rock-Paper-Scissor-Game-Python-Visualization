# Name: Kriti Sharma 
# Date of Creation: 12/04/2022, 12:30 P.M.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Description: Language : Python
#             The below program is to make the rock, paper scissor game using python GUI.
#             The program asks the user's name and start the game. The user get chance to make a choice and computer
#             choose randomly. The winner pops up on the screen and ask user to play more or not. The screen is updated
#             as per user's choice. If user selects no the program exits.
#             Program Requirements- Python 3.10
#             OS used - MacOs
#             Pip3 install pillow
#             Brew install python-tk
# --------------------------------------------------------------------------------------------------------------------------------------

# importing libraries/ modules
import random
import tkinter
from tkinter import *
from tkinter import Canvas, NW, Button
from PIL import Image
from PIL import ImageTk as itk

game = tkinter.Tk()
game.title("Rock, Paper, Scissors")  # title
game.geometry("1000x1000")  # size
game.resizable(True, True)
label = Label(game, text="", font=("Courier 22 bold"))  # creating label
label.pack()

# Intializing the variables
comp = 0
player = 0


# function to display and get username
def display_text():
    string = entry.get()
    label.configure(text=string)
    mycanvas.forget()


# function to state the rules of the game
def rock(a):
    comp = random.choice(["rock", "paper", "scissor"])
    show_image(comp)
    if comp == a:
        show_result("It's a tie!!")  # calling the result function
    elif comp == "paper":
        show_result(" Computer wins!!")
    elif comp == "scissor":
        show_result(entry.get() + " wins!!")


def scissor(b):
    comp = random.choice(["rock", "paper", "scissor"])
    show_image(comp)
    if comp == b:
        show_result("It's a tie!!")
    elif comp == "paper":
        show_result(entry.get() + " wins!!")
    elif comp == "rock":
        show_result("Computer wins!!")


def paper(c):
    comp = random.choice(["rock", "paper", "scissor"])
    show_image(comp)
    if comp == c:
        show_result("It's a tie !!")
    elif comp == "rock":
        show_result(entry.get() + " wins!!")
    elif comp == "scissor":
        show_result("Computer wins!!")


# function to show the computer choice
def show_image(comp):
    gamecanvas.create_text(200, 450, text="Computer Chose: ", fill="black", font='Helvetica 15 bold',
                           tag='comp_chose')
    gamecanvas.pack()
    if comp == "rock":
        gamecanvas.create_image(350, 400, anchor=NW, image=player_rock, tag="rock_image")
    elif comp == "scissor":
        gamecanvas.create_image(350, 400, anchor=NW, image=player_scissor, tag="scissor_image")
    elif comp == "paper":
        gamecanvas.create_image(350, 400, anchor=NW, image=player_paper, tag="paper_image")


# to show the result of the game
def show_result(e):
    # disabling images, buttons and text to start the game again
    gamecanvas.delete("some_tag")
    gamecanvas.delete('play_more_tag')
    gamecanvas.delete("startagain")
    # creating the text to show result
    gamecanvas.create_text(800, 500, text=e, fill="red", font=('Bebas', 25), tag="some_tag")
    gamecanvas.create_text(720, 600, text="Play more?", fill="Blue", font=('Helvetica 15 bold'), tag="playmoretext")

    # creating play more button to choose yes or no
    playmorebutton_yes = Radiobutton(game, text="Yes", border=2, command=play_more)
    playmorebutton_yes.place(x=800, y=600)  # setting the coordinates
    gamecanvas.create_window(800, 600, window=playmorebutton_yes, tag='play_more_tag')

    playmorebutton_no = Radiobutton(game, text="No", border=2, command=exit)
    playmorebutton_no.place(x=870, y=600)  # setting the coordinates
    gamecanvas.create_window(870, 600, window=playmorebutton_no, tag='play_more_tag')
    # disabling the buttons
    rock_button["state"] = "disabled"
    scissor_button["state"] = "disabled"
    paper_button["state"] = "disabled"

    gamecanvas.pack()


def play_more():  # function initiated to play more
    gamecanvas.delete("rock_image")
    gamecanvas.delete("scissor_image")
    gamecanvas.delete("paper_image")
    gamecanvas.delete("some_tag")
    gamecanvas.delete("play_more_tag")
    gamecanvas.delete("playmoretext")
    gamecanvas.delete("comp_chose")
    gamecanvas.create_text(800, 600, text="Start again!! Choose any one!", fill="green", font=('Helvetica 25 bold'),
                           tag="startagain")  # text to start again
    # activating the buttons again
    rock_button["state"] = 'active'
    scissor_button["state"] = 'active'
    paper_button["state"] = 'active'
    gamecanvas.pack()
    return True


while True:
    # creating the main canvas
    mycanvas = Canvas(game, width=1000, height=1000, bg="light blue")
    mycanvas.pack()
    # creating the game screen canvas
    gamecanvas = Canvas(game, width=1000, height=1000, bg="light blue")
    gamecanvas.pack()
    mycanvas.create_text(450, 60, text="Lets Play!! Rock, Paper, Scissors", fill="black", font=('Helvetica 35 bold'))
    mycanvas.pack()
    mycanvas.create_text(400, 200, text="What do you want to be called in this game:", fill="black",
                         font=('Helvetica 20 bold'))
    mycanvas.pack()
    # TextBox Creation
    entry = Entry(mycanvas)
    entry.pack()
    mycanvas.create_window(720, 200, window=entry)
    # start button
    user_input = Button(game, text="Start", width=30, command=display_text)
    user_input.place(x=470, y=280)
    mycanvas.create_window(470, 280, window=user_input)
    mycanvas.pack()

    gamecanvas.create_text(480, 50, text="CHOOSE ANY ONE!", fill="black", font=('Helvetica 20 bold'))
    gamecanvas.pack()

    # setting up images on the canvas
    player_rock = itk.PhotoImage(Image.open(r"rock.jpg"))
    player_scissor = itk.PhotoImage(Image.open(r"scissor.jpg"))
    player_paper = itk.PhotoImage(Image.open(r"paper.jpg"))

    # creating radio buttons for choice of the user
    rock_button = Radiobutton(game, text="Rock", border=2, command=lambda: rock("rock"))
    rock_button.place(x=120, y=350)
    gamecanvas.create_window(120, 350, window=rock_button)
    scissor_button = Radiobutton(game, text="Scissor", border=2, command=lambda: scissor("scissor"))
    scissor_button.place(x=440, y=350)
    gamecanvas.create_window(450, 350, window=scissor_button)
    paper_button = Radiobutton(game, text="Paper", border=2, command=lambda: paper("paper"))
    paper_button.place(x=750, y=350)
    gamecanvas.create_window(750, 350, window=paper_button)

    # setting up the images position
    p_rock = gamecanvas.create_image(30, 70, anchor=NW, image=player_rock)
    p_scissor = gamecanvas.create_image(350, 70, anchor=NW, image=player_scissor)
    p_paper = gamecanvas.create_image(650, 70, anchor=NW, image=player_paper)
    game.mainloop()
    playmoregame = play_more()  # calling play more function
    if not playmoregame:  # check the users choice
        break
    else:
        continue
