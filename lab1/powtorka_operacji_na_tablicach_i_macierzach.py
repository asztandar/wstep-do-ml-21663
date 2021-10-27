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

def tablicaZawierajacaLiczbyOd10Do50():
    tab = np.arange(10,51,1)
    print("Treść: utwórz tablicę zawierającą liczby od 10 do 50")
    print(tab)

def macierzOWymiarach3x3ZawOd0Do8():
    tab = np.arange(9).reshape(3,3)
    print("Treść: utwórz macierz (tablica wielowymiarowa) o wymiarach 3x3 zawierającą liczby od 0 do 8")
    print(tab)


def macierzJednostkowa3x3():
    tab = np.eye(3)
    print("Treść: utwórz macierz jednostkową o wymiarach 3x3")
    print(tab)

def macierz5x5Dystrybucji():
    tab = np.random.normal(size=(5,5))
    print("Treść: utwórz macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej (Gaussa)")
    print(tab)

def macierz10x10ZawOd001Do1ZKrokiem001():
    tab = np.arange(0.01,1.01,0.01).reshape(10,10)
    print("Treść: utwórz macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01")
    print(tab)

def tablica20Liniowo0A1Wlacznie():
    tab = np.linspace(0.0, 1.0, num=20)
    print("Treść: utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1)")
    print(tab)

def tablicaLosoweOd1Do25Macierz5x5():
    tab = np.random.randint(1,25, size=25)
    print("Treść: utwórz tablicę zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami")
    print("tablica:")
    print(tab)
    matrix = tab.reshape(5,5)
    print("macierz:")
    print(matrix)
    sumaLiczbMacierzy(matrix)
    sredniaLiczbMacierzy(matrix)
    standardowaDewiacjaMacierzy(matrix)
    sumaKolumnyMacierzyDoTablicy(matrix)
    
def sumaLiczbMacierzy(matrix):
    matrixSum = matrix.sum()
    print("suma liczb macierzy = ", end='')
    print(matrixSum)

def sredniaLiczbMacierzy(matrix):
    matrixSr = matrix.mean()
    print("średnia liczb macierzy = ", end='')
    print(matrixSr)

def standardowaDewiacjaMacierzy(matrix):
    matrixStd = matrix.std()
    print("standardowa dewiacja = ", end='')
    print(matrixStd)

def sumaKolumnyMacierzyDoTablicy(matrix):
    matrixKolumnSum =  matrix.sum(axis=0)
    print("suma kolumn = ", end='')
    print(matrixKolumnSum)

def macierz5x5LosoweOd0Do100():
    tab = np.random.randint(0,100, size=(5,5))
    print("task: utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) oraz:")
    print("macierz:")
    print(tab)
    medianaMacierzy(tab)
    najmniejszaLiczbaMacierzy(tab)
    najwiekszaLiczbaMacierzy(tab)

def medianaMacierzy(matrix):
    matrixMedian = np.median(matrix)
    print("mediana = ", end='')
    print(matrixMedian)

def najmniejszaLiczbaMacierzy(matrix):
    matrixMin = matrix.min()
    print("najmniejsza = ", end='')
    print(matrixMin)

def najwiekszaLiczbaMacierzy(matrix):
    matrixMax = matrix.max()
    print("najwieksza = ", end='')
    print(matrixMax)

def macierzMxNTranspozycja():
    tab = np.random.randint(0,100, size=(3,5))
    print("macierz:")
    print(tab)
    tabTranspose = tab.transpose()
    print("macierz transponowana:")
    print(tabTranspose)

def sumaDwochMacierzy():
    matrixA = np.random.randint(100, size=(3, 3))
    matrixB = np.random.randint(100, size=(3, 3))
    print("Macierz A:")
    print(matrixA)
    print("Macierz B:")
    print(matrixB)
    matrixSum = np.add(matrixA,matrixB)
    print("suma macierzy = ")
    print(matrixSum)

def mnozenieDwochMacierzy():
    matrixA = np.random.randint(4, size=(3, 4))
    matrixB = np.random.randint(4, size=(4, 3))
    print("Macierz A:")
    print(matrixA)
    print("Macierz B:")
    print(matrixB)
    matrixMultiplication = np.matmul(matrixA,matrixB)
    print("wymnożona macierz matmul = ")
    print(matrixMultiplication)
    matrixMultiplication2 = np.dot(matrixA,matrixB)
    print("wymnożona macierz dot = ")
    print(matrixMultiplication2)

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
#tablicaZawierajaca10Zer() 
#tablicaZawierajaca10Piatek()
#tablicaZawierajacaLiczbyOd10Do50()
#macierzOWymiarach3x3ZawOd0Do8()
#macierzJednostkowa3x3()
#macierz5x5Dystrybucji()
#macierz10x10ZawOd001Do1ZKrokiem001()
#tablica20Liniowo0A1Wlacznie()
#tablicaLosoweOd1Do25Macierz5x5()
#macierz5x5LosoweOd0Do100()
#macierzMxNTranspozycja()
#sumaDwochMacierzy()
mnozenieDwochMacierzy()