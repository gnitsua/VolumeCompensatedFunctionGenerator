import logging
import threading
import time
from queue import Queue

import visa
from pyvisa import VisaIOError

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s')

class Agilent33220A():
    def __init__(self, BUF_SIZE=10):
        self.command_queue = Queue(BUF_SIZE)
        c = ConsumerThread(self.command_queue)
        c.start()

    def write(self, command):
        """
        Allows the command to be written to the Agilent asynchronously
        :param command:
        :return:
        """
        if not self.command_queue.full():
            self.command_queue.put(command)
        else:
            raise IOError("Command buffer full")


class ConsumerThread(threading.Thread):
    def __init__(self, queue):
        super(ConsumerThread, self).__init__()
        self.queue = queue

        rm = visa.ResourceManager()
        resource_list = rm.list_resources()
        print("Connected devices", resource_list)

        resource = ""

        for index in range(len(resource_list)):
            if "0x0957::0x0407::" in resource_list[index]:
                resource = resource_list[index]
                break
        if resource != "":
            print("Connecting to %s" % (resource))
            try:
                AGILENT_33220A = rm.open_resource(resource)
                print(AGILENT_33220A.query('*IDN?'))
                self.generator = AGILENT_33220A
            except VisaIOError as e:
                # raise e
                print(e)
        else:
            print("Error: Agilent 33220A not connected.")
            raise IOError()

        return

    def run(self):
        while True:
            if not self.queue.empty():
                item = self.queue.get()
                logging.debug("Sending Command:%s" % (item))
                # self.generator.write(item)
                time.sleep(0.1)
        return
