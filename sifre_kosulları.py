dogru_kullanici = "admin"
dogru_sifre = "1234"

# Kullanıcıdan giriş alalım
kullanici_adi = input("Kullanıcı adınızı girin: ")
sifre = input("Şifrenizi girin: ")

# Bilgileri kontrol edelim
if kullanici_adi == dogru_kullanici and sifre == dogru_sifre:
    print("Sisteme hoş geldiniz! Giriş başarılı.")
elif kullanici_adi != dogru_kullanici:
    print("Hata: Kullanıcı adı sistemde kayıtlı değil.")
else:
    print("Hata: Şifreniz yanlış, lütfen tekrar deneyin.")
