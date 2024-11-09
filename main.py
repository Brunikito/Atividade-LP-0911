import enum

# Classe com enum para o tipo do instrumento
class InstrumentType(enum.Enum):
    BASS = enum.auto()
    GUITAR = enum.auto()
    electric_GUITAR = enum.auto()

# Classe base para instrumento
class Instrument:
    def __init__(self, brand, model, price, number_of_strings, famous = None):
        self._brand = brand
        self._model = model
        self._price = price
        self._number_of_strings = number_of_strings
        self._famous = famous
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def model(self):
        return self._model
    
    @property
    def price(self):
        return self._price
    
    @property
    def number_of_strings(self):
        return self._number_of_strings
    
    @property
    def famous(self):
        return self._famous

# Classes para cada tipo de instrumento, herdadas da classe Instrument
class Bass(Instrument):
    def __init__(self, brand, model, price, number_of_strings, famous = None):
        self._type = InstrumentType(1)
        super().__init__(brand, model, price, number_of_strings, famous)
    
    @property
    def type_(self):
        return self._type
    
    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(brand={self.brand!r}, model={self.model!r}, price={self.price!r}, number_of_strings={self.number_of_strings!r}, famous={self.famous!r})"

class Guitar(Instrument):
    def __init__(self, brand, model, price, number_of_strings, famous = None):
        self._type = InstrumentType(2)
        super().__init__(brand, model, price, number_of_strings, famous)
    
    @property
    def type_(self):
        return self._type

    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(brand={self.brand!r}, model={self.model!r}, price={self.price!r}, number_of_strings={self.number_of_strings!r}, famous={self.famous!r})"

class ElectricGuitar(Instrument):
    def __init__(self, brand, model, price, number_of_strings, famous = None):
        self._type = InstrumentType(3)
        super().__init__(brand, model, price, number_of_strings, famous)
    
    @property
    def type_(self):
        return self._type

    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(brand={self.brand!r}, model={self.model!r}, price={self.price!r}, number_of_strings={self.number_of_strings!r}, famous={self.famous!r})"

# Exemplo de objeto
# guitar1 = ElectricGuitar('Tagima', 'Stratocaster', 1200, 5)
# print(guitar1)

##########################################################

# Classe com enum para o cargo
class Roles(enum.Enum):
    CEO = enum.auto()
    MANAGER = enum.auto()
    WORKER = enum.auto()
    TRAINEE = enum.auto()

# Classe para o empregado
class Employee:
    def __init__(self, name, cpf, wage, role, current_store = None):
        self._name = name
        self._cpf = cpf
        self._wage = wage
        self._role = role
        self._current_store = current_store
    
    @property
    def name(self):
        return self._name

    @property
    def cpf(self):
        return self._cpf

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, wage):
        self._wage = wage

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def current_store(self):
        return self._current_store

    @current_store.setter
    def current_store(self, current_store):
        self._current_store = current_store
    
    def change_role(self, new_role):
        self._role = new_role

    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(name={self.name!r}, cpf={self.cpf!r}, wage={self.wage!r} role={self.role.name!r}, current_store={self.current_store!r})"
    
# Exemplo de objeto
# employee1 = Employee('Ricardo', 11111111111, 2000, Roles(1))
# print(employee1)

##########################################################

# Classe para a localização
class Location:
    def __init__(self, country, state, city, street, number):
        self._country = country
        self._state = state
        self._city = city
        self._street = street
        self._number = number
    
    @property
    def country(self):
        return self._country
    
    @property
    def state(self):
        return self._state
    
    @property
    def city(self):
        return self._city
    
    @property
    def street(self):
        return self._street
    
    @property
    def number(self):
        return self._number

    def __repr__(self) -> str:
        return (f"Location(country={self._country!r}, state={self._state!r}, "
                f"city={self._city!r}, street={self._street!r}, number={self._number!r})")
    
    def __str__(self) -> str:
        return (f"{self._street} {self._number}, {self._city} - {self._state}, {self._country}")

# Classe para o estoque
class Stock:
    def __init__(self, instruments = []):
        self._instruments = instruments

    @property
    def instruments(self):
        return self._instruments

    def add_instrument(self, instrument):
        self._instruments.append(instrument)

    def remove_instrument(self):
        self._instruments.remove(self._instruments[-1])

    def count_instruments(self, instrument_type):
        return sum(1 for instrument in self._instruments if isinstance(instrument, instrument_type))

    @property
    def bass_count(self):
        return self.count_instruments(Bass)

    @property
    def guitar_count(self):
        return self.count_instruments(Guitar)

    @property
    def electric_guitar_count(self):
        return self.count_instruments(ElectricGuitar)
    
    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(instruments: {self.instruments!r})"
    
    def __str__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(bass_count: {self.bass_count!r}, guitar_count: {self.guitar_count!r}, electric_gruitar_count: {self.electric_guitar_count!r})"

# Classe para a loja
class Store:
    def __init__(self, location):
        self.location = location
        self._employees_list = []
        self._stock = Stock()
        self.closest_store = None
    
    def set_closest_store(self, store):
        self.closest_store = store

    def add_employee(self, employee):
        self._employees_list.append(employee)
        employee.current_store = self

    def remove_employee(self):
        employee = self._employees_list[-1]
        self._employees_list.remove(employee)
        employee.current_store = None

    def add_instrument(self, instrument):
        self.stock.add_instrument(instrument)

    def remove_instrument(self):
        self.stock.remove_instrument()
    
    def count_employees_role(self, role):
        return sum(1 for employee in self._employees_list if employee.role == role)

    @property
    def employees(self):
        return {role.name: self.count_employees_role(role) for role in Roles}
    
    @property
    def stock(self):
        return self._stock

    def __repr__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(location={self.location!r}, employees={self.employees!r}, stock={self.stock!r})"
    
    def __str__(self) -> str:
        class_ = self.__class__.__name__
        return f"{class_}(location={str(self.location)!r}, employees={self.employees!r}, stock={str(self.stock)!r})"

# Exemplo
if __name__ == "__main__":
    store1_location = Location("Brasil", "RJ", "Rio de Janeiro", "Rua 9 de novembro", 42)
    store1 = Store(store1_location)

    employee1 = Employee("Ricardo", "111.111.111-11", 2000, Roles.WORKER)
    store1.add_employee(employee1)

    bass1 = Bass("Fender", "Jazz Bass", 4000, 4)
    store1.add_instrument(bass1)

    guitar1 = ElectricGuitar('Tagima', 'Stratocaster', 1200, 5)
    store1.add_instrument(guitar1)

    print(store1)
    print(employee1)
    print('#'*42)

    store1.remove_employee()
    print(store1)
    print(employee1)
    print('#'*42)

    store1.remove_instrument()
    print(store1)
    print('#'*42)
