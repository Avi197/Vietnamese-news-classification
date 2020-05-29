# Vietnamese news classification
Data crawl from multiple big name news papers in Vietnam: `Dantri`, `Tuoitre`, `Thanhnien`, `Vietnamnet`,`Vnexpress`, `Vtv`


### Tokenizing
All text is tokenized using VnCoreNLP


### Data structure
Each line contain a list of labels, followed by the corresponding title
All label start with ```__label__``` prefix

Apply word segmentation on each label, space got replace with ``-``


#### E.g: 
```
__label__cà_phê-Trung_Nguyên __label__Buôn_Ma_Thuột __label__Đặng_Lê_Nguyên_Vũ __label__Giấc-mơ __label__Trung_Nguyên Hành_trình ông chủ Trung_Nguyên mang giấc mơ từ quê nghèo ra thế_giới 
```










### Data problem:  
 
###### Dantri is absolutely horrible
- large amount of records are unusable, which are titles with bad tags, not related tags
- some tags are just too long, contain many smaller tags but are treated as one single tag
- no category fields in original crawled data file (possible bad crawling)

###### Vnexpress
- many tags are just copy of the titles, some time add an extra string ` - VnExpress Đời sống`
- some tags are just copy of the titles, but randomly split into smaller string and
then add ` - VnExpress Đời sống` to the last smaller string, and
those smaller string become tags for the title
- some title are just broken, very short, make no sense, contain half a word, or a single character, ... titles might be cut off after the dash symbol, e.g: máy bay F-22 => máy bay F (possibly bad crawling)

###### Vnn
- contain some english news
- some titles have irrelevant, non related marking tags, e.g: `vnn`, `vietnamnet doc bao`, ...
- one/ a few(?) record(s) have tag which is just a url
- lots of tags are conjoined (eg: "thương mại" is written as "thươngmại")

###### Tuoitre
- lots of titles with no tags
- some titles are just 'Noname'

