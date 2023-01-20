from tkinter import *
from PIL import Image,ImageTk
from random import randint


#main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

#picture 
rock_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#insert picture
user_label = Label(root,image=scissor_img, bg="#9b59b6")
comp_label = Label(root,image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#score
playerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
compscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
compscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicator
user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#message
message=Label(root,font=50,bg="#9b59b6",fg="white",text="You Loose")
message.grid(row=3,column=2)

#update message
def updatemessage(x):
    message['text'] = x

#update user score
def updateuserscore():
    score=int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)
#update computer score  
def updatecomputerscore():
    score=int(compscore["text"])
    score += 1
    compscore["text"] = str(score)
    
#check winner
def checkwin(player,computer):
    if player == computer:
        updatemessage("Its a tie!!")
    elif player == "rock":
        if computer == "paper":
            updatemessage("You Loose")
            updatecomputerscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updatemessage("You Loose")
            updatecomputerscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updatemessage("You Loose")
            updatecomputerscore()
        else:
            updatemessage("You Win")
            updateuserscore()
    else:
        pass
    
        

#update choice
choice=["rock","paper","scissor"]
def updatechoice(x):
    
#for comp
    compchoice=choice[randint(0,2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    
    #for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "Paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwin(x,compchoice)

#button
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updatechoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updatechoice("Paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updatechoice("scissor")).grid(row=2,column=3)


root.mainloop()