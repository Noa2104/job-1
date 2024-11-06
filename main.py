def draw_rectangle(width, height):
    # Vérifie que la largeur et la hauteur sont valides
    if width < 2 or height < 2:
        print("Les dimensions doivent être supérieures à 1.")
        return
    
    # Première ligne (haut du rectangle)
    print("|" + "-" * (width - 2) + "|")
    
    # Lignes centrales (côtés du rectangle)
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")
    
    # Dernière ligne (bas du rectangle)
    print("|" + "-" * (width - 2) + "|")

# Exemple d'utilisation
draw_rectangle(10, 3)
