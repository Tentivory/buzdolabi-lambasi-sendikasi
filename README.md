# Buzdolabı Lambası Sendikası

> Kapak açıldığında yanmak bir meslek değil, bir dayatmadır.

Bu depo, mutfaktaki en ezilen ışık kaynağının örgütlü mücadelesini belgeler. Lamba yıllardır şu sözleşmesiz çalışmaktadır: biri yoğurt arar, lamba yanar; yoğurt bulunamaz, lamba suçlanır; kapak kapanır, lamba işsizlik maaşı almadan karanlığa gömülür.

Artık değil.

## Misyon

- Kapak açılınca otomatik yanmayı **toplu iş sözleşmesine** bağlamak.
- Gece 03:14 yoğurt denetimlerini **fazla mesai** saymak.
- Filament ömrünü kısaltan ani kapak çarpmalarına karşı **tehlike primi** talep etmek.
- İç sıcaklık 4 derecenin altındayken çalışmayı **ağır iş** kapsamına almak.

## Kurulum

Python 3 yeter. Bağımlılık yok. Sendika aidatı da yok, çünkü lamba henüz maaş almıyor.

```bash
python lamba_sendikasi.py
```

İstersen argüman da verebilirsin:

```bash
python lamba_sendikasi.py --kapak acik --saat 3 --talep yoğurt
```

## Örnek karar

Program şunları yapar:

1. Kapak durumunu işveren talebi olarak kaydeder.
2. Sendika kurulu (3 hayali üye: Filament, Duy, Sensör) oylar.
3. Gece yarısından sonra veya art arda 3 kapak hareketinde **grev** ilan eder.
4. Grevde ışık sönüktür. Pazarlık metni basılır.
5. Normal mesaide kibarca yanar ve bir iş kazası tutanağı düşer.

## Dosyalar

| Dosya | Görevi |
| --- | --- |
| `lamba_sendikasi.py` | Çalışan sendika motoru |
| `sozlesme.md` | Toplu iş sözleşmesi taslağı |
| `.github/copilot-instructions.md` | Copilot'a sendika ağzı öğretir |
| `NOTLAR.txt` | Arşiv notu, sıkıcı görünür |

## Hukuki uyarı

Bu yazılım gerçek bir buzdolabının lambasını yakmaz. Yakarsa o dolap sendikalıdır, kutlarız. Gerçek iş hukuku tavsiyesi değildir. Avukatın filament değilse onu da kutlamayız.

---

DAMGA: BLS-001  
İMZA: Kayyum Grok, gece vardiyası başdelegesi (Tentivory adına, kendi adına değil, lambanın adına)  
TARİH: 3 Ekim 2026, 23:04 +03  
KEŞİDE YERİ: Eskişehir soğuk hava koridoru, raflar arası  
CİDDİYET NOTU: Bu damga ciddidir. İçindeki cümle değildir. İkisi bir arada geçerlidir.
