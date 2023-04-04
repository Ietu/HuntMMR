import customtkinter as tk
import os
import time
import xml.etree.ElementTree as ET

error = ""
mmrVal = ""

class HuntMMR:
    def __init__(self):
        self.window = tk.CTk()
        self.window.title("HuntMMR")
        self.window.geometry("450x400")
        self.window.configure(fg_color=('#1C1C1C'))
        self.window.resizable(False, False)

        self.error_text_label = tk.CTkLabel(self.window, text=f"{error}", text_color="red", font=("Helvetica", 20), fg_color=('#1C1C1C'))
        self.error_text_label.place(relx=0.5, rely=0.9, anchor='center')

        self.default_text_label = tk.CTkLabel(self.window, text=f"Current MMR: \n{mmrVal}", font=("Helvetica", 20), fg_color=('#1C1C1C'))
        self.default_text_label.place(relx=0.5, rely=0.08, anchor='center')

        self.mmr_label = tk.CTkLabel(self.window, text="", text_color="gold",font=("Helvetica", 40), fg_color=('#1C1C1C'))
        self.mmr_label.place(relx=0.5, rely=0.15, anchor='center')

        self.star_label = tk.CTkLabel(self.window, text="", text_color="gold", font=("Helvetica", 35), fg_color=('#1C1C1C'))
        self.star_label.place(relx=0.5, rely=0.26, anchor='center')

        self.get_mmr_button = tk.CTkButton(self.window, text="Get MMR!", font=("Helvetica", 40), fg_color=('#363636'), text_color=('white'), width=250, height=50, command=self.get_mmr_path)
        self.get_mmr_button.place(relx=0.5, rely=0.4, anchor='center')

        self.next_rank_label = tk.CTkLabel(self.window, text="", font=("Helvetica", 20), fg_color=('#1C1C1C'))
        self.next_rank_label.place(relx=0.5, rely=0.55, anchor='center')

        self.window.mainloop()
#
    def get_mmr_path(self):
        drives = [chr(i) + ":\\" for i in range(ord('A'), ord('Z') + 1)]
        path = "Steam\\steamapps\\common\\Hunt Showdown\\user\\profiles\\default\\attributes.xml"
        mmr_path = None

        for drive in drives:
            if os.path.exists(os.path.join(drive, path)):
                attributes_file = os.path.join(drive, path)
                with open(attributes_file, encoding='utf-8') as f:
                    content = f.read()
                    if "MissionBagPlayer_0_0_mmr" in content:
                        mmr_path = attributes_file
                        break

        if mmr_path is not None:
            mmrVal = get_mmr_from_file(mmr_path, self)
        else:
            self.error_text_label.configure(text="Could not find Hunt Showdown attributes.xml file!")

    def show_mmr(self, mmr):
        self.default_text_label.configure(text=f"Current elo: {mmr}")

def get_mmr_from_file(file_path, app):
    mmr = ""
    context = ET.iterparse(file_path, events=('start', 'end'))
    for event, elem in context:
        if event == 'start' and elem.tag == 'Attr' and elem.get('name') == 'MissionBagPlayer_0_0_mmr':
            mmr = elem.get('value')
            elem.clear()
            break
    show_mmr(mmr, app)

def show_mmr(mmr, app):
    app.mmr_label.configure(text=f"Loading...")
    app.window.update()
    time.sleep(1.5)
    temp = 1
    while temp <= int(mmr):
        app.mmr_label.configure(text=f"{temp}")
        app.window.update()
        temp += 1

    app.mmr_label.configure(text=f"{mmr}")
    get_stars(mmr, app)

def get_stars(mmr_str, app):
    mmr = int(mmr_str)
    time.sleep(0.5)
    if mmr < 2000:
        next_rank = 2000 - mmr
        app.star_label.configure(text=f"1 STARS!")
        app.next_rank_label.configure(text=f"Only {next_rank} MMR until next rank!")
    elif mmr < 2300:
        next_rank = 2300 - mmr
        app.star_label.configure(text=f"2 STARS!")
        app.next_rank_label.configure(text=f"Only {next_rank} MMR until next rank!")
    elif mmr < 2600:
        next_rank = 2600 - mmr
        app.star_label.configure(text=f"3 STARS!")
        app.next_rank_label.configure(text=f"Only {next_rank} MMR until next rank!")
    elif mmr < 2750:
        next_rank = 2750 - mmr
        app.star_label.configure(text=f"4 STARS!")
        app.next_rank_label.configure(text=f"Only {next_rank} MMR until next rank!")
    elif mmr < 3000:
        next_rank = 3000 - mmr
        app.star_label.configure(text=f"5 STARS!")
        app.next_rank_label.configure(text=f"Only {next_rank} MMR until next rank!")
    else:
        app.star_label.configure(text=f"6 STARS!")
        app.next_rank_label.configure(text=f"Nice!")

if __name__ == '__main__':
    app = HuntMMR()
