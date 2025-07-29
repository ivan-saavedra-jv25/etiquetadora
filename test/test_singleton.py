class MetaData:
    def __init__(self, _token) -> None:
        self.TOKEN = _token
        pass
    def get_token(self):
        return self.TOKEN
    
class Singleton():

    _instance = None
    _value = MetaData('este es el token')

    @classmethod
    def get_instance(cls): # Constructor alternativo que retorna una nueva instancia
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def get_value(self):
        return self._value

    def set_value(self, v):
        self._value = v



A = Singleton.get_instance()
B = Singleton.get_instance()

A.set_value(MetaData('este es le token'))

print("¿A es el mismo objeto que B?: ", A is B)

print(f'A: {A._instance}\nB: {B._instance}')

_meta = A.get_instance().get_value()

print(_meta.get_token())