from fastcs.attributes import AttrR
from fastcs.controller import Controller
from fastcs.datatypes import String


class KdsLegatoController(Controller):
    device_version = AttrR(String())
