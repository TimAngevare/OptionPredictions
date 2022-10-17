
class Stock:
    def __init__(self, callsign) -> None:
        self.callsign = callsign

    def __str__(self) -> str:
        return self.callsign
