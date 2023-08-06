from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

uz = KeyboardButton("O'zbekcha 🇺🇿")
eng = KeyboardButton("English 🇺🇸")
ru = KeyboardButton("Русский 🇷🇺")
languages = ReplyKeyboardMarkup(resize_keyboard=True).add(uz).add(eng).add(ru)


bankomatlar = KeyboardButton('Bankomatlar')
dorixonalar = KeyboardButton('Dorixonalar')
hotels = KeyboardButton('Restoranlar Va Kafelar ☕️')
mehmonxonalar = KeyboardButton('Mehmonxonalar')
fastnumber = KeyboardButton('Shoshilinch xizmat telefon raqamlari ☎️')
buttonlar = ReplyKeyboardMarkup(resize_keyboard=True).add(bankomatlar).add(dorixonalar).add(hotels).add(fastnumber).add(mehmonxonalar)


enbankomatlar = KeyboardButton('ATMs')
endorixonalar = KeyboardButton('Pharmacies')
enhotels = KeyboardButton('Restaurants And Cafes ☕️')
enfastnumber = KeyboardButton('Emergency phone numbers ☎️')
enmehmonxonalar = KeyboardButton('Hotels')
enbuttonlar = ReplyKeyboardMarkup(resize_keyboard=True).add(enbankomatlar).add(endorixonalar).add(enhotels).add(enfastnumber).add(enmehmonxonalar)

rubankomatlar = KeyboardButton('Банкоматы')
rudorixonalar = KeyboardButton('Аптеки')
ruhotels = KeyboardButton('Рестораны и кафе ☕️')
rufastnumber = KeyboardButton('Телефоны экстренных служб ☎️')
rumehmonxonalar = KeyboardButton('Отели')
rubuttonlar = ReplyKeyboardMarkup(resize_keyboard=True).add(rubankomatlar).add(rudorixonalar).add(ruhotels).add(rufastnumber).add(rumehmonxonalar)


rubankomat1 = KeyboardButton('1-банкомат')
rubankomat2 = KeyboardButton('2-банкомат')
rubankomat3 = KeyboardButton('3-банкомат')
rubankomat4 = KeyboardButton('4-банкомат')
rubankomat5 = KeyboardButton('5-банкомат')
ruorqaga = KeyboardButton('назад ⬅️')
rubankomatlarbutton = ReplyKeyboardMarkup(resize_keyboard=True).add(rubankomat1).add(rubankomat2).add(rubankomat3).add(rubankomat4).add(rubankomat5).add(ruorqaga)

ruapteka1 = KeyboardButton('1-Аптека')
ruapteka2 = KeyboardButton('2-Аптека')
ruapteka3 = KeyboardButton('3-Аптека')
ruapteka4 = KeyboardButton('4-Аптека')
ruapteka5 = KeyboardButton('5-Аптека')
ruortga = KeyboardButton('назад ⬅️')
ruaptekalar = ReplyKeyboardMarkup(resize_keyboard=True).add(ruapteka1).add(ruapteka2).add(ruapteka3).add(ruapteka4).add(ruapteka5).add(ruortga)

rurestoran1 = KeyboardButton('1-Ресторан')
rurestoran2 = KeyboardButton('2-Ресторан')
rurestoran3 = KeyboardButton('3-Ресторан')
rurestoran4 = KeyboardButton('4-Ресторан')
rurestoran5 = KeyboardButton('5-Ресторан')
ruorqagaa = KeyboardButton('назад ⬅️')
rurestoranlar = ReplyKeyboardMarkup(resize_keyboard=True).add(rurestoran1).add(rurestoran2).add(rurestoran3).add(rurestoran4).add(rurestoran5).add(ruorqagaa)

bankomat1 = KeyboardButton('1-Bankomat')
bankomat2 = KeyboardButton('2-Bankomat')
bankomat3 = KeyboardButton('3-Bankomat')
bankomat4 = KeyboardButton('4-Bankomat')
bankomat5 = KeyboardButton('5-Bankomat')
orqaga = KeyboardButton('Orqaga ⬅️')
bankomatlarbutton = ReplyKeyboardMarkup(resize_keyboard=True).add(bankomat1).add(bankomat2).add(bankomat3).add(bankomat4).add(bankomat5).add(orqaga)

