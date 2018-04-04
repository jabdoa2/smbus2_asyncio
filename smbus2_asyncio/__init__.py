"""Smbus2 asyncio support."""
import asyncio
from functools import partial

from smbus2 import SMBus


class SMBus2Asyncio:

    """Asyncio version of SMBus2."""

    def __init__(self, bus, *, loop=None, executor=None):
        """Initialise SMBus2 Asyncio."""
        self.bus = bus
        self.smbus = None
        if not loop:
            loop = asyncio.get_event_loop()
        self.loop = loop
        self.executor = executor
        self.lock = asyncio.Lock(loop=loop)

    def open_sync(self):
        """Open synchronous."""
        self.smbus = SMBus(self.bus)

    @asyncio.coroutine
    def open(self):
        """Open async."""
        return self.loop.run_in_executor(self.executor, self.open_sync)

    @asyncio.coroutine
    def read_byte_data(self, i2c_addr, register):
        """Read a single byte from a designated register."""
        assert self.smbus
        yield from self.lock.acquire()
        result = yield from self.loop.run_in_executor(self.executor, partial(self.smbus.read_byte_data,
                                                                             i2c_addr, register))
        self.lock.release()
        return result

    @asyncio.coroutine
    def read_i2c_block_data(self, i2c_addr, register, length):
        """Read a block of byte data from a given register."""
        assert self.smbus
        yield from self.lock.acquire()
        result = yield from self.loop.run_in_executor(self.executor, partial(self.smbus.read_i2c_block_data,
                                                                             i2c_addr, register, length))
        self.lock.release()
        return result

    @asyncio.coroutine
    def write_byte_data(self, i2c_addr, register, value):
        """Write a byte to a given register."""
        assert self.smbus
        yield from self.lock.acquire()
        result = yield from self.loop.run_in_executor(self.executor, partial(self.smbus.write_byte_data,
                                                                             i2c_addr, register, value))
        self.lock.release()
        return result
