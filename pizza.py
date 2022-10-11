import tkinter
import tkinter.messagebox

class myPizzaGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x400')
        self.main_window.title("Good Pizza")

        #framing widgets
        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        #prompt widgets
        self.WelcomeMessage = tkinter.Label(self.topframe, text = "Welcome to Good Pizza, home of the Good Pizza!")
        self.WelcomeMessage2 = tkinter.Label(self.topframe, text = "Can I take your order?")
        self.StartPrice = tkinter.Label(self.topframe, text = "(Pizzas starting at 5.99!)")
        self.namepromptlabel1 = tkinter.Label(self.topframe, text = "Enter your name:")
        self.nameEntry = tkinter.Entry(self.topframe, width=10)

        #packing widgets
        self.topframe.pack()
        self.WelcomeMessage.pack()
        self.WelcomeMessage2.pack()
        self.StartPrice.pack()
        self.namepromptlabel1.pack()
        self.nameEntry.pack()

        #check boxes for toppings
        self.Toppingsprompt_Space = tkinter.Label(self.topframe, text = "")
        self.Toppingspromptlabel1 = tkinter.Label(self.topframe, text = "Select your toppings:")

        self.cb1_var = tkinter.IntVar()
        self.cb2_var = tkinter.IntVar()
        self.cb3_var = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.topframe,text="Meatballs (+$0.50)",variable=self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.topframe,text="Onions (+$0.50)",variable=self.cb2_var)
        self.cb3 = tkinter.Checkbutton(self.topframe,text="Pineapple (+$0.50)",variable=self.cb3_var)

        #check boxes packing
        self.Toppingsprompt_Space.pack()
        self.Toppingspromptlabel1.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        #radio buttons for crust
        self.radio_var = tkinter.IntVar()

        self.Crustpromptlabel1_Space = tkinter.Label(self.topframe, text = "")
        self.Crustpromptlabel1 = tkinter.Label(self.topframe, text = "Select your crust:")

        self.rb1 = tkinter.Radiobutton(self.topframe,text="Thin Crust ($1.00)",variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.topframe,text="Stuffed Crust ($3.00)",variable=self.radio_var,value=3)
        self.rb3 = tkinter.Radiobutton(self.topframe,text="Flatbread ($2.00)",variable=self.radio_var,value=2)

        self.rb2.select()

        #packing radio buttons
        self.Crustpromptlabel1_Space.pack()
        self.Crustpromptlabel1.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #buttons for price and quit
        self.price_button = tkinter.Button(self.main_window, text="Average", command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text="Quit", command=self.main_window.destroy)

        #packing the buttons
        self.price_button.pack(side="left")
        self.quitbutton.pack(side="right")

        self.topframe.pack()
        self.bottomframe.pack()

        tkinter.mainloop()

    #module to get it to do something
    def do_something(self):
        #tkinter.messagebox.showinfo("Response","Thanks for clicking me!")
        total_cost = 5.99

        #message to show order
        message_order = "\nYour Order: The Good Pizza (+$5.99)"

        #message to show toppings
        message_toppings = "\n\nYour toppings are:\n"

        if self.cb1_var.get() == 1:
            message_toppings += "Meatballs (+$0.50)\n"
            total_cost += 0.50
        if self.cb2_var.get() ==1:
            message_toppings += "Onions (+$0.50)\n"
            total_cost += 0.50
        if self.cb3_var.get() == 1:
            message_toppings += "Pineapple (+$0.50)\n"
            total_cost += 0.50

        #message to show crust
        message_crust = "\nYour crust is:\n"
        if self.radio_var.get() == 1:
            message_crust += "Thin Crust (+$1.00)\n"
        if self.radio_var.get() ==3:
            message_crust += "Stuffed Crust (+$3.00)\n"
        if self.radio_var.get() == 2:
            message_crust += "Flatbread (+$2.00)\n"

        #adding value of crust to total_cost
        total_cost += self.radio_var.get()

        tkinter.messagebox.showinfo("Receipt", "Thanks, " + self.nameEntry.get() + 
        "!" +
        message_order +
        message_toppings + 
        message_crust +'\n'+
        "The total cost of your pizza is: " + "$" + str(total_cost))


my_pizza = myPizzaGUI()

print("I am done!")