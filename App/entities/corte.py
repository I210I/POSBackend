from datetime import datetime

class Corte:
    def __init__(self, id_corte: int = None, id_usuario: int = None, __50: int = None, _1: int = None, _2: int = None,
                 _5: int = None, _10: int = None, _20: int = None, _50: int = None, _100: int = None, _200: int = None,
                 _500: int = None, _1000: int = None, tarjeta_cantidad: int = None, tarjeta_monto: float = None,
                 fecha_corte: datetime = None):
        self.id_corte = id_corte
        self.id_usuario = id_usuario
        self.__50 = __50
        self._1 = _1
        self._2 = _2
        self._5 = _5
        self._10 = _10
        self._20 = _20
        self._50 = _50
        self._100 = _100
        self._200 = _200
        self._500 = _500
        self._1000 = _1000
        self.tarjeta_cantidad = tarjeta_cantidad
        self.tarjeta_monto = tarjeta_monto
        self.fecha_corte = fecha_corte

    def __repr__(self):
        return f'<Corte {self.id_corte}>'
