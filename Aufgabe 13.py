#Eigene werte müssen hinzugefügt werden
import numpy as np

# Simulierte Herzfrequenzwerte und Zeit
time = np.arange(0, 30, 3)  # Zeit in Minuten
HR_rest = 60  # Ruheherzfrequenz in bpm
HR_max = 180  # Maximale Herzfrequenz in bpm
HR_activity = np.linspace(HR_rest + 10, HR_max - 30, len(time))  # Simulierte Herzfrequenzwerte während Aktivität

# Berechnung von HRnet
HRnet = HR_activity - HR_rest

# Berechnung des Energieverbrauchs (EE) mit Formel 3 / Körpergewicht und Geschecht in die Formel einfügen
EE = 1.08 * HRnet  # EE in kcal/min / wir haben für jede 2ml eien HR wert Achtung das wir richtig rechnen

# Integration des gesamten Energieverbrauchs über die Zeit (in Minuten)
total_energy_kcal = np.trapz(EE, time) #wir haben für jede 2ml eien HR wert Achtung das wir richtig rechnen

# Umrechnung in verschiedene Einheiten
total_energy_joule = total_energy_kcal * 4184  # Joule
total_energy_calories = total_energy_kcal * 1000  # Kalorien
ritter_sport = total_energy_kcal / 563  # Rittersport Tafeln
beer_units = total_energy_kcal / 150  # Bierflaschen

# Berechnung des täglichen Kalorienbedarfs (z. B. Harris-Benedict-Formel)
# Beispielwerte: Alter = 25, Gewicht = 70 kg, Größe = 175 cm, Aktivitätsfaktor = 1.55
weight = 70  # Gewicht in kg
height = 175  # Größe in cm
age = 25  # Alter in Jahren
activity_factor = 1.55  # Beispiel: moderat aktive Person
bmr = 10 * weight + 6.25 * height - 5 * age + 5  # Grundumsatz (Männer)
daily_calorie_need = bmr * activity_factor  # Gesamtkalorienbedarf

# Anteil des Experiments am täglichen Kalorienbedarf
percent_of_daily_need = (total_energy_kcal / daily_calorie_need) * 100

# Ergebnisse ausgeben
print(f"Gesamter Energieverbrauch: {total_energy_kcal:.2f} kcal")
print(f"Entspricht: {total_energy_joule:.2f} J")
print(f"Entspricht: {total_energy_calories:.2f} cal")
print(f"Entspricht: {ritter_sport:.2f} Rittersport-Tafeln")
print(f"Entspricht: {beer_units:.2f} Bierflaschen")
print(f"Anteil am täglichen Kalorienbedarf: {percent_of_daily_need:.2f} %")
