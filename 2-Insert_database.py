import pymysql
from datetime import datetime  
try:
    # Veritabanı bağlantısı
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="parola",
        database="schooldb"
    )

    while True:
        # Kullanıcıdan giriş al
        student_number = int(input("Öğrenci numarasını girin: "))
        student_name = input("Öğrenci adını girin: ")
        student_surname = input("Öğrenci soyadını girin: ")
        birthdate_str = input("Doğum Tarihini girin (GG.AA.YYYY): ")
        Gender = input("Cinsiyet Gir:")

        # Doğum tarihini datetime formatına çevir
        birthdate = datetime.strptime(birthdate_str, '%d.%m.%Y')

        # Bağlantı üzerinden bir cursor oluştur
        cursor = mydb.cursor()

        # SQL sorgusu
        sql_query = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate,Gender) VALUES (%s, %s, %s, %s, %s)"

        # Sorguyu çalıştır
        cursor.execute(sql_query, (student_number, student_name, student_surname, birthdate, Gender))

        # Değişiklikleri kaydet
        mydb.commit()
        print("Öğrenci başarıyla eklendi.")

        # Kullanıcıdan devam etmek isteyip istemediğini sor
        devam_et = input("Devam etmek istiyor musunuz? (Evet / Hayır): ")
        if devam_et.lower() != "evet":
            break  # Döngüyü kapat

except pymysql.Error as err:
    print(f"Hata: {err}")

finally:
    # Bağlantı ve cursor'ı kapat
    if 'cursor' in locals():
        cursor.close()
    if 'mydb' in locals():
        mydb.close()