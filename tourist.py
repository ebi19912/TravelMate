class TourismSupportSystem:
    def __init__(self):
        self.flights = {}
        self.hotels = {}
        self.taxis = {}
        self.bookings = []

    def add_flight(self, origin, destination, date, price):
        if origin not in self.flights:
            self.flights[origin] = {}
        if destination not in self.flights[origin]:
            self.flights[origin][destination] = []
        self.flights[origin][destination].append((date, price))

    def add_hotel(self, city, name, price_per_night):
        if city not in self.hotels:
            self.hotels[city] = []
        self.hotels[city].append((name, price_per_night))

    def add_taxi(self, city, price_per_km):
        self.taxis[city] = price_per_km

    def search_flights(self, origin, destination):
        if origin in self.flights and destination in self.flights[origin]:
            return self.flights[origin][destination]
        else:
            return None

    def search_hotels(self, city):
        if city in self.hotels:
            return self.hotels[city]
        else:
            return None

    def book_flight(self, origin, destination, date, price):
        self.bookings.append(
            {
                "type": "flight",
                "origin": origin,
                "destination": destination,
                "date": date,
                "price": price,
            }
        )
        print(f"Flight from {origin} to {destination} on {date} booked successfully!")

    def book_hotel(self, city, hotel_name, price_per_night, num_nights):
        self.bookings.append(
            {
                "type": "hotel",
                "city": city,
                "hotel": hotel_name,
                "price_per_night": price_per_night,
                "num_nights": num_nights,
            }
        )
        print(
            f"Hotel {hotel_name} in {city} booked for {num_nights} nights successfully!"
        )

    def book_taxi(self, city, distance):
        if city in self.taxis:
            price = self.taxis[city] * distance
            self.bookings.append(
                {
                    "type": "taxi",
                    "city": city,
                    "distance": distance,
                    "price": price,
                }
            )
            print(
                f"Taxi booked in {city} for {distance} km. Total price: {price}"
            )
        else:
            print("Taxi service not available in this city.")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings yet.")
        else:
            print("Your bookings:")
            for booking in self.bookings:
                print(booking)

    def show_travel_plan(self, origin, destination, travel_date):
        print(f"Travel Plan from {origin} to {destination} on {travel_date}:")

        # Find flights
        flights = self.search_flights(origin, destination)
        if flights:
          print("\nAvailable Flights:")
          for date, price in flights:
            if date == travel_date:
              print(f"- Flight on {date}: Price = {price}")
        else:
          print("No flights found for this route.")

        # Find hotels
        hotels = self.search_hotels(destination)
        if hotels:
          print("\nAvailable Hotels:")
          for name, price_per_night in hotels:
            print(f"- {name}: Price per night = {price_per_night}")
        else:
          print("No hotels found in this city.")

    def run(self):
        # Sample Data
        self.add_flight("Tehran", "Mashhad", "2024-03-25", 150)
        self.add_flight("Tehran", "Mashhad", "2024-03-26", 140)
        self.add_flight("Tehran", "Shiraz", "2024-03-25", 120)

        self.add_hotel("Mashhad", "Hotel 1", 50)
        self.add_hotel("Mashhad", "Hotel 2", 70)
        self.add_hotel("Shiraz", "Hotel A", 60)

        self.add_taxi("Mashhad", 1.5)
        self.add_taxi("Shiraz", 1.2)

        while True:
            print("\nTourism Support System Menu:")
            print("1. Show Travel Plan")
            print("2. Book Flight")
            print("3. Book Hotel")
            print("4. Book Taxi")
            print("5. View Bookings")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                origin = input("Enter origin city: ")
                destination = input("Enter destination city: ")
                travel_date = input("Enter travel date (YYYY-MM-DD): ")
                self.show_travel_plan(origin, destination, travel_date)
            elif choice == "2":
                origin = input("Enter origin city: ")
                destination = input("Enter destination city: ")
                date = input("Enter date (YYYY-MM-DD): ")
                flights = self.search_flights(origin, destination)
                if flights:
                  found = False
                  for f_date, f_price in flights:
                    if f_date == date:
                      self.book_flight(origin, destination, date, f_price)
                      found = True
                      break
                  if not found:
                    print("No flights found on this date.")

                else:
                    print("No flights found for this route.")
            elif choice == "3":
                city = input("Enter city: ")
                hotels = self.search_hotels(city)
                if hotels:
                    hotel_name = input("Enter hotel name: ")
                    num_nights = int(input("Enter number of nights: "))
                    found = False
                    for h_name, h_price in hotels:
                      if h_name == hotel_name:
                        self.book_hotel(city, hotel_name, h_price, num_nights)
                        found = True
                        break
                    if not found:
                      print("No hotel found with this name.")
                else:
                    print("No hotels found in this city.")
            elif choice == "4":
                city = input("Enter city: ")
                distance = float(input("Enter distance in km: "))
                self.book_taxi(city, distance)
            elif choice == "5":
                self.view_bookings()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    system = TourismSupportSystem()
    system.run()