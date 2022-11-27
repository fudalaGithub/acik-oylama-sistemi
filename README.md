# Açık Kaynak Oylama Sistemi.

Gelecekte insanlar, mutlaka cep telefonları ile yönetim kadrosuna dahil olmak zorundalar. Bu sistem de halkların, milletvekillerini elimine ederek, yönetime dahil olması durumunda, kullanılacak yazılıma kaynak olsun diye hazırlanmaktadır. Bu yazılımın çözmeyi vaat ettiği şey, açık kaynak kodların değiştirilmeden çalıştığını garanti ederek bir sistem oluşturmaktır. Destek olur ve el atarsanız seviniriz.

fudalaMail@gmail.com

### Neden Python ?

Oylama sistemi her türlü şaibeyi ortadan kaldırmalıdır. Açık kaynak ve platform bağımsız olmalıdır. Anlaşılır, basit ve bir o kadar da kullanıcıları korumalıdır. Tüm bunları sağlayabilecek başka diller de mutlaka vardır ama bizce Python açık kaynak kodlama ruhuna en uygun dildir.

### Oy Veren (Voter)

Sistemin oy veren (Voter) tarafında, kullanıcı bilgilerini korumak için hash algoritmalarını kullanacağız. Bizim tercihimiz SHA256 algoritmasıdır. Kullanıcı, cep telefonu ile, kişisel bilgilerini girerek kendi hash kodunu oluşturabilmelidir. Ad, Soyad, doğum tarihi , ana adı, baba adı gibi bilgiler yeterli olmayacakdır. Bunlara ilaveten, kullanıcıdan kendisine özgü 7 kelime daha girmesi istenecektir. Bunun sebebi, belediye (municipality) tarafında kötüye kullanımı engellemek içindir. Engellemeye çalıştığımız, yapmış olduğumuz sistemden kaynaklanan sorunları çözmek veya aynı hash'den iki tane olmasını önlemek değildir. İktidar, muhalefet, belediye çalışanları gibi, oylardan çıkar elde edebilecek, oy kullanmayan veya kullanamayan kişilerin bilgilerini kullanarak hash oluşturup, klon cihaz ve hash'lerle oylamaya dahil olmalarını engellemektir.  

Vatandaş, yasal oy kullanma yaşına ulaştığında, diğerleri gibi, hash kodunu veri tabanına ekletmelidir. TC vatandaşı olmayan kişilerin oy kullanmasını engellemek için, vatandaşlar bulundukları yerleşim yerlerinin büyük şehir belediyelerine gidip, veri tabanına kayıt olmalıdırlar. Her seçimde oy sandıklarına gidip gelme zahmeti bu sayede tek seferlik bir kayıt ile bitmiş olur.

