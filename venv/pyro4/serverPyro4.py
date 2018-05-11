import Pyro4
import socket
from database import myDB
from classes import Agenda

@Pyro4.expose
class serverPyro4(object):
    def ping(self):
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        return "Server "+ name+ " cu adresa "+ip+":7543";
    def addEveniment(self,denumire,locatie,descriere,data,type,id_user):

        myDB.insert_ev(denumire,locatie,descriere,data,type, id_user)
        print("Succesful operation")
    def listEveniments(self,id_user):
        #myDB.get_all()
        listS = []
        for x in myDB.get_all(id_user):

            listS.append(str(x))
            #print(str(x))
        return listS
    def deleteEveniment(self,id, id_user):
        if (myDB.get_one(id).get_idUser() == id_user):
            myDB.delete_ev(id)
            print("Succesful operation")
        else:
            print("Nu aveti autorizatie asupra evenimentului")

    def updateEveniment(self,id,denumire,locatie,descriere,data,type,id_user):
        if (myDB.get_one(id).get_idUser() == id_user):
            myDB.update_ev(id,denumire,locatie,descriere,data,type)
            print("Succesful operation")
        else:
            print("Nu aveti autorizatie asupra evenimentului")

    def eveniment(self,id,id_user):
        return str(myDB.get_one(id))

    def listaEvensDupaData(self,id_user):
        #myDB.get_all()
        listD = []
        for x in myDB.get_cronological_list(id_user):
            listD.append(str(x))
            #print(str(x))
        return listD
    def listEvensDupaLoc(self,locatie,id_user):
        listD = []
        for x in myDB.filtrare_locatie(locatie,id_user):
            listD.append(str(x))
            # print(str(x))
        return listD

    def filtrareByDate(self,data,id_user):
        # myDB.get_all()
        listD = []
        for x in myDB.get_all(id_user):

            if (data == x.get_data()):
                listD.append(str(x))
            # print(str(x))
        return listD

    def filtrareByType(self,type,id_user):
        # myDB.get_all()
        listT = []
        for x in myDB.get_all(id_user):
            if (type == x.get_type()):
                listT.append(str(x))
            # print(str(x))
        return listT

    def filtrareByCaracteristici(self,proprietate,id_user):

        listT = []
        for x in myDB.get_all(id_user):
            proprietati = []
            proprietati = x.get_descriere().split(",")
            for p in proprietati:
                if (p == proprietate):
                    listT.append(str(   x))
            # print(str(x))
        return listT
    def login(self,username,password):
        return myDB.login(username,password)

    def register(self, name, age, email, phone, username, password):
        myDB.register(name, age, email, phone, username, password)
daemon = Pyro4.Daemon(port = 7543)
uri = daemon.register(serverPyro4(),"exec")
print("Python ExecPyro4 waiting at: ",uri)
daemon.requestLoop()
