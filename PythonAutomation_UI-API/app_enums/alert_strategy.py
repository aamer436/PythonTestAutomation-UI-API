from enum import Enum

class AlertStrategy(Enum):
    ACCEPT=1
    DISMISS = 2
    SEND_KEYS = 3
    GET_TEXT = 4