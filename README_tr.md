[English](README.md) | **Türkçe** | [简体中文](README_zh.md) | [Русский](README_RU.md)

<br>

<p align="center">
  <img src="./docs/images/Anx-logo.jpg" alt="Anx-logo" width="100" />
</p>
<h1 align="center">Anx Reader</h1>

> **Kişisel fork:** Bu depo, [Anx Reader](https://github.com/Anxcye/anx-reader) temel alınarak kişisel geliştirme ve özelleştirme amacıyla sürdürülmektedir; yukarı akış projesinin resmî dağıtım veya destek kanalı değildir.

Anx Reader, kitap severler için özenle hazırlanmış bir e-kitap okuma uygulamasıdır. Güçlü yapay zeka yetenekleri ve geniş format desteğiyle okuma deneyimini daha akıllı ve odaklı hâle getirir. Modern arayüz tasarımıyla, saf okuma keyfini sunmayı hedefliyoruz.


![](./docs/images/main.jpg)


| Özellik | Detaylar | Durum |
| --- | --- | --- |
| Format Desteği | EPUB/MOBI/AZW3/FB2/TXT/PDF formatları tam destekli | ✅ |
| Platformlar Arası Senkronizasyon | Android/iOS/macOS/Windows desteği<br>Kitapları, notları ve okuma ilerlemesini WebDAV üzerinden senkronize edin | ✅ |
| AI Asistanı | Rafları okuma ilerlemesine ve tona göre düzenler<br>Derin anlayış için zihin haritaları oluşturur<br>İhtiyaca göre AI sözlük ve çeviri sağlar<br>Bakış açısı analizi ve özetler üretir | ✅ |
| Özelleştirilebilir Okuma Deneyimi | Harf, satır, paragraf ve kenar boşluklarını ayarlayın<br>Yazı tipi boyutu, stili ve kalınlığını seçin<br>Temaları, arka planları, hizalamayı ve stilleri özelleştirin | ✅ |
| Not Alanı | Çeşitli renk/stil hazır ayarları<br>Zamana veya bölüme göre sıralama, renge göre filtreleme<br>TXT/Markdown/CSV olarak dışa aktarma<br>Paylaşılabilir, özenle tasarlanmış kartlar oluşturma | ✅ |
| Okuma Analizleri | Okuma süresini takip edin<br>Günlük/haftalık/aylık/yıllık istatistikleri görüntüleyin<br>Okuma alışkanlıklarını gösteren ısı haritası | ✅ |
| Gelişmiş Özellikler | Çok sesli, hız, ton ve uyku zamanlayıcılı TTS<br>Yan yana görünümle tam kitap çevirisi<br>Kitapları bulutta saklayıp gerektiğinde indirin<br>Basitleştirilmiş/Geleneksel Çince arasında tek dokunuşla geçiş | ✅ |
| OPDS Katalogları | Yerleşik OPDS desteği ve özel katalog yönetimi | 🛠️ Çalışılıyor |





## Sorun giderme
[Sorun giderme kılavuzuna](./docs/troubleshooting.md) bakın.

### Ekran Görüntüleri
| ![](./docs/images/wide1.png) | ![](./docs/images/wide2.png) |
| :------------------------------: | :----------------------------: |
|   ![](./docs/images/wide3.png)   |  ![](./docs/images/wide4.png)  |
|   ![](./docs/images/wide5.png)   |  ![](./docs/images/wide6.png)  |
|   ![](./docs/images/wide7.png)   |  ![](./docs/images/wide8.png)  |


| ![](./docs/images/mobile1.png) | ![](./docs/images/mobile2.png) | ![](./docs/images/mobile3.png) |
| :----------------------------: | :----------------------------: | :----------------------------: |
| ![](./docs/images/mobile4.png) | ![](./docs/images/mobile5.png) | ![](./docs/images/mobile6.png) |
| ![](./docs/images/mobile7.png) | ![](./docs/images/mobile8.png) | ![](./docs/images/mobile9.png) |

## Derleme
Anx Reader'ı kaynak kodundan derlemek ister misiniz? Lütfen şu adımları izleyin:
- [Flutter](https://flutter.dev) kurun.
- Projeyi klonlayın ve dizine girin.
- `flutter pub get` komutunu çalıştırın.
- Çok dilli dosyaları oluşturmak için `flutter gen-l10n` çalıştırın.
- Riverpod kodunu oluşturmak için `dart run build_runner build --delete-conflicting-outputs` çalıştırın.
- Uygulamayı başlatmak için `flutter run` komutunu çalıştırın.

Flutter sürüm uyumsuzluklarıyla karşılaşabilirsiniz. Detaylar için [Flutter dokümantasyonuna](https://flutter.dev/docs/get-started/install) bakın.


Ek geliştirme notları: [docs/DEVELOPMENT.md](./docs/DEVELOPMENT.md).

## Lisans
Bu proje [MIT Lisansı](./LICENSE) ile lisanslanmıştır.

Sürüm 1.1.4'ten itibaren, Anx Reader projesinin açık kaynak lisansı MIT Lisansından GNU Genel Kamu Lisansı sürüm 3 (GPLv3) olarak değiştirilmiştir.

Sürüm 1.2.6'dan sonra seçim ve vurgulama özelliği yeniden yazılmış ve açık kaynak lisansı GPL-3.0 Lisansından MIT Lisansına dönmüştür. Tüm katkıda bulunanlar bu değişikliği kabul etmiştir (#116).

## Teşekkürler
[foliate-js](https://github.com/johnfactotum/foliate-js), MIT lisanslıdır ve e-kitap görüntüleyici olarak kullanılmaktadır. Böylesine harika bir proje sunduğu için yazara teşekkür ederiz.

[foliate](https://github.com/johnfactotum/foliate), GPL-3.0 lisanslıdır; seçim ve vurgulama özelliği bu projeden ilham almıştır. Ancak 1.2.6 sürümünden beri bu özellik yeniden yazılmıştır.

Ve birçok [diğer açık kaynak proje](./pubspec.yaml); katkıda bulunan tüm yazarlara teşekkürler.
