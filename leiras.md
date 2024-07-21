A beadandóm témájának a képfelismerést választottam, elkészítéséhez az órai anyagot 
(object detection picture version mappa) és a GitHub Copilotot használtam fel.

A teljes kód az object_detection.py és multiple_object_detection.py fájlokban van, a pic_upload.py fájlban pedig egy alap volt a 
képfeltöltésnek és az ablak megjelenítésének (amit átmásoltam és átalakítottam a másik fájlban).
A launcher.py pedig egy indító ablak, ahol lehet választani, hogy egy objektumot vagy többet szeretnénk analizálni.

A felépítésük úgy néz ki, hogy a coco.name.two nevű fájlban lévő, 
előre megadott objektumokat egy listába helyeztem, és ezen objektumok közül választhatunk egyet vagy többet 
attól függően, melyikre mentünk rá. 
Ha egy objektumos ablak van, akkor egyre rákattintunk, a kép feltöltéséhez szükséges ablak megjelenik, kiválasztunk egy tetszőleges képet, 
majd megjelenik az analizált kép ablaka, illetve egy üzenetet mutató ablak, ami kiírja, hogy a kiválasztott 
képen látható-e a kiválasztott objektum vagy sem.
Ha több objektumos van, akkor többet ki lehet jelölni a listából, és egy analizálás nevű gombra kattintva tudjuk meg az eredményt,
az üzenetet mutató ablakban pedig ki vannak válogatva azok a kijelölt objektumok, amik láthatóak a képen, és amik nem.

Több funkciót és if elágazásokat is alkalmaztam, mert például a képernyők bezárásával voltak gondok, 
mivel azok a képernyők is bezárultak sokszor, amiknek nem kellett volna, ezért több részre szedtem a kódot,
így sikerült elérni, hogy minden helyesen működjön. Még azt is megcsináltam, hogy a kép bezárása után is lehessen
választani még objektumot és képet, amik szintén analizálásra kerülnek, mert alapjáraton véve csak egyszer futott
volna le.

Nagyon tetszett ez a téma, sok lehetőség van benne, bővíteni is lehetett volna még, de így is sikerült elmerülni benne.