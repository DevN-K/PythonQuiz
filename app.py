from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

QUIZ_DATA = [
    {
        "id": 1,
        "frage": "Welche Programmiersprache ist Python?",
        "optionen": ["Interpretiert", "Kompiliert", "Hybrid", "Maschinencode"],
        "korrekt": 0
    },
    {
        "id": 2,
        "frage": "Was gibt print(5 ** 2) aus?",
        "optionen": ["25", "10", "7", "52"],
        "korrekt": 0
    },
    {
        "id": 3,
        "frage": "Welche Datenstruktur ist geordnet und änderbar?",
        "optionen": ["Tupel", "Liste", "String", "Set"],
        "korrekt": 1
    },
    {
        "id": 4,
        "frage": "Was ist der Output von len([1, 2, 3])?",
        "optionen": ["1", "3", "2", "0"],
        "korrekt": 1
    },
    {
        "id": 5,
        "frage": "Mit welchem Schlüsselwort definierst du eine Funktion?",
        "optionen": ["function", "def", "define", "func"],
        "korrekt": 1
    }
]

@app.route('/')
def index():
    return render_template('quiz.html')

@app.route('/api/quiz-data')
def get_quiz_data():
    return jsonify(QUIZ_DATA)

@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    question_id = data.get('question_id')
    selected_option = data.get('selected_option')
    
    question = next((q for q in QUIZ_DATA if q['id'] == question_id), None)
    
    if not question:
        return jsonify({'error': 'Frage nicht gefunden'}), 404
    
    is_correct = selected_option == question['korrekt']
    
    return jsonify({
        'is_correct': is_correct,
        'correct_answer': question['korrekt'],
        'correct_text': question['optionen'][question['korrekt']]
    })

if __name__ == '__main__':
    app.run(debug=True)