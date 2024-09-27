"""This program is propriety of Freney Studios"""
import random

facts = [
    "So suonare il pianoforte!!",
    "So usare Tkinter!!",
    "So disegnare (abbastanza) bene! (?)",
    "Nelle mie passioni c'è lo sci",
    "Nelle mie passioni c'è il nuoto",
    "Nelle mie passioni c'è il disegno",
    "Nelle mie passioni c'è l' hacking?!",
    "Nelle mie passioni c'è la tecnologia",
    "So usare Blender!!",
    "So usare Gimp!!",
    "So usare un computer,wow",
    "Nelle mie passioni c'è lo sviluppo di sistemi operativi (OSDEV)",
    "Nelle mie passioni c'è lo sviluppo di applicazioni (APPDEV)",
    "Nelle mie passioni c'è lo sviluppo di videogiochi (GAMEDEV)",
]

"""Main function
   @params: N/A
   @return: str"""
def main()->str:
    return random.choice(facts)

if __name__ == "__main__":
    fact = main()
    print("Ecco un fatto su di me:",fact) 
