import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://postgres:***@localhost:5432/postgres')
connection = engine.connect()

# название и год выхода альбомов, вышедших в 2018 году
select_album_2018 = connection.execute("""SELECT title, year_of_release FROM album
    WHERE year_of_release = '2018-01-01';""").fetchall()
print(select_album_2018)

# название и продолжительность самого длительного трека
select_track = connection.execute("""SELECT name, duration FROM track 
    ORDER BY duration DESC LIMIT 1;""").fetchall()
print(select_track)

# название треков, продолжительность которых не менее 3,5 минуты
select_duration = connection.execute("""SELECT name FROM track 
    WHERE duration >= 210;""").fetchall()
print(select_duration)

# названия сборников, вышедших в период с 2018 по 2020 год включительно
select_collection = connection.execute("""SELECT name_of_collection, create_year FROM music_collection
    WHERE create_year >= '2018-01-01' AND create_year <='2020-01-01';""").fetchall()
print(select_collection)

# исполнители, чье имя состоит из 1 слова
select_alias = connection.execute("""SELECT alias FROM musician 
    WHERE alias NOT LIKE '%% %%';""").fetchall()
print(select_alias)

# название треков, которые содержат слово "мой"/"my"
select_my = connection.execute("""SELECT name FROM track 
    WHERE name LIKE '%%My%%';""").fetchall()
print(select_my)
