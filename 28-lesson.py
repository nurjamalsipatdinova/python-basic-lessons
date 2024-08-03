from tkinter import  *
from tkinter import messagebox as mb
# class Window:
#     def __init__(self, width, heigth, title="Python", resizable=(False, False), icon=None ):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{heigth}+400+200")
#         self.root.resizable(resizable[0], resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#     def draw_widgets(self):
#         Button(self.root, text="info", width=10, command=lambda: messagebox.showinfo("Info", "message info")).pack()
#         Button(self.root, text="warning", width=10, command=lambda: messagebox.showwarning("Warning", "message warning")).pack()
#         Button(self.root, text="error", width=10, command=lambda: messagebox.showerror("Error", "message error")).pack()
#         Button(self.root, text="quit", width=10, command=self.exit).pack()
#     def exit(self):
#         choise=messagebox.askyesnocancel("quit", "do you want to quit?")
#         if choise:
#             self. root.destroy()
# if __name__=="__main__":
#     win=Window(500, 300)
#     win.run()

.



    ##################################Entry######################################################
# from tkinter import *
# from tkinter import messagebox as mb
#
# class Window:
#     def __init__(self, width, height, title="Python tkinter", resizable=(False, False), icon=r"icon.ico"):
#         self.root = Tk()
#         self.root.title(title)
#         self.root.geometry(f"{width}x{height}+200+200")
#         self.root.resizable(resizable[0],resizable[1])
#         if icon:
#             self.root.iconbitmap(icon)
#
#         self.login_entry = Entry(self.root)
#         self.age_entry = Entry(self.root)
#         self.password_entry = Entry(self.root, show="*")
#
#     def run(self):
#         self.draw_widgets()
#         self.root.mainloop()
#
#     def draw_widgets(self):
#         Label(self.root, text="Login:", justify=LEFT).grid(row=0, column=0, sticky=W)
#         self.login_entry.grid(row=0, column=1, sticky=W + E, padx=5, pady=5)
#         Label(self.root, text="Age:", justify=LEFT).grid(row=1, column=0, sticky=W)
#         self.age_entry.grid(row=1, column=1, sticky=W + E, padx=5, pady=5)
#         Label(self.root, text="Password:", justify=LEFT).grid(row=2, column=0, sticky=W)
#         self.password_entry.grid(row=2, column=1, sticky=W + E, padx=5, pady=5)
#
#         Button(self.root, text="Clear", width=10, command=self.clear).grid(row=3, column=2, padx=5, sticky=E)
#
#         Button(self.root, text="Save", width=10, command=self.save_data).grid(row=3, column=0, padx=5, sticky=E)
#         Button(self.root, text="Quit", width=10, command=self.exit).grid(row=3, column=1, sticky=E)
#
#     def exit(self):
#         choice = mb.askokcancel("Quit", "Do you want to quit?")
#         if choice:
#             self.root.destroy()
#
#     def save_data(self):
#         login = self.login_entry.get()
#         age = int(self.age_entry.get())
#         password = self.password_entry.get()
#
#         mb.showinfo("User Data", f"Hello, {login}! You're {age} y.o.")
#
#     def clear(self):
#         self.login_entry.delete(0, END)
#         self.age_entry.delete(0, END)
#         self.password_entry.delete(0, END)
#
#
# if __name__ == "__main__":
#     window = Window(500, 500, "TKINTER")
#     window.run()

