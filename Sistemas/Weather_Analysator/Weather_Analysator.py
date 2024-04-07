'''The following code creates a list of size 30 with random integers between 0 and 35 using the
randint() function from the random library. The list represents daily temperatures between 0°C and
35°C for a month (30 days).
import random
daily_temperatures = [random.randint(0, 35) for _ in range(30)]
Run this code and print the daily_temperatures. (The values will be different every time you run
the code).
Using this list of daily temperatures, write separate for-loops to do the following. You can use the
enumerate method in the for-loop statement to keep track of the days.
• Find the day with the lowest temperature.
• Find the day with the highest temperature.
• Find the days where the temperature rises above 20°C.
• Find the days where the temperature drops below 10°C.
• Find the days where the temperature increased from the day before.
• Find the days where the temperature was hotter than any of the days previous in the
month.

Now generate another list for rainfall values between 0mm and 10mm for a month (30 days).
Imagine these are the same 30 days as the daily temperatures list. For example, one day could have
a temperature of 11°C and a rainfall of 3mm.
daily_rainfall = [random.randint(0, 10) for _ in range(30)]
Using the list of daily temperatures and daily rainfall, write separate for-loops to do the following.
You can use the zip method in the for-loop statements to traverse through both lists simultaneously.
• Record the amount of ‘bad weather’ days, the number of days that the rainfall is above 3mm
and the temperature is below 10°C.
• Record the amount of ‘average weather’ days, the number of days that the rainfall is
between 1mm and 5mm and the temperature is between 10°C and 18°C.
• Record the amount ‘good weather’ days, the number of days that the rainfall is below 2mm,
and the temperature is above 18°C.
Remember, the random generator code will change your lists every time you run your program so
expect different lists each execution.'''

import random
import time
dias_temperatura = dict()

print(" ")
time.sleep(2)
print(27*"\033[33m=-=", "\033[1mWEATHER ANALYSER", 27*"\033[33m=-=")
time.sleep(2)
print(" ")

dl = []
da = 0

for i in range(1, 31):
    dias = i
    time.sleep(0.3)
    print(f'\033[37mDay: {i}th ')
    temperatura = (random.randint(0, 35))
    print(f'\033[37mTemperature: {temperatura}ºC \n')
    dias_temperatura.update({dias: temperatura})

    if temperatura > da:
        dl.append(dias)
    da = temperatura

menor = dias_temperatura[min(dias_temperatura, key=dias_temperatura.get)]
time.sleep(2)
print('\033[36mThe day(s) with the lowest temperature was:')
time.sleep(2)
for dias, temperatura in dias_temperatura.items():
    if temperatura == menor:
        time.sleep(0.3)
        print(f'Day {dias}th with {menor}°C')
print(" ")

maior = dias_temperatura[max(dias_temperatura, key=dias_temperatura.get)]
time.sleep(2)
print('\033[32mThe day(s) with the highest temperature was:')
time.sleep(2)
for dias, temperatura in dias_temperatura.items():
    if temperatura == maior:
        time.sleep(0.3)
        print(f'Day {dias}th with {maior}°C')
print(" ")

above = 20
time.sleep(2)
print("\033[33mThe days where the temperature rises above 20°C was: ")
time.sleep(2)
for dias, temperatura in dias_temperatura.items():
    if temperatura > above:
        time.sleep(0.3)
        print(f'Day {dias}th with {temperatura} C°')
print(" ")

below = 10
time.sleep(2)
print("\033[34mThe days where the temperature rises below 10°C was: ")
time.sleep(2)
for dias, temperatura in dias_temperatura.items():
    if temperatura < below:
        time.sleep(0.3)
        print(f'Day {dias}th with {temperatura} C°')
print(" ")

time.sleep(2)
print("\033[31mThe days where the temperature increased from the day before was: ")
time.sleep(2)
print(f'{dl}th')
print(" ")

dias_chuva = dict()
for i in range(1, 31):
    diasc = i
    chuva = random.randint(0,10)
    dias_chuva.update({diasc: chuva})

dias_chuva = dict()
for i in range(1, 31):
    diasc = i
    chuva = random.randint(0,10)
    dias_chuva.update({diasc: chuva})

dt = []
dc = []
for dias, temperatura in dias_temperatura.items():
    if temperatura < 10:
        dt.append(dias)
#print(f'Days that the temperature is below 10°C:\n{dt}th')
print("")

for diasc, chuva in dias_chuva.items():
   if chuva > 3:
     dc.append(diasc)
#print(f'Days that the rainfall is above 3mm:\n{dc}th')
#print("")

bad_weather = []
for index, data in enumerate(zip(dt, dc)):
    i, j = data
    if i in dc:
        bad_weather.append(i)
contar = len(bad_weather)
time.sleep(2)
print(f'\033[34mThe number of days that the rainfall is above 3mm and the temperature is below 10°C was:{contar}')
time.sleep(2)
print(f'Bad Weather in: {bad_weather}th')
print(" ")

mt = []
mr = []
for dias, temperatura in dias_temperatura.items():
    if 10 <= temperatura <= 18:
        mt.append(dias)
#print(f'Temperatura entre 10 e 18:\n{mt}th')
#print("")

for diasc, chuva in dias_chuva.items():
   if 5 >= chuva >= 1:
     mr.append(diasc)
#print(f'Chuva entre 5mm e 1mm\n{mr}th')
#print("")

median_weather = []
for index, data in enumerate(zip(mt, mr)):
    i, j = data
    if i in mr:
        median_weather.append(i)

contard = len(median_weather)
time.sleep(2)
print(f'\033[32mThe number of days that the rainfall is between 1mm and 5mm and the temperature is between 10°C and 18°C was: {contard}')
time.sleep(2)
print(f'Average Weather in: {median_weather}th')
print("")

gt = []
gr = []
for dias, temperatura in dias_temperatura.items():
    if temperatura > 18:
        gt.append(dias)
#print(f'Temperatura maior que 18:\n{gt}th')
#print("")

for diasc, chuva in dias_chuva.items():
    if chuva < 1:
     gr.append(diasc)
#print(f'Chuva menor que 2mm\n{gr}th')
#print("")

good_weather = []
for index, data in enumerate(zip(gt, gr)):
    i, j = data
    if i in gr:
        good_weather.append(i)

contarg = len(good_weather)
time.sleep(2)
print(f'\033[1mThe number of days that the rainfall is below 2mm, and the temperature is above 18°C was: {contarg}')
time.sleep(2)
print(f'Good Weather in: {good_weather}th')
print("")

time.sleep(3)
print(27*"\033[33m=-=", "\033[1mANALYSIS COMPLETED", 27*"\033[33m=-=")





