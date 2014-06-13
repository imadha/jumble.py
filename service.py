from flask import Flask, jsonify
import jumble

app = Flask(__name__)

@app.route('/jumble/<word>')
def jumble_(word):
    word = word.strip().lower()
    words = jumble.jumble(word, jumble.build_dictionary('./english-words'))
    return jsonify(
            input=word,
            results=words
    )

if __name__ == '__main__':
    app.run()
