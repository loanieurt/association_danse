from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

def load_data():
    with open('database.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/', methods=['GET'])
def index():
    data = load_data()
    return render_template('index.html', evenements=data['Evenements'])

@app.route('/select_event', methods=['POST'])
def select_event():
    data = load_data()
    selected_event = request.form['event_name']
    return render_template('index.html', evenements=data['Evenements'], selected_event=selected_event)

@app.route('/save_presence', methods=['POST'])
def save_presence():
    """Traite le formulaire de présence et met à jour le fichier JSON."""
    event_name = request.form['event_name']
    data = load_data()
    # Trouver l'événement correspondant dans les données
    for event in data['Evenements']:
        if event['nom_evenement'] == event_name:
            # Mettre à jour la présence pour chaque participant listé pour cet événement
            for participant in event['participants']:
                participant_key = f"{participant['prenom']} {participant['nom']}"
                # Cochez si le nom du participant est dans les clés envoyées avec le formulaire
                participant['presence'] = request.form.get(participant_key) == 'on'
    save_data(data)  # Sauvegarde des modifications dans le fichier JSON
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
