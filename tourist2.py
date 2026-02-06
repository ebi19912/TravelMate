import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import locale

try:
    locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, "fa_IR") 
    except locale.Error:
      print("Warning: Could not set locale to Persian. Displaying numbers might not be correct.")
      pass


class TourismSupportSystem:
    def __init__(self):
        self.flights = {}
        self.hotels = {}
        self.taxis = {}
        self.bookings = []
        self.window = tk.Tk()
        self.window.title("سامانه پشتیبانی گردشگری")
        self.window.geometry("800x600")
       
        self.create_widgets()
        self.add_sample_data()
        

    def add_sample_data(self):
        self.add_flight("تهران", "مشهد", "2024-03-25", 150)
        self.add_flight("تهران", "مشهد", "2024-03-26", 140)
        self.add_flight("تهران", "شیراز", "2024-03-25", 120)

        self.add_hotel("مشهد", "هتل 1", 50)
        self.add_hotel("مشهد", "هتل 2", 70)
        self.add_hotel("شیراز", "هتل A", 60)

        self.add_taxi("مشهد", 1.5)
        self.add_taxi("شیراز", 1.2)

    def create_widgets(self):
        # Main Menu Frame
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(pady=20)

        # Buttons
        ttk.Button(
            self.menu_frame,
            text="نمایش برنامه سفر",
            command=self.show_travel_plan_window,
            width=20
        ).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(
            self.menu_frame,
            text="رزرو بلیط هواپیما",
            command=self.show_book_flight_window,
            width=20
        ).grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(
            self.menu_frame,
            text="رزرو هتل",
            command=self.show_book_hotel_window,
            width=20
        ).grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(
            self.menu_frame,
            text="رزرو تاکسی",
            command=self.show_book_taxi_window,
            width=20
        ).grid(row=3, column=0, padx=10, pady=10)
        ttk.Button(
            self.menu_frame,
            text="مشاهده رزروها",
            command=self.view_bookings,
            width=20
        ).grid(row=4, column=0, padx=10, pady=10)
        ttk.Button(
            self.menu_frame, text="خروج", command=self.window.quit, width=20
        ).grid(row=5, column=0, padx=10, pady=10)

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
        messagebox.showinfo(
            "موفقیت",
            f"پرواز از {origin} به {destination} در تاریخ {date} با موفقیت رزرو شد!",
        )

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
        messagebox.showinfo(
            "موفقیت",
            f"هتل {hotel_name} در {city} به مدت {num_nights} شب با موفقیت رزرو شد!",
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
            messagebox.showinfo(
                "موفقیت",
                f"تاکسی در {city} به مسافت {distance} کیلومتر رزرو شد. هزینه کل: {price}",
            )
        else:
            messagebox.showerror("خطا", "سرویس تاکسی در این شهر موجود نیست.")

    def view_bookings(self):
        if not self.bookings:
            messagebox.showinfo("رزروها", "هیچ رزرروی تاکنون انجام نشده است.")
        else:
            bookings_window = tk.Toplevel(self.window)
            bookings_window.title("مشاهده رزروها")

            bookings_text = ""
            for booking in self.bookings:
                bookings_text += str(booking) + "\n"

            tk.Label(bookings_window, text=bookings_text, justify="right").pack(
                padx=20, pady=20
            )
      
    def format_persian_number(self, num):
      try:
        return locale.format_string("%d", num, grouping=True)
      except:
        return str(num)
        
    def show_travel_plan_window(self):
        travel_plan_window = tk.Toplevel(self.window)
        travel_plan_window.title("نمایش برنامه سفر")

        # Labels and Entry fields
        tk.Label(travel_plan_window, text="مبدا:").grid(row=0, column=1, padx=10, pady=10, sticky="e")
        origin_entry = tk.Entry(travel_plan_window)
        origin_entry.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(travel_plan_window, text="مقصد:").grid(row=1, column=1, padx=10, pady=10, sticky="e")
        destination_entry = tk.Entry(travel_plan_window)
        destination_entry.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(travel_plan_window, text="تاریخ سفر (YYYY-MM-DD):").grid(
            row=2, column=1, padx=10, pady=10, sticky="e"
        )
        travel_date_entry = tk.Entry(travel_plan_window)
        travel_date_entry.grid(row=2, column=0, padx=10, pady=10)

        def show_plan():
          
            origin = origin_entry.get()
            destination = destination_entry.get()
            travel_date = travel_date_entry.get()

            plan_text = f"برنامه سفر از {origin} به {destination} در تاریخ {travel_date}:\n\n"

            # Find flights
            flights = self.search_flights(origin, destination)
            if flights:
                plan_text += "پروازهای موجود:\n"
                for date, price in flights:
                    if date == travel_date:
                        plan_text += f"- پرواز در تاریخ {date}: قیمت = {self.format_persian_number(price)}\n"
            else:
                plan_text += "هیچ پروازی برای این مسیر پیدا نشد.\n"

            # Find hotels
            hotels = self.search_hotels(destination)
            if hotels:
                plan_text += "\nهتل‌های موجود:\n"
                for name, price_per_night in hotels:
                    plan_text += (
                        f"- {name}: قیمت هر شب = {self.format_persian_number(price_per_night)}\n"
                    )
            else:
                plan_text += "هیچ هتلی در این شهر پیدا نشد.\n"

            # Display in a new window
            result_window = tk.Toplevel(travel_plan_window)
            result_window.title("برنامه سفر")
            tk.Label(result_window, text=plan_text, justify="right").pack(
                padx=20, pady=20
            )

        # Button
        ttk.Button(
            travel_plan_window, text="نمایش برنامه", command=show_plan, width=20
        ).grid(row=3, column=0, columnspan=2, pady=20)

    def show_book_flight_window(self):
        book_flight_window = tk.Toplevel(self.window)
        book_flight_window.title("رزرو بلیط هواپیما")

        # Labels and Entry fields
        tk.Label(book_flight_window, text="مبدا:").grid(row=0, column=1, padx=10, pady=10, sticky="e")
        origin_entry = tk.Entry(book_flight_window)
        origin_entry.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(book_flight_window, text="مقصد:").grid(row=1, column=1, padx=10, pady=10, sticky="e")
        destination_entry = tk.Entry(book_flight_window)
        destination_entry.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(book_flight_window, text="تاریخ (YYYY-MM-DD):").grid(
            row=2, column=1, padx=10, pady=10, sticky="e"
        )
        date_entry = tk.Entry(book_flight_window)
        date_entry.grid(row=2, column=0, padx=10, pady=10)

        def book_selected_flight():
            origin = origin_entry.get()
            destination = destination_entry.get()
            date = date_entry.get()

            flights = self.search_flights(origin, destination)
            if flights:
              found = False
              for f_date, f_price in flights:
                if f_date == date:
                  self.book_flight(origin, destination, date, f_price)
                  found = True
                  break
              if not found:
                messagebox.showerror("خطا", "پروازی در این تاریخ یافت نشد")
            else:
              messagebox.showerror("خطا", "پروازی برای این مسیر یافت نشد")

        # Button
        ttk.Button(
            book_flight_window, text="رزرو پرواز", command=book_selected_flight, width=20
        ).grid(row=3, column=0, columnspan=2, pady=20)

    def show_book_hotel_window(self):
        book_hotel_window = tk.Toplevel(self.window)
        book_hotel_window.title("رزرو هتل")

        # Labels and Entry fields
        tk.Label(book_hotel_window, text="شهر:").grid(row=0, column=1, padx=10, pady=10, sticky="e")
        city_entry = tk.Entry(book_hotel_window)
        city_entry.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(book_hotel_window, text="نام هتل:").grid(row=1, column=1, padx=10, pady=10, sticky="e")
        hotel_name_entry = tk.Entry(book_hotel_window)
        hotel_name_entry.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(book_hotel_window, text="تعداد شب‌ها:").grid(
            row=2, column=1, padx=10, pady=10, sticky="e"
        )
        num_nights_entry = tk.Entry(book_hotel_window)
        num_nights_entry.grid(row=2, column=0, padx=10, pady=10)

        def book_selected_hotel():
            city = city_entry.get()
            hotel_name = hotel_name_entry.get()
            try:
              num_nights = int(num_nights_entry.get())
            except ValueError:
              messagebox.showerror("خطا", "تعداد شب ها باید عدد باشد")
              return
            
            hotels = self.search_hotels(city)
            if hotels:
              found = False
              for h_name, h_price in hotels:
                if h_name == hotel_name:
                  self.book_hotel(city, hotel_name, h_price, num_nights)
                  found = True
                  break
              if not found:
                messagebox.showerror("خطا", "هتلی با این نام یافت نشد")
            else:
              messagebox.showerror("خطا", "هتلی در این شهر یافت نشد")

        # Button
        ttk.Button(
            book_hotel_window, text="رزرو هتل", command=book_selected_hotel, width=20
        ).grid(row=3, column=0, columnspan=2, pady=20)

    def show_book_taxi_window(self):
        book_taxi_window = tk.Toplevel(self.window)
        book_taxi_window.title("رزرو تاکسی")

        # Labels and Entry fields
        tk.Label(book_taxi_window, text="شهر:").grid(row=0, column=1, padx=10, pady=10, sticky="e")
        city_entry = tk.Entry(book_taxi_window)
        city_entry.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(book_taxi_window, text="مسافت (کیلومتر):").grid(
            row=1, column=1, padx=10, pady=10, sticky="e"
        )
        distance_entry = tk.Entry(book_taxi_window)
        distance_entry.grid(row=1, column=0, padx=10, pady=10)

        def book_selected_taxi():
            city = city_entry.get()
            try:
              distance = float(distance_entry.get())
            except ValueError:
              messagebox.showerror("خطا", "مسافت باید عدد باشد")
              return

            self.book_taxi(city, distance)

        # Button
        ttk.Button(
            book_taxi_window, text="رزرو تاکسی", command=book_selected_taxi, width=20
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    system = TourismSupportSystem()
    system.run()