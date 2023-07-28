from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3


def extract_text():
    file = filedialog.askopenfile(parent=root, mode="rb", title="Choose a PDF file")
    if file is not None:
        pdfreader = PyPDF2.PdfReader(file)
        global text_extracted
        text_extracted = ""
        for page_num in range(len(pdfreader.pages)):
            page_object = pdfreader.pages[page_num]
            text_extracted += page_object.extract_text()
        file.close()

def speak_text(text, rate, male, female):
    rate = int(rate.get())
    engine.setProperty("rate", rate)
    all_voices = engine.getProperty("voices")
    male_voice = all_voices[0].id
    female_voice = all_voices[1].id
    if male.get() == 1 and female.get() == 0:
        engine.setProperty("voice", male_voice)
    elif female.get() == 1 and male.get() == 0:
        engine.setProperty("voice", female_voice)
    else:
        engine.setProperty("voice", male_voice)

    engine.say(text)
    engine.runAndWait()


def stop_speaking():
    engine.stop()


def Application(root):
    root.geometry("{}x{}".format(1000, 1000))
    root.resizable(width=False, height=False)
    root.title("PDF 2 Audio")
    root.configure(background="light green")

    frame1 = Frame(root, width=500, height=200, bg="indigo")
    frame2 = Frame(root, width=500, height=450, bg="indigo")
    frame1.pack(side="top", fill="both")
    frame2.pack(side="top", fill="y")

    name1 = Label(frame1, text="PDF 2 Audio", fg="black", bg="blue", font="Arial 28 bold")
    name1.pack()
    name2 = Label(frame1, text="Listen to Your PDF File", fg="black", bg="blue", font="Arial 28 bold")
    name2.pack()

    button = Button(frame2, text="Select PDF File", activeforeground="red", command=lambda: extract_and_speak(), padx=70, pady=20, fg="white", bg="black", font="Arial 28 bold")
    button.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(frame2, text="Enter Rate of Speech", fg="black", bg="blue", font="Arial 28")
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=W)
    rate_entry = Entry(frame2, text="200", fg="black", bg="blue", font="Arial 28")
    rate_entry.grid(row=1, column=1, padx=30, pady=15, sticky=W)

    voice_text = Label(frame2, text="Select Voice", fg="black", bg="blue", font="Arial 28")
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)

    male_var = IntVar()
    male_opt = Checkbutton(frame2, text="Male", fg="black", bg="blue", font="Arial 28", variable=male_var, onvalue=1, offvalue=0)
    male_opt.grid(row=2, column=1, pady=0, padx=30, sticky=W)

    female_var = IntVar()
    female_opt = Checkbutton(frame2, text="Female", fg="black", bg="blue", font="Arial 28", variable=female_var, onvalue=1, offvalue=0)
    female_opt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

    submit_button = Button(frame2, text="Play PDF File", command=lambda: speak_text(text_extracted, rate_entry, male_var, female_var), activeforeground="red", padx=60, pady=10, fg="white", bg="black", font="Arial 28 bold")
    submit_button.grid(row=4, pady=65, column=0)

    stop_button = Button(frame2, text="Stop Playing", command=stop_speaking, activeforeground="red", padx=60, pady=10, fg="white", bg="black", font="Arial 28 bold")
    stop_button.grid(row=4, column=1, pady=65)

def extract_and_speak():
    global text_extracted
    text_extracted = extract_text()
    if text_extracted:
        speak_text(text_extracted, rate, male, female)

if __name__ == "__main__":
    engine = pyttsx3.init()
    root = Tk()
    Application(root)
    root.mainloop()