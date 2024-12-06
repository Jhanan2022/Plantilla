from collections import defaultdict

class Room:
    def __init__(self, room_number: int, room_type: str, room_price: float, room_services: dict):
        self.room_number = room_number
        self.room_type = room_type
        self.room_price = room_price
        self.room_services = room_services
        self.room_status = "Active" #puede ser "Active", "Deactivated"

class RoomManagement:
    def __init__(self):
        self.rooms = defaultdict(dict)

    def add_room(self, room: Room):
        self.services = defaultdict(dict)
        self.services = {**room.room_services}
        if not room.room_number in self.rooms:
            self.rooms[room.room_number] = {**room.__dict__} #usamos ** para desempaquetar el objeto room en un diccionario con los atributos de la clase Room
            self.rooms[room.room_number]["room_services"] = self.services #añadimos el diccionario de servicios a la habitación
            print(f"Habitación {room.room_number} creada exitosamente.")
        else:
            print("La habitación ya existe")
            return

    def check_availability(self, room_number):
        if room_number in self.rooms and self.rooms[room_number]["room_status"] == "Active":
            print(f"La habitación {room_number} está disponible")
            return True
        print(f"La habitación {room_number} no está disponible")
        return False

if __name__ == "__main__":
    room1 = Room(1, "Single", 100, {"TV": True, "WiFi": True, "AirConditioning": True})
    room_mngmt = RoomManagement()
    room_mngmt.add_room(room1)
    room_mngmt.add_room(room1) #comprobamos que no se añada nuevamente una habitación con el mismo número