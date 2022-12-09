def describe_city(city,country = "Philippines"): #city function with default country parameter
    print(f'The {city.title()} city is in {country.title()}') #message to be printed

describe_city(city = "manila") #calls the city parameter
describe_city(city = 'makati')
describe_city(city = 'new york', country = 'united states of america') #overwrites the default countr parameter