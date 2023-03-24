from dataclasses import dataclass

@dataclass
class Pojistenec:
    jmeno: str
    prijmeni: str
    vek: int
    telefon: int

    def __str__(self):
        return f"Jméno a příjmení: {self.jmeno} {self.prijmeni} \t\tVěk: {self.vek} \tTelefon: {self.telefon}"