import json


with open('countries.json') as file:
    json_data = json.load(file)
countries_dict = json_data


class CountryIterator:

    def __init__(self, countries):
        self.countries = open(countries)
        self.json = json.load(self.countries)
        self.counter = 0


    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.countries):
            raise StopIteration

        country = json[self.counter]['name']['common']
        country_url = 'https://ru.wikipedia.org/' + country

        return country_url

if __name__ == '__main__':
    obj = CountryIterator(countries_dict)
    print(obj)













    # def __next__(self):
    #     if self.counter < self.limit:
    #         self.counter += 1
    #         return 1
    #     else:
    #         raise StopIteration

    # def __iter__(self):
    #     for number in range(len(countries_dict)):
    #         country = json_data[number]['name']['common']
    #         yield country


# def getCountry():
#     for number in range(len(countries_dict)):
#         country = json_data[number]['name']['common']
#         yield country
#
#
# for country in getCountry():
#     print(country)
#
# # class iterator():
