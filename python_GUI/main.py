import tkinter as tk
from PIL import ImageTk, Image


def WelcomePage():
    window = tk.Tk()
    window.title("CoRoLa")
    window.geometry("1920x1080")
    window.config(bg="LightSteelBlue1")

    def openWordsAnalogiesPage():
        window.destroy()
        WordsAnalogiesPage()

    def openSimilarWordsPage():
        window.destroy()
        SimilarWordsPage()

    def openHyponymyPercentagePage():
        window.destroy()
        HyponymyPercentagePage()

    label1 = tk.Label(window,
                      text="Analogiile de cuvinte sunt de forma vec(A) - vec(B) + vec(C), unde vec(A), vec(B) si "
                           "vec(C) sunt reprezentarile vectoriale ale cuvintelor introduse.", bg="misty rose",
                      height=4, width=117, font=("None", 20))

    label2 = tk.Label(window, text="Pe baza cuvantului introdus se va afisa o lista de cuvinte asemanatoare.",
                      bg="misty "
                         "rose",
                      height=4, width=117, font=("None", 20))

    label3 = tk.Label(window, text="Se vor afisa hiponimele cuvantului introdus.",
                      bg="misty "
                         "rose",
                      height=4, width=117, font=("None", 20))

    title1 = tk.Label(window, text="CoRoLa", bg="LightSteelBlue1", font=("Courier", 60, 'bold'))
    title2 = tk.Label(window, text="Bine ati venit!", bg="LightSteelBlue1", font=("Courier", 45))

    button1 = tk.Button(window, text="Analogii de cuvinte", height=2, width=17, bg="DarkOrchid3", fg="white",
                        font=("None", 20), command=openWordsAnalogiesPage)
    button2 = tk.Button(window, text="Cuvinte similare", height=2, width=17, bg="DarkOrchid3", fg="white",
                        font=("None", 20), command=openSimilarWordsPage)
    button3 = tk.Button(window, text="Hiponime", height=2, width=17, bg="DarkOrchid3", fg="white",
                        font=("None", 20), command=openHyponymyPercentagePage)

    title1.pack(pady=10)
    title2.pack(pady=15)

    button1.pack(pady=10)
    label1.pack(pady=10)

    button2.pack(pady=10)
    label2.pack(pady=10)

    button3.pack(pady=10)
    label3.pack(pady=10)

    tk.mainloop()


def SimilarWordsPage():
    window = tk.Tk()
    window.title("CoRoLa")
    window.geometry("1920x1080")
    window.config(bg="LightSteelBlue1")

    def openWordsAnalogiesPage():
        window.destroy()
        WordsAnalogiesPage()

    def openHyponymyPercentagePage():
        window.destroy()
        HyponymyPercentagePage()

    title1 = tk.Label(window, text="CoRoLa", bg="LightSteelBlue1", font=("Courier", 45, 'bold'))

    label1 = tk.Label(window, text="Introduceti un cuvant pentru a obtine altele asemanatoare:", bg="LightSteelBlue1",
                      font=("None", 30))
    label2 = tk.Label(window, text="Cuvantul", bg="LightSteelBlue1", font=("None", 30))

    t = tk.Text(window, height=3, width=40, bg="misty rose")

    button1 = tk.Button(window, text="Analogii de cuvinte", height=2, width=20, bg="DarkOrchid3", fg="white",
                        font=("Nonne", 20), command=openWordsAnalogiesPage)
    button2 = tk.Button(window, text="Hiponime", height=2, width=20, bg="DarkOrchid3", fg="white",
                        font=("Nonne", 20), command=openHyponymyPercentagePage)
    button3 = tk.Button(window, text="Reset", height=2, width=20, bg="DarkOrchid3", fg="white", font=("None", 20))
    button4 = tk.Button(window, text="Start", height=2, width=20, bg="DarkOrchid3", fg="white",
                        font=("None", 20))

    checkbox1 = tk.Checkbutton(window, text="Arata vectori", bg="LightSteelBlue1", font=("None", 20))

    label3 = tk.Label(window, text="Lista cuvinte similare", bg="white", width=20, height=15, font=("None", 20))
    label4 = tk.Label(window, text="Spatiu pentru afisarea vectorilor", bg="white", width=107, height=6,
                      font=("None", 20))

    title1.place(relx=0.5, anchor="center", rely=0.05)

    label1.place(relx=0.5, anchor="center", rely=0.12)
    label2.place(relx=0.05, anchor="w", rely=0.30)

    t.place(relx=0.25, anchor="w", rely=0.30)

    button1.place(relx=0.05, anchor="w", rely=0.47)
    button2.place(relx=0.26, anchor="w", rely=0.47)
    button3.place(relx=0.47, anchor="w", rely=0.47)
    button4.place(relx=0.47, anchor="w", rely=0.30)

    checkbox1.place(relx=0.05, anchor="w", rely=0.6)

    label3.place(relx=0.70, anchor="w", rely=0.4)
    label4.place(relx=0.05, anchor="w", rely=0.85)

    tk.mainloop()


