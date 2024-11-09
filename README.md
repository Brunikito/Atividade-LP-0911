# Atividade-LP-0911

## Estruturação do código:

As classes utiizadas foram as seguintes:
**InstrumentType, Instrument, Bass, Guitar, ElectricGuitar, Roles, Employee, Location, Stock, Store.**

As relações são as seguintes:

Herança entre **Bass, Guitar, ElectricGuitar** e **Instrument**. Cada tipo de instrumento continua sendo um instrumento e tem todas as propriedades de um instrumento. Assim, eles herdam isso da classe instrumento.

**Associação** entre **Instrument** e **InstrumentType**. Cada instrumento tem o seu tipo, que foi definido em uma classe enum.

**Associação** entre **Roles** e **Employee**. Cada funcionário tem o seu próprio cargo, que foi definido em uma classe enum.

**Associação** entre **Store** e **Location**. Cada loja tem um endereço associado.


**Agregação** entre **Bass, Guitar, ElectricGuitar** e **Stock**. O estoque agrega os instrumentos, que podem existir sem ele.

**Agregação** entre **Employee** e **Store**. Os funcionários fazem parte de uma lista de funcionários da loja, mas podem existir sem ela.


**Composição** entre **Stock** e **Store**. A loja possui um estoque, que não pode existir sem ela.