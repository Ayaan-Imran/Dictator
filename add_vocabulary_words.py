from tkinter import *

window = Tk()
window.title("Add vocabulary words to 'spelling words.txt'")
window.geometry('650x570')


# All items here
word_1 = Label(window, text="Word 1:", font=("Arial Bold", 30))
word_2 = Label(window, text="Word 2:", font=("Arial Bold", 30))
word_3 = Label(window, text="Word 3:", font=("Arial Bold", 30))
word_4 = Label(window, text="Word 4:", font=("Arial Bold", 30))
word_5 = Label(window, text="Word 5:", font=("Arial Bold", 30))
word_6 = Label(window, text="Word 6:", font=("Arial Bold", 30))
word_7 = Label(window, text="Word 7:", font=("Arial Bold", 30))
word_8 = Label(window, text="Word 8:", font=("Arial Bold", 30))
word_9 = Label(window, text="Word 9:", font=("Arial Bold", 30))
word_10 = Label(window, text="Word 10:", font=("Arial Black", 25))

word_1_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_2_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_3_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_4_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_5_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_6_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_7_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_8_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_9_txt = Entry(window,width=20, font=("Tw cen mt", 30))
word_10_txt = Entry(window,width=20, font=("Tw cen mt", 30))

def clicked():
    word_list = [word_1_txt.get(), word_2_txt.get(), word_3_txt.get(), word_4_txt.get(), word_5_txt.get(), word_6_txt.get(), word_7_txt.get(), word_8_txt.get(), word_9_txt.get(), word_10_txt.get()]
    
    with open("Spelling words.txt", "w")as file:
        word_string = ""
        for word in word_list:
            word_string += word + ","
        word_string = word_string[:-1]
        
        file.write(word_string)

add_to_list_button = Button(window, text="Add to 'Spelling Words'", command=clicked, bg="orange", fg="red", font=("Arial Black", 15), width=50)

# All items grided here
word_1.grid(column=0, row=0)
word_2.grid(column=0, row=1)
word_3.grid(column=0, row=2)
word_4.grid(column=0, row=3)
word_5.grid(column=0, row=4)
word_6.grid(column=0, row=5)
word_7.grid(column=0, row=6)
word_8.grid(column=0, row=7)
word_9.grid(column=0, row=8)
word_10.grid(column=0, row=9)


word_1_txt.grid(column=1, row=0)
word_2_txt.grid(column=1, row=1)
word_3_txt.grid(column=1, row=2)
word_4_txt.grid(column=1, row=3)
word_5_txt.grid(column=1, row=4)
word_6_txt.grid(column=1, row=5)
word_7_txt.grid(column=1, row=6)
word_8_txt.grid(column=1, row=7)
word_9_txt.grid(column=1, row=8)
word_10_txt.grid(column=1, row=9)

add_to_list_button.grid(row = 10, column = 0, columnspan = 2)

window.mainloop()