def HyponymyPercentagePage():
    window = tk.Tk()
    window.title("CoRoLa")
    window.geometry("1920x1080")
    window.config(bg="LightSteelBlue1")

    def openSimilarWordsPage():
        window.destroy()
        SimilarWordsPage()

    def openWordsAnalogiesPage():
        window.destroy()
        WordsAnalogiesPage()

    title1 = tk.Label(window, text="CoRoLa", bg="LightSteelBlue1", font=("Courier", 45, 'bold'))

    label1 = tk.Label(window, text="Introduceti un cuvant pentru a ii afisa hiponimele.", bg="LightSteelBlue1",
                      font=("None", 30))
    label2 = tk.Label(window, text="Cuvantul", bg="LightSteelBlue1", font=("None", 30))

    t = tk.Text(window, height=3, width=40, bg="misty rose")

    button1 = tk.Button(window, text="Analogii de cuvinte", height=2, width=20, bg="DarkOrchid3", fg="white",
                        font=("Nonne", 20), command=openWordsAnalogiesPage)
    button2 = tk.Button(window, text="Cuvinte similare", height=2, width=20, bg="DarkOrchid3", fg="white",
                        font=("Nonne", 20), command=openSimilarWordsPage)
    button3 = tk.Button(window, text="Reset", height=2, width=20, bg="DarkOrchid3", fg="white", font=("None", 20))
    button4 = tk.Button(window, text="Start", height=2, width=20, bg="DarkOrchid3", fg="white",
                        font=("None", 20))

    checkbox1 = tk.Checkbutton(window, text="Arata vectori", bg="LightSteelBlue1", font=("None", 20))

    label3 = tk.Label(window, text="Lista hiponime", bg="white", width=20, height=15, font=("None", 20))
    label4 = tk.Label(window, text="Spatiu pentru afisarea vectorilor", bg="white", width=107, height=6,
                      font=("None", 20))

    title1.place(relx=0.5, anchor="center", rely=0.05)

    label1.place(relx=0.5, anchor="center", rely=0.12)
    label2.place(relx=0.05, anchor="w", rely=0.30)

    t.place(relx=0.25, anchor="w", rely=0.30)

    button1.place(relx=0.05, anchor="w", rely=0.47)
    button2.place(relx=0.26, anchor="w", rely=0.47)
    button3.place(relx=0.47, anchor="w", rely=0.47)
    button4.place(relx=0.47, anchor="w", rely=0.30)

    checkbox1.place(relx=0.05, anchor="w", rely=0.6)

    label3.place(relx=0.70, anchor="w", rely=0.4)
    label4.place(relx=0.05, anchor="w", rely=0.85)

    tk.mainloop()


