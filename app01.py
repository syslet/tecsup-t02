from datetime import datetime

# --- Clases del sistema
class Socio:
    def __init__(self, id_socio, nombre, apellido, email, telefono, membresia):
        self.id_socio = id_socio
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.membresia = membresia
        self.registros = []
        self.pagos = []

    def reservar_cancha(self, servicio, calendario):
        if calendario.consultar_disponibilidad() == "Disponible":
            calendario.reservar_horario()
            registro = Registro(len(self.registros)+1, datetime.now(), self, servicio)
            self.registros.append(registro)
            print(f"{self.nombre} ha reservado la cancha para el servicio {servicio.tipo_servicio}.")
            return registro
        else:
            print("No se pudo reservar, horario ocupado.")
            return None

    def pagar_servicio(self, monto, metodo_pago):
        pago = Pago(len(self.pagos)+1, monto, datetime.now(), metodo_pago, "Pendiente")
        pago.procesar_pago()
        self.pagos.append(pago)
        print(pago.emitir_recibo())


class Servicio:
    def __init__(self, id_servicio, tipo_servicio, precio, duracion):
        self.id_servicio = id_servicio
        self.tipo_servicio = tipo_servicio
        self.precio = precio
        self.duracion = duracion


class Registro:
    def __init__(self, id_registro, fecha_registro, socio, servicio):
        self.id_registro = id_registro
        self.fecha_registro = fecha_registro
        self.socio = socio
        self.servicio = servicio


class Calendario:
    def __init__(self, id_calendario, fecha, hora_inicio, hora_fin, cancha, estado="Disponible"):
        self.id_calendario = id_calendario
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.cancha = cancha
        self.estado = estado

    def reservar_horario(self):
        self.estado = "Reservado"
        print(f"Horario reservado en cancha {self.cancha}.")

    def consultar_disponibilidad(self):
        return self.estado


class Pago:
    def __init__(self, id_pago, monto, fecha_pago, metodo_pago, estado):
        self.id_pago = id_pago
        self.monto = monto
        self.fecha_pago = fecha_pago
        self.metodo_pago = metodo_pago
        self.estado = estado

    def procesar_pago(self):
        self.estado = "Completado"
        print(f"Pago {self.id_pago} procesado con éxito.")

    def emitir_recibo(self):
        return f"Recibo Pago {self.id_pago} - Monto: {self.monto} - Estado: {self.estado}"


# --- Aplicación de consola ---
def main():
    print("================================================")
    print("=== Sistema de Reservas de Canchas de Fútbol ===")
    print("================================================")

    nombreSocio = input("Ingresar su nombre: ")
    apellidoSocio = input("Ingresar su Apellido: ")
    correoSocio = nombreSocio + "." + apellidoSocio + "@mail.com"

    # 1. Crear socio
    socio = Socio(1, nombreSocio, apellidoSocio, correoSocio, "9549230", "Premium")
    print(f"Socio creado: {socio.nombre} {socio.apellido}")

    # 2. Crear servicio y calendario
    servicio = Servicio(1, "Alquiler Cancha", 50.0, "90 minutos")
    calendario = Calendario(1, "2026-06-15", "18:00", "19:30", "Cancha 1")

    # 3. Reservar cancha
    registro = socio.reservar_cancha(servicio, calendario)

    # 4. Procesar pago
    if registro:
        socio.pagar_servicio(servicio.precio, "Tarjeta de Crédito")

    print("=== Fin de Registro ===")
    print("")


if __name__ == "__main__":
    main()
