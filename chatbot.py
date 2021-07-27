# -*- coding: utf-8 -*-
import aiml
import os


class ChatBot:
    def __init__(self, path):
        self.path = path
        self.kernel = aiml.Kernel()
        self.read_brain()

    def read_brain(self):
        if os.path.isfile("mybot_brain.brn"):
            self.kernel.bootstrap(brainFile="mybot_brain.brn")
        else:
            self.kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
            for filename in os.listdir(self.path):
                if filename.endswith(".aiml"):
                    self.kernel.learn(os.path.join(self.path, filename))
            self.kernel.saveBrain("mybot_brain.brn")

    def get_response(self, input_text):
        response = self.kernel.respond(input_text)
        return response
