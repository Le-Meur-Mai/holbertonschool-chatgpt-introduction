#!/usr/bin/env python3

import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # On décrémente n à chaque tour
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <nombre_entier>")
    else:
        try:
            num = int(sys.argv[1])
            if num < 0:
                print("Le factoriel n'est pas défini pour les nombres négatifs.")
            else:
                f = factorial(num)
                print(f)
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")
