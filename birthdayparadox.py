import random , datetime

def getBirthdays(numberofBirthdays):
    
    birthdays = []
    for i in range(numberofBirthdays):
        startOfYear=datetime.date(2001,1,1)
        
    randomNumberOfDay = datetime.timedelta(random.randint(0,364))
    birthday= startOfYear + randomNumberOfDay
    birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a , birthdayA in enumerate(birthdays):
        for b , birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA
        
        
print(''' Doğum günü paradoksu bize N kişilik bir grupta olasılıkların
ikisinin doğum günlerinin aynı olması şaşırtıcı derecede büyük.
Bu program bir Monte Carlo simülasyonu yapar (yani tekrarlanan rastgele
simülasyonlar) bu kavramı keşfetmek için.

(Aslında bu bir paradoks değil, sadece şaşırtıcı bir sonuç.)''')


MONTHS = ('Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasim', 'Aralik' )


while True:
    print('Kaç doğum günü oluşturmalıyım? (En fazla 100)')
    response = input('>')
    if response.isdecimal() and (0 < int(response) <= 10000):
        numBDays = int(response)
        break
    print()
    
    print('Burada', numBDays, 'birthdays:')
    birthdays=getBirthdays(numBDays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
            monthName = MONTHS[birthday.month - 1]
            dateText = '{} {}'.format(monthName, birthday.day)
            print(dateText, end='')
            
print()
print()  
birthdays = []     
match = getMatch(birthdays)    

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText= '{} {}'.format(monthName, match.day)
    
    print('Birçok insan bu doğum gününe sahip', dateText)
    
else:
    print('Eşleşen dogum günü yok')
print()


print('Oluşturuluyor', numBDays, '100.000 kez rastgele doğum günleri...') 
input('Başlamak için Enter a basın...')  
print('100.000 simülasyon daha çalıştıralım.')
simMatch = 0
for i in range(100000):
    if i % 10000 == 0:
        birthdays= getBirthdays(numBDays)
        if getMatch(birthdays) != None:
            simMatch = simMatch + 1
print('100.000 simülasyon çalıştırıldı.')

probability = round(simMatch / 100000 * 100, 2)
print('100.000 simülasyondan biri', numBDays, 'insanlar vardı')
print('bu grupta eşleşen doğum günü', simMatch, 'zamanlar. Bunun anlamı')
print('bu', numBDays, 'insanların bir', probability, '% şansı var')
print('kendi grubunda eşleşen bir doğum gününe sahip.'),
print('Bu muhtemelen düşündüğünüzden daha fazlasıdır!')
        
        