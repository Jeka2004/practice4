class Instrument:
    def get_type(self):
        raise NotImplementedError("Цей метод має бути реалізований у підкласі")

class Percussion(Instrument):  # Ударні
    def get_type(self):
        return "Ударні"

class Wind(Instrument):  # Духові
    def get_type(self):
        return "Духові"

class Keyboard(Instrument):  # Клавішні
    def get_type(self):
        return "Клавішні"

class Drum(Percussion):  # Барабан
    pass

class Tambourine(Percussion):  # Бубон
    pass

class Trombone(Wind):  # Тромбон
    pass

class Flute(Wind):  # Флейта
    pass

class Organ(Keyboard):  # Орган
    pass

class Harmonica(Keyboard):  # Гармоніка
    pass

class Bayan(Keyboard):  # Баян
    pass

class Piano(Keyboard):  # Рояль
    pass

drum = Drum()
tambourine = Tambourine()
trombone = Trombone()
flute = Flute()
organ = Organ()
harmonica = Harmonica()
bayan = Bayan()
piano = Piano()

percussion_instruments = [drum, tambourine]
wind_instruments = [trombone, flute]
keyboard_instruments = [organ, harmonica, bayan, piano]

def print_instrument_types(instruments):
    for instrument in instruments:
        print(f"{instrument.__class__.__name__}: {instrument.get_type()}")

print("Ударні інструменти:")
print_instrument_types(percussion_instruments)

print("\nДухові інструменти:")
print_instrument_types(wind_instruments)

print("\nКлавішні інструменти:")
print_instrument_types(keyboard_instruments)
