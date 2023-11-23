import tkinter as tk
from tkinter import scrolledtext
from tkcalendar import Calendar
import os
from tkinter import messagebox

class Naptar:
    def __init__(self, main_window):
        self.ablak = main_window
        self.ablak.title("Naptár")
        self.ablak.geometry("350x500")  # A naptár alkalmazás mérete

        # Fő ablak méretezése és középre igazítása
        window_width = 350
        window_height = 500
        screen_width = self.ablak.winfo_screenwidth()
        screen_height = self.ablak.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)
        self.ablak.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

        self.event_data = {}

        # Magának az alkalmazásnak az inicializálása és középre igazítása
        self.naptar = Calendar(main_window, selectmode="day")
        self.naptar.place(relx=0.5, rely=0.2, anchor="center")

        # Esemény beírása - szövegdoboz
        self.event_desc_msbox = tk.Text(main_window, height=5, width=31)
        self.event_desc_msbox.place(relx=0.5, rely=0.48, anchor="center")

        # Események megtekintése - gomb
        self.megtekintes_gomb = tk.Button(main_window, text="Események megtekintése(adott nap)", command=self.view_an_event)
        self.megtekintes_gomb.place(relx=0.5, rely=0.62, anchor="center")

        # Mentés - gomb
        self.mentes_gomb = tk.Button(main_window, text="Esemény mentése", command=self.save_event)
        self.mentes_gomb.place(relx=0.5, rely=0.68, anchor="center")

        # Törlés - gomb
        self.torles_gomb = tk.Button(main_window, text="Esemény törlése", command=self.delete_an_event)
        self.torles_gomb.place(relx=0.5, rely=0.74, anchor="center")

        # Összes esemény listázása - gomb
        self.osszes_gomb = tk.Button(main_window, text="Összes esemény listázása", command=self.list_all_events)
        self.osszes_gomb.place(relx=0.28, rely=0.84, anchor="center")

        # Összes esemény törlése - gomb
        self.osszes_torles_gomb = tk.Button(main_window, text="Összes esemény törlése", command=self.delete_all_events)
        self.osszes_torles_gomb.place(relx=0.72, rely=0.84, anchor="center")

        self.load_events()

    def save_event(self):
        selected_date = self.naptar.get_date()
        event_description = self.event_desc_msbox.get("1.0", "end-1c")
        if event_description:
            formatted_date = selected_date
            if formatted_date in self.event_data:
                self.event_data[formatted_date].append(event_description)
            else:
                self.event_data[formatted_date] = [event_description]
            with open("esemenyek.txt", mode="a") as file:
                file.write(f"{formatted_date} - {event_description}\n")
            self.show_info_with_timeout("Mentés", "Az esemény sikeresen elmentve a fájlba.")
        else:
            self.show_warning_with_timeout("Figyelem", "Az esemény leírása nem lehet üres a mentéshez.")
        self.event_desc_msbox.delete("1.0", tk.END)

    def delete_an_event(self):
        selected_date = self.naptar.get_date()
        formatted_date = selected_date
        if formatted_date in self.event_data:
            del self.event_data[formatted_date]
            with open("esemenyek.txt", "r") as file:
                lines = file.readlines()
            with open("esemenyek.txt", "w") as file:
                for line in lines:
                    if not line.startswith(formatted_date):
                        file.write(line)
            self.show_info_with_timeout("Törlés", "Az összes esemény törölve az adott napon.")
        else:
            self.show_warning_with_timeout("Nincs esemény", "Nincs elmentett esemény az adott napon.")

    def delete_all_events(self):
        answer = messagebox.askquestion("Törlés megerősítése", "Biztosan törölni szeretnéd az összes eseményt?")
        if answer == 'yes':
            with open("esemenyek.txt", "w") as file:
                file.write("")
            self.event_data = {}  # Opcionális -> az esemény adatok törlődnek a memóriából is
            self.show_info_with_timeout("Összes törölve", "Az összes esemény sikeresen törölve.")
        else:
            self.show_info_with_timeout("Művelet megszakítva", "Az összes esemény törlése megszakítva.")

    def load_events(self):
        file_path = "esemenyek.txt"
        if not os.path.exists(file_path): # Ha a fájl nem létezik, létrehozzuk
            with open(file_path, "w") as file:
                self.show_warning_with_timeout("Fájl nem létezett", "A fájl nem létezett, de létrehoztuk!")
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(" - ", 1)
                    if len(parts) == 2:
                        date, event = parts
                        if date in self.event_data:
                            self.event_data[date].append(event)
                        else:
                            self.event_data[date] = [event]
        except FileExistsError:
            self.show_warning_with_timeout("HIBA", "A fájlt valamiért nem lehet létrehozni")
            pass

    def view_an_event(self):
        selected_date = self.naptar.get_date()
        formatted_date = selected_date
        events = self.event_data.get(formatted_date, [])
        if events:
            esemenyek_ablak = tk.Toplevel(self.ablak)
            esemenyek_ablak.title(f"Események - {formatted_date}")
            esemenyek_ablak.geometry("400x400")

            x = self.ablak.winfo_x() + (self.ablak.winfo_width() / 2) - (400 / 2)
            y = self.ablak.winfo_y() + (self.ablak.winfo_height() / 2) - (400 / 2)
            esemenyek_ablak.geometry(f"400x400+{int(x)}+{int(y)}")

            esemenyek_szovegdoboz = scrolledtext.ScrolledText(esemenyek_ablak, height=10, width=30)
            event_text = "\n".join(events)
            if event_text:
                esemenyek_szovegdoboz.insert("1.0", event_text)
            else:
                esemenyek_szovegdoboz.insert("1.0", "Nincs elmentett esemény az adott napon.")
            esemenyek_szovegdoboz.pack()
        else:
            self.show_warning_with_timeout("Nincs esemény", "Nincs elmentett esemény az adott napon.")

    def list_all_events(self):
        file_path = "esemenyek.txt"
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
                all_events = "\n".join(lines)
                if all_events:
                    self.show_info_with_timeout("Összes esemény", all_events, wait_close=True)
                else:
                    self.show_warning_with_timeout("Nincs esemény", "Nincsenek elmentett események.")
        except FileNotFoundError:
            self.show_warning_with_timeout("HIBA", "A fájl nem található")

    def show_info_with_timeout(self, title, message, timeout=2500, wait_close=False):
        info_window = tk.Toplevel(self.ablak)
        info_window.title(title)
        info_window.geometry("300x300")
        x = self.ablak.winfo_x() + (self.ablak.winfo_width() / 2) - (300 / 2)
        y = self.ablak.winfo_y() + (self.ablak.winfo_height() / 2) - (300 / 2)
        info_window.geometry(f"300x300+{int(x)}+{int(y)}")
        tk.Label(info_window, text=message, wraplength=250).pack()
        if not wait_close:
            self.ablak.after(timeout, info_window.destroy)

    def show_warning_with_timeout(self, title, message, timeout=2500):
        warning_window = tk.Toplevel(self.ablak)
        warning_window.title(title)
        warning_window.geometry("300x300")
        x = self.ablak.winfo_x() + (self.ablak.winfo_width() / 2) - (300 / 2)
        y = self.ablak.winfo_y() + (self.ablak.winfo_height() / 2) - (300 / 2)
        warning_window.geometry(f"300x300+{int(x)}+{int(y)}")
        tk.Label(warning_window, text=message).pack()
        self.ablak.after(timeout, warning_window.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    alkalmazas = Naptar(root)
    root.mainloop()
