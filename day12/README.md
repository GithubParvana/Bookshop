## E-commerce by Flask

### 12.day tasks

* Proyektə SQLAlchemy quraşdırılmalıdır
* Book modeli düzəldilməlidir (fildlər: id, title, author, price, description, image_url, stock, genre, language, publisher)
* Databazaya 6 fərqli kitab məlumatları daxil edilməlidir. (insert)
* İndex səhifəsinin render funksiyasında Book modelinin bütün obyektləri çağırılaraq tamplate-ə göndərilməlidir.
* Template-də jinja vasitəsi ilə bütün kitablar ekrana çıxarılmalıdır. (for loop)


### Step 2

* Əlavə dinamik route yaradılmalıdır. ('/book/<int:book_ind>')
* Dəyişən olaraq book_ind almalıdır.
* Funksiya verilən kitab indeksinə uyğun gələn kitabı databazadan seçməli və həmin kitab obyektini template-lə birgə render etməlidir.
* Tamplate folderində book.html adında yeni fayl yaradılmalıdır. Yuxarıdakı funksiya bu faylı render etməlidir.
* Bu fayl product.html səhifəsi ilə birəbir eyni olacaq. Kitab haqqında bütün məlumatlar render zamanı dinamik dəyişəcək.
* Ana səhifədə kitabların Ətraflı düyməsinə basdıqda, müvafiq olaraq http://127.0.0.1:5000/book/`həmin kitabın id-si` url-inə yönlənməlidir.


### Extra

* Genre və language modelləri yaradın
* Book modellərinin uyğun field-ləri ilə bu modellər arasında əlaqə yaradın.
* book.html faylında jinja-da da dəyişiklik etmək lazım olacaq.