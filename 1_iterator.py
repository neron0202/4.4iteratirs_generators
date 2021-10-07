import json


class CountryIterator:

    def __init__(self):
        self.counter = -1
        with open('countries.json') as file:
            self.json_data = json.load(file)

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.json_data):
            raise StopIteration
        country = self.json_data[self.counter]['name']['common']
        return country


if __name__ == '__main__':
        with open ('wiki_links.txt', 'w') as file:
            for country in CountryIterator():
                country_link = country.replace(" ", "_")
                file.write(f'{country} - https://en.wikipedia.org/wiki/{country_link}\n')


