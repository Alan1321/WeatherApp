from weatherInfo import weatherinfo
from tkinter import *
from linkedlist import linkedlist
from arraylist import arraylist
from keyboard import press

arraylist = arraylist('popular_cities.txt')
linkedlist = linkedlist('previous_searches.txt')

root = Tk()
root.title("Weather_App")

mainfont = ('Verdana', 13)
xfont = ('Verdana', 9)

def weather_data(root):
    city = textField.get()
    weather_info = weatherinfo(city)
    linkedlist.delete_insert(city.capitalize())
    info = weather_info.toString()
    label1.config(text=info)


def hit_button(city_name):
    textField.delete(0, END)
    textField.insert(INSERT, str(city_name))
    press('enter')


def btn(p_row, p_col, place):
    b1 = Button(leftFrame, text=place, font=xfont, width=10, command=lambda: hit_button(place))
    b1.grid(row=p_row, column=p_col)


leftFrame = Frame(root)
leftFrame.grid(row=6, column=4)
textField = Entry(leftFrame, justify='left', width=20, font=mainfont)
textField.grid(row=0, column=0, columnspan=1)
textField.focus()
textField.bind('<Return>', weather_data)

label1 = Label(leftFrame, font=mainfont, justify='left')
label1.grid(row=1, column=0, rowspan=7)

#################################################################################

label2 = Label(leftFrame, font=xfont, justify='right', text='Popular Cities')
label2.grid(row=0, column=1, columnspan=3)

array_popular = []
for i in range(6):
    array_popular.append(arraylist.getNext())

btn(1, 1, array_popular[0])
btn(1, 2, array_popular[1])
btn(1, 3, array_popular[2])
btn(2, 1, array_popular[3])
btn(2, 2, array_popular[4])
btn(2, 3, array_popular[5])

###############################################################################

label3 = Label(leftFrame, font=xfont, justify='right', text='Previous Searches')
label3.grid(row=3, column=1, columnspan=3)

array_previous = []
for i in range(6):
    array_previous.append(linkedlist.getNext())

btn(4, 1, array_previous[0])
btn(4, 2, array_previous[1])
btn(4, 3, array_previous[2])
btn(5, 1, array_previous[3])
btn(5, 2, array_previous[4])
btn(5, 3, array_previous[5])

################################################################################
root.mainloop()
