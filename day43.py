#Matrix Calculator
import numpy as np

def get_matrix():
    try:
        rows = int(input("Satır sayısı: "))
        cols = int(input("Sütun sayısı: "))
        print("Matris elemanlarını satır satır gir:")

        elements = []
        for i in range(rows):
            row = list(map(float, input(f"{i+1}. satır: ").split()))
            if len(row) != cols:
                raise ValueError("Sütun sayısı uyuşmuyor!")
            elements.append(row)

        return np.array(elements)

    except ValueError as e:
        print("Hata:", e)
        return None

def get_vector():
    try:
        size = int(input("Vektör boyutu: "))
        vector = list(map(float, input("Vektör elemanları: ").split()))
        if len(vector) != size:
            raise ValueError("Vektör boyutu uyuşmuyor!")
        return np.array(vector)
    except ValueError as e:
        print("Hata:", e)
        return None

def matrix_operations(A, B):
    print("\n--- MATRİS İŞLEMLERİ ---")
    print("A:\n", A)
    print("B:\n", B)

    try:
        print("\nToplama:\n", A + B)
        print("\nÇıkarma:\n", A - B)
        print("\nEleman Bazlı Çarpma:\n", A * B)
    except ValueError:
        print("\nToplama / Çıkarma / Eleman çarpımı yapılamaz")

    try:
        print("\nMatris Çarpımı (dot):\n", np.dot(A, B))
    except ValueError:
        print("\nMatris çarpımı yapılamaz")

    print("\nA Transpoz:\n", A.T)

    try:
        print("\nDeterminant(A):", np.linalg.det(A))
        print("\nA'nın Tersi:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("\nDeterminant veya ters matris hesaplanamaz")

def scalar_operation(matrix):
    scalar = float(input("Skaler değer gir: "))
    print("\nSkaler Çarpım Sonucu:\n", matrix * scalar)

def vector_operations(v1, v2):
    print("\nV1:", v1)
    print("V2:", v2)

    try:
        print("\nVektör Toplama:", v1 + v2)
        print("Dot Product:", np.dot(v1, v2))
    except ValueError:
        print("Vektör işlemleri yapılamaz")
        
def save_matrix(matrix):
    filename = input("Dosya adı (örn: matris.npy): ")
    np.save(filename, matrix)
    print("Matris kaydedildi.")

def load_matrix():
    filename = input("Yüklenecek dosya adı: ")
    return np.load(filename)

def main():
    print("\n=== MATRIX CALCULATOR ===")
    print("1 - Matris işlemleri")
    print("2 - Vektör işlemleri")
    print("3 - Skaler x Matris")
    print("4 - Matris Kaydet")
    print("5 - Matris Yükle")
    choice = input("Seçimin: ")

    if choice == "1":
        print("\nMatris A")
        A = get_matrix()
        print("\nMatris B")
        B = get_matrix()
        if A is not None and B is not None:
            matrix_operations(A, B)

    elif choice == "2":
        print("\nVektör 1")
        v1 = get_vector()
        print("\nVektör 2")
        v2 = get_vector()
        if v1 is not None and v2 is not None:
            vector_operations(v1, v2)

    elif choice == "3":
        matrix = get_matrix()
        if matrix is not None:
            scalar_operation(matrix)

    elif choice == "4":
        matrix = get_matrix()
        if matrix is not None:
            save_matrix(matrix)

    elif choice == "5":
        matrix = load_matrix()
        print("Yüklenen Matris:\n", matrix)

    else:
        print("Geçersiz seçim")

if __name__ == "__main__":
    main()
