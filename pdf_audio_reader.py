from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3


def extract_text():
    file = filedialog.askopenfile(parent=root, mode="rb", title="Choose a PDF file")
    if file != None:
        pdfreader = PyPDF2.PdfFileReader(file)
        global text_extracted
        text_extracted = ""
        for page_num in range(pdfreader.numPages):
            page_object = pdfreader.getPage(page_num)
            text_extracted += page_object.extract_text()
        file.close()




def Application(root):
    root.geometry("{}x{}".format(700, 600))
    root.resizable(width=False, height=False)
    root.title("PDF 2 Audio")
    root.configure(background="light green")
    global rate, male, female
    frame1 = Frame(root, width=500, height=200, bg="indigo")
    frame2 = Frame(root, width=500, height=450, bg="indigo")
    frame1.pack(side="top", fill="both")
    frame2.pack(side="top", fill="y")

    name1 = Label(frame1, text="PDF 2 Audio", fg="black", bg="blue", font="Arial 28 bold")
    name1.pack()
    name2 = Label(frame1, text="Listen to Your PDF File", fg="black", bg="blue", font="Arial 28 bold")
    name2.pack()

    button = Button(frame2, text="Select PDF File", activeforeground="red", command=extract_text(), padx=70, pady=20, fg="white", bg="black",
                    font="Arial 28 bold")
    button.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(frame2, text="Enter Rate of Speech",fg="black", bg="blue", font="Arial 28")
    rate_text.grid(row=1, column=0, pady=15, padx=0, sticky=W)
    rate = Entry(frame2, text="200", fg="black", bg="blue", font="Arial 28")
    rate.grid(row=1, column=1, padx=30, pady=15, sticky=W)

    voice_text = Label(frame2, text="Select Voice", fg="black", bg="blue", font="Arial 28")
    voice_text.grid(row=2, column=0, pady=15, padx=0, sticky=E)

    male = IntVar()
    male_opt = Checkbutton(frame2, text="Male", fg="black", bg="blue", font="Arial 28", variable=male, onvalue=1, offvalue=0)
    male_opt.grid(row=2, column=1, pady=0, padx=30, sticky=W)
    female = IntVar()
    female_opt = Checkbutton(frame2, text="Female", fg="black", bg="blue", font="Arial 28", variable=female, onvalue=1, offvalue=0)
    female_opt.grid(row=3, column=1, pady=0, padx=30, sticky=W)

    submit_button = Button(frame2, text="Play PDF File", command=speak_text(), activeforeground="red", padx=60, pady=10, fg="white", bg="black",
                    font="Arial 28 bold")
    submit_button.grid(row=4, pady=65, colum=0)
    stop_button = Button(frame2, text="Stop Playing", command=stop_speaking(), activeforeground="red", padx=60, pady=10, fg="white", bg="black",
                    font="Arial 28 bold")
    stop_button.grid(row=4, column=1, pady=65)


if __name__ == "__main__":
    my_text, rate, male, female = "", 100, 0, 0
    engine = pyttsx3.init()
    root = Tk()
    Application(root)
    root.mainloop()