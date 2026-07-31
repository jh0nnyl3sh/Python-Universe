# Section 16 - Gün 17: Version Kontrol Sistemleri

## 1. Git Başlatmak (`git init`)
- Bir klasörü Git ile takip edebilir bir repository haline getirmek için kullanılan ilk komuttur. Bu komut çalıştırıldığında, ilgili dizinde `.git` adında gizli bir klasör oluşturulur ve **Git** bu andan itibaren dosyalardaki tüm değişiklikleri izlemeye başlar.



**Bash**
`
#Proje dizininde Gti'i başlatır
- `git init`



## 2. İlk Commit
- Git'te yaptığınız değişiklikleri kaydetme işlemine `commit` denir. Ancak bir dosyayı commit etmeden önce onu `staging area`'ya eklemeniz gerekir. İlk commit, genellikle projenin iskeletinin oluşturulduğu anı temsil ederi.

**Bash**
`
#Tüm dosyaları staging area'ya ekler
- `git add .`

#Değişiklikleri bir mesaj ile birlikte commit eder
- `git commit -m "Initial commit"`
`



## 3. Commit Örnekleri
#İyi bir commit mesajı, yapılan değişikliğin amacını net bir şekilde açıklamalıdır. Gelecekte kod geçmişine bakıldığında, hangi değişikliğin neden yapıldığı kolayca anlaşılabilmelidir.

**Bash**
`
#Yeni bir özellik eklendiğinde
- `git commit -m "Add user authentication feature"`

#Bir hata düzeltildiğinde
- `git commit -m "Fix database connection timeout error"`

#Dokümantasyon güncellendiğinde
- `git commit -m "Update README.md with setup instructions"`
`

## 4. Branch Nedir?
#Branch, projenin ana kod tabanından (genellikle `main` veya `master`) bağımsız olarak yeni özellikler geliştirmek veya hata düzeltmeleri yapmak için oluşturulan izole çalışma ortamıdır.
#Bir branch üzerinden yaptığımız hiçbir değişiklik, siz onaylamayana kadar diğer branch'leri etkilemez. Bu sayede canlı sistemdeki kodu bozmadan güvenle kod yazabilirsiniz.


## 5. Branch Örnekleri
#Günlük geliştirme sürecinde yeni branch oluşturmak ve branch'ler arasında geçiş yapmak oldukça yaygındır.

**Bash**
`
#Mevcut branch'leri listeler
- `git branch`

#"feature-login" adında yeni bir branch oluşturur
- `git branch feature-login`

#Oluşturulan "feature-login" branch'ine geçiş yapar
- `git checkout feature-login`
- `git switch feature-login`
- #NOT: checkout commitler arasında gezmek içinde kullanılır. Bu sebeple branch'ler arasında geçiş yaparken `switch` kullanacağız.

#TEK ADIMDA: Yeni bir branch oluşturur ve anında o branch'e geçer
- `git chechout -b feature-payment`
`


## 6. Merge İşlemleri
#Farklı bir branch üzerinde yaptığınız geliştirmeler tamamlandığında, bu değişiklikleri ana kod tabanına entegre etemek için `merge` işlemi yapılır.

#Örneğin, `feature-login` isimli branch'te çalıştığınızı ve işinizi bitirdiğinizi varsayalım. 

**Bash**
`
#1.Önce değişiklikleri alacağımız hedef (ana) branch'e geçiş yapıyoruz.
- `git checkout main`

#Üzerinde çalıştığımız branch'i, şu an bulunduğumuz (main) branch ile merge ediyoruz.
`git merge feature-login`

`


