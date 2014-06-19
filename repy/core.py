# -*- coding: utf-8 -*-

# python std lib
import re
import timeit
import logging

Log = logging.getLogger(__name__)


class Core(object):

    def __init__(self):
        """
        """
        Log.debug("Init core")
        self.regex = None
        self.text = None
        self.timeit_itterations = 10000
        self.log_stdout = True

    def setup(self, regex, text, timeit_itterations=10000, log_stdout=True):
        """
        log_stdout is good to have if you import Core and use it as a lib and not cli tool.
        """
        Log.debug("Setup core")
        self.regex = regex
        self.text = text
        self.timeit_itterations = timeit_itterations
        self.log_stdout = log_stdout

    def msg(self, msg):
        """
        Wrapper for printing output to somewhere
        """
        if self.log_stdout:
            print(msg)
        else:
            Log.debug("Supressing log message : {}".format(msg))

    def run(self):
        """
        Parse the regex, print output, return all result objects
        """
        Log.debug("Running core")

        r = None
        m = None
        tt = None
        regex = re.compile(self.regex)

        ##################################################################
        self.msg("# Search for all matches")
        self.msg(">>> regex = re.compile(self.regex)")
        self.msg(">>> r = regex.search(self.text)")
        self.msg(">>> r is not None")
        r = regex.search(self.text)
        self.msg(r is not None)
        # <_sre.SRE_Match object at 0xbcb87c187f861cd0>

        ##################################################################
        if r:
            self.msg("")

            self.msg("# Find what indexes the regex matched")
            self.msg(">>> r.regs")
            self.msg(r.regs)
            # ((0, 6),)

            ##################################################################
            self.msg("")

            self.msg("# Test if regex matches text")
            self.msg(">>> m = regex.match(self.text)")
            self.msg(">>> m is not None")
            m = regex.match(self.text)
            self.msg(m is not None)
            # <_sre.SRE_Match object at 0xbcb87c187f861de0>

        ##################################################################
        if r:
            self.msg("")

            self.msg("# List the groups found")
            self.msg(">>> r.groups()")
            self.msg(r.groups())
            # (u'color', u'fsck')

            ##################################################################
            self.msg("")

            self.msg("# List the named dictionary objects found")
            self.msg(">>> r.groupdict()")
            self.msg(r.groupdict())
            # {u'key': u'color', u'value': u'fsck'}

        ##################################################################
        self.msg("")

        self.msg("# Run findall")
        self.msg(">>> f = regex.findall(text)")
        self.msg(">>> f")
        f = regex.findall(self.text)
        self.msg(f)
        # [(u'color', u'fsck'), (u'animal', u'aasvogel'), (u'vegetable', u'rutabaga'), (u'', u'')]

        ##################################################################
        self.msg("")

        self.msg("# Run timeit test")
        self.msg(">>> setup = ur'import re; regex =re.compile('%s');string='%s'" % (self.regex, self.text))
        self.msg(">>> t = timeit.Timer('regex.search(string)',setup)")
        self.msg(">>> t.timeit(10000)")
        setup = r"import re; regex=re.compile('%s');string='%s'" % (self.regex, self.text)
        t = timeit.Timer("regex.search('%s')" % self.text, setup)
        tt = t.timeit(self.timeit_itterations)
        self.msg(tt)
        # 0.03866742999525741

        # returns (regex.search(), regex.match(), regex.findall(), timeit-time)
        return (r, m, f, tt)
