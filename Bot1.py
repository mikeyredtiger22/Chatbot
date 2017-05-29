#!flask/bin/python
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from flask import Flask, jsonify, abort, make_response, request
import json

bot1 = Flask(__name__)

chatbot = ChatBot(
        'Ron Obvious',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
        database='./database.json',
        storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
        input_adapter='chatterbot.input.VariableInputTypeAdapter',
        output_adapter='chatterbot.output.OutputAdapter',
        chatterbox_adapters=['chatterbot.logic.BestMatch'],
        silence_performance_warning=True)


@bot1.route('/', methods=['POST'])
def talk():
    if not request.json:  # or not 'message' in request.json:
        abort(400)

    input_item = request.json
    print "input item: ", input_item

    parsed_json = json.loads(input_item)
    string = parsed_json['message']
    print "string: ", parsed_json, string
    response = str(chatbot.get_response(string))

    print "response: ", response
    return response


# noinspection PyUnusedLocal
@bot1.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)


# noinspection PyUnusedLocal
@bot1.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'Error': 'Invalid Json Format'}), 400)

if __name__ == '__main__':
    bot1.run()

