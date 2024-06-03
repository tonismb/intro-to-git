class KriptoValuta:
    def __init__(self, ime, vrijednost, trend_24h, trend_24h_postotak, trend_7d, trend_7d_postotak) -> None:
        self.ime = ime
        self.vrijednost = vrijednost
        self.trend_24h = trend_24h
        self.trend_24h_postotak = trend_24h_postotak
        self.trend_7d = trend_7d
        self.trend_7d_postotak = trend_7d_postotak

    def __str__(self) -> str:
        return f"{self.ime}, {self.vrijednost}, 24H: {self.trend_24h_postotak} ({self.trend_24h}), 7D: {self.trend_7d_postotak} ({self.trend_7d})"
