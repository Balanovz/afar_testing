from pymeasure.instruments.agilent import Agilent33220A
from pyvisa.errors import VisaIOError
import logging


DEFAULT_IP = '192.168.0.209'

class WFG:
    def __init__(self, ip=DEFAULT_IP):
        self.connection_status = False
        self.try_connect(ip)

    def try_connect(self, ip):
        try:
            self.adapter = Agilent33220A(f"TCPIP::{ip}::inst0::INSTR")
            self.connection_status = True
        except VisaIOError:
            logging.error("Ошибка подключения устройства Agilent33220a (Волновой генератор)")
            self.connection_status = False

    def get_output(self):
        if self.connection_status:
            try:
                output = self.adapter.output
                self.connection_status = True
                return output
            except VisaIOError:
                logging.error("Ошибка при выдаче параметра output")
                self.connection_status = False
        else:
            logging.error('Agilent33220a не подключен')

    def get_amplitude(self):
        if self.connection_status:
            try:
                amplitude = self.adapter.amplitude
                self.connection_status = True
                return amplitude
            except VisaIOError:
                logging.error("Ошибка при выдаче параметра amplitude")
                self.connection_status = False
        else:
            logging.error('Agilent33220a не подключен')

    def get_shape(self):
        if self.connection_status:
            try:
                shape = self.adapter.shape
                self.connection_status = True
                return shape
            except VisaIOError:
                logging.error("Ошибка при выдаче параметра shape")
                self.connection_status = False
        else:
            logging.error('Agilent33220a не подключен')

    def get_frequency(self):
        if self.connection_status:
            try:
                frequency = self.adapter.frequency
                self.connection_status = True
                return frequency
            except VisaIOError:
                logging.error("Ошибка при выдаче параметра frequency")
                self.connection_status = False
        else:
            logging.error('Agilent33220a не подключен')

    def set_output(self, status: bool):
        self.get_output()
        if self.connection_status:
            self.adapter.output = status

    def set_shape(self, func: str):
        try:
            if func not in ('SIN', 'SQU', 'RAMP', 'PULS', 'NOIS', 'USER'):
                raise ValueError
            self.get_shape()
            if self.connection_status:
                self.adapter.shape = func
            else:
                logging.error('Agilent33220a не подключен')
        except ValueError:
            logging.error(f'Неверный параметр для установки формы сигнала: {func}')

    # в зависимости от функции меняется минимальное и максимальное значение
    # на вход приходят kHz
    def set_frequency(self, freq: float):
        try:
            if not 0.000001 <= freq <= 20000000.0:
                raise ValueError
            self.get_frequency()
            if self.connection_status:
                self.adapter.frequency = freq
        except ValueError:
            logging.error(f'Неверное значение для установки частоты сигнала: {freq}')

    def set_amplitude(self, ampl: float):
        try:
            if not 0.01 <= ampl <= 10.0:
                raise ValueError
            self.get_amplitude()
            if self.connection_status:
                self.adapter.amplitude = ampl
        except ValueError:
            logging.error(f'Неверное значение для амплитуды: {ampl}')