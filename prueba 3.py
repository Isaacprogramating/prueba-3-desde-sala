import json

class SurExplora:
    def __init__(self):
        self.reservas = []
        self.destinos = ["Torres del Paine", "Carretera Austral", "Chiloé"]

    def registrar_reserva(self):
        nombre = input("Nombre y apellido del cliente: ").strip()
        ciudad = input("Ciudad de origen: ").strip()
        if not nombre or not ciudad:
            print("El nombre y la ciudad no pueden estar vacíos.")
            return
        for i, destino in enumerate(self.destinos, 1):
            print(f"{i}. {destino}")
        try:
            tour_index = int(input("Ingrese el número del tour: ")) - 1
            if tour_index not in range(len(self.destinos)):
                raise ValueError
        except ValueError:
            print("Selección inválida.")
            return
        try:
            cantidad_personas = int(input("Cantidad de personas: ").strip())
        except ValueError:
            print("La cantidad de personas debe ser un número.")
            return

        self.reservas.append({
            "Cliente": nombre,
            "Ciudad": ciudad,
            "Tour": self.destinos[tour_index],
            "Cantidad de Personas": cantidad_personas
        })
        print("Reserva registrada con éxito.")

    def listar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas.")
            return
        for reserva in self.reservas:
            print(f"{reserva['Cliente']} - {reserva['Ciudad']} - {reserva['Tour']} - {reserva['Cantidad de Personas']} personas")

    def imprimir_detalle_por_destino(self):
        for i, destino in enumerate(self.destinos, 1):
            print(f"{i}. {destino}")
        try:
            tour_index = int(input("Ingrese el número del destino: ")) - 1
            if tour_index not in range(len(self.destinos)):
                raise ValueError
        except ValueError:
            print("Selección inválida.")
            return

        destino_seleccionado = self.destinos[tour_index]
        reservas_filtradas = [r for r in self.reservas if r["Tour"] == destino_seleccionado]

        if not reservas_filtradas:
            print(f"No hay reservas para {destino_seleccionado}.")
            return

        archivo_txt = f"{destino_seleccionado.replace(' ', '_')}_reservas.txt"
        archivo_json = f"{destino_seleccionado.replace(' ', '_')}_reservas.json"

        with open(archivo_txt, 'w') as file_txt:
            for reserva in reservas_filtradas:
                file_txt.write(f"{reserva['Cliente']} - {reserva['Ciudad']} - {reserva['Tour']} - {reserva['Cantidad de Personas']} personas\n")
        
        with open(archivo_json, 'w') as file_json:
            json.dump(reservas_filtradas, file_json, indent=4)

        print(f"Detalles guardados en {archivo_txt} y {archivo_json}.")

    def run(self):
        while True:
            print("\n1. Registrar Reserva\n2. Listar Todas las Reservas\n3. Imprimir Detalle de Reservas por Destino\n4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.registrar_reserva()
            elif opcion == "2":
                self.listar_reservas()
            elif opcion == "3":
                self.imprimir_detalle_por_destino()
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    app = SurExplora()
    app.run()