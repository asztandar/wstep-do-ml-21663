# region imports
import numpy as np
# endregion

def tablicaZawierajaca10Zer():
    tab = np.zeros(10)
    print("Treść: utwórz tablicę zawierającą 10 zer")
    print(tab)
    
def tablicaZawierajaca10Piatek():
    tab = np.full(10,5)
    print("Treść: utwórz tablicę zawierającą 10 piątek")
    print(tab)

#region menu
def menu():
    wyjscie_z_programu = False
    wybor_menu = -1
    while wyjscie_z_programu==False:
        print('Lab. nr 1 - "Powtórka operacji na tablicach i macierzach"')
        print("Menu:")
        print("1. utwórz tablicę zawierającą 10 zer")
        print("2. utwórz tablicę zawierającą 10 piątek")
        print("3. utwórz tablicę zawierającą liczby od 10 do 50")
        print("4. utwórz macierz (tablica wielowymiarowa) o wymiarach 3x3 zawierającą liczby od 0 do 8")
        print("5. utwórz macierz jednostkową o wymiarach 3x3")
        print("6. utwórz macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej (Gaussa),")
        print("7. utwórz macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01")
        print("8. utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1)")
        print("9. utwórz tablicę zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami:")
        print("\t-oblicz sumę wszystkich liczb w ww. macierzy\n\t-oblicz średnią wszystkich liczb w ww. macierzy\n\t-oblicz standardową dewiację dla liczb w ww. macierzy\n\t-oblicz sumę każdej kolumny ww. macierzy i zapisz ją do tablicy")
        print("11. utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) oraz:")
        print("\t-oblicz medianę tych liczb\n\t-znajdź najmniejszą liczbę tej macierzy\n\t-znajdź największą liczbę tej macierzy")
        print("12. utwórz macierz o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji")
        print("13. utwórz dwie macierze o odpowiednich wymiarach, większych od 2x2 i dodaj je do siebie")
        print("14. utwórz dwie macierze o odpowiednich wymiarach różnych od siebie i większych od 2, a następnie pomnóż je przez siebie za pomocą dwóch różnych funkcji ")
        print("0. Wyjście")
        wybor_menu = input("Wprowadź pozycję z menu i zatwierdź enterem:")
        print("Twoj wybor to:" + wybor_menu)
        if wybor_menu == "0":
            print("Wyjście z programu")
            wyjscie_z_programu = True
        else: 
            print("wybor")
    quit()
#endregion
tablicaZawierajaca10Zer() 
tablicaZawierajaca10Piatek()