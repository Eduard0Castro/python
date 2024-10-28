from tkinter import *
from tkinter import ttk 


class Funcs:

    def write_test(self, root: Tk):

        self.escrever = Label(root, text = "Test Label from command", bg = "#929ca9",
                              font = ("Times New Roman", 12, "bold", "italic"))
        self.escrever.place(x = 20, y = 190, width = 360, height = 30)

    def clean_test(self, entry: Entry):
        entry.delete(0, END)
        

class TesteTKinter():

    def __init__(self, root: Tk):

        self.root = root
        self.funcs = Funcs()
        self.tela()
        # self.frames()
        self.widgets()
        self.labels()
        self.create_list()

    def tela(self) -> None:

        self.root.title("Teste")
        self.root.configure(background = "#929ca9")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.maxsize(width = 600, height = 600)
        self.root.minsize(width=300, height = 300)


    def frames(self) ->None:
        metadinha = Frame(self.root, background = "black")
        metadinha.place(relx = 5/40, rely = 5/40, relwidth = 3/4, relheight=3/4)

    def widgets(self) -> None:

        self.search_button = Button(self.root, text="Search", bd=2)
        self.search_button.place(x = 117, y = 350, width = 54, height=25)
        
        self.clean_button = Button(self.root, text = "Clean", bd = 2,
                                   command = lambda :self.digitar.delete(0, END))
        self.clean_button.place(x = 173, y = 350, width=54, height=25)

        self.write_button = Button(self.root, text = "Write", bd = 2, 
                           command = lambda : self.funcs.write_test(self.root))
        self.write_button.place(x = 229, y = 350, width = 54, height = 25)

        self.digitar = Entry(self.root)
        self.digitar.place(x = 50, y = 100, width = 90, height = 30)

        self.slide_saturation = Scale(self.root, from_= -10, to=10, resolution=1, length=100, 
                                      orient=HORIZONTAL, state=NORMAL)
        
        self.slide_saturation.place(x= 20, y = 20, width=110, height=30)


    def labels(self) -> None:
        self.camera = Label(self.root, text = "Camera", bg = "#929ca9", fg = "#0b1d21",
                            font = ("Times New Roman", 14, "bold"))
        self.camera.place(x = 170, y = 30, width = 80, height = 20)

        self.digitar_label = Label(self.root, text = "Digite: ", bg = "#929ca9", 
                                   font = ("DejaVu Serif", 10, "bold"), justify = "left")
        self.digitar_label.place(x = 50, y = 80, width = 100, height = 20)

    def create_list(self) -> None:

        self.lista_tree = ttk.Treeview(self.root, height = 3, 
                                       columns = ("Continente", "País", "Estado", "Cidade"))
        
        self.lista_tree.heading(0, text = "Continente")
        self.lista_tree.heading(1, text = "País")
        self.lista_tree.heading(2, text = "Estado")
        self.lista_tree.heading(3, text = "Cidade")

        self.lista_tree.column("#0", width = 0, stretch=NO)
        self.lista_tree.column(0, width = 80)
        self.lista_tree.column(1, width = 50)
        self.lista_tree.column(2, width = 50)
        self.lista_tree.column(3, width = 50)

        self.lista_tree.place(x = 20, y = 220, width = 360, height = 80)

        self.scroll_list = Scrollbar(self.root, orient="vertical")
        self.lista_tree.configure(yscroll = self.scroll_list.set)
        self.scroll_list.place(x = 381, y = 220, width=10, height = 80)


        

if __name__ == "__main__":

    root = Tk()
    teste = TesteTKinter(root=root)
    mainloop()
    