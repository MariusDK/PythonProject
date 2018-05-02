import Pyro4
import sys
import cgi
from datetime import datetime
from tkinter import *





def inc_i(i):
    i= i+1


class clientPyro4():
    def __init__(self,urlServ):
        i =0
        proxy = Pyro4.Proxy(urlServ)
        root = Tk()
        l1 = Label(root, text="Name")
        l2 = Label(root, text="Locatie")
        l3 = Label(root, text="Descriere")
        l4 = Label(root, text="Data")
        l5 = Label(root, text="Type")
        e1 = Entry(root)
        e2 = Entry(root)
        e3 = Entry(root)
        e4 = Entry(root)
        e5 = Entry(root)

        l1.grid(row=0, sticky=E)
        l2.grid(row=1, sticky=E)
        l3.grid(row=2, sticky=E)
        l4.grid(row=3, sticky=E)
        l5.grid(row=4, sticky=E)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e4.insert(0, "yyyy-mm-dd")
        e5.grid(row=4, column=1)
        if i > 0:
            def add_ev():
                name = e1.get()
                locatie = e2.get()
                descriere = e3.get()
                data = e4.get()
                print(data)
                d = datetime.strptime(data, '%Y-%m-%d')
                type = e5.get()
                proxy.addEveniment(name, locatie, descriere, d, type)
                print("\nEvent Added")
        button_1 = Button(root, text="Save eveniment", command=inc_i(i))
        button_1.grid(row=5)

        root.mainloop()


        # ans = True
        # while ans:
        #     print(urlServ)
        #     print("ping: \t" + proxy.ping())
        #     print("""
        #     1.Add a Eveniment
        #     2.List all eveniments
        #     4.Exit/Quit
        #     """)
        #     ans = input("What would you like to do?")
        #
        #     if ans == "1":
        #
        #
        #         name = getData()
        #         print(name)
        #         locatie = input("Introduceti locatia")
        #         descriere = input("Introduceti descrierea")
        #         data = input("Introduceti data format yyyy-mm-dd")
        #         print(data)
        #         d = datetime.strptime(data , '%Y-%m-%d')
        #         type = input("Introduceti typul")
        #         proxy.addEveniment(name,locatie,descriere,d,type)
        #         print("\nEvent Added")
        #     if ans == "2":
        #         print(ans)
        #         proxy.listEveniments()
        #     if ans == "3":
        #         proxy
        #     if ans == "4":
        #         print("\n Goodbye")
        #         break
        #
        #     elif ans != "":
        #         print("\n Not Valid Choice Try again")
        #         break

    # def add_ev():
    #         name = input("Introduceti numele evenimentului")
    #         locatie = input("Introduceti locatia")
    #         descriere = input("Introduceti descrierea")
    #         data = input("Introduceti data format yyyy-mm-dd")
    #         print(data)
    #         d = datetime.strptime(data, '%Y-%m-%d')
    #         type = input("Introduceti typul")
    #         proxy.addEveniment(name, locatie, descriere, d, type)
    #         print("\nEvent Added")

    def add_ev():
        name = e1.get()
        locatie = e2.get()
        descriere = e3.get()
        data = e4.get()
        print(data)
        d = datetime.strptime(data, '%Y-%m-%d')
        type = e5.get()
        proxy.addEveniment(name, locatie, descriere, d, type)
        print("\nEvent Added")
if len(sys.argv) > 1:
    clientPyro4(sys.argv[1])
else:
    clientPyro4("PYRO:exec@localhost:7543")

