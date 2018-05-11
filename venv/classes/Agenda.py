class Eveniment(object):

    def __init__(self, denumire, descriere, locatie, data, type, id, idUser):
        self.denumire = denumire
        self.descriere = descriere
        self.locatie = locatie
        self.data = data
        self.type = type
        self.id = id
        self.idUser = idUser

    def get_denumire(self):
        return self.denumire
    def get_descriere(self):
        return self.descriere
    def get_data(self):
        return self.data
    def set_denumire(self, denumire):
        self.denumire = denumire
    def set_descriere(self, descriere):
        self.descriere = descriere
    def set_data(self,data):
        self.data = data
    def get_locatie(self):
        return self.locatie
    def set_locatie(self,locatie):
        self.locatie = locatie
    def set_type(self,type):
        self.type = type
    def get_type(self):
        return self.type
    def get_id(self):
        return self.id;
    def get_idUser(self):
        return self.idUser;
    def set_idUser(self,idUser):
        self.idUser = idUser
    def __str__(self):
        return str(self.get_id()) + " " + self.get_denumire()+" "+self.get_descriere()+" "+\
               self.get_data()+" "+self.get_locatie()+ " " +self.get_type()