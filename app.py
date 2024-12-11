import tkinter as tk
from tkinter import messagebox
from Platforms import platforms

class PriceProcessor:
    def __init__(self, urun, platform, fiyat_liste):
        self.urun = urun
        self.platform = platform
        self.fiyat_liste = fiyat_liste if fiyat_liste else []  # None kontrolü
        self.temiz_fiyat_liste = []

    def temizle_ve_donustur(self, fiyat, para_birimi="TL"):
        """Bir fiyat string'ini temizler ve float'a dönüştürür."""
        temiz_fiyat = (
            fiyat.replace(para_birimi, "")
            .replace(".", "")
            .replace(",", ".")
            .strip()
        )
        return float(temiz_fiyat)

    def fiyatlari_isle(self):
        """Fiyat listesini temizler ve sayıya dönüştürür."""
        for fiyat in self.fiyat_liste:
            try:
                self.temiz_fiyat_liste.append(self.temizle_ve_donustur(fiyat))
            except ValueError:
                print(f"{self.platform}: Geçersiz fiyat formatı atlandı: {fiyat}")

    def ortalama_hesapla(self):
        """Temizlenmiş fiyat listesinin ortalamasını hesaplar."""
        if not self.temiz_fiyat_liste:
            return None
        return sum(self.temiz_fiyat_liste) / len(self.temiz_fiyat_liste)

def fiyatlari_isle_ve_goster(urun):
    """Verilen ürün için platformlardan fiyatları al ve sonuçları göster."""
    platforms_to_check = {
        "Amazon": platforms.amazon,
        "N11": platforms.n11,
        "Trendyol": platforms.trendyol,
        "Hepsiburada": platforms.hepsiburada,
    }

    results = []

    for platform_name, platform_func in platforms_to_check.items():
        fiyat_liste = platform_func(urun=urun)
        if fiyat_liste is None:
            fiyat_liste = []  # None durumunda boş listeye dönüştür
        
        processor = PriceProcessor(urun, platform_name, fiyat_liste)
        processor.fiyatlari_isle()
        ortalama = processor.ortalama_hesapla()

        if ortalama is not None:
            results.append(f"{platform_name}: {ortalama:.2f} TL")
        else:
            results.append(f"{platform_name}: Fiyat bulunamadı")

    return results

def isleme_basla():
    """Arayüzdeki kullanıcı girişine göre fiyatları işleyip sonuçları gösterir."""
    urun = urun_girisi.get()

    if not urun.strip():
        messagebox.showwarning("Uyarı", "Lütfen bir ürün ismi girin!")
        return

    sonuc_listesi.delete(0, tk.END)  # Mevcut sonuçları temizle

    try:
        results = fiyatlari_isle_ve_goster(urun)
        for result in results:
            sonuc_listesi.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

# Tkinter Arayüzü
pencere = tk.Tk()
pencere.title("Ürün Fiyat Karşılaştırma")
pencere.geometry("400x450")

urun_label = tk.Label(pencere, text="Ürün İsmi:", font=("Arial", 12))
urun_label.pack(pady=5)

urun_girisi = tk.Entry(pencere, width=40, font=("Arial", 12))
urun_girisi.pack(pady=5)

basla_butonu = tk.Button(pencere, text="İşleme Başla", command=isleme_basla, font=("Arial", 12), bg="lightblue")
basla_butonu.pack(pady=10)

sonuc_listesi = tk.Listbox(pencere, width=50, height=15, font=("Arial", 10))
sonuc_listesi.pack(pady=10)

pencere.mainloop()
