cityCodes={'Ahmedabad':21, 'Vadodara':10, 'Surat':5, 'Veraval':99}
CityPlaces={'Ahmedabad':'IIM','Vadodara':'Croc', 'Surat':'Kites', 'Veraval':'Sea'}

CityPlacesCopy=CityPlaces.copy()
print('Copied Dictonary ',CityPlacesCopy)

print('Before Updateing the codes are ', cityCodes)
cityCodes.update(CityPlaces)
print('Updated codes are: ',cityCodes)

print('Values of city codes: ', cityCodes.values())
print('Keys of city codes: ', cityCodes.keys())

print('city code items: ', cityCodes.items())

cityCodes.clear()

print('After clear: ', cityCodes)