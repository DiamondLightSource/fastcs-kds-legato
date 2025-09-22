from fastcs.attributes import AttrR
from fastcs.connections import (
    SerialConnection,
    SerialConnectionSettings,
)
from fastcs.controller import Controller
from fastcs.datatypes import String


class KdsLegatoController(Controller):
    device_version = AttrR(String())

    def __init__(self, settings: SerialConnectionSettings):
        super().__init__()

        self._serial_settings = settings
        self.connection = SerialConnection()

    async def connect(self):
        await self.connection.connect(self._serial_settings)