def WordsAnalogiesPage():
    window = tk.Tk()
    window.title("CoRoLa")
    window.geometry("1920x1080")
    window.config(bg="LightSteelBlue1")

    def openSimilarWordsPage():
        window.destroy()
        SimilarWordsPage()

    def openHyponymyPercentagePage():
        window.destroy()
        HyponymyPercentagePage()

    h = tk.Label(window, text="CoRoLa", bg="LightSteelBlue1", font=("Courier", 45, 'bold'))

    explanation = """Introduceti cuvinte in campurile de mai jos pentru a obtine o analogie de forma """
    explanation2 = """A - B + C, unde A, B si C sunt reprezentarile vectoriale ale cuvintelor."""

    e = tk.Label(window, text=explanation, bg="LightSteelBlue1", font=("None", 25))
    e2 = tk.Label(window, text=explanation2, bg="LightSteelBlue1", font=("None", 25))

    a = tk.Label(window, text="Cuvantul A", bg="LightSteelBlue1", font=("None", 25))
    b = tk.Label(window, text="Cuvantul B", bg="LightSteelBlue1", font=("None", 25))
    c = tk.Label(window, text="Cuvantul C", bg="LightSteelBlue1", font=("None", 25))

    a_input = tk.Text(window, height=3, width=40, bg="misty rose")
    b_input = tk.Text(window, height=3, width=40, bg="misty rose")
    c_input = tk.Text(window, height=3, width=40, bg="misty rose")

    var = tk.IntVar()
    checkbox = tk.Checkbutton(window, text='Arata vectori', bg="LightSteelBlue1", font=("None", 25), variable=var,
                              onvalue=1, offvalue=0)

    button1 = tk.Button(window, text='Cuvinte similare', bg="DarkOrchid3", fg="white", font=("None", 20), width=15,
                        height=2, command=openSimilarWordsPage)
    button2 = tk.Button(window, text='Hiponime', bg="DarkOrchid3", fg="white", font=("None", 20), width=15,
                        height=2, command=openHyponymyPercentagePage)
    button3 = tk.Button(window, text='Reset', bg="DarkOrchid3", fg="white", font=("None", 20), width=15, height=2)
    button4 = tk.Button(window, text='Start', bg="DarkOrchid3", fg="white", font=("None", 20), width=15, height=2)

    text1 = tk.Label(window, text="Spatiu pentru afisarea analogiei", bg="white", width=107, height=5,
                     font=("None", 20))
    text2 = tk.Label(window, text="Spatiu pentru afisarea vectorilor", bg="white", width=107, height=6,
                     font=("None", 20))

    h.place(relx=0.5, anchor="center", rely=0.05)

    e.place(relx=0.5, anchor="center", rely=0.13)
    e2.place(relx=0.5, anchor="center", rely=0.17)

    a.place(relx=0.15, anchor="w", rely=0.25)
    b.place(relx=0.45, anchor="w", rely=0.25)
    c.place(relx=0.75, anchor="w", rely=0.25)

    a_input.place(relx=0.10, anchor="w", rely=0.35)
    b_input.place(relx=0.40, anchor="w", rely=0.35)
    c_input.place(relx=0.70, anchor="w", rely=0.35)

    load1 = Image.open("plus.png")
    load1 = load1.resize((40, 35), Image.ANTIALIAS)
    plus = ImageTk.PhotoImage(load1)
    img = tk.Label(window, image=plus, borderwidth=0)
    img.image = plus
    img.place(relx=0.62, anchor="w", rely=0.35)
    load2 = Image.open("minus.png")
    load2 = load2.resize((50, 30), Image.ANTIALIAS)
    minus = ImageTk.PhotoImage(load2)
    img = tk.Label(window, image=minus, borderwidth=0)
    img.image = minus
    img.place(relx=0.32, anchor="w", rely=0.35)

    var = tk.IntVar()
    checkbox.place(relx=0.43, anchor="w", rely=0.40)

    button1.place(relx=0.12, anchor="w", rely=0.47)
    button2.place(relx=0.32, anchor="w", rely=0.47)
    button3.place(relx=0.52, anchor="w", rely=0.47)
    button4.place(relx=0.72, anchor="w", rely=0.47)

    text1.place(relx=0.05, anchor="w", rely=0.65)
    text2.place(relx=0.05, anchor="w", rely=0.83)

    tk.mainloop()


def start():
    WelcomePage()


start()
