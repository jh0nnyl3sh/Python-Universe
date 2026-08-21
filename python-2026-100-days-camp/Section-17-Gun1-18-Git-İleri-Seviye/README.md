# Section 17 - Gün 18: Git İleri Seviye Notları

Bu `repository`, Git üzerinde ileri seviye işlemleri ve komutları anlamak amacıyla oluşturulmuştur. Aşağıda temel başlıkların açıklamaları ve kullanım örnekleri yer almaktadır.

## Merge Örnekleri

Farklı `branch`'lerde yapılan geliştirmeleri birleştirmek için `merge` işlemi kullanılır. Temel olarak iki yaygın `merge` türü vardır:

*   **Fast-Forward Merge:** Eğer ana `branch` üzerinde hiçbir yeni `commit` yoksa, Git sadece işaretçiyi (pointer) ileri taşır.
*   **3-Way Merge:** Her iki `branch` de kendi `commit` geçmişine sahipse, Git bu iki geçmişi birleştirerek yeni bir `merge commit` oluşturur.

**Kullanımı:**
```bash
# Hangi branch'e entegre edilecekse o branch'e geçiş yapılır
git checkout main

# Diğer branch main üzerine merge edilir
git merge feature-branch
```

## Conflict Çözmek

Aynı dosyanın aynı satırlarında farklı `branch`'lerde değişiklik yapıldığında Git bu durumu otomatik birleştiremez ve bir `conflict` oluşturur. 

**Çözüm Adımları:**
1. Git, `conflict` olan dosyaları `modified` olarak işaretler. Dosyayı açtığında şu işaretçileri görürsün:
   ```text
   <<<<<<< HEAD
   Mevcut branch'teki kod
   =======
   Gelen branch'teki (merge edilen) kod
   >>>>>>> feature-branch
   ```
2. Hangi kodun kalması gerektiğine karar ver ve Git işaretçilerini (`<<<<<<<`, `=======`, `>>>>>>>`) manuel olarak sil.
3. Dosyayı kaydet ve `staging area`'ya ekle:
   ```bash
   git add dosya_adi.txt
   ```
4. İşlemi tamamlamak için `commit` oluştur:
   ```bash
   git commit -m "Merge conflict çözüldü"
   ```

## Commitler Arası Gezmek

Projenin geçmişindeki belirli bir duruma geri dönmek veya eski kodları incelemek için `checkout` komutu kullanılır. Bu işlem seni **"detached HEAD"** durumuna geçirir; yani sadece okuma yapabilirsin, kalıcı bir değişiklik yapmak için yeni bir `branch` açman gerekir.

**Kullanımı:**
```bash
# Geçmişteki commit'lerin hash (kimlik) değerlerini görmek için
git log --oneline

# Belirli bir commit'e gitmek için (örnek hash: a1b2c3d)
git checkout a1b2c3d

# Tekrar en güncel duruma (main branch'ine) dönmek için
git checkout main
```

## Reset ve Revert

Yapılan hatalı işlemleri veya `commit`'leri geri almak için iki farklı yöntem kullanılır:

*   **Reset:** `commit` geçmişini silerek geriye döner. Genellikle henüz `remote repository`'ye `push` edilmemiş yerel değişiklikler için kullanılır. Üç seviyesi vardır:
    *   `--soft`: `commit`'i iptal eder ama değişiklikleri `staging area`'da tutar.
    *   `--mixed` (Varsayılan): `commit`'i ve `staging area`'yı iptal eder, değişiklikler `working directory`'de kalır.
    *   `--hard`: Her şeyi siler ve dosyaları eski haline döndürür. **DİKKATLİ KULLANILMALIDIR.**
    ```bash
    git reset --hard HEAD~1 # Bir önceki commit'e tamamen geri döner
    ```

*   **Revert:** Mevcut `commit`'leri silmez. Bunun yerine, istenmeyen `commit`'teki değişiklikleri geri alan **yeni bir `commit`** oluşturur. Takım çalışmalarında, uzak sunucuya gönderilmiş kodlar için en güvenli yöntemdir.
    ```bash
    git revert <commit_hash>
    ```

## Stash ve Tag

*   **Stash:** Üzerinde çalıştığın ancak henüz `commit` atmaya hazır olmayan değişiklikleri geçici olarak saklamak için kullanılır. Bu sayede `working directory` temizlenir ve güvenle başka bir `branch`'e geçebilirsin.
    ```bash
    git stash          # Değişiklikleri saklar
    git stash list     # Saklanan değişikliklerin listesini gösterir
    git stash pop      # Saklanan değişiklikleri geri getirir ve stash listesinden siler
    ```

*   **Tag:** Projenin önemli noktalarını (örneğin v1.0, release-beta) etiketlemek için kullanılır. Genellikle versiyon sürümlerini (release) belirlemek için tercih edilir.
    ```bash
    git tag v1.0.0             # Bulunulan commit'e tag ekler
    git push origin v1.0.0     # Tag'i remote repository'ye gönderir
    ```