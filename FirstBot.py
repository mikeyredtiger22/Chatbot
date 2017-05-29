# -*- coding: utf-8 -*-
from chatterbot import ChatBot


class FirstBot(ChatBot):

    def __init__(self):
        super(FirstBot, self).__init__('Ron Obvious',
                                       trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
                                       database='./database.json',
                                       storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
                                       input_adapter='chatterbot.input.TerminalAdapter',
                                       output_adapter='chatterbot.output.TerminalAdapter',
                                       chatterbox_adapters=['chatterbot.logic.BestMatch'],
                                       silence_performance_warning=True)

    def run(self):
        # Train based on the english corpus
        print "training"
        self.train("chatterbot.corpus.english")

        # Get a response to an input statement
        print "getting response"
        # response = chatbot.get_response("Hello, how are you today?")

        while True:
            try:
                bot_input = self.get_response(None)

            except(KeyboardInterrupt, EOFError, SystemExit):
                break
