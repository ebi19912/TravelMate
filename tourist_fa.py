import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import locale

# تنظیمات مربوط به زبان فارسی
try:
    locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, "fa_IR")
    except locale.Error:
        print("هشدار: تنظیمات زبان فارسی اعمال نشد. ممکن است اعداد به درستی نمایش داده نشوند.")
        pass


class TourismSupportSystem:
    def __init__(self):
        # دیکشنری‌های اطلاعات
        self.flights = {}  # اطلاعات پروازها
        self.hotels = {}  # اطلاعات هتل‌ها
        self.taxis = {}  # اطلاعات تاکسی‌ها
        self.bookings = []  # اطلاعات رزروها

        # ایجاد پنجره اصلی
        self.window = tk.Tk()
        self.window.title("سامانه پشتیبانی گردشگری")
        self.window.geometry("800x600")

        # ایجاد ویجت‌ها
        self.create_widgets()
        # اضافه کردن اطلاعات نمونه
        self.add_sample_data()

    def add_sample_data(self):
        # اطلاعات نمونه پرواز
        self.add_flight("تهران", "مشهد", "2024-03-25", 150)
        self.add_flight("تهران", "مشهد", "2024-03-26", 140)
        self.add_flight("تهران", "شیراز", "2024-03-25", 120)
        self.add_flight("مشهد", "تهران", "2024-03-30", 160)

        # اطلاعات نمونه هتل
        self.add_hotel("مشهد", "هتل 1", 50)
        self.add_hotel("مشهد", "هتل 2", 70)
        self.add_hotel("شیراز", "هتل A", 60)
        self.add_hotel("تهران", "هتل پارس", 90)

        # اطلاعات نمونه تاکسی
        self.add_taxi("مشهد", 1.5)
        self.add_taxi("شیراز", 1.2)
        self.add_taxi("تهران", 2.0)

    def create_widgets(self):
        # فریم منوی اصلی
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(pady=20)

        # دکمه‌های منوی اصلی
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

    # اضافه کردن اطلاعات پرواز
    def add_flight(self, origin, destination, date, price):
        if origin not in self.flights:
            self.flights[origin] = {}
        if destination not in self.flights[origin]:
            self.flights[origin][destination] = []
        self.flights[origin][destination].append((date, price))

    # اضافه کردن اطلاعات هتل
    def add_hotel(self, city, name, price_per_night):
        if city not in self.hotels:
            self.hotels[city] = []
        self.hotels[city].append((name, price_per_night))

    # اضافه کردن اطلاعات تاکسی
    def add_taxi(self, city, price_per_km):
        self.taxis[city] = price_per_km

    # جستجوی پرواز
    def search_flights(self, origin, destination):
        if origin in self.flights and destination in self.flights[origin]:
            return self.flights[origin][destination]
        else:
            return None

    # جستجوی هتل
    def search_hotels(self, city):
        if city in self.hotels:
            return self.hotels[city]
        else:
            return None

    # رزرو پرواز
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

    # رزرو هتل
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

    # رزرو تاکسی
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

    # نمایش رزروها
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

    # تبدیل اعداد به فرمت فارسی
    def format_persian_number(self, num):
        try:
            return locale.format_string("%d", num, grouping=True)
        except:
            return str(num)

    # نمایش پنجره برنامه سفر
    def show_travel_plan_window(self):
        travel_plan_window = tk.Toplevel(self.window)
        travel_plan_window.title("نمایش برنامه سفر")

        # مبدا
        tk.Label(travel_plan_window, text="مبدا:").grid(
            row=0, column=1, padx=10, pady=10, sticky="e"
        )
        origin_var = tk.StringVar(travel_plan_window)
        origin_options = list(self.flights.keys())
        origin_dropdown = ttk.Combobox(
            travel_plan_window, textvariable=origin_var, values=origin_options, state="readonly"
        )
        origin_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # مقصد
        tk.Label(travel_plan_window, text="مقصد:").grid(
            row=1, column=1, padx=10, pady=10, sticky="e"
        )
        destination_var = tk.StringVar(travel_plan_window)
        destination_dropdown = ttk.Combobox(
            travel_plan_window, textvariable=destination_var, values=[], state="readonly"
        ) # مقادیر به صورت پویا آپدیت خواهند شد
        destination_dropdown.grid(row=1, column=0, padx=10, pady=10)

        # تابع برای آپدیت مقاصد بر اساس مبدا
        def update_destinations(*args):
            origin = origin_var.get()
            if origin:
                destination_options = list(self.flights[origin].keys())
                destination_dropdown["values"] = destination_options
            else:
                destination_dropdown["values"] = []

        origin_var.trace("w", update_destinations)

        # تاریخ سفر
        tk.Label(travel_plan_window, text="تاریخ سفر:").grid(
            row=2, column=1, padx=10, pady=10, sticky="e"
        )
        travel_date_var = tk.StringVar(travel_plan_window)
        travel_date_options = []  # بر اساس مبدا و مقصد آپدیت خواهد شد
        travel_date_dropdown = ttk.Combobox(
            travel_plan_window, textvariable=travel_date_var, values=[], state="readonly"
        )
        travel_date_dropdown.grid(row=2, column=0, padx=10, pady=10)

        # تابع برای آپدیت تاریخ‌ها
        def update_dates(*args):
            origin = origin_var.get()
            destination = destination_var.get()

            if origin and destination:
                dates = [date for date, price in self.search_flights(origin, destination)]
                travel_date_dropdown["values"] = dates
            else:
                travel_date_dropdown["values"] = []

        destination_var.trace("w", update_dates)

        # تابع نمایش برنامه سفر
        def show_plan():
            origin = origin_var.get()
            destination = destination_var.get()
            travel_date = travel_date_var.get()

            # بررسی خالی نبودن فیلدها
            if not all([origin, destination, travel_date]):
                messagebox.showerror("خطا", "لطفاً مبدا، مقصد و تاریخ سفر را انتخاب کنید.")
                return

            plan_text = f"برنامه سفر از {origin} به {destination} در تاریخ {travel_date}:\n\n"

            # جستجوی پروازها
            flights = self.search_flights(origin, destination)
            if flights:
                plan_text += "پروازهای موجود:\n"
                for date, price in flights:
                    if date == travel_date:
                        plan_text += f"- پرواز در تاریخ {date}: قیمت = {self.format_persian_number(price)}\n"
            else:
                plan_text += "هیچ پروازی برای این مسیر پیدا نشد.\n"

            # جستجوی هتل‌ها
            hotels = self.search_hotels(destination)
            if hotels:
                plan_text += "\nهتل‌های موجود:\n"
                for name, price_per_night in hotels:
                    plan_text += (
                        f"- {name}: قیمت هر شب = {self.format_persian_number(price_per_night)}\n"
                    )
            else:
                plan_text += "هیچ هتلی در این شهر پیدا نشد.\n"

            # نمایش در پنجره جدید
            result_window = tk.Toplevel(travel_plan_window)
            result_window.title("برنامه سفر")
            tk.Label(result_window, text=plan_text, justify="right").pack(
                padx=20, pady=20
            )

        # دکمه نمایش برنامه
        ttk.Button(
            travel_plan_window, text="نمایش برنامه", command=show_plan, width=20
        ).grid(row=3, column=0, columnspan=2, pady=20)

    # نمایش پنجره رزرو پرواز
    def show_book_flight_window(self):
        book_flight_window = tk.Toplevel(self.window)
        book_flight_window.title("رزرو بلیط هواپیما")

        # مبدا
        tk.Label(book_flight_window, text="مبدا:").grid(
            row=0, column=1, padx=10, pady=10, sticky="e"
        )
        origin_var = tk.StringVar(book_flight_window)
        origin_options = list(self.flights.keys())
        origin_dropdown = ttk.Combobox(
            book_flight_window, textvariable=origin_var, values=origin_options, state="readonly"
        )
        origin_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # مقصد
        tk.Label(book_flight_window, text="مقصد:").grid(
            row=1, column=1, padx=10, pady=10, sticky="e"
        )
        destination_var = tk.StringVar(book_flight_window)
        destination_dropdown = ttk.Combobox(
            book_flight_window, textvariable=destination_var, values=[], state="readonly"
        )
        destination_dropdown.grid(row=1, column=0, padx=10, pady=10)

        # آپدیت مقصدها بر اساس مبدا
        def update_destinations(*args):
            origin = origin_var.get()
            if origin:
                destination_options = list(self.flights[origin].keys())
                destination_dropdown["values"] = destination_options
            else:
                destination_dropdown["values"] = []

        origin_var.trace("w", update_destinations)

        # تاریخ
        tk.Label(book_flight_window, text="تاریخ:").grid(
            row=2, column=1, padx=10, pady=10, sticky="e"
        )
        date_var = tk.StringVar(book_flight_window)
        date_dropdown = ttk.Combobox(
            book_flight_window, textvariable=date_var, values=[], state="readonly"
        )
        date_dropdown.grid(row=2, column=0, padx=10, pady=10)

        # آپدیت تاریخ‌ها
        def update_dates(*args):
            origin = origin_var.get()
            destination = destination_var.get()

            if origin and destination:
                dates = [date for date, price in self.search_flights(origin, destination)]
                date_dropdown["values"] = dates
            else:
                date_dropdown["values"] = []

        destination_var.trace("w", update_dates)

        # تابع رزرو پرواز
        def book_selected_flight():
            origin = origin_var.get()
            destination = destination_var.get()
            date = date_var.get()

            # بررسی خالی نبودن فیلدها
            if not all([origin, destination, date]):
                messagebox.showerror("خطا", "لطفاً مبدا، مقصد و تاریخ را انتخاب کنید.")
                return

            flights = self.search_flights(origin, destination)
            if flights:
                for f_date, f_price in flights:
                    if f_date == date:
                        self.book_flight(origin, destination, date, f_price)
                        return
                messagebox.showerror("خطا", "پروازی در این تاریخ یافت نشد.")
            else:
                messagebox.showerror("خطا", "پروازی برای این مسیر یافت نشد.")

        # دکمه رزرو پرواز
        ttk.Button(
            book_flight_window, text="رزرو پرواز", command=book_selected_flight, width=20
        ).grid(row=3, column=0, columnspan=2, pady=20)

