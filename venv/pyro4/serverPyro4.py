import Pyro4
import socket
from database import myDB
from classes import Eveniment

@Pyro4.expose
class serverPyro4(object):
    def ping(self):
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        return "Server "+ name+ " cu adresa "+ip+":7543";
    def addEveniment(self,denumire,locatie,descriere,data,type):
        print(denumire)
        print(data)
        print(locatie)
        print(type)
        print(descriere)
        myDB.insert_ev(denumire,locatie,descriere,data,type)
        print("Succesful operation")
    def listEveniments(self):
        print("Salut")
        myDB.get_all()
daemon = Pyro4.Daemon(port = 7543)
uri = daemon.register(serverPyro4(),"exec")
print("Python ExecPyro4 waiting at: ",uri)
daemon.requestLoop()
