from API_aviasales import API_aviasales

print(API_aviasales("samara", "питер"))         # 3500
print(API_aviasales("samara", "Москва"))  # 3500
print(API_aviasales("samara", "Москва"))        # 0 (город не найден)
print(API_aviasales("samara", "Челябинск"))     # 0 (маршрут не прописан)
