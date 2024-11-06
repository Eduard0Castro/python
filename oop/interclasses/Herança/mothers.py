class Mother:
    def __init__(self, name: str):
        self.name = name

    def study(self):
        print(f"{self.name} está estudando")

    def gym(self):
        print("Só os cambito")


class Daugther(Mother):
    def __init__(self, name: str, school: str):
        super().__init__(name)
        self.school = school

    def joke(self):
        print(f"{self.name} está brincando")

    def series(self):
        print("Bom dia, Verônica")

    def get_school(self):
        return self.school


class Granddaugther(Daugther):
    def __init__(self, name: str, school: str):
        super().__init__(name, school)

    def nothing(self):
        print("Nothing")


if __name__ == "__main__":
    fabricia = Mother("Fabricia")
    giulia = Daugther("Giulia", "ISJ")
    kika = Granddaugther("KIka", "ISJ")

    kika.gym()
    print(kika.school)

    print(giulia.get_school())
    giulia.series()




