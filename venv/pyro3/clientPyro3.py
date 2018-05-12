import Pyro.core
import sys
import cgi
from datetime import datetime


class clientPyro3():
    def __init__(self, urlServ):

        Pyro.core.initClient()
        proxy = Pyro.core.getProxyForURI(urlServ)
        ans = False
        print "1. Loagare"
        print "2. Inregistrare"

        a = raw_input("Ce doriti sa alegeti? ")

        if (a == "1"):
            username = raw_input("Username ")
            password = raw_input("Password ")
            id_user = proxy.login(username,password)
            if id_user!=0:
                ans = True
            else:
                print "Please try again!"
        elif (a == "2"):
            name = raw_input("Name ")
            age = raw_input("Varsta ")
            email = raw_input("Email ")
            phone = raw_input("Telefon ")
            username = raw_input("Username ")
            password = raw_input("Password ")

            proxy.register(name,age,email,phone,username,password)

        while ans:
            print(urlServ)
            print("ping: \t" + proxy.ping())
            print """
            1.Add a Eveniment
            2.List all eveniments
            3.Sterge Eveniment
            4.Actualizeaza Eveniment
            5.Afisare cronologica dupa data
            6.Filtrare dupa locatie
            7.Filtrare dupa data
            8.Filtrare dupa tip
            9.Filtrare dupa proprietati
            
            x.Exit/Quit
            """
            ans = input("Ce optiune alegeti? ")

            if ans == "1":


                name = input("Introduceti denumirea evenimentului ")
                locatie = input("Introduceti locatia ")
                descriere = input("Introduceti descrierea ")
                data = input("Introduceti data format yyyy-mm-dd ")
                d = datetime.strptime(data , '%Y-%m-%d')
                dt = datetime.date(d)
                type = input("Introduceti tipul evenimentului ")
                proxy.addEveniment(name,locatie,descriere,dt,type,id_user)
                print("\nEvent Added!")
            if ans == "2":
                list = proxy.listEveniments(id_user)
                for x in list:
                     print(x)
            if ans == "3":
                ras = input("Afisam lista cu evenimente? ")
                if ras == "da":
                    for x in proxy.listEveniments(id_user):
                        print(x)

                id = input("Introduceti id-ul evenimentului: ")
                proxy.deleteEveniment(id, id_user)
            if ans == "4":
                ras = input("Afisam lista cu evenimente?")
                if ras == "da":
                    for x in proxy.listEveniments(id_user):
                        print(x)

                id = input("Introduceti id-ul:")
                name = input("Introduceti numele")
                locatie = input("Introduceti locatia")
                descriere = input("Introduceti descrierea")
                data = input("Introduceti data format yyyy-mm-dd")

                d = datetime.strptime(data, '%Y-%m-%d')
                dt = datetime.date(d)
                type = input("Introduceti typul")

                proxy.updateEveniment(id,name,locatie,descriere,dt,type,id_user)
                print "Eveniment printed"

            if ans == "5":
                for x in proxy.listaEvensDupaData(id_user):
                     print(x)

            if ans == "6":
                ras = input("Afisam lista cu evenimente? ")
                if ras == "da":
                    for x in proxy.listEveniments(id_user):
                        print(x)

                locatie = input("Introduceti locatie: ")
                for x in proxy.listEvensDupaLoc(locatie,id_user):
                    print(x)

            if ans == "7":
                ras = input("Afisam lista cu evenimente? ")
                if ras == "da":
                    for x in proxy.listEveniments(id_user):
                        print(x)

                data = input("Introduceti data format yyyy-mm-dd ")

                d = datetime.strptime(data, '%Y-%m-%d')
                d2 = datetime.date(d)
                for x in proxy.filtrareByDate(data,id_user):
                    print(x)

            if ans == "8":
                ras = input("Afisam lista cu evenimente?")
                if ras == "da":
                    for x in proxy.listEveniments(id_user):
                        print(x)

                type = input("Introduceti typul: ")

                for x in proxy.filtrareByType(type,id_user):
                    print(x)

            if ans == "9":
                ras = input("Afisam lista cu evenimente?")
                if ras == "da":
                    for x in proxy.listEveniments(id_user):
                        print(x)

                prop = input("Introduceti proprietate: ")

                for x in proxy.filtrareByCaracteristici(prop,id_user):
                    print(x)

            if ans == "x":
                print "\n Goodbye"
                break

            elif ((ans != "1") & (ans !="2") & (ans !="3") & (ans !="4") & (ans !="5") & (ans !="6") & (ans !="7") & (ans !="8") & (ans !="9")):
                print("\n Not Valid Choice Try again!")
                break

if len(sys.argv) > 1:
    clientPyro3(sys.argv[1])
else:
    clientPyro3("PYROLOC://localhost:7766/exec")
