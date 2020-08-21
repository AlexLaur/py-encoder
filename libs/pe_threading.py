import sys
import traceback
from PySide2 import QtGui, QtCore, QtWidgets

from libs.pe_logger import logger

class ThreadPool(QtCore.QThreadPool):
    def __init__(self):
        super(ThreadPool, self).__init__()
        self.setExpiryTimeout(3000)

        logger.info('Init Threadpool done.')

    def execution(self, function, *args, **kwargs):
        logger.info('Got a work.')
        worker = Runnable(function, *args, **kwargs)

        self.start(worker, 1)


class Runnable(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Runnable, self).__init__()

        self.fn = fn
        self.args = args
        self.kwargs = kwargs

        logger.info('Init worker')

    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
            logger.info('function %s done.' % self.fn)
        except Exception as e:
            print(e)
            logger.warning(e)

