#Graph Plotter
import matplotlib.pyplot as plt #Grafik çizmek için matplotlib’in plot modülü
import pandas as pd #CSV’den veri okuyabilmek için

def get_manual_data():
    x = list(map(float, input("X değerlerini boşlukla gir: ").split())) #veri alır, float yapar, listeye çevirir
    y = list(map(float, input("Y değerlerini boşlukla gir: ").split()))
    return x, y

def get_csv_data():
    path = input("CSV dosya yolu: ")
    df = pd.read_csv(path)
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    return x, y

def graph_plotter():
    print("\n=== GRAPH PLOTTER ===")
    print("1 - Line Graph")
    print("2 - Bar Chart")
    print("3 - Scatter Plot")
    print("4 - Pie Chart")
    print("5 - Histogram")

    choice = input("Grafik türü seç: ")

    print("\n1 - Manuel veri")
    print("2 - CSV dosyasından")
    data_choice = input("Veri kaynağı seç: ")

    if data_choice == "1":
        x, y = get_manual_data()
    else:
        x, y = get_csv_data()

    color = input("Renk seç (örn: red, blue, green): ")
    title = input("Grafik başlığı: ")
    xlabel = input("X ekseni adı: ")
    ylabel = input("Y ekseni adı: ")

    if choice == "1":
        marker = input("Marker seç (o, x, *, +): ")
        plt.plot(x, y, color=color, marker=marker, label="Line")

    elif choice == "2":
        plt.bar(x, y, color=color, label="Bar")

    elif choice == "3":
        plt.scatter(x, y, color=color, label="Scatter")

    elif choice == "4":
        plt.pie(y, labels=x, autopct="%1.1f%%") #Y=dilim büyüklüğü, X=etiket, % otomatik hesaplanır

    elif choice == "5":
        plt.hist(y, bins=5, color=color) #bins = çubuk sayısı

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    save = input("Grafik kaydedilsin mi? (e/h): ")
    if save.lower() == "e":
        filename = input("Dosya adı (örn: grafik.png): ")
        plt.savefig(filename) #Grafik .png olarak kaydedilir
        print("Grafik kaydedildi")

    plt.show()

if __name__ == "__main__":
    graph_plotter()
    