apteka1 = KeyboardButton('1-Dorixona')
apteka2 = KeyboardButton('2-Dorixona')
apteka3 = KeyboardButton('3-Dorixona')
apteka4 = KeyboardButton('4-Dorixona')
apteka5 = KeyboardButton('5-Dorixona')
ortga = KeyboardButton('Orqaga ⬅️')
aptekalar = ReplyKeyboardMarkup(resize_keyboard=True).add(apteka1).add(apteka2).add(apteka3).add(apteka4).add(apteka5).add(ortga)

restoran1 = KeyboardButton('1-Restoran')
restoran2 = KeyboardButton('2-Restoran')
restoran3 = KeyboardButton('3-Restoran')
restoran4 = KeyboardButton('4-Restoran')
restoran5 = KeyboardButton('5-Restoran')
orqagaa = KeyboardButton('Orqaga ⬅️')
restoranlar = ReplyKeyboardMarkup(resize_keyboard=True).add(restoran1).add(restoran2).add(restoran3).add(restoran4).add(restoran5).add(orqagaa)



enbankomat1 = KeyboardButton('1-ATM')
enbankomat2 = KeyboardButton('2-ATM')
enbankomat3 = KeyboardButton('3-ATM')
enbankomat4 = KeyboardButton('4-ATM')
enbankomat5 = KeyboardButton('5-ATM')
enorqaga = KeyboardButton('Back ⬅️')
enbankomatlarb = ReplyKeyboardMarkup(resize_keyboard=True).add(enbankomat1).add(enbankomat2).add(enbankomat3).add(enbankomat4).add(enbankomat5).add(enorqaga)

enapteka1 = KeyboardButton('1-Pharmacy')
enapteka2 = KeyboardButton('2-Pharmacy')
enapteka3 = KeyboardButton('3-Pharmacy')
enapteka4 = KeyboardButton('4-Pharmacy')
enapteka5 = KeyboardButton('5-Pharmacy')
enortga = KeyboardButton('Back ⬅️')
enaptekalar = ReplyKeyboardMarkup(resize_keyboard=True).add(enapteka1).add(enapteka2).add(enapteka3).add(enapteka4).add(enapteka5).add(enortga)


enrestoran1 = KeyboardButton('1-Restaurant')
enrestoran2 = KeyboardButton('2-Restaurant')
enrestoran3 = KeyboardButton('3-Restaurant')
enrestoran4 = KeyboardButton('4-Restaurant')
enrestoran5 = KeyboardButton('5-Restaurant')
enorqagaa = KeyboardButton('Back ⬅️')
enrestoranlar = ReplyKeyboardMarkup(resize_keyboard=True).add(enrestoran1).add(enrestoran2).add(enrestoran3).add(enrestoran4).add(enrestoran5).add(enorqagaa)


enhotel1 = KeyboardButton('Marvarid Hotel')
enhotel2 = KeyboardButton('Shodlik Hotel')
enhotel3 = KeyboardButton('Poykent Bukhara Hotel')
enhotel4 = KeyboardButton('Burji Bukhara Hotel')
enhotelback = KeyboardButton('Back ⬅️')

enhotelbuttons = ReplyKeyboardMarkup(resize_keyboard=True).add(enhotel1).add(enhotel2).add(enhotel3).add(enhotel4).add(enhotelback)


uzhotel1 = KeyboardButton('Marvarid mehmonxonasi')
uzhotel2 = KeyboardButton('Shodlik mehmonxonasi')
uzhotel3 = KeyboardButton('Poykent Bukhara mehmonxonasi')
uzhotel4 = KeyboardButton('Burji Buxoro mehmonxonasi')
uzhotelortga = KeyboardButton('Orqaga ⬅️')

uzhotelbuttons = ReplyKeyboardMarkup(resize_keyboard=True).add(uzhotel1).add(uzhotel2).add(uzhotel3).add(uzhotel4).add(uzhotelortga)


ruhotel1 = KeyboardButton('Марварид Отель')
ruhotel2 = KeyboardButton('Шодлик Отель')
ruhotel3 = KeyboardButton('Пойкент Отель')
ruhotel4 = KeyboardButton('Буржи Бухара Отель')
ruhotelortga = KeyboardButton('назад ⬅️')
ruhotelbuttons = ReplyKeyboardMarkup(resize_keyboard=True).add(ruhotel1).add(ruhotel2).add(ruhotel3).add(ruhotel4).add(ruhotelortga)