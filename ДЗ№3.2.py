def polzovatel(name,surname,birth_year,city,email,tel):
    return print(f'Имя={name} Фамилия={surname} Год рождения={birth_year} Город проживания={city} Почта={email} Телефон={tel}')

polzovatel(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    birth_year=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('Почта: '),
    tel=input('Телефон: '))
