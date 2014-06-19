# -*- coding: utf-8 -*-
__author__ = "Johan Grok Andersson <Grokzen@gmail.com>"

# python std lib
import logging

# repy imports
from repy.core import Core

Log = logging.getLogger(__name__)


class Interactive(object):

    def __init__(self):
        Log.debug("Init interactive mode")

    def run(self):
        Log.debug("Running interactive mode")

        i = True
        j = True

        while i is True:
            regex = input("\n\nInput regex: ")
            text = input("Input text (Only sinle line is supported): ")
            print("\n")

            c = Core()
            c.setup(regex, text)
            result = c.run()
            Log.debug(result)

            # Ask the user if another query should be runned
            while j is True:
                awnser = input("\n\n\nDo you want to run another query? (y/n/q) : ").lower()

                if awnser == "y":
                    # Loop another round
                    i = True
                    j = False
                elif awnser == "n" or awnser == "q":
                    i = False
                    j = False
                else:
                    print(" Unknown input...")
