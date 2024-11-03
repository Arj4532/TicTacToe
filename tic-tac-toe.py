from tkinter import *
from tkinter import messagebox
root= Tk()
root.title("Tic-Tac-Toe")
root.config(bg="navy")
root.geometry("600x600")
root.resizable(0,0)
photo_arj= PhotoImage(file="C:\\Users\\arpit\\OneDrive\\Desktop\\PROJECTS\\TicTacToe\\img\\tac.png")
i1=Label(root,image=photo_arj)
i1.place(x=0, y=0)

PX="X"      #players
P0="0"
tiles_but=[[0, 0, 0],       #for indexing the boxes
            [0, 0, 0],
            [0, 0, 0]]
curplayer=PX
turns = 0
game_over= False
#=========color used: blue - #4584b6, yellow- #ffde57==========#
#====================gray- #343434, light gray- #646464==========#
#============combinations for winning===============#
win_combs =[(0,1,2),(3,4,5),(6,7,8),       
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
#==============for input thhe values in XO rows & columns=============#
def input_XO(row, column):      
    global curplayer
#=======Don't play next turn if win========#    
    if (game_over):
        return
#===========don't overwrite===========#
    if tiles_but[row][column]["text"]!= "" :    
        #Already Filled
        return
    tiles_but[row][column]["text"]= curplayer      #enter
    if curplayer==P0: #switching the player from 0 to X
        curplayer= PX
    else:
        curplayer=P0
    tiles_but[row][column].config(bg="lightblue" if curplayer=="0" else"lightgreen")
    # label["text"]=curplayer+"'s turn"
    label.config(text= curplayer+"'s turn")
    check_winner()
#==============Check the winner==============#
def check_winner():                             #00    01    02
    global turns, game_over                     #10    11    12
    turns +=1                                   #20    21    22
#================Check the winner horizontally, i.e.; 3 rows===================#
    for row in range(3):
        if(tiles_but[row][0]["text"]==tiles_but[row][1]["text"]==tiles_but[row][2]["text"]
        and tiles_but[row][0]["text"]!=""):
            # label["text"]=tiles_but[row][0]["text"]+ " is the winner..!"
            label.config(text=tiles_but[row][0]["text"]+ " is the winner..!", fg= "#ffde57")
            for column in range(3):
                tiles_but[row][column].config(fg="#ffde57", bg="#646464")
            game_over= True
            return
#================Check the winner vertically, i.e.; 3 rows===================#
    for column in range(3):
        if (tiles_but[0][column]["text"]==tiles_but[1][column]["text"]==tiles_but[2][column]["text"]
        and tiles_but[0][column]["text"]!=""):
            label.config(text=tiles_but[0][column]["text"]+ " is the winner..!", fg= "#ffde57")
            for row in range(3):
                tiles_but[row][column].config(fg="#ffde57", bg="#646464")
            game_over= True
            return
#==============check winner diagonally(\)==============#
    if(tiles_but[0][0]["text"]== tiles_but[1][1]["text"]==tiles_but[2][2]["text"]
    and tiles_but[0][0]["text"]!=""):
        label.config(text=tiles_but[0][0]["text"]+ " is the winner..!", fg="#ffde57")
        for i in range(3):
            tiles_but[i][i].config(fg="#ffde57", bg="#646464")    #[i][i] is imp. for the style of winning pos.
        game_over= True
        return
#==============check winner diagonally(/)==============#
    if(tiles_but[0][2]["text"]== tiles_but[1][1]["text"]==tiles_but[2][0]["text"]
    and tiles_but[0][2]["text"]!=""):
        label.config(text=tiles_but[0][2]["text"]+ " is the winner..!", fg="#ffde57")
        tiles_but[0][2].config(fg="#ffde57", bg="#646464")      #can't put [i][i] type comb.
        tiles_but[1][1].config(fg="#ffde57", bg="#646464")      #so, try manually
        tiles_but[2][0].config(fg="#ffde57", bg="#646464")
        game_over= True
        return
#=================match Draw======================#
    if(turns==9):
        game_over= True
        label.config(text="Draw..!", fg="#ffde57")
        messagebox.showwarning('Draw',"Match Draw..!", icon="warning")

#===============Restart the Game================#
def restart():
    global turns, game_over
    turns=0
    game_over= False

    label.config(text= curplayer+"'s turn", fg="white")
    for row in range (3):
        for column in range(3):
            tiles_but[row][column].config(text="", fg= "#4584b6", bg="#343434")

frame=Frame(root)
label=Label(frame, text=curplayer+"'s turn", font="Consolas 20", background="#343434", foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")
frame.pack(padx=20,pady=10)

#=========9 Tiles button creation=============#
for box_row in range(3):
    for box_column in range(3):                 #set text="#" to see the change
        tiles_but[box_row][box_column]=Button(frame, text="", font="consolas 50 bold", bd=4, bg="#343434", fg="#4584b6", width=4, height=1,
                                      command= lambda row=box_row, column=box_column: input_XO(row, column))
        
        tiles_but[box_row][box_column].grid(row=box_row+1, column=box_column)

#==============Button for Restart===============#
restart_button=Button(frame,text="Restart", font="Consolas 20 bold", bd=5, bg="#343434",fg="white", command=restart)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")



root.mainloop()