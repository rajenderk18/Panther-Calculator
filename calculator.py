#!/usr/bin/env python
"""
#######################################################
# Panther Calculator
# Author: Rajender Kumar
# VERSION: 0.1

This is the simplest calculator designed using Tkinter for Windows, Linux and OSX.

#######################################################
"""
version = '0.1'
revision = '0'
######################################################

from tkinter import *
from math import sqrt as sqr
from ttkthemes import themed_tk as tk

class Application(Frame):
    """
    An example of a calculator app developed using the
    Tkinter GUI.
    """

    def __init__(self, master):
        """
        Initializes the frame.
        :param master: root.Tk()
        """
        Frame.__init__(self, master)
        self.entry = Entry(master, font=("Arial", 25))
        #self.entry.grid(row=0, column=0, columnspan=6, sticky="w")
        self.entry.place(relx= 0, rely= 0, relheight= 0.1, relwidth = 1)
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets(master)
        self.bind_buttons(master)
        self.grid()

    def add_chr(self, char, btn=None):
        """
        Concatenates a character passed from a button press (or key type)
        to a string.
        :param char: string to add passed from a button
        :param btn: button name to use if key is pressed (to flash)
        :return: None
        """
        self.entry.configure(state="normal")
        self.flash(btn) # Flash a button correspond to keystroke
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def clear(self):
        """
        Allows user to backspace their entry.
        :return: None
        """
        self.entry.configure(state="normal")
        if self.entry.get() != "Invalid Input":
            # Clears full entry when "Invalid Input"
            text = self.entry.get()[:-1]
            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clear_all(self):
        """
        Allows user to clear the full entry.
        :return: None
        """
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def calculate(self):
        """
        Changes the operation symbols to their mathematical representation used in
        the eval() method.
        :return: None
        """
        self.entry.configure(state="normal")
        e = self.entry.get()
        e = e.replace("√","sqr")
        e = e.replace("×", "*")
        e = e.replace("²", "**2")
        e = e.replace("^", "**")
        e = e.replace("÷", "/")

        try:
            ans = eval(e)
        except Exception as ex:
            self.entry.delete(0,END)
            self.entry.insert(0, "Invalid Input")
        else:
            self.entry.delete(0,END)
            if len(str(ans)) > 20: # Alleviates problem of large numbers
                self.entry.insert(0, '{:.10e}'.format(ans))
            else:
                self.entry.insert(0, ans)
        self.entry.configure(state="disabled")

    def flash(self,btn):
        """
        Flashes a corresponding button when key is pressed.
        :param btn: button
        :return: None
        """
        if btn != None:
            btn.config(bg="yellow")
            if btn == self.c_bttn:
                self.clear()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            elif btn == self.eq_bttn:
                self.master.after(100, lambda: btn.config(bg="lightgrey"))
                self.calculate()
            elif btn == self.ac_bttn:
                self.clear_all()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            elif (btn == self.one_bttn or btn == self.two_bttn or btn == self.three_bttn or btn == self.four_bttn or btn == self.five_bttn or btn == self.six_bttn or btn == self.seven_bttn or btn == self.eight_bttn or btn == self.nine_bttn or btn == self.zero_bttn):
                self.master.after(100, lambda: btn.config(bg="White"))
            else:
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
        else:
            pass

    def bind_buttons(self, master):
        """
        Binds keys to their appropriate input
        :param master: root.Tk()
        :return: None
        """
        master.bind("<Return>", lambda event, btn=self.eq_bttn: self.flash(btn))
        master.bind("<BackSpace>", lambda event, btn=self.c_bttn: self.flash(btn))
        master.bind("9", lambda event, char="9", btn=self.nine_bttn: self.add_chr(char, btn))
        master.bind("8", lambda event, char="8", btn=self.eight_bttn: self.add_chr(char, btn))
        master.bind("7", lambda event, char="7", btn=self.seven_bttn: self.add_chr(char, btn))
        master.bind("6", lambda event, char="6", btn=self.six_bttn: self.add_chr(char, btn))
        master.bind("5", lambda event, char="5", btn=self.five_bttn: self.add_chr(char, btn))
        master.bind("4", lambda event, char="4", btn=self.four_bttn: self.add_chr(char, btn))
        master.bind("3", lambda event, char="3", btn=self.three_bttn: self.add_chr(char, btn))
        master.bind("2", lambda event, char="2", btn=self.two_bttn: self.add_chr(char, btn))
        master.bind("1", lambda event, char="1", btn=self.one_bttn: self.add_chr(char, btn))
        master.bind("0", lambda event, char="0", btn=self.zero_bttn: self.add_chr(char, btn))
        master.bind("*", lambda event, char="×", btn=self.mult_bttn: self.add_chr(char, btn))
        master.bind("/", lambda event, char="÷", btn=self.div_bttn: self.add_chr(char, btn))
        master.bind("^", lambda event, char="^", btn=self.sqr_bttn: self.add_chr(char, btn))
        master.bind("%", lambda event, char="%", btn=self.mod_bttn: self.add_chr(char, btn))
        master.bind(".", lambda event, char=".", btn=self.dec_bttn: self.add_chr(char, btn))
        master.bind("-", lambda event, char="-", btn=self.sub_bttn: self.add_chr(char, btn))
        master.bind("+", lambda event, char="+", btn=self.add_bttn: self.add_chr(char, btn))
        master.bind("(", lambda event, char="(", btn=self.lpar_bttn: self.add_chr(char, btn))
        master.bind(")", lambda event, char=")", btn=self.rpar_bttn: self.add_chr(char, btn))
        master.bind("c", lambda event, btn=self.ac_bttn: self.flash(btn), self.clear_all)

    def create_widgets(self, master):
        """
        Creates the widgets to be used in the grid.
        :return: None
        """
        btn_frame = Frame(master, bg="RED")
        btn_frame.place(relx=0, rely=0.1, relheight=0.9, relwidth=1)

        self.mod_bttn = Button(btn_frame, text="%", width=9, height=3, font='Times 30', command=lambda: self.add_chr('%'))
        # self.mod_bttn.grid(row=4, column=2)
        self.mod_bttn.place(relx=0, rely=0, relheight=0.2, relwidth=0.2)

        self.ac_bttn = Button(btn_frame, text='CE', width=9, height=3,  font='Times 30', command=lambda: self.clear_all())
        # self.ac_bttn.grid(row=1, column=4)
        self.ac_bttn.place(relx=0.2, rely=0, relheight=0.2, relwidth=0.2)

        self.lpar_bttn = Button(btn_frame, text="(", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('('))
        # self.lpar_bttn.grid(row=2, column=4)
        self.lpar_bttn.place(relx=0.4, rely=0, relheight=0.2, relwidth=0.2)

        self.rpar_bttn = Button(btn_frame, text=")", width=9, height=3,  font='Times 30', command=lambda: self.add_chr(')'))
        # self.rpar_bttn.grid(row=2, column=5)
        self.rpar_bttn.place(relx=0.6, rely=0, relheight=0.2, relwidth=0.2)

        self.c_bttn = Button(btn_frame, text='←', width=9, height=3, font='Times 30',  command=lambda: self.clear())
        # self.c_bttn.grid(row=1, column=5 )
        self.c_bttn.place(relx=0.8, rely=0, relheight=0.2, relwidth=0.2)

        self.sq_bttn = Button(btn_frame, text="√", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('√('))
        # self.sq_bttn.grid(row=3, column=4)
        self.sq_bttn.place(relx=0, rely=0.2, relheight=0.2, relwidth=0.2)

        self.seven_bttn = Button(btn_frame, text="7", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(7))
        # self.seven_bttn.grid(row=1, column=0)
        self.seven_bttn.place(relx=0.2, rely=0.2, relheight=0.2, relwidth=0.2)

        self.eight_bttn = Button(btn_frame, text="8", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(8))
        # self.eight_bttn.grid(row=1, column=1)
        self.eight_bttn.place(relx=0.4, rely=0.2, relheight=0.2, relwidth=0.2)

        self.nine_bttn = Button(btn_frame, text="9", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(9))
        # self.nine_bttn.grid(row=1, column=2)
        self.nine_bttn.place(relx=0.6, rely=0.2, relheight=0.2, relwidth=0.2)

        self.mult_bttn = Button(btn_frame, text="×", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('×'))
        # self.mult_bttn.grid(row=2, column=3)
        self.mult_bttn.place(relx=0.8, rely=0.2, relheight=0.2, relwidth=0.2)

        self.sqr_bttn = Button(btn_frame, text="^", width=9, height=3, font='Times 30', command=lambda: self.add_chr('^'))
        # self.sqr_bttn.grid(row=3, column=5)
        self.sqr_bttn.place(relx=0, rely=0.4, relheight=0.2, relwidth=0.2)

        self.four_bttn = Button(btn_frame, text="4", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(4))
        # self.four_bttn.grid(row=2, column=0)
        self.four_bttn.place(relx=0.2, rely=0.4, relheight=0.2, relwidth=0.2)

        self.five_bttn = Button(btn_frame, text="5", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(5))
        # self.five_bttn.grid(row=2, column=1)
        self.five_bttn.place(relx=0.4, rely=0.4, relheight=0.2, relwidth=0.2)

        self.six_bttn = Button(btn_frame, text="6", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(6))
        # self.six_bttn.grid(row=2, column=2)
        self.six_bttn.place(relx=0.6, rely=0.4, relheight=0.2, relwidth=0.2)

        self.sub_bttn = Button(btn_frame, text="-", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('-'))
        # self.sub_bttn.grid(row=3, column=3)
        self.sub_bttn.place(relx=0.8, rely=0.4, relheight=0.2, relwidth=0.2)

        self.pai_bttn = Button(btn_frame, text="π", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('3.1415'))
        # self.pai_bttn.grid(row=3, column=3)
        self.pai_bttn.place(relx=0, rely=0.6, relheight=0.2, relwidth=0.2)

        self.one_bttn = Button(btn_frame, text="1", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(1))
        # self.one_bttn.grid(row=3, column=0)
        self.one_bttn.place(relx=0.2, rely=0.6, relheight=0.2, relwidth=0.2)

        self.two_bttn = Button(btn_frame, text="2", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(2))
        # self.two_bttn.grid(row=3, column=1)
        self.two_bttn.place(relx=0.4, rely=0.6, relheight=0.2, relwidth=0.2)

        self.three_bttn = Button(btn_frame, text="3", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(3))
        # self.three_bttn.grid(row=3, column=2)
        self.three_bttn.place(relx=0.6, rely=0.6, relheight=0.2, relwidth=0.2)

        self.add_bttn = Button(btn_frame, text="+", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('+'))
        # self.add_bttn.grid(row=4, column=3)
        self.add_bttn.place(relx=0.8, rely=0.6, relheight=0.2, relwidth=0.2)

        self.floor_bttn = Button(btn_frame, text="//", width=9, height=3, font='Times 30 bold', command=lambda: self.add_chr('//'))
        # self.floor_bttn.grid(row=4, column=3)
        self.floor_bttn.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.2)

        self.dec_bttn = Button(btn_frame, text=".", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('.'))
        # self.dec_bttn.grid(row=4, column=1)
        self.dec_bttn.place(relx=0.2, rely=0.8, relheight=0.2, relwidth=0.2)

        self.zero_bttn = Button(btn_frame, text="0", width=9, height=3, bg= "white", font='Times 30 bold', command=lambda: self.add_chr(0))
        # self.zero_bttn.grid(row=4, column=0)
        self.zero_bttn.place(relx=0.4, rely=0.8, relheight=0.2, relwidth=0.2)

        self.eq_bttn = Button(btn_frame, text="=", width=20, height=3, bg="lightgrey",  font='Times 30', command=lambda: self.calculate())
        # self.eq_bttn.grid(row=4, column=4, columnspan=2)
        self.eq_bttn.place(relx=0.6, rely=0.8, relheight=0.2, relwidth=0.2)

        self.div_bttn = Button(btn_frame, text="÷", width=9, height=3,  font='Times 30', command=lambda: self.add_chr('/'))
        # self.div_bttn.grid(row=1, column=3)
        self.div_bttn.place(relx=0.8, rely=0.8, relheight=0.2, relwidth=0.2)

root = Tk()
root.title('Panther Calculator')
root.iconbitmap('images/panther.ico')
# root = tk.ThemedTk()
# root.get_themes() # Returns a list of all themes that can be set
# print(root.get_themes())
# root.set_theme("black")

root.minsize(1080,750)
# root.resizable(0, 0)
root.geometry()
app = Application(root)
root.mainloop()
