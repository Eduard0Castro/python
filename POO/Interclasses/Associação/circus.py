class Circus:

    def present(self, presenter: None):
        presenter.present()


class Clown:
    def present(self):
        print("Clown presents his show")
        


class Juggler:
    def present(self):
        print("Juggler presents his show")
        

class Tamer:
    def present(self):
        print("Tamer presents his show")

clown = Clown()
juggler = Juggler()
tamer = Tamer()
circus = Circus()

circus.present(clown)
circus.present(juggler)
circus.present(tamer)
        
        