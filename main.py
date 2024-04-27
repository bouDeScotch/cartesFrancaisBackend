from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()


@app.get("/api/v1/cards")
async def get_cards():
	conn = sqlite3.connect('cartes.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM cartes')
	cards = []
	for row in cursor.fetchall():
		cards.append({
			"id": row[0],
			"nom": row[1],
			"image_url": row[2],
			"description": row[3],
			"bonus": row[4],
			"malus": row[5],
			"question": row[6],
			"reponse": row[7]
		})
	conn.close()
	return {"cards": cards}


@app.get("/api/v1/cards/{identifiant}")
async def get_card(identifiant: int):
	conn = sqlite3.connect('cartes.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM cartes WHERE id = ?', (identifiant,))
	row = cursor.fetchone()
	conn.close()
	if row is None:
		raise HTTPException(status_code=404, detail="Carte non trouvée")
	return {
		"id": row[0],
		"nom": row[1],
		"image_url": row[2],
		"description": row[3],
		"bonus": row[4],
		"malus": row[5],
		"question": row[6],
		"reponse": row[7]
	}
