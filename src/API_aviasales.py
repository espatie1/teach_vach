import csv
import difflib

# ПРИНЦИП РАБОТЫ 
# для работы с библиотекой - from API_aviasales import API_aviasales
# вызов функции - API_aviasales(city_Samara,city_destination),
# функция возвращает значение в виде целого числа (примерная цена в РУБ)
# если же город не существует или не имеет аэропорта - возвращает 0


_city_alias_map = {}

_internal_prices = {}

def _load_city_names(path='city_names.csv'):
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            alias = row['alias'].strip().lower()
            canonical = row['canonical'].strip()
            _city_alias_map[alias] = canonical

def _load_prices(path='internal_prices.csv'):
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            frm = row['from'].strip()
            to = row['to'].strip()
            price = int(row['price'])
            _internal_prices[(frm, to)] = price

def _normalize_city_name(user_input):
    user_input = user_input.strip().lower()
    if user_input in _city_alias_map:
        return _city_alias_map[user_input]
    match = difflib.get_close_matches(user_input, _city_alias_map.keys(), n=1, cutoff=0.8)
    if match:
        return _city_alias_map[match[0]]

    return None

def API_aviasales(city_from, city_to) -> int:
    norm_from = _normalize_city_name(city_from)
    norm_to = _normalize_city_name(city_to)

    if norm_from is None or norm_to is None:
        return 0 

    return _internal_prices.get((norm_from, norm_to), 0)  

_load_city_names()
_load_prices()
