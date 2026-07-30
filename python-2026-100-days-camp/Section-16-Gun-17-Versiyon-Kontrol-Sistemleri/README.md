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
- git commit -m "Add user authentication feature"

#Bir hata düzeltildiğinde
- git commit -m "Fix database connection timeout error"

#Dokümantasyon güncellendiğinde
- git commit -m "Update README.md with setup instructions"
`

## 4. Branch Nedir?
## 5. Branch Örnekleri
## 6. Merge İşlemleri


