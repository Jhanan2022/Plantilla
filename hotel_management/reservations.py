from collections import defaultdict
from datetime import datetime

class Reservation:
    def __init__(self, customer_name: str, reservation_id: int, check_in_date: str, check_out_date: str, number_of_guests: int, room_number: int):
        self.customer_name = customer_name
        self.reservation_id = reservation_id
        self.check_in_date = datetime.strptime(check_in_date, "%d-%m-%Y") #usamos strptime para convertir la fecha en un objeto datetime con formato especificado (dd-mm-yyyy)
        self.check_out_date = datetime.strptime(check_out_date, "%d-%m-%Y")
        self.number_of_guests = number_of_guests
        self.room_number = room_number
        self.status = "active" #puede ser "active", "canceled" o "completed"

class ReservationSystem:
    def __init__(self):
        self.reservations = defaultdict(dict)
    
    def add_reservation(self, reservation: Reservation):
        if reservation.reservation_id in self.reservations:
            print("La reserva ya existe")
            return
        self.reservations[reservation.reservation_id] = {**reservation.__dict__}
        print(f"Reserva {reservation.reservation_id} creada exitosamente para {reservation.customer_name}.")
        return True

    def cancel_reservation(self, reservation_id):
        if reservation_id in self.reservations and self.reservations[reservation_id]["status"] == "active":
            self.reservations[reservation_id]["status"] = "canceled"
            print(f"Reserva {reservation_id} cancelada exitosamente")
        else:
            print(f"Reserva {reservation_id} no encontrada.")

if __name__ == "__main__":
    reservation_1 = Reservation("Alice", 1, "03-12-2024", "07-12-2024", 4, 1)
    reservation_mngmt = ReservationSystem()
    reservation_mngmt.add_reservation(reservation_1)
    reservation_mngmt.add_reservation(reservation_1) #comprobamos que no se añada nuevamente una reserva con el mismo ID
    reservation_mngmt.cancel_reservation(1)

