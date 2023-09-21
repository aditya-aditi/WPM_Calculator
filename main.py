# import tkinter as tk
import customtkinter as ctk
import random
import time


time_start = 0
# Event Handlers
def start_writing():
    global time_start
    txt_write_para.configure(state="normal")
    time_start = time.time()


def generate_para():
    paragraphs = [
        "The sun dipped below the horizon, painting the sky in hues of orange and pink. As darkness crept in, the stars emerged, sprinkling the night canvas with their shimmering light. A gentle breeze rustled the leaves, and the world seemed to exhale as the day came to a close.",
        "The old bookstore stood with its weathered facade, inviting passersby with the aroma of old paper and ink. Shelves upon shelves of books lined the walls, each one telling a different story. It was a sanctuary for book lovers, a place where time seemed to slow down as they immersed themselves in the worlds created by words.",
        "The little girl giggled as she chased after the butterflies, her laughter echoing through the meadow. The butterflies flitted around her, dancing in the sunlight. Her eyes sparkled with wonder as she tried to catch one, but they always slipped through her tiny fingers, leaving her in fits of laughter.",
        "The rain poured relentlessly, drumming on the roof and windows. Inside, a cozy fireplace crackled, casting a warm glow over the room. The sound of raindrops created a soothing melody, and the scent of wet earth filled the air. It was a perfect day to stay indoors with a good book and a cup of hot cocoa.",
        "The old oak tree stood tall and proud, its gnarlaed branches reaching toward the sky. It had witnessed generations pass by, and its bark held the stories of time. Birds nested in its branches, and children sought refuge in its shade on sunny days. It was a silent guardian, standing firm through the changing seasons.",
        "The city came alive as the night descended. Neon lights illuminated the streets, and the hustle and bustle of life continued. Each person carried their own story, their dreams, and aspirations, woven into the tapestry of the urban landscape. In the midst of the chaos, there was a strange beauty in the symphony of lives intertwining.",
        "The aroma of freshly baked bread filled the bakery, drawing people in like a magnet. The baker worked with practiced hands, kneading the dough with love and skill. Each loaf was a work of art, and as they emerged from the oven, they were met with appreciative smiles from customers eager to savor the warm goodness."
    ]
    rand_num = random.randint(0, len(paragraphs)-1)
    # txt_para.insert("1.0", paragraphs[rand_num])
    random_para = paragraphs[rand_num]
    return random_para

def calculate_wpm():
    txt_para = txt_write_para.get("1.0", ctk.END)
    words = txt_para.split()
    wpm = len(words) / ((time.time() - time_start)/60)
    # txt_wpm = tk.Text(height=10, width=50, padx=10, pady=10, font=('helvetica', 14))
    # txt_wpm.insert("1.0", "WPM: " + str(round(wpm, 2)))
    # txt_wpm.pack(fill=tk.BOTH)
    # todo: find a way to display the wpm in the GUI instead of the console
    print("WPM: " + str(wpm))

# Tkinter Window
window = ctk.CTk()
window.title("WPM Calculator")
window.geometry("800x600")

window.grid_rowconfigure([0, 1], weight=1)
window.grid_columnconfigure([0], weight=1)

frame_para = ctk.CTkFrame(master=window, fg_color='#ececec')#relief=ctk.SUNKEN, borderwidth=3
frame_para.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

# lbl_para = tk.Label(master=frame_para ,text="The paragraph")
# lbl_para.pack()

txt_para = ctk.CTkTextbox(master=frame_para, font=('helvetica', 14), height=300)
txt_para.insert("1.0", generate_para())
txt_para.configure(state="disabled")
txt_para.pack(fill=ctk.X)

txt_write_para = ctk.CTkTextbox(master=window, height=10, width=50, padx=10, pady=10, font=('helvetica', 14))
txt_write_para.configure(state="disabled")
txt_write_para.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

frame_btn = ctk.CTkFrame(master=window, fg_color='#ececec')
frame_btn.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

btn_calculate_wpm = ctk.CTkButton(master=frame_btn, text="Calculate WPM", command=calculate_wpm)
btn_calculate_wpm.pack(padx=10, pady=10)

btn_start_writing = ctk.CTkButton(master=frame_btn, text="Start Writing", command=start_writing)
btn_start_writing.pack(padx=10, pady=10)

window.mainloop()
