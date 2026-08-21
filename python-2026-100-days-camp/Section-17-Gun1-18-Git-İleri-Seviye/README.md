# Section 17 - Gün 18: Git İleri Seviye Notları
- Bu repository Git üzerinde ileri seviye işlemleri ve komutları anlamak amacıyla oluşturulmuştur. Aşağıda temel başlıkların açıklamaları ve kullanım örnekleri yer almaktadır.

# 1.Merge Örnekleri
- Farklı `branch`'lerde yapılan geliştirmeleri birleştirmek için `merge` işlemi kullanılır. Temel olarak iki yaygın `merge`türü vardır:
- **1.Fast-Forward Merge**: Eğer ana `branch`üzerinde hiçbir yeni `commit`yoksa, Git sadece işaretçiyi (pointer) ileri taşır.
- **2.3-Way Merge**: Her iki `branch`de kendi commit geçmişine sahipse, Git bu iki geçmişi birleştirerek yeni bir `merge commit`oluşturur.

### 1.1.Merge Kullanımı
`
**Bash**
#Hangi branch'e entegre edilecekse o branch'e geçiş yapılır.
- `git checkout main`

#Diğer branch main üzerine merge edilir.....
- `git merge feature-branch`
`

## 2.Conflict Çözmek
- Aynı dosyanın aynı satırlarında farklı `branch`'lerde değişiklik yapıldığında Git bu durumu otomatik birleştiremez ve bir `conflict` oluşturur.

- Çözüm Adımları : 
- 1. Git, `conflict` olan dosyaları `modified` olarak işaretler. Dosyayı açtığında şu işaretçileri görürsün:
- `
`Planintext`
<<<<<<<< HEAD 
mevcut bracnh'teki kod
========
Gelen branch'teki (merge edilen) kod
>>>>>>>> feature-branch

`


## 3.Commitler Arası Gezmek

## Reset ve Revert

## Stash ve Tag