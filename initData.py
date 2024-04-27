import sqlite3

# Connexion à la base de données (créera une nouvelle base de données si elle n'existe pas)
conn = sqlite3.connect('cartes.db')

# Création du curseur
cursor = conn.cursor()

# Création de la table pour stocker les informations sur les cartes à jouer
cursor.execute(
	'''CREATE TABLE IF NOT EXISTS cartes (id INTEGER PRIMARY KEY,nom TEXT,image_url TEXT,description TEXT,bonus INTEGER,malus INTEGER,question TEXT, reponse TEXT)''')

# Commit et fermeture de la connexion
conn.commit()
conn.close()


def ajouter_carte(nom, image_url, description, bonus, malus, question, reponse):
	conn = sqlite3.connect('cartes.db')
	cursor = conn.cursor()
	cursor.execute(
		'''INSERT INTO cartes (nom, image_url, description, bonus, malus, question, reponse) VALUES (?, ?, ?, ?, ?, ?, ?)''',
		(nom, image_url, description, bonus, malus, question, reponse))
	conn.commit()
	conn.close()


def supprimer_carte(id):
	conn = sqlite3.connect('cartes.db')
	cursor = conn.cursor()
	cursor.execute('DELETE FROM cartes WHERE id = ?', (id,))
	conn.commit()
	conn.close()

def print_all():
	conn = sqlite3.connect('cartes.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM cartes')
	for row in cursor.fetchall():
		print(row)


# Ici j'ajouterais toutes les cartes à mesure que je les crées.
# Pour l'instant, je met des placeholders pour créer le reste de l'application
ajouter_carte("Carte 1 - Tests", "https://lh3.google.com/u/0/d/144fdFbOtVbH7gabZNyiThL3sh3IGQoXl=w2490-h1299-iv2", "Auteur du livre", 10, -10,"Quel est le nom de l'auteur du livre ?", "Edmond Rostand")
ajouter_carte("Carte 2 - Tests", "https://lh3.google.com/u/0/d/144fdFbOtVbH7gabZNyiThL3sh3IGQoXl=w2490-h1299-iv2", "Nom du livre", 1, -100,"Quel est le nom du livre ?", "Cyrano de Bergerac")
ajouter_carte("Carte 3 - Tests", "https://lh3.google.com/u/0/d/144fdFbOtVbH7gabZNyiThL3sh3IGQoXl=w2490-h1299-iv2", "Un physique particulier", 5, -50,"Quel est le physique particulier du personnage principal ?", "Un grand nez")
ajouter_carte("Carte 4 - Tests", "https://lh3.google.com/u/0/d/144fdFbOtVbH7gabZNyiThL3sh3IGQoXl=w2490-h1299-iv2", "Un personnage principal", 5, -50,"Quel est le nom du personnage principal ?", "Cyrano")
ajouter_carte("Carte 5 - Tests", "https://lh3.google.com/u/0/d/144fdFbOtVbH7gabZNyiThL3sh3IGQoXl=w2490-h1299-iv2", "Une fin tragique", 5, -50,"Comment se termine l'histoire ?", "Cyrano meurt")
# ...
# ...

# Pour vérifier que les cartes ont bien été ajoutées
# print_all()
