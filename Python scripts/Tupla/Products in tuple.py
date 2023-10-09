tupla = ("Pão", 3.50, "Gorgonzola", 17.80,
          "Presunto", 5.28, "Amendoim", 14.90, "Iogurte", 5.50)

for i in range(0, len(tupla), 2):
    print(f"{tupla[i]:-<30}", f"R${tupla[i+1]:>6.2f}")

