import sqlite3

class DataBaseManager:
    def __init__(self, db_name="ventes.db"):
        self.db_name = db_name

    def connector(self):
        return sqlite3.connect(self.db_name)

    def afficher_statut(self):
        print(f"Connexion à {self.db_name} établie.")

    def creer_table(self):
        try:
            with self.connector() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS utilisateurs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nom TEXT NOT NULL
                    )
                """)
                print("Table 'utilisateurs' prête.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la création de la table : {e}")

    def inserer_utilisateur(self, nom):
        try:
            with self.connector() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO utilisateurs (nom) VALUES (?)", (nom,))
                print(f"Utilisateur '{nom}' ajouté avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'insertion : {e}")

    def chercher_utilisateur(self, id_user):
        try:
            with self.connector() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE id = ?", (id_user,))
                return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Erreur lors de la recherche : {e}")
            return None

    def lire_utilisateurs(self):
        try:
            with self.connector() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM utilisateurs")
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erreur lors de la lecture : {e}")
            return []

    def modifier_utilisateur(self, id_user, nouveau_nom):
        try:
            with self.connector() as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE utilisateurs SET nom = ? WHERE id = ?", (nouveau_nom, id_user))
                print(f"Utilisateur {id_user} modifié avec succès.")
        except sqlite3.Error as e:
            print(f"Erreur lors de la modification : {e}")

    def supprimer_utilisateur(self, id_user):
        try:
            with self.connector() as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM utilisateurs WHERE id = ?", (id_user,))
                print(f"Utilisateur {id_user} supprimé !")
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression : {e}")


# --- TEST DES FONCTIONNALITÉS ---
if __name__ == "__main__":
    db = DataBaseManager("ventes.db")
    db.afficher_statut()
    db.creer_table()

    # Insertion d'utilisateurs (l'ID est généré automatiquement)
    db.inserer_utilisateur("John")
    db.inserer_utilisateur("Alice")

    # Lecture de tous les utilisateurs
    print("\n--- Liste des utilisateurs ---")
    utilisateurs = db.lire_utilisateurs()
    for utilisateur in utilisateurs:
        print(f"ID : {utilisateur[0]} | NOM : {utilisateur[1]}")

    # Recherche d'un utilisateur
    print("\n--- Recherche de l'utilisateur ID 1 ---")
    u1 = db.chercher_utilisateur(1)
    if u1:
        print(f"Trouvé -> ID : {u1[0]} | NOM : {u1[1]}")

    # Modification
    db.modifier_utilisateur(1, "John Modifier")

    # Suppression
    db.supprimer_utilisateur(2)