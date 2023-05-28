from pymeasure.instruments.agilent import Agilent34410A
from pyvisa.errors import VisaIOError
import logging


DEFAULT_IP = '192.168.0.232'

class Multimeter:
    def __init__(self, ip=DEFAULT_IP):
        self.connection_status = False
        self.ip = ip
        self.try_connect()

    def try_connect(self, ip=DEFAULT_IP):
        self.ip = ip
        try:
            self.adapter = Agilent34410A(f"TCPIP::{self.ip}::inst0::INSTR")
            self.connection_status = True
        except VisaIOError:
            logging.error(f'Ошибка при подключении к устройтсву [Agilent34411A Мультиметр]')
            self.connection_status = False

    def get_voltage_ac(self):
        if self.connection_status:
            try:
                return self.adapter.voltage_ac
            except VisaIOError:
                logging.error('Ошибка при получении переменного напряжения [Agilent34411A Мультиметр]')
                self.connection_status = False
        else:
            logging.error(f'Ошибка при подключении к устройтсву [Agilent34411A Мультиметр] при обращении к переменному напряжению')

    def get_voltage_dc(self):
        if self.connection_status:
            try:
                return self.adapter.voltage_dc
            except VisaIOError:
                logging.error('Ошибка при получении постоянного напряжения [Agilent34411A Мультиметр]')
                self.connection_status = False
        else:
            logging.error(f'Ошибка при подключении к устройтсву [Agilent34411A Мультиметр] при обращении к постоянному напряжению')

    def get_current_ac(self):
        if self.connection_status:
            try:
                return self.adapter.current_ac
            except VisaIOError:
                logging.error('Ошибка при получении переменного тока [Agilent34411A Мультиметр]')
                self.connection_status = False
        else:
            logging.error(f'Ошибка при подключении к устройтсву [Agilent34411A Мультиметр] при обращении к переменному току')

    def get_current_dc(self):
        if self.connection_status:
            try:
                return self.adapter.current_dc
            except VisaIOError:
                logging.error("Ошибка при получении постоянного тока [Agilent34411A Мультиметр]")
                self.connection_status = False
        else:
            logging.error('Ошибка при подключении к устройтсву [Agilent34411A Мультиметр] при обращении к постоянному току')