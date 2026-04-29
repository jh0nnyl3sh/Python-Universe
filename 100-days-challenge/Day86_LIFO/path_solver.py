def path_traversal_cozucu(path):
    print(f"\n[*] Gelen Orijinal Path: {path}")

    parcalar = path.split('/')
    stack = []

    for parca in parcalar:
        if parca == "" or parca == ".":
            pass
        elif parca == "..":
            if stack:
                stack.pop()    
        else:
            stack.append(parca)

    print(f"[+] İşlem Sonrası Stack: {stack}")
    
    # GÖREV 3: Stack içindeki elemanları '/' ile birleştir.
    # Unix tabanlı sistemler (senin MacBook veya hedef Linux makinesi)
    # path'lerin başında her zaman bir kök dizin işareti ('/') bekler.
    # İPUCU: final_path = "/" + "/".join(stack)
    final_path = "/" + "/".join(stack)
    
    print(f"[+] Çözülmüş Nihai Path: {final_path}")
    return final_path

# Test edelim
test_yolu = "var/www/html/../../log/apache2/../nginx"
path_traversal_cozucu(test_yolu)