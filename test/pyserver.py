#!/home/hensch/tmp/python-sandbox/bin/python
import sys
import os
import time

from tuxedo.atmi import *
import tuxedo.reloader

import pyserver


tux = tuxedo.atmi

class server:
        def subscTOUPPER(self, arg):
                ret = str.upper(arg)
                tpnotify(self.cltid, ret)
                return TPSUCCESS

        def TOUPPERFAIL(self, arg):
                ret = str.upper(arg)
                return TPFAIL

        def COUNTER(self, arg):
                self.counter += 1
                return repr(self.counter)

        def RESETCOUNTER(self, arg):
                self.counter = 0
                return TPSUCCESS

        def TOUPPER(self, arg):     # get string and return string
                print(self.name)
                try:
                        print(self.cd)
                except:
                        print("No Conversation ")
                print(self.flags)
                print(self.appkey)
                print(self.cltid)

                userlog("client-ID = %s" % (self.cltid))

                print("converting %s" % arg)
                return str.upper(arg)

        def UNSOLmethod_for_call_from_service_UNSOL(self, arg):     # get string and return string

                print("UNSOL: %s" % self.cltid)
                tpnotify(self.cltid, "from server: 1")
                time.sleep(1)
                tpnotify(self.cltid, "from server: 2")
                tpnotify(self.cltid, "from server: 3")

                tpbroadcast("simple", None, None, "from server: 4")

                return str.upper(arg)

        def TUPPER(self, arg):
                print("call TUPPER")
                tpforward("TOUPPER", arg)

        def service123456789abcdefghijklm(self, arg):   # change FML argument buffer and return it
                print("call service_1")
                print(list(arg.keys()))
                arg['TA_OPERATION'][0] = "OK"
                arg['TA_OPERATION'].append("NOK")
                print(arg)
                return arg

        def ping(self, arg):
                print("call ping and return ", arg)
                return arg

        def service_3(self, arg):   # get whatever and return new FML buffer (elements are lists)
                print("call service_3")

                return { 'VORNAME': ['Ralf', 'Andreas'], 'NACHNAME': ['Henschkowski'] }

        def service_4(self, arg):
                print("call service_4")  # return new FML buffer (elements can be strings -> occurence 0)

                return { 'VORNAME': 'Ralf_Andreas', 'NACHNAME': ['Henschkowski'] }

        def service_5(self, arg):   # return  returncode                print "call service_5"
                tpunadvertise("service_4")
                return TPSUCCESS

        def __init__(self):         # called whenever class is loaded/instantiated
                self.RESETCOUNTER(0)

        def init(self, arguments):  # called on server boot
                tpopen()
                tpadvertise("ping")
                tpadvertise("TOUPPER")
                tpadvertise("TOUPPERFAIL")
                tpadvertise("COUNTER")
                tpadvertise("RESETCOUNTER")
                tpadvertise("service_3")
                tpadvertise("UNSOL", "UNSOLmethod_for_call_from_service_UNSOL")
                tpadvertise("subscTOUPPER")

                tpsubscribe("TOUPPER_EVT", "", { 'flags': TPEVSERVICE, 'name1': "subscTOUPPER" } )

if __name__ == '__main__':

        myserver = pyserver.server()   # initial server class instance
        rel = tuxedo.reloader.Reloader(pyserver, myserver) # dynamic reloader
        tuxedo.atmi.mainloop(sys.argv, myserver, rel.reloader_func)

# Local Variables:
# mode:python
# End:

