# Vietnamese-news-classification

Data crawl from multiple big name news papers in Vietnam: `Dantri`, `Tuoitre`, `Thanhnien`, `Vietnamnet`,`Vnexpress`, `Vtv`


All text is tokenized using VnCoreNLP

Each line contain a list of labels, followed by the corresponding title
All label start with ```__label__``` prefix

Apply word segmentation on each label, space got replace with ``-``

E.g: 
```
__label__cà_phê-Trung_Nguyên __label__Buôn_Ma_Thuột __label__Đặng_Lê_Nguyên_Vũ __label__Giấc-mơ __label__Trung_Nguyên Hành_trình ông chủ Trung_Nguyên mang giấc mơ từ quê nghèo ra thế_giới 
```










#### Note:  
###### Dantri
- Dantri has a lot of titles with wrong tags    
- Scripts can pick up around half of the data as usable data    
- The rest might have to be pick manually
 
###### Vnexpress
 - Vnexpress has tags that contain `- VnExpress Đời sống` are just title that are split randomly into tags 
