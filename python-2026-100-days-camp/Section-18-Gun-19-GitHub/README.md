# GitHub Kullanım Rehberi

Bu `repository`, GitHub üzerinde proje yönetimi, kod paylaşımı ve takım çalışması süreçlerini anlamak için hazırlanmıştır. Aşağıda GitHub'ın temel özellikleri ve sık kullanılan komutlar yer almaktadır.

## Remote Repository ve Clone

GitHub, projelerini bulut üzerinde barındırdığın bir **Remote Repository** (uzak depo) hizmetidir. GitHub üzerindeki bir projeyi kendi bilgisayarına (Local) indirmek için `clone` işlemi yapılır.

**Kullanımı:**
```bash
# Mevcut bir GitHub projesini bilgisayara indirmek için
git clone [https://github.com/kullaniciadi/proje-adi.git](https://github.com/kullaniciadi/proje-adi.git)

# İndirilen projenin klasörüne girmek için
cd proje-adi
```

## Local Repository'yi GitHub'a Bağlamak

Kendi bilgisayarında oluşturduğun (Local) bir projeyi GitHub'daki bir `repository`'ye bağlamak için `remote` eklemen gerekir.

**Kullanımı:**
```bash
# Projeye GitHub bağlantısını (origin adıyla) eklemek
git remote add origin [https://github.com/kullaniciadi/proje-adi.git](https://github.com/kullaniciadi/proje-adi.git)

# Mevcut bağlantıları listelemek için
git remote -v
```

## Push ve Pull İşlemleri

Yerelde yaptığın değişiklikleri GitHub'a göndermek veya GitHub'daki yeni güncellemeleri kendi bilgisayarına çekmek için kullanılır.

*   **Push:** `Local` ortamdaki `commit`'leri `Remote` sunucuya (GitHub) gönderir.
*   **Pull:** `Remote` sunucudaki (GitHub) değişiklikleri alır ve otomatik olarak senin mevcut `branch`'in ile `merge` eder.

**Kullanımı:**
```bash
# İlk defa gönderirken branch'i remote'a bağlamak için (-u veya --set-upstream)
git push -u origin main

# Daha sonraki gönderimler için sadece
git push

# GitHub'daki son güncellemeleri yerel projeye çekmek için
git pull origin main
```

## Fork ve Pull Request (PR)

Özellikle açık kaynak (Open Source) projelerde veya kalabalık takım çalışmalarında kullanılan en önemli süreçtir.

*   **Fork:** Başkasına ait bir `repository`'nin birebir kopyasını kendi GitHub hesabına oluşturma işlemidir. Bu işlem GitHub arayüzündeki **"Fork"** butonu ile yapılır.
*   **Pull Request (PR):** Kendi `branch`'inde veya `fork` ettiğin projede yaptığın geliştirmelerin, orijinal (veya ana) `branch`'e `merge` edilmesi için açtığın birleştirme talebidir. Takım arkadaşların bu talebi inceler (Code Review) ve onaylarsa kod ana projeye dahil edilir.

## Issues ve GitHub Actions (Ekstra Özellikler)

*   **Issues:** Projedeki hataları (bug), eklenecek yeni özellikleri (feature) veya yapılacak görevleri takip etmek için kullanılan tartışma/bildirim panosudur. Her bir `Issue`'ya etiketler (labels) atanabilir ve belirli kişilere yönlendirilebilir.
*   **GitHub Actions:** Projene CI/CD (Sürekli Entegrasyon ve Sürekli Dağıtım) süreçleri eklemeni sağlar. Örneğin; her `push` işleminde kodların otomatik test edilmesi veya sunucuya otomatik `deploy` (yükleme) edilmesi gibi işlemleri `.yml` dosyaları ile yönetebilirsin.