#Temperature Plotter
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data = pd.read_csv(file_path, parse_dates=["Date"])
        print("Veri başarıyla yüklendi")
        return data
    except Exception as e:
        print("Veri yüklenemedi:", e)
        return None

def plot_temperature(data, save_file=None):
    # 7 günlük hareketli ortalama
    data["7_Day_Avg"] = data["Temperature"].rolling(window=7).mean() #Her gün için son 7 günün ortalaması

    # Anomali tespiti için referans değerler
    mean_temp = data["Temperature"].mean()
    std_temp = data["Temperature"].std()

    # Anomali tanımı
    data["Anomaly"] = (
        (data["Temperature"] > mean_temp + 2 * std_temp) |
        (data["Temperature"] < mean_temp - 2 * std_temp)
    )

    # Grafik stili
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.figure(figsize=(10, 6))

    # Günlük sıcaklık
    plt.plot(
        data["Date"],
        data["Temperature"],
        label="Günlük Sıcaklık",
        color="blue"
    )

    # 7 günlük ortalama
    plt.plot(
        data["Date"],
        data["7_Day_Avg"],
        label="7 Günlük Ortalama",
        linestyle="--",
        color="orange"
    )

    # Anomaliler
    plt.scatter(
        data[data["Anomaly"]]["Date"],
        data[data["Anomaly"]]["Temperature"],
        color="red",
        label="Anomali"
    )

    plt.title("Sıcaklık Trendleri")
    plt.xlabel("Tarih")
    plt.ylabel("Sıcaklık (°C)")
    plt.legend()
    plt.grid(True)

    if save_file:
        plt.savefig(save_file)
        print(f"Grafik kaydedildi → {save_file}")
    else:
        plt.show()

def main():
    print("=== TEMPERATURE PLOTTER ===")

    file_path = input("Sıcaklık CSV dosya yolunu gir: ")
    data = load_data(file_path)

    if data is None:
        return

    save_choice = input("Grafik kaydedilsin mi? (e/h): ")

    if save_choice.lower() == "e":
        filename = input("Dosya adı (örn: temperature.png): ")
        plot_temperature(data, filename)
    else:
        plot_temperature(data)

    print("\nİşlem tamamlandı!")

if __name__ == "__main__":
    main()
