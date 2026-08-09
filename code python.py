import sqlite3

class DataBaseManager:

    def __init__(self, db_name):                #intialisation de la classe
        self.db_name = db_name

    def connector(self):                        #methode de connection a sql
        conn = sqlite3.connect(self.db_name)
        return(conn)

    def creer_table(self):                      #methode de creation d'une table
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS utilisateurs(id INTEGER PRIMARY KEY, name TEXT)")
        conn.commit()
        conn.close()

    def inserer_utilisateur(self,id,name):      #methode d'insertion d'utilisateur dans la table
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO utilisateurs(id, name) VALUES(?, ?)", (id, name))
        conn.commit()
        conn.close()

    def supprimer_utilisateur(self, id):        #methode de suppresion utilisateur 
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM utilisateurs WHERE id = ? ", (id,))
        conn.commit()
        conn.close() 

    def modifier_utilisateur(self, id, nouveau_nom):
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("UPDATE utilisateurs SET name = ? WHERE id = ?", (nouveau_nom, id))
        conn.commit()
        conn.close()

    def lire_utilisateur(self):                 #methode de lecture de la table
        conn = self.connector()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilisateurs ")
        resultat = cursor.fetchall()
        conn.close()
        return(resultat)

    def afficher_statut(self):                  #methode d'affichage de status 
        print(f"connexion a {self.db_name} etablie")

db = DataBaseManager("ventes.db")
db.creer_table()    
#db.inserer_utilisateur(1, 'Alice')
#db.inserer_utilisateur(2, 'bob')
#db.supprimer_utilisateur(1,)
db.modifier_utilisateur(1, 'Alice modifier')
utilisateurs = db.lire_utilisateur()

for utilisateur in utilisateurs:                #modification de l'affichage dans la console 
    print(f"ID : {utilisateur[0]} | NOM : {utilisateur[1]}")