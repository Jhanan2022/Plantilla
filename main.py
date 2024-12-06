import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    # Inicializar sistemas
    customer_mgmt = CustomerManagement()
    room_mngmt = RoomManagement()
    reservation_mngmt = ReservationSystem()

    # Crear habitaciones
    room1 = Room(101, "Single", 100, {"TV": True, "WiFi": True, "AirConditioning": True})
    room2 = Room(102, "Double", 200, {"TV": True, "WiFi": True, "AirConditioning": True})
    room_mngmt.add_room(room1)
    room_mngmt.add_room(room2)

    # Agregar clientes
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")
    customer_mgmt.add_customer(customer1)
    customer_mgmt.add_customer(customer2)

    # Verificar disponibilidad de habitaciones

    # Crear reservas
    reservation_1 = Reservation("Alice", 1, datetime.now().strftime("%d-%m-%Y"), datetime.now().strftime("%d-%m-%Y"), 4, 101)
    reservation_2 = Reservation("Bob", 2, datetime.now().strftime("%d-%m-%Y"), datetime.now().strftime("%d-%m-%Y"), 2, 102)

    # Verificar disponibilidad de habitaciones
    if room_mngmt.check_availability(reservation_2.room_number):
        reservation_mngmt.add_reservation(reservation_1)
        room_mngmt.rooms[reservation_1.room_number]["room_status"] = "Deactivated"

        # Procesar pago asincrónicamente
        await process_payment(customer1.customer_name, room_mngmt.rooms[reservation_1.room_number]["room_price"])

    # Verificar disponibilidad de habitaciones
    if room_mngmt.check_availability(reservation_2.room_number):
        reservation_mngmt.add_reservation(reservation_2)
        room_mngmt.rooms[reservation_2.room_number]["room_status"] = "Deactivated"

        # Procesar pago asincrónicamente
        await process_payment(customer2.customer_name, room_mngmt.rooms[reservation_2.room_number]["room_price"])

    # Cancelar reservas
    reservation_mngmt.cancel_reservation(1)
    #reservation_mngmt.cancel_reservation(2)

if __name__ == "__main__":
    asyncio.run(main())

