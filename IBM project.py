from tkinter import *

window = Tk()
window.title("HASHIRA'S RESTAURENT")
window.geometry("700x600")

bg = PhotoImage(file='bg.png')

label17 = Label(window, image=bg)

label17.place(x=0, y=0)

def calculate():

	dic = {'Non-veg Burger': [e1, 129],
		'Non-veg Pizza': [e2, 169],
		'Chicken biriyani': [e3, 180],
		'Chicken Shawarma': [e4, 99],
		'Grill chicken': [e5, 420],
                'Mutton biriyani': [e6, 280],
                'Chicken dum biriyani': [e7, 190],
                'Mushroom rice': [e8, 140],
                'Vegetable pulao': [e9, 120],
                'Paneer biriyani': [e10, 180],
                'Paneer 65': [e11, 160]}
	total = 0
	for key, val in dic.items():
		if val[0].get() != "":
			total += int(val[0].get())*val[1]

	label16 = Label(window,
					text="Your Total Bill is - "+str(total),
					font="times 18")

	
	label16.place(x=20, y=650)
	label16.after(1000, label16.destroy)
	window.after(1000, calculate)


label8 = Label(window,
			text="HASHIRA'S Restaurant",
			font="arial 34 bold")
label8.place(x=600, y=20, anchor="center")


label1 = Label(window,
			text="Menu",
			font="arial 28 bold")

label1.place(x=1000, y=70)

label2 = Label(window, text="Non-veg Burger \
Rs 129", font="arial 18")

label2.place(x=900, y=130)

label3 = Label(window, text="Non-veg Pizza \
Rs 169", font="arial 18")

label3.place(x=900, y=170)

label4 = Label(window, text="Chicken biriyani	 \
Rs 180", font="arial 18")
label4.place(x=900, y=210)

label5 = Label(window, text="Chicken Shawarma \
Rs 99", font="arial 18")

label5.place(x=900, y=250)

label6 = Label(window, text="Grill chicken \
Rs 420", font="arial 18")

label6.place(x=900, y=290)

label7 = Label(window, text="Mutton biriyani  \
Rs 280", font="arial 18")

label7.place(x=900, y=330)

label8 = Label(window, text="Chicken dum biriyani  \
Rs 190", font="arial 18")

label8.place(x=900, y=370)

label9 = Label(window, text="Mushroom rice  \
Rs 140", font="arial 18")

label9.place(x=900, y=410)

labe20 = Label(window, text="Vegetable pulao  \
Rs 120", font="arial 18")

labe20.place(x=900, y=450)

labe21 = Label(window, text="Paneer biriyani  \
Rs 180", font="arial 18")

labe21.place(x=900, y=490)

labe22 = Label(window, text="Paneer 65  \
Rs 160", font="arial 18")

labe22.place(x=900, y=530)


labe23 = Label(window, text="Enter the Quantity",
			font="arial 18")
labe23.place(x=115, y=70)

label10 = Label(window,
				text="Non-veg Burger",
				font="arial 18")
label10.place(x=20, y=120)

e1 = Entry(window)
e1.place(x=20, y=150)

label11 = Label(window, text="Non veg Pizza",
				font="arial 18")
label11.place(x=20, y=200)

e2 = Entry(window)
e2.place(x=20, y=230)

label12 = Label(window, text="Chicken briyani",
				font="arial 18")
label12.place(x=20, y=280)

e3 = Entry(window)
e3.place(x=20, y=310)

label13 = Label(window,
				text="Chicken Shawarma",
				font="arial 18")
label13.place(x=20, y=360)

e4 = Entry(window)
e4.place(x=20, y=390)

label14 = Label(window,
				text="Grill chicken",
				font="arial 18")
label14.place(x=250, y=120)

e5 = Entry(window)
e5.place(x=250, y=150)

label15 = Label(window,
				text="Mutton biriyani",
				font="arial 18")

label15.place(x=250, y=200)

e6 = Entry(window)
e6.place(x=250, y=230)

label16 = Label(window,
				text="Chicken dum biriyani",
				font="arial 18")

label16.place(x=250, y=280)

e7= Entry(window)
e7.place(x=250, y=310)

label17 = Label(window,
				text="Mushroom rice",
				font="arial 18")

label17.place(x=250, y=360)

e8 = Entry(window)
e8.place(x=250, y=390)

label18 = Label(window,
				text="Vegetable pulao",
				font="arial 18")

label18.place(x=250, y=440)

e9 = Entry(window)
e9.place(x=250, y=470)

label19 = Label(window,
				text="Paneer biriyani",
				font="arial 18")

label19.place(x=20, y=440)

e10 = Entry(window)
e10.place(x=20, y=470)

label20 = Label(window,
				text="Paneer 65",
				font="arial 18")

label20.place(x=20, y=520)

e11 = Entry(window)
e11.place(x=20, y=550)


window.after(1000, calculate)


window.mainloop()
