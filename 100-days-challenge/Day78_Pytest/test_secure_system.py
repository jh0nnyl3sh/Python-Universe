import pytest
import secure_system

# 1. FIXTURE TANIMLAMALARI (Hazırlık Merkezleri)
@pytest.fixture
def make_admin():
    """Testten önce kullanıcıyı Admin yapar, test bitince temizler."""
    original_role = secure_system.current_user["role"] # Eski rolü yedekle
    secure_system.current_user["role"] = "admin"       # Admin yap
    
    yield # BURASI ÇOK ÖNEMLİ: Testin kendisi burada çalışır!
    
    # Test bittikten sonra sistemi eski haline döndür (Teardown)
    secure_system.current_user["role"] = original_role

@pytest.fixture
def make_user():
    """Testten önce kullanıcıyı Normal User yapar."""
    original_role = secure_system.current_user["role"]
    secure_system.current_user["role"] = "user"
    
    yield
    
    secure_system.current_user["role"] = original_role


# 2. TESTLER (Sadece Fixture ismini parametre olarak veriyoruz!)
def test_admin_can_delete_record(make_admin):
    # Arrange kısmı Fixture tarafından halledildi! Sadece Act ve Assert yapıyoruz.
    result = secure_system.delete_database_record(404)
    assert result == "RECORD_404_DELETED"

def test_normal_user_is_denied(make_user):
    result = secure_system.delete_database_record(404)
    assert result == "ACCESS_DENIED"