import unittest
from main import InstrumentType, Bass, Guitar, ElectricGuitar, Employee, Roles, Location, Stock, Store  

class TestInstrumentClasses(unittest.TestCase):
    
    def test_bass_type(self):
        bass = Bass("Fender", "Jazz Bass", 4000, 4)
        self.assertEqual(bass.type_.name, "BASS")

    def test_guitar_type(self):
        guitar = Guitar("Gibson", "Les Paul", 3000, 6)
        self.assertEqual(guitar.type_.name, "GUITAR")

    def test_electric_guitar_type(self):
        electric_guitar = ElectricGuitar("Tagima", "Stratocaster", 1200, 5)
        self.assertEqual(electric_guitar.type_.name, "electric_GUITAR")

class TestEmployee(unittest.TestCase):

    def test_employee_role_multiple_changes(self):
        employee = Employee("Ricardo", "111.111.111-11", 2000, Roles.WORKER)
        employee.change_role(Roles.MANAGER)
        self.assertEqual(employee.role, Roles.MANAGER)
        employee.change_role(Roles.CEO)
        self.assertEqual(employee.role, Roles.CEO)
        employee.change_role(Roles.TRAINEE)
        self.assertEqual(employee.role, Roles.TRAINEE)

    def test_invalid_role_change(self):
        employee = Employee("Ricardo", "111.111.111-11", 2000, Roles.WORKER)
        with self.assertRaises(ValueError):
            employee.change_role("INVALID_ROLE")

class TestStock(unittest.TestCase):
    
    def test_add_multiple_instruments(self):
        stock = Stock()
        bass = Bass("Fender", "Jazz Bass", 4000, 4)
        guitar = Guitar("Gibson", "Les Paul", 3000, 6)
        electric_guitar = ElectricGuitar("Tagima", "Stratocaster", 1200, 5)

        stock.add_instrument(bass)
        stock.add_instrument(guitar)
        stock.add_instrument(electric_guitar)

        self.assertEqual(stock.bass_count, 1)
        self.assertEqual(stock.guitar_count, 1)
        self.assertEqual(stock.electric_guitar_count, 1)

    def test_remove_instrument_empty_stock(self):
        stock = Stock()
        stock.remove_instrument()
        self.assertEqual(stock.bass_count, 0)
        self.assertEqual(stock.guitar_count, 0)
        self.assertEqual(stock.electric_guitar_count, 0)

    def test_add_remove_multiple_instruments(self):
        stock = Stock()
        bass = Bass("Fender", "Jazz Bass", 4000, 4)
        guitar = Guitar("Gibson", "Les Paul", 3000, 6)

        stock.add_instrument(bass)
        stock.add_instrument(guitar)
        stock.remove_instrument()

        self.assertEqual(stock.bass_count, 1)
        self.assertEqual(stock.guitar_count, 0)

    def test_stock_multiple_additions(self):
        stock = Stock()
        bass = Bass("Fender", "Jazz Bass", 4000, 4)
        guitar = Guitar("Gibson", "Les Paul", 3000, 6)

        stock.add_instrument(bass)
        stock.add_instrument(guitar)
        stock.add_instrument(bass)

        self.assertEqual(stock.bass_count, 2)
        self.assertEqual(stock.guitar_count, 1)

class TestStore(unittest.TestCase):

    def test_store_initialization_empty_stock(self):
        store_location = Location("Brasil", "RJ", "Rio de Janeiro", "Rua 9 de novembro", 42)
        store = Store(store_location)
        self.assertEqual(store.stock.bass_count, 0)
        self.assertEqual(store.stock.guitar_count, 0)
        self.assertEqual(store.stock.electric_guitar_count, 0)

    def test_store_closest_store(self):
        store_location_1 = Location("Brasil", "RJ", "Rio de Janeiro", "Rua 9 de novembro", 42)
        store_location_2 = Location("Brasil", "SP", "São Paulo", "Av. Paulista", 100)
        store_1 = Store(store_location_1)
        store_2 = Store(store_location_2)

        store_1.set_closest_store(store_2)
        self.assertEqual(store_1.closest_store.location.city, "São Paulo")

    def test_add_remove_employee_store(self):
        store_location = Location("Brasil", "RJ", "Rio de Janeiro", "Rua 9 de novembro", 42)
        store = Store(store_location)

        employee1 = Employee("Ricardo", "111.111.111-11", 2000, Roles.WORKER)
        employee2 = Employee("Ana", "222.222.222-22", 2500, Roles.MANAGER)

        store.add_employee(employee1)
        store.add_employee(employee2)

        self.assertEqual(len(store._employees_list), 2)
        self.assertEqual(store.employees['WORKER'], 1)
        self.assertEqual(store.employees['MANAGER'], 1)

        store.remove_employee()
        self.assertEqual(len(store._employees_list), 1)
        self.assertEqual(store.employees['WORKER'], 1)
        self.assertEqual(store.employees['MANAGER'], 0)

    def test_add_multiple_instruments_to_store(self):
        store_location = Location("Brasil", "RJ", "Rio de Janeiro", "Rua 9 de novembro", 42)
        store = Store(store_location)

        bass = Bass("Fender", "Jazz Bass", 4000, 4)
        guitar = Guitar("Gibson", "Les Paul", 3000, 6)

        store.add_instrument(bass)
        store.add_instrument(guitar)

        self.assertEqual(store.stock.bass_count, 1)
        self.assertEqual(store.stock.guitar_count, 1)

    def test_remove_instrument_from_store(self):
        store_location = Location("Brasil", "RJ", "Rio de Janeiro", "Rua 9 de novembro", 42)
        store = Store(store_location)

        bass = Bass("Fender", "Jazz Bass", 4000, 4)
        store.add_instrument(bass)
        store.remove_instrument()

        self.assertEqual(store.stock.bass_count, 0)

class TestLocation(unittest.TestCase):

    def test_location_str(self):
        location = Location("Brasil", "RJ", "Rio de Janeiro", "Rua 9 de novembro", 42)
        self.assertEqual(str(location), "Rua 9 de novembro 42, Rio de Janeiro - RJ, Brasil")

if __name__ == "__main__":
    unittest.main()