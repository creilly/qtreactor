Qt4Reactor (sitz lab edition)

Installation
------------

1. unzip the zipped project file, 
2. open up a terminal in the Python environment of your choice (i.e. open a "cmd.exe" window in anaconda)
3. navigate to the root 
4. run ``pip install -e ./``

Usage
-----

We use the following boilerplate in our gui applications combining twisted (i.e. pylabrad) and qt:
::

    import sys
    from PySide import QtGui, QtCore
    if QtCore.QCoreApplication.instance() is None:
        app = QtGui.QApplication(sys.argv)
        import qt4reactor
        qt4reactor.install()

old readme
==========

Using the QtReactor
-------------------

Before running / importing any other Twisted code, invoke:

::

    app = QApplication(sys.argv) # your code to init QtCore
    from twisted.application import reactors
    reactors.installReactor('pyqt4')

or

::

    app = QApplication(sys.argv) # your code to init QtCore
    from twisted.application import reactors
    reactors.installReactor('pyside4')

alternatively (gui example):

::

    app = PyQt4.QtGui(sys.argv) # your code to init QtGui
    from qtreactor import pyqt4reactor
    pyqt4reactor.install()

Testing
~~~~~~~

::

   trial --reactor=pyqt4 [twisted] [twisted.test] [twisted.test.test_internet]

Testing with a Gui
~~~~~~~~~~~~~~~~~~

Twisted trial can be run for a Gui test using gtrial. Run Trial in the
same directory as bin/gtrial and it pops up a trivial gui... hit the
buton and it all runs the same... don't use the --reactor option when
calling gtrial... but all the other options appear to work.

::

    cp gtrial <test-directory>

    cd <test-directory> && trial

If you're writing a conventional Qt application and just want twisted as
an addon, you can get that by calling reactor.runReturn() instead of
run(). This call needs to occur after your installation of of the
reactor and after QApplication.exec\_() (or QCoreApplication.exec\_()
whichever you are using.

reactor.run() will also work as expected in a typical twisted
application

Note that if a QApplication or QCoreApplication instance isn't
constructed prior to calling reactor run, an internally owned
QCoreApplication is created and destroyed. This won't work if you call
runReturn instead of run unless you take responsibility for destroying
QCoreApplication yourself...

However, most users want this reactor to do gui stuff so this shouldn't
be an issue.

Performance impact of Qt has been reduced by minimizing use of signaling
which is expensive.

Examples / tests in ghtTests
