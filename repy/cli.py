# -*- coding: utf-8 -*-

""" repy - command line interface """


def main():
    """
    Run repy application. Only called from cli.py
    """

    # python std library
    import logging

    # 3rd party imports
    from docopt import docopt

    # Import repy package
    import repy

    #####
    ##### parse arguments
    #####

    __docopt__ = """
Usage:
  repy -i [-v ...]
  repy -r REGEX -t TEXT [-v ...]
  repy --version [--help]

Options:
  -i --interactive         run in interactive mode
  -r --regex               regex to match text to
  -t --text                text to match regex against. Only supports single line input.
  -h --help                show this help
  -v --verbose             verbose terminal output
  -V --version             display the version number and exit
    """

    # Parse all cli arguments with docopt
    args = docopt(__docopt__, version=repy.__version__)

    #####
    ##### validate arguments only, dont go into other code/logic
    #####

    # Init logging & configure verbosity level
    repy.init_logging()
    Log = logging.getLogger(__name__)

    # Calculates what level to set to all loggers
    if not args["--verbose"]:
        level = 20
    else:
        # If anything is specefied
        level = 60 - (args["--verbose"] * 10)

    # Loop all implemented loggers and update them
    for key, _logger in logging.Logger.manager.loggerDict.items():
        if key.startswith("repy"):
            l = logging.getLogger(key)
            l.setLevel(level)
            for handler in l.handlers:
                handler.level = level

    Log.debug("Setting verbose level: {}".format(args["--verbose"]))
    Log.debug("Arguments from CLI: {}".format(args))

    #####
    ##### run application logic
    #####

    if args["--interactive"]:
        Log.info("Run in interactive mode")
        from repy.interactive import Interactive
        i = Interactive()
        i.run()
    else:
        Log.debug("Run in parse mode : {} : {} : ".format(args["REGEX"], args["TEXT"]))
        from repy.core import Core
        c = Core()
        c.setup(args["REGEX"], args["TEXT"])
        c.run()
