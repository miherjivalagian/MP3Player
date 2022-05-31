from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
# creating the root window
root=Tk()
root.title('Mihers Python MP3 Player App')

# mixer init
mixer.init()

#creating the listbox to contain the songs
songsList=Listbox(root, selectmode=SINGLE, bg="black", fg="white", font= ('arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
songsList.grid(columnspan=9)

# font is defined
definedFont = font.Font(family='Helvetica')

#--------------------Buttons-------------------------

#play
playButton=Button(root, text="Play",width=7,command=Play)
playButton['font']=definedFont
playButton.grid(row=1,column=0)

#pause
pauseButton=Button(root, text="Pause",width=7,command=Pause)
pauseButton['font']=definedFont
pauseButton.grid(row=1,column=1)

#stop
stopButton=Button(root,text="Stop",width =7,command=Stop)
stopButton['font']=definedFont
stopButton.grid(row=1,column=2)

#resume
resumeButton=Button(root,text="Resume",width =7,command=Resume)
resumeButton['font']=definedFont
resumeButton.grid(row=1,column=3)

#previous
previousButton=Button(root,text="Prev",width =7,command=Previous)
previousButton['font']=definedFont
previousButton.grid(row=1,column=4)

#next
nextButton=Button(root,text="Next",width =7,command=Next)
nextButton['font']=definedFont
nextButton.grid(row=1,column=5)

#-----------------END OF BUTTONS------------------------------------

#menu design
myMenu=Menu(root)
root.config(menu=myMenu)
addSongMenu=Menu(myMenu)
myMenu.add_cascade(label="Menu", menu=addSongMenu)
addSongMenu.add_command(label="Add songs", command=addSongs)
addSongMenu.add_command(label="Delete song", command=deleteSong)


mainloop()

#add many songs to the playlist of python mp3 player
def addSongs():
    tempSong=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    ##loop through every item in the list to insert in the listbox
for s in tempSong:
        s=s.replace("C:/Users/DataFlair/python-mp3-music-player/","")
songsList.insert(END,s)

def deleteSong():
    currSong=songsList.curselection()
    songsList.delete(currSong[0])

def Play():
    song=songsList.get(ACTIVE)
    song=f'C:/FILL IN HERE '
    mixer.music.load(song)
    mixer.music.play()

#PAUSE
def Pause():
    mixer.music.pause()

#STOP
def Stop():
    mixer.music.stop()
    songsList.selection_clear(ACTIVE)

#RESUME
def Resume():
    mixer.music.unpause()

#Functions to navigate from the current track
def Previous():
    previousOne=songsList.curselection()
    previousOne=previousOne[0]-1
    temp2=songsList.get(previousOne)
    temp2=f'C:/Users/DataFlair/python-mp3-music-player/{temp2}'    
    mixer.music.load(temp2)
    mixer.music.play()
    songsList.selection_clear(0,END)
    songsList.activate(previousOne)
    songsList.selection_set(previousOne)

def Next():
    
    nextOne=songsList.curselection()
    nextOne=nextOne[0]+1
    #to get the next song 
    temp=songsList.get(nextOne)
    temp=f'C:/Users/DataFlair/python-mp3-music-player/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songsList.selection_clear(0,END)
    #activate newsong
    songsList.activate(nextOne)
     #set the next song
    songsList.selection_set(nextOne)