from __future__ import print_function
__author__ = 'ght'

import q

from twisted.application import reactors

reactors.installReactor('kqueue')

from twisted.python import log

import sys

log.startLogging(sys.stdout)

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""

    def dataReceived(self, data):
        q('server: ', data)
        "As soon as any data is received, write it back."
        self.transport.write(data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()