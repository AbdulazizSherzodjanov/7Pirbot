import logging
from buttons import *
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("🇺🇿 Assalomu alaykum ! Tilni Tanlang 👇\n🇷🇺 Привет! Выберите язык 👇\n🇺🇸 Hello ! Select the language 👇",reply_markup=languages)
@dp.message_handler(commands=['set_lang'])
async def send_welcome(message: types.Message):
  await message.reply("🇺🇿 Tilni Tanlang 👇\n🇷🇺 Выберите язык 👇\n🇺🇸 Select the language 👇",reply_markup=languages)
@dp.message_handler(types.Message)
async def bankomat(message:types.Message):
  if message.text == "O'zbekcha 🇺🇿":
    await message.reply("O'zbekcha 🇺🇿",reply_markup=buttonlar)
  elif message.text == 'Русский 🇷🇺':
    await message.reply('Русский 🇷🇺',reply_markup=rubuttonlar)
  elif message.text == 'Банкоматы':
    await message.reply('Банкоматы в Бухаре 👇',reply_markup=rubankomatlarbutton)
  elif message.text == 'Bankomatlar':
    await message.reply('Buxoradagi Bankomatlar\nIsh vaqti 24/7 👇',reply_markup=bankomatlarbutton)
  elif message.text == '1-Bankomat':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D0%B4+24%2F7/@39.7709877,64.444743,19.33z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f500524f4b527a9:0x46076dbe7d3b74ff!8m2!3d39.7712047!4d64.4449915!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11hdnrd5my')
  elif message.text == '2-Bankomat':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82%D1%8B+24%2F7/@39.7550581,64.4265485,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f50071c51f3a333:0x12237ee4bddf3d3f!8m2!3d39.7551015!4d64.4274959!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11hzd03ms0')
  elif message.text == '3-Bankomat':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+24%2F7/@39.7629056,64.4251391,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f500747aeb140d9:0x99b6dcebbc754cf7!8m2!3d39.7629056!4d64.42633!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11h23t5clx')
  elif message.text == '4-Bankomat':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+IPAK+YOLIBANKI/@39.7735238,64.4191192,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f5007992c4b318b:0xea64f37a44d4c8c5!8m2!3d39.7735238!4d64.4203101!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11syz4kbl0')
  elif message.text == '5-Bankomat':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+Kapitalbank/@39.7736336,64.4204986,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f5007377f02f33d:0x1d0e0ded7ed260c1!8m2!3d39.7736336!4d64.4216895!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11qbbh7k4r')
  elif message.text == 'Restoranlar Va Kafelar ☕️':
    await message.reply('Buxoradagi Restoranlar Va Kafelar ☕️\nIsh vaqti 24/7 👇',reply_markup=restoranlar)
  elif message.text == '1-Restoran':
    await message.reply('https://www.google.com/maps/place/Rozmarin+Cafe/@39.7710162,64.4080229,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f5007ac46c67141:0x6ccf4b0a9f07ebb8!8m2!3d39.780669!4d64.4309001!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11s56svkz3')
  elif message.text == '2-Restoran':
    await message.reply('https://www.google.com/maps/place/%D0%A0%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD+Ismoil/@39.7710162,64.4080229,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f500799563597b9:0x908501b9fd3ba57!8m2!3d39.7481425!4d64.4266572!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11h53fkb8g')
  elif message.text == '3-Restoran':
    await message.reply('https://www.google.com/maps/place/Lavita/@39.7375064,64.3953082,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f500429bffaadf5:0xdd64b98a616eda33!8m2!3d39.7374348!4d64.4334163!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11dzt564mj')
  elif message.text == '4-Restoran':
    await message.reply('https://www.google.com/maps/place/Edem/@39.7728194,64.3931479,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f5007faaf82f43d:0xa41a2829be7f95a7!8m2!3d39.7728194!4d64.4312567!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11qnt0b1vt')
  elif message.text == '5-Restoran':
    await message.reply('https://www.google.com/maps/place/Spanish+bar/@39.7728194,64.3931479,14z/data=!4m9!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m5!1s0x3f5005e361c853d3:0x9bb7b0be9453c107!8m2!3d39.7720462!4d64.4377956!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA')
  elif message.text == 'Dorixonalar':
    await message.reply('Buxoradagi Dorixonalar\nIsh vaqti 24/7 👇',reply_markup=aptekalar)
  elif message.text == '1-Dorixona':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5008bdcb12fe61:0xd314d10e2f1c419b!8m2!3d39.7903128!4d64.4110362!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11csqbkgpz')
  elif message.text == '2-Dorixona':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5007d1019ba037:0x8ff576b5cf41fef8!8m2!3d39.7721807!4d64.4316827!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g0723swy')
  elif message.text == '3-Dorixona':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0+%22Europharm%22/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005813a382953:0xaefcd093f25dc7bd!8m2!3d39.7681199!4d64.443689!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11j23vsktd')
  elif message.text == '4-Dorixona':
    await message.reply('https://www.google.com/maps/place/Arzon+Dorixona/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005ad45a5d76b:0xe03cca738405b81a!8m2!3d39.7804658!4d64.4336889!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11fv7vd_h4')
  elif message.text == '5-Dorixona':
    await message.reply('https://www.google.com/maps/place/Apteka/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f50072dd9537d09:0x4014db8bc96df75c!8m2!3d39.7802303!4d64.429065!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11j5tt_h0h')
  elif message.text == 'Shoshilinch xizmat telefon raqamlari ☎️':
    await message.reply('Shoshilinch xizmat telefon raqamlari☎️\n📞101   -  Yong`in xavfsizligi xizmati\n📞102   -  Ichki ishlar organlari 🚓\n📞103   -  Birinchi tibbiy yordam 🚑\n📞104   -  Favqulodda gaz xizmati\n📞1050 - Qutqaruv xizmati (FVT)\n📞1008 -  Adliya vazirligining ishonch telefon liniyasi')
  elif message.text == 'Orqaga ⬅️':
    await message.reply('Orqaga ⬅️',reply_markup=buttonlar)
  elif message.text == '1-банкомат':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D0%B4+24%2F7/@39.7709877,64.444743,19.33z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f500524f4b527a9:0x46076dbe7d3b74ff!8m2!3d39.7712047!4d64.4449915!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11hdnrd5my')
  elif message.text == '2-банкомат':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82%D1%8B+24%2F7/@39.7550581,64.4265485,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f50071c51f3a333:0x12237ee4bddf3d3f!8m2!3d39.7551015!4d64.4274959!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11hzd03ms0')
  elif message.text == '3-банкомат':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+24%2F7/@39.7629056,64.4251391,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f500747aeb140d9:0x99b6dcebbc754cf7!8m2!3d39.7629056!4d64.42633!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11h23t5clx')
  elif message.text == '4-банкомат':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+IPAK+YOLIBANKI/@39.7735238,64.4191192,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f5007992c4b318b:0xea64f37a44d4c8c5!8m2!3d39.7735238!4d64.4203101!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11syz4kbl0')
  elif message.text == '5-банкомат':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+Kapitalbank/@39.7736336,64.4204986,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f5007377f02f33d:0x1d0e0ded7ed260c1!8m2!3d39.7736336!4d64.4216895!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11qbbh7k4r')
  elif message.text == 'Аптеки':
    await message.reply('Аптеки',reply_markup=ruaptekalar)
  elif message.text == 'Рестораны и кафе ☕️':
    await message.reply('Рестораны и кафе ☕️',reply_markup=rurestoranlar)
  elif message.text == '1-Аптека':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5008bdcb12fe61:0xd314d10e2f1c419b!8m2!3d39.7903128!4d64.4110362!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11csqbkgpz')
  elif message.text == '2-Аптека':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5007d1019ba037:0x8ff576b5cf41fef8!8m2!3d39.7721807!4d64.4316827!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g0723swy')
  elif message.text == '3-Аптека':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0+%22Europharm%22/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005813a382953:0xaefcd093f25dc7bd!8m2!3d39.7681199!4d64.443689!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11j23vsktd')
  elif message.text == '4-Аптека':
    await message.reply('https://www.google.com/maps/place/Arzon+Dorixona/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005ad45a5d76b:0xe03cca738405b81a!8m2!3d39.7804658!4d64.4336889!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11fv7vd_h4')
  elif message.text == '5-Аптека':
    await message.reply('https://www.google.com/maps/place/Apteka/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f50072dd9537d09:0x4014db8bc96df75c!8m2!3d39.7802303!4d64.429065!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11j5tt_h0h')
  elif message.text == '1-Ресторан':
    await message.reply('https://www.google.com/maps/place/Rozmarin+Cafe/@39.7710162,64.4080229,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f5007ac46c67141:0x6ccf4b0a9f07ebb8!8m2!3d39.780669!4d64.4309001!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11s56svkz3')
  elif message.text == '2-Ресторан':
    await message.reply('https://www.google.com/maps/place/%D0%A0%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD+Ismoil/@39.7710162,64.4080229,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f500799563597b9:0x908501b9fd3ba57!8m2!3d39.7481425!4d64.4266572!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11h53fkb8g')
  elif message.text == '3-Ресторан':
    await message.reply('https://www.google.com/maps/place/Lavita/@39.7375064,64.3953082,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f500429bffaadf5:0xdd64b98a616eda33!8m2!3d39.7374348!4d64.4334163!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11dzt564mj')
  elif message.text == '4-Ресторан':
    await message.reply('https://www.google.com/maps/place/Arzon+Dorixona/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005ad45a5d76b:0xe03cca738405b81a!8m2!3d39.7804658!4d64.4336889!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11fv7vd_h4')
  elif message.text == '5-Ресторан':
    await message.reply('https://www.google.com/maps/place/Spanish+bar/@39.7728194,64.3931479,14z/data=!4m9!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m5!1s0x3f5005e361c853d3:0x9bb7b0be9453c107!8m2!3d39.7720462!4d64.4377956!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA')
  elif message.text == 'назад ⬅️':
    await message.reply('назад ⬅️',reply_markup=rubuttonlar)
  elif message.text == 'Телефоны экстренных служб ☎️':
    await message.reply('Телефоны экстренных служб☎️\n📞101 - Пожарная служба\n📞102 - Органы внутренних дел 🚓\n📞103 - Скорая помощь 🚑\n📞104 - Аварийная газовая служба\n📞1050 - Аварийно-спасательная служба (СПС)\n 📞1008 - горячая линия Минюста')
  elif message.text == 'English 🇺🇸':
    await message.reply('English 🇺🇸',reply_markup=enbuttonlar)
  elif message.text == 'ATMs':
    await message.reply('ATMs',reply_markup=enbankomatlarb)
  elif message.text == 'Pharmacies':
    await message.reply('Pharmacies',reply_markup=enaptekalar)
  elif message.text == 'Restaurants And Cafes ☕️':
    await message.reply('Restaurants And Cafes ☕️',reply_markup=enrestoranlar)
  elif message.text == 'Emergency phone numbers ☎️':
    await message.reply('Emergency service phone numbers☎️\n📞101 - Fire safety service\n📞102 - Internal affairs bodies 🚓\n📞103 - First aid 🚑\n📞104 - Emergency gas service\n📞1050 - Rescue service (FVT )\n📞1008 - hotline of the Ministry of Justice')
  elif message.text == '1-ATM':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D0%B4+24%2F7/@39.7709877,64.444743,19.33z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f500524f4b527a9:0x46076dbe7d3b74ff!8m2!3d39.7712047!4d64.4449915!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11hdnrd5my')
  elif message.text == '2-ATM':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82%D1%8B+24%2F7/@39.7550581,64.4265485,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f50071c51f3a333:0x12237ee4bddf3d3f!8m2!3d39.7551015!4d64.4274959!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11hzd03ms0')
  elif message.text == '3-ATM':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+24%2F7/@39.7629056,64.4251391,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f500747aeb140d9:0x99b6dcebbc754cf7!8m2!3d39.7629056!4d64.42633!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11h23t5clx')
  elif message.text == '4-ATM':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+IPAK+YOLIBANKI/@39.7735238,64.4191192,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f5007992c4b318b:0xea64f37a44d4c8c5!8m2!3d39.7735238!4d64.4203101!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11syz4kbl0')
  elif message.text == '5-ATM':
    await message.reply('https://www.google.com/maps/place/%D0%91%D0%B0%D0%BD%D0%BA%D0%BE%D0%BC%D0%B0%D1%82+Kapitalbank/@39.7736336,64.4204986,19z/data=!4m10!1m2!2m1!1z0JHQsNC90LrQvtC80LDRgtGL!3m6!1s0x3f5007377f02f33d:0x1d0e0ded7ed260c1!8m2!3d39.7736336!4d64.4216895!15sChLQkdCw0L3QutC-0LzQsNGC0YuSAQNhdG3gAQA!16s%2Fg%2F11qbbh7k4r')

  elif message.text == 'Pharmacies':
    await message.reply('Pharmacies',reply_markup=enaptekalar)
  elif message.text == 'Restaurants And Cafes ☕️':
    await message.reply('Restaurants And Cafes ☕️',reply_markup=enrestoranlar)
  elif message.text == '1-Pharmacy':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5008bdcb12fe61:0xd314d10e2f1c419b!8m2!3d39.7903128!4d64.4110362!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11csqbkgpz')
  elif message.text == '2-Pharmacy':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5007d1019ba037:0x8ff576b5cf41fef8!8m2!3d39.7721807!4d64.4316827!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11g0723swy')
  elif message.text == '3-Pharmacy':
    await message.reply('https://www.google.com/maps/place/%D0%90%D0%BF%D1%82%D0%B5%D0%BA%D0%B0+%22Europharm%22/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005813a382953:0xaefcd093f25dc7bd!8m2!3d39.7681199!4d64.443689!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11j23vsktd')
  elif message.text == '4-Pharmacy':
    await message.reply('https://www.google.com/maps/place/Arzon+Dorixona/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005ad45a5d76b:0xe03cca738405b81a!8m2!3d39.7804658!4d64.4336889!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11fv7vd_h4')
  elif message.text == '5-Pharmacy':
    await message.reply('https://www.google.com/maps/place/Apteka/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f50072dd9537d09:0x4014db8bc96df75c!8m2!3d39.7802303!4d64.429065!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11j5tt_h0h')
  elif message.text == '1-Restaurant':
    await message.reply('https://www.google.com/maps/place/Rozmarin+Cafe/@39.7710162,64.4080229,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f5007ac46c67141:0x6ccf4b0a9f07ebb8!8m2!3d39.780669!4d64.4309001!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11s56svkz3')
  elif message.text == '2-Restaurant':
    await message.reply('https://www.google.com/maps/place/%D0%A0%D0%B5%D1%81%D1%82%D0%BE%D1%80%D0%B0%D0%BD+Ismoil/@39.7710162,64.4080229,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f500799563597b9:0x908501b9fd3ba57!8m2!3d39.7481425!4d64.4266572!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11h53fkb8g')
  elif message.text == '3-Restaurant':
    await message.reply('https://www.google.com/maps/place/Lavita/@39.7375064,64.3953082,14z/data=!4m10!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m6!1s0x3f500429bffaadf5:0xdd64b98a616eda33!8m2!3d39.7374348!4d64.4334163!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA!16s%2Fg%2F11dzt564mj')
  elif message.text == '4-Restaurant':
    await message.reply('https://www.google.com/maps/place/Arzon+Dorixona/@39.770901,64.4080229,14.25z/data=!4m10!1m2!2m1!1z0JDQv9GC0LXQutC4!3m6!1s0x3f5005ad45a5d76b:0xe03cca738405b81a!8m2!3d39.7804658!4d64.4336889!15sCgzQkNC_0YLQtdC60LhaDiIM0LDQv9GC0LXQutC4kgEIcGhhcm1hY3ngAQA!16s%2Fg%2F11fv7vd_h4')
  elif message.text == '5-Restaurant':
    await message.reply('https://www.google.com/maps/place/Spanish+bar/@39.7728194,64.3931479,14z/data=!4m9!1m2!2m1!1z0KDQtdGB0YLQvtGA0LDQvdGL!3m5!1s0x3f5005e361c853d3:0x9bb7b0be9453c107!8m2!3d39.7720462!4d64.4377956!15sChLQoNC10YHRgtC-0YDQsNC90YtaFCIS0YDQtdGB0YLQvtGA0LDQvdGLkgEKcmVzdGF1cmFudOABAA')
  elif message.text == 'Back ⬅️':
    await message.reply('Back ⬅️',reply_markup=enbuttonlar)
  elif message.text == 'Mehmonxonalar':
    await message.reply('Mehmonxonalar',reply_markup=uzhotelbuttons)
  elif message.text == 'Marvarid mehmonxonasi':
    await message.reply('Manzil : G`ijduvon tumani, Yusuf Hamadoniy ko`chasi, 91-uy\nTelefon : 65. 57-27-137\nXizmatlar : Avtoturargoh, Nonushta, Wifi\nAdminstrator : Rizayev Ulug`bek +998 91-312-55-45\n50 kishiga mo`ljallangan\nStandart xonalar : 6ta\nEkonom xonalar : 13ta')
  elif message.text == 'Shodlik mehmonxonasi':
    await message.reply('Manzil : G`ijduvon tumani, Ahmad Donish ko`chasi 7/1 uy\nTelefon : 65.57-222-14\nAdminstrator : Raupova Musharraf +998 90 747-45-07\nXizmatlar : Avtoturargoh, Nonushta, Wifi\n80 kishiga mo`ljallangan\nLyuks xonalar : 48ta\nPollyuks xonalar : 20ta')
  elif message.text == 'Poykent Bukhara mehmonxonasi':
    await message.reply('Manzil : Kogon tumani, Suxor MFY, Sayyid Amir Kulol ko`chasi, Sayyid Amir Kulol ziyoratgohida\nTelefon: +998 65 220 65 40\nAdminstrator: Umarxodjayev Abdulla  +998 98 123-49-44\n14ta xona, 35ta o`rin')
  elif message.text == 'Burji Buxoro mehmonxonasi':
    await message.reply('Manzil : Kogon Tumani, B.Naqshband QFY, Bahouddin Naqshband ziyoratgohi yonida\nTelefon : 65.221-58-50;  65-52-76-1-66\nAdminstrator : Berdiyev Rustam +998 90 715-02-04\n18ta xona, 36ta o`rin')
  elif message.text == 'Hotels':
    await message.reply('Hotels',reply_markup=enhotelbuttons)
  elif message.text == 'Marvarid Hotel':
    await message.reply('Address: Yusuf Hamadoni street, 91, G`iduvan district\nTelephone: 65. 57-27-137\nServices: Parking, Breakfast, Wifi\nAdminstrator: Rizayev Ulug`bek +998 91-312-55-45 \nDesigned for 50 people\nStandard rooms: 6\nEconomy rooms: 13')
  elif message.text == 'Shodlik Hotel':
    await message.reply('Address: 7/1 Ahmed Donish street, G`iduvan district\nTelephone: 65.57-222-14\nAdminstrator: Raupova Musharraf +998 90 747-45-07\nServices: Parking, Breakfast, Wifi\nFor 80 people designed\nLuxury rooms: 48\nPolyluxury rooms: 20')
  elif message.text == 'Poykent Bukhara Hotel':
    await message.reply('Address: Sayyid Amir Kulol Street, Sayyid Amir Kulol Shrine, Kogon District, Sukhor MFY\nTelephone: +998 65 220 65 40\nAdminstrator: Umarkhodjayev Abdulla +998 98 123-49-44\n14 rooms, 35 beds')
  elif message.text == 'Burji Bukhara Hotel':
    await message.reply('Address: Kogon District, B. Naqshband QFY, near Bahauddin Naqshband shrine\nTelephone: 65.221-58-50; 65-52-76-1-66\nAdminstrator: Berdiyev Rustam +998 90 715-02-04\n18 rooms, 36 beds')
  elif message.text == '⬅️Back':
    await message.reply('⬅️Back',reply_markup=enbuttonlar)
  elif message.text == '⬅Orqaga':
    await message.reply('⬅Orqaga',reply_markup=buttonlar)
  elif message.text == 'Отели':
    await message.reply('Отели',reply_markup=ruhotelbuttons)
  elif message.text == 'Марварид Отель':
    await message.reply('Адрес: улица Юсуфа Хамадони, 91, Гидуванский район\nТелефон: 65. 57-27-137\nУслуги: Парковка, Завтрак, Wifi\nАдминистратор: Ризаев Улугбек +998 91-312-55-45 \nРассчитан на 50 человек\nСтандартные номера: 6\nЭконом номера: 13')
  elif message.text == 'Шодлик Отель':
    await message.reply('Адрес: ул. Ахмеда Дониша, 7/1, район Гидуван\nТелефон: 65.57-222-14\nАдминистратор: Раупова Мушарраф +998 90 747-45-07\nУслуги: Парковка, Завтрак, Wi-Fi\nРассчитан на 80 человек\nНомера класса люкс : 48\nПолилюкс номеров: 20')
  elif message.text == 'Пойкент Отель':
    await message.reply('Адрес: улица Сайид Амир Кулол, храм Сайид Амир Кулол, Когонский район, Сухорский МФЮ\nТелефон: +998 65 220 65 40\nАдминистратор: Умарходжаев Абдулла +998 98 123-49-44\n14 номеров, 35 коек')
  elif message.text == 'Буржи Бухара Отель':
    await message.reply('Адрес: Когонский район, Б. Накшбанд QFY, возле храма Бахауддина Накшбанда\nТелефон: 65.221-58-50; 65-52-76-1-66\nАдминистратор: Бердиев Рустам +998 90 715-02-04\n18 номеров, 36 мест')



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)