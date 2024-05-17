database = {}

def create_record(record_id, data):
    if record_id in database:
        print("Запись с таким идентификатором уже существует")
    else:
        database[record_id] = data
        print("Запись успешно создана")

def read_record(record_id):
    if record_id in database:
        return database[record_id]
    else:
        print("Запись с таким идентификатором не найдена")

def update_record(record_id, data):
    if record_id in database:
        database[record_id] = data
        print("Запись успешно обновлена")
    else:
        print("Запись с таким идентификатором не найдена")

def delete_record(record_id):
    if record_id in database:
        del database[record_id]
        print("Запись успешно удалена")
    else:
        print("Запись с таким идентификатором не найдена")

create_record(1, "Данные записи 1")
create_record(2, "Данные записи 2")
print(read_record(1))
update_record(1, "Обновленные данные записи 1")
print(read_record(1))
delete_record(2)