import discord


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')
    print('------')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Teknoloji kirliliği gelecekte sorun'):
        await message.channel.send("İnsanları bilinçlendirirsek sorun çıkmaz.")
    elif message.content.startswith('Teknolojik aletlerin hep yeni modeli'):
        await message.channel.send("Eğer insanların işlerini görüyorsa teknolojik cihazlarının yenisini almasına gerek yoktur.")
    elif message.content.startswith("Teknolojik silahların aşırı gelişmesi"):
        await message.channel.send("Teknolojik silahların yani atom bombası/hidrojen bombası gibi silahlar hem doğayı hemde insan yaşamını olumsuz etkiliyor. Bu yüzden üretimleri durdurulması gerek.")
    elif message.content.startswith("Bilgi kirliliği"):
        await message.channel.send("Bilgi kirliliğinin önüne geçmek için arama motorlarının kendinden bilgiyi birden çok kaynakta araştırıp bize sadece tek sonuç çıkartması gerekir.")
  
client.run("token")
