"""Smbus2 asyncio support."""
import asyncio

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
        self.lock = asyncio.Lock()

    def open_sync(self):
        """Open synchronous."""
        self.smbus = SMBus(self.bus)

    async def open(self):
        """Open async."""
        return await self.loop.run_in_executor(self.executor, self.open_sync)

    async def read_byte_data(self, i2c_addr, register):
        """Read a single byte from a designated register."""
        assert self.smbus
        async with self.lock:
            result = await self.loop.run_in_executor(
                self.executor, self.smbus.read_byte_data, i2c_addr, register
            )
        return result

    async def read_i2c_block_data(self, i2c_addr, register, length):
        """Read a block of byte data from a given register."""
        assert self.smbus
        async with self.lock:
            result = await self.loop.run_in_executor(
                self.executor,
                self.smbus.read_i2c_block_data,
                i2c_addr,
                register,
                length,
            )
        return result

    async def write_byte_data(self, i2c_addr, register, value):
        """Write a byte to a given register."""
        assert self.smbus
        async with self.lock:
            result = await self.loop.run_in_executor(
                self.executor, self.smbus.write_byte_data, i2c_addr, register, value
            )

        return result

    async def write_i2c_block_data(self, i2c_addr, register, data):
        """Write a block of byte data to a given register."""
        assert self.smbus
        async with self.lock:
            result = await self.loop.run_in_executor(
                self.executor, self.smbus.write_i2c_block_data, i2c_addr, register, data
            )

        return result
    
    async def write_quick(self, i2c_addr):
        """Perform quick transaction. Throws IOError if unsuccessful."""
        assert self.smbus
        async with self.lock:
            result = await self.loop.run_in_executor(
                self.executor, self.smbus.write_quick, i2c_addr
            )

        return result

    async def i2c_rdwr(self, *i2c_msgs):
        """Perform a series of I2C transactions."""
        assert self.smbus
        async with self.lock:
            result = await self.loop.run_in_executor(
                self.executor, self.smbus.i2c_rdwr, *i2c_msgs
            )

        return result
