from tkinter import *
from tkinter import ttk
import random

from quickSort import quick_sort
from bubbleSort import bubble_sort


root = Tk()
root.title("Sorting Algorithm Visualisation by 1301200362 and 1301204238")
root.maxsize(1350, 1000)
root.config(bg='#142F43')
style = ttk.Style(root)
style.theme_use("clam")

#variables
selected_alg = StringVar()
data = []

#function
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['#FF1700' for x in range(len(data))])

def strt_enter(e):
   startBTN.config(background='#BD574E', foreground= "#FFFFFF")

def strt_leave(e):
   startBTN.config(background= 'SystemButtonFace', foreground= 'black')

def dat_enter(e):
   datBTN.config(background='#3E8E7E', foreground= "#FFFFFF")

def dat_leave(e):
   datBTN.config(background= 'SystemButtonFace', foreground= 'black')

def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    drawData(data, ['#34BE82' for x in range(len(data))])

def close_win(x):
   root.destroy()

#frame / base lauout
##Display name frame
UI_Name = Frame(root, width= 590, height=50, bg='#C3B091')
UI_Name.grid(row=0, column=0, padx=10, pady=5)

##Display main frame
UI_frame = Frame(root, width= 600, height=200, bg='#C3B091')
UI_frame.grid(row=1, column=0, padx=10, pady=5)

##Display main canvas
canvas = Canvas(root, width=620, height=435, bg='#F5F5F5')
canvas.grid(row=2, column=0, padx=10, pady=5)

#User Interface Area
##Row[0]
###Display information name
name1 = Label(UI_Name, text="Sorting Algorithms Visualization", font=('Consolas', 16, 'bold'), bg='#C3B091')
name1.grid(row=0, column=0, padx=101, pady=15, sticky=N)

'''
by = Label(UI_Name, text="by", font=('Times New Roman', 12), bg='#C3B091')
name1.grid(row=2, column=1, padx=101, pady=5, sticky=S)
'''

##Row[1]
### Display Algorithm type option
Label(UI_frame, text="Algorithm Type: ", bg='#C3B091').grid(row=1, column=0, padx=30, pady=35, sticky=SW)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Quick Sort', 'Bubble Sort'])
algMenu.grid(row=1, column=1, padx=5, pady=5)
algMenu.current(0)

### Display Speed of Sorting Algorithm 
speedScale = Scale(UI_frame, from_=5.0, to=0.1, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed (Slow - Speed)")
speedScale.grid(row=1, column=2, padx=5, pady=5)

### Display Start button to start the process of Sorting Algorithm
startBTN = Button(UI_frame, text="Start", command=StartAlgorithm, bg='#F0ECE3')
startBTN.grid(row=1, column=3, padx=5, pady=5)

startBTN.bind('<Enter>', strt_enter)
startBTN.bind('<Leave>', strt_leave)

##Row[2]
### Display Data size slider
sizeEntry = Scale(UI_frame, from_=3, to=100, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=2, column=0, padx=5, pady=5)

### Display Minimum value slider
minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=2, column=1, padx=5, pady=5)

### Display Maximum slider
maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=2, column=2, padx=5, pady=5)

## Display New data button
### To generate new data randomly
datBTN = Button(UI_frame, text="New Data", command=Generate, bg='#FFFFFF')
datBTN.grid(row=2, column=3, padx=5, pady=5)

datBTN.bind('<Enter>', dat_enter)
datBTN.bind('<Leave>', dat_leave)

##Row[3]
## Display String "Press esc to close"
msg = Label(root , bg='#142F43', fg='#FFFFFF', font="Helvetica 14", text = "Press escape to close")
msg.grid(row=3, column=0, padx=10, pady=10, sticky=S)

# Bind the ESC key with the callback function
root.bind('<Escape>', lambda x: close_win(x))

root.mainloop()