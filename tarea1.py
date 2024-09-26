# Clase Visitante
class Visitante:
    def __init__(self, nombre, edad, altura, dinero):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = []  # lista para almacenar los tickets comprados

    def comprar_ticket(self, atraccion):
        if self.dinero >= atraccion.precio:  # verifica si el visitante tiene dinero suficiente
            self.tickets.append(Ticket(atraccion.nombre, atraccion.precio))
            self.dinero -= atraccion.precio  # deduce el costo del ticket
            print(f"{self.nombre} compró un ticket para {atraccion.nombre}.")
        else:
            print(f"{self.nombre} no tiene suficiente dinero para comprar el ticket de {atraccion.nombre}.")

    def entregar_ticket(self, atraccion):
        for ticket in self.tickets:
            if ticket.atraccion == atraccion.nombre:
                self.tickets.remove(ticket)  # elimina el ticket usado
                print(f"{self.nombre} entregó su ticket para {atraccion.nombre}.")
                return
        print(f"{self.nombre} no tiene un ticket para {atraccion.nombre}.")

# Clase Atraccion
class Atraccion:
    def __init__(self, nombre, capacidad, precio):
        self.nombre = nombre
        self.capacidad = capacidad
        self.precio = precio
        self.cola = []  # lista de visitantes en la cola
        self.estado = "activo"  # la atracción comienza activa

    def iniciar_ronda(self):
        if self.estado == "activo" and len(self.cola) > 0:
            print(f"Iniciando la ronda en {self.nombre} con {min(len(self.cola), self.capacidad)} visitantes.")
            self.cola = self.cola[self.capacidad:]  # quita los visitantes que ya entraron
        else:
            print(f"{self.nombre} no está activa o no hay visitantes en la cola.")

# Clase Ticket
class Ticket:
    def __init__(self, atraccion, precio):
        self.atraccion = atraccion
        self.precio = precio

# Clase AtraccionInfantil (hereda de Atraccion)
class AtraccionInfantil(Atraccion):
    def verificar_restricciones(self, visitante):
        if visitante.edad > 10:
            print(f"{visitante.nombre} no puede subir a {self.nombre}. Solo para menores de 10 años.")
            return False
        return True

# Clase MontañaRusa (hereda de Atraccion)
class MontañaRusa(Atraccion):
    def __init__(self, nombre, capacidad, precio, velocidad_maxima, altura_requerida):
        super().__init__(nombre, capacidad, precio)
        self.velocidad_maxima = velocidad_maxima
        self.altura_requerida = altura_requerida

    def verificar_restricciones(self, visitante):
        if visitante.altura < self.altura_requerida:
            print(f"{visitante.nombre} no puede subir a {self.nombre}. Necesita medir al menos {self.altura_requerida} cm.")
            return False
        return True

# Ejemplo simple de uso
visitante = Visitante("Ana", 12, 150, 50)
montaña_rusa = MontañaRusa("Montaña Rusa", 5, 20, 100, 140)
atraccion_infantil = AtraccionInfantil("Carrusel", 10, 5)

# Comprar tickets
visitante.comprar_ticket(montaña_rusa)
visitante.comprar_ticket(atraccion_infantil)

# Verificar restricciones y hacer cola
if montaña_rusa.verificar_restricciones(visitante):
    montaña_rusa.cola.append(visitante)

if atraccion_infantil.verificar_restricciones(visitante):
    atraccion_infantil.cola.append(visitante)

# Iniciar rondas
montaña_rusa.iniciar_ronda()
atraccion_infantil.iniciar_ronda()
