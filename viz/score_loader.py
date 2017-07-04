import flask
from flask import Flask
import pickle

# Load dictionary of model scores from pickle file
# dictionary keys = the value of the binary code correlated to the active columns
# dictionary values = two sub dictionares:
# sub dictionary 1: score - includes F1, accuracy, recall and precision scores for the model
# sub dictionary 2: params - includes the best parameters from grid search (for printing to console)

data = pickle.load(open("../model_dict.p", "rb"))

app = Flask(__name__)

@app.route('/')
def hello_word():
    with open('index.html', 'r') as viz:
        return viz.read()

@app.route('/analyze', methods=['POST'])
def return_scores():    
    print("test")
    key_dict = flask.request.json
    key = key_dict["key"][0]
    print(key)
    results = {'scores': data[key]['scores'], 
               'params': data[key]['params']
     }
    return flask.jsonify(results)

if __name__ == '__main__':
    app.run()