# نمایش پنجره رزرو هتل
    def show_book_hotel_window(self):
        book_hotel_window = tk.Toplevel(self.window)
        book_hotel_window.title("رزرو هتل")

        # شهر
        tk.Label(book_hotel_window, text="شهر:").grid(
            row=0, column=1, padx=10, pady=10, sticky="e"
        )
        city_var = tk.StringVar(book_hotel_window)
        city_options = list(self.hotels.keys())
        city_dropdown = ttk.Combobox(
            book_hotel_window, textvariable=city_var, values=city_options, state="readonly"
        )
        city_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # نام هتل
        tk.Label(book_hotel_window, text="نام هتل:").grid(
            row=1, column=1, padx=10, pady=10, sticky="e"
        )
        hotel_name_var = tk.StringVar(book_hotel_window)
        hotel_name_dropdown = ttk.Combobox(
            book_hotel_window, textvariable=hotel_name_var, values=[], state="readonly"
        )
        hotel_name_dropdown.grid(row=1, column=0, padx=10, pady=10)

        # آپدیت نام‌های هتل بر اساس شهر
        def update_hotel_names(*args):
            city = city_var.get()
            if city:
                hotel_names = [name for name, price in self.search_hotels(city)]
                hotel_name_dropdown["values"] = hotel_names
            else:
                hotel_name_dropdown["values"] = []

        city_var.trace("w", update_hotel_names)

        # تعداد شب‌ها
        tk.Label(book_hotel_window, text="تعداد شب‌ها:").grid(
            row=2, column=1, padx=10, pady=10, sticky="e"
        )
        num_nights_var = tk.IntVar(book_hotel_window, value=1)  # پیش‌فرض: 1 شب
        num_nights_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # می‌توانید محدوده را تغییر دهید
        num_nights_dropdown = ttk.Combobox(
            book_hotel_window,
            textvariable=num_nights_var,
            values=num_nights_options,
            state="readonly",
        )
        num_nights_dropdown.grid(row=2, column=0, padx=10, pady=10)

        # تابع رزرو هتل
        def book_selected_hotel():
            city = city_var.get()
            hotel_name = hotel_name_var.get()
            num_nights = num_nights_var.get()

            # بررسی خالی نبودن فیلدها
            if not all([city, hotel_name, num_nights]):
                messagebox.showerror("خطا", "لطفاً شهر، نام هتل و تعداد شب‌ها را انتخاب کنید.")
                return

            hotels = self.search_hotels(city)
            if hotels:
                for h_name, h_price in hotels:
                    if h_name == hotel_name:
                        self.book_hotel(city, hotel_name, h_price, num_nights)
                        return
                messagebox.showerror("خطا", "هتلی با این نام در این شهر یافت نشد.")
            else:
                messagebox.showerror("خطا", "هتلی در این شهر یافت نشد.")

        # دکمه رزرو هتل
        ttk.Button(
            book_hotel_window, text="رزرو هتل", command=book_selected_hotel, width=20
        ).grid(row=3, column=0, columnspan=2, pady=20)

    # نمایش پنجره رزرو تاکسی
    def show_book_taxi_window(self):
        book_taxi_window = tk.Toplevel(self.window)
        book_taxi_window.title("رزرو تاکسی")

        # شهر
        tk.Label(book_taxi_window, text="شهر:").grid(
            row=0, column=1, padx=10, pady=10, sticky="e"
        )
        city_var = tk.StringVar(book_taxi_window)
        city_options = list(self.taxis.keys())
        city_dropdown = ttk.Combobox(
            book_taxi_window, textvariable=city_var, values=city_options, state="readonly"
        )
        city_dropdown.grid(row=0, column=0, padx=10, pady=10)

        # مسافت
        tk.Label(book_taxi_window, text="مسافت (کیلومتر):").grid(
            row=1, column=1, padx=10, pady=10, sticky="e"
        )
        distance_var = tk.DoubleVar(book_taxi_window, value=1.0) # پیش‌فرض: 1 کیلومتر
        distance_options = [1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 20.0] # مثال
        distance_dropdown = ttk.Combobox(
            book_taxi_window,
            textvariable=distance_var,
            values=distance_options,
            state="readonly"
        )
        distance_dropdown.grid(row=1, column=0, padx=10, pady=10)

        # تابع رزرو تاکسی
        def book_selected_taxi():
            city = city_var.get()
            distance = distance_var.get()

            # بررسی خالی نبودن فیلدها
            if not all([city, distance]):
                messagebox.showerror("خطا", "لطفاً شهر و مسافت را انتخاب کنید.")
                return

            self.book_taxi(city, distance)

        # دکمه رزرو تاکسی
        ttk.Button(
            book_taxi_window, text="رزرو تاکسی", command=book_selected_taxi, width=20
        ).grid(row=2, column=0, columnspan=2, pady=20)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    system = TourismSupportSystem()
    system.run()