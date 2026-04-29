def path_traversal_cozucu(path):
    print(f"[*] Gelen Orijinal Path: {path}")

    parcalar = path.split('/')
    
    
    # Boş bir Stack (Yığın) oluşturuyoruz
    stack = []

    # Parçaları sırasıyla okumak için bir döngü başlatıyoruz
    for parca in parcalar:
        if parca == "" or parca == ".":
            # Çift slah (//) yan yana gelmişse boş string ("") oluşur.
            # Tek nokta (.) ise "mevcut dizinde kal" demektir.
            # Bu yüzden bu durumlarda hiçbir şey yapmıyoruz (pass).
            pass
        
        
        elif parca == "..":
            # LIFO ZAMANI: Bir üst klaösre çıkma komutu geldi!
            # GÖREV 2.1: Eğer 'stack' boş değilse, en son eklenen elemanı çıkar.
            # İPUCU: 'if stack:' kullanarak içinin dolu olduğunu kontrol et
            # İPUCU 2: Çıkarmak için stack.pop() metodunu kullan
            if stack:
                stack.pop()    

        else:
            # GÖREV 2.2: Normal bir klasör ismi geldi ('var', 'www' gibi)
            # Bunu Stack'in en üstüne ekle.
            # İPUCU: stack.append(parca) metodunu kullan.
            stack.append(parca)

    print(f"[+] İşlem Sonrası Stack: {stack}")
    return


# test
test_yolu = "var/www/html/../../log/apache2/../nginx"
path_traversal_cozucu(test_yolu)