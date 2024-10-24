
---

# Kalp Hastalığı Tahmin Modeli

Bu proje, kalp hastalığı riskini tahmin etmek için yapay zeka ve makine öğrenimi tekniklerini kullanan bir uygulamadır. Python programlama dili ile geliştirilmiştir ve kullanıcıdan aldığı verilere dayanarak kalp hastalığı riski tahminleri yapmaktadır.

## Kullanılan Kütüphaneler

Bu projede aşağıdaki Python kütüphaneleri kullanılmaktadır:

- `numpy`: Sayısal hesaplamalar için.
- `pandas`: Veri işleme ve analiz için.
- `sklearn`: Makine öğrenimi algoritmaları ve veri ön işleme için.
- `imblearn`: Dengesiz veri setleriyle başa çıkmak için SMOTE tekniği.
- `tensorflow`: Yapay sinir ağları için.
- `keras`: Derin öğrenme uygulamaları için.

## Proje İçeriği

### Veri Seti

Proje, `heart.csv` adında bir veri seti kullanmaktadır. Bu veri seti, kalp hastalığı ile ilgili özellikleri içermektedir. Özellikler arasında yaş, cinsiyet, göğüs ağrısı tipi, dinlenme kan basıncı, kolesterol gibi değişkenler bulunmaktadır.

### Özellikler

- **Yapay Sinir Ağları**: Kalp hastalığı tahmini yapmak için bir yapay sinir ağı modeli kullanır.
- **Random Forest**: Makine öğrenmesi tabanlı bir sınıflandırma algoritmasıdır.
- **Karar Ağaçları**: Veriyi ağaç yapısına göre sınıflandırarak tahminlerde bulunur.
- **Lojistik Regresyon**: Kalp hastalığı riskini tahmin etmek için kullanılır.

### Kullanım

1. **Veri Setini Yükleme**: `heart.csv` dosyasını projeye dahil edin.
2. **Gerekli Kütüphaneleri Yükleyin**: Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyebilirsiniz:
   ```bash
   pip install numpy pandas scikit-learn imbalanced-learn tensorflow
   ```
3. **Modeli Çalıştırma**: Aşağıdaki komutu kullanarak Python dosyasını çalıştırın:
   ```bash
   python model1.py
   ```
4. **Kullanıcı Girdisi**: Program çalıştığında, sizden yaş, cinsiyet, göğüs ağrısı tipi, dinlenme kan basıncı ve kolesterol değerlerini girmeniz istenecektir.
5. **Tahmin Sonucu**: Girilen verilere dayanarak kalp hastalığı risk oranınız tahmin edilecektir.

### Kullanıcıdan Veri Alma

Program, kullanıcıdan yaş, cinsiyet (M/F), göğüs ağrısı tipi (ATA, NAP, ASY, TA), dinlenme kan basıncı ve kolesterol değerlerini alır. Kullanıcı girdisi doğrulaması yapılarak hatalı girişler kontrol edilmektedir.

### Proje Geliştirme ve Genişletme

- Kullanıcı arayüzü eklenebilir.
- Farklı veri setleri ile test edilebilir.
- Diğer makine öğrenimi algoritmaları eklenerek karşılaştırmalar yapılabilir.

## Sonuç

Bu proje, kalp hastalığı riskini tahmin etmek için kullanıcı dostu bir arayüz sunarak yapay zeka ve makine öğrenimini bir araya getirir. Geliştirilmeye açık bir projedir ve kullanıcıların sağlık durumlarını değerlendirmelerine yardımcı olmayı hedeflemektedir.

---

