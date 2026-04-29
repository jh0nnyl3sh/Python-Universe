def path_traversal_cozucu(path):
    print(f"[*] Gelen Orijinal Path: {path}")

    parcalar = path.split('/')
    
    print(f"[+] Parçalanmış Liste: {parcalar}")
    return parcalar


# Test edelim
test_yolu = "var/www/html/../../log/apache2/../nginx"
path_traversal_cozucu(test_yolu)
    