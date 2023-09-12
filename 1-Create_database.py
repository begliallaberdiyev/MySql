import pymysql

try:
    # Veritabanı bağlantısı oluşturma
    db_connection = pymysql.connect(
        host="localhost",   # MySQL sunucu adresi
        user="kullanici_adi",   # MySQL kullanıcı adı
        password="parola",  # MySQL kullanıcı parolası
    )

    # Veritabanı işlemcisi oluşturma
    db_cursor = db_connection.cursor()

    # Schooldb veritabanını oluşturma sorgusu
    create_db_query = "CREATE DATABASE IF NOT EXISTS schooldb"

    # Veritabanı oluşturma işlemi
    db_cursor.execute(create_db_query)

    # Veritabanı seçimi
    db_cursor.execute("USE schooldb")

    # Students tablosunu oluşturma sorgusu
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        StudentNumber INT,
        Name VARCHAR(50),
        Surname VARCHAR(50),
        Birthdate DATE,
        Gender VARCHAR(10)
    )
    """

    # Tabloyu oluşturma işlemi
    db_cursor.execute(create_table_query)

    # Değişiklikleri kaydet
    db_connection.commit()

    print("schooldb veritabanı ve students tablosu oluşturuldu.")

except pymysql.Error as e:
    print("Hata:", e)

finally:
    # Bağlantıyı kapat
    db_cursor.close()
    db_connection.close()
