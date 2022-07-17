import json


def load_candidates_from_json() -> list[dict]:
    """
    Получение данных из JSON-файла
    :return: список кандидатов с данными, полученными из JSON-файла
    """
    # Записываем в переменную название JSON-файла
    file_json = "candidates.json"
    # Открываем на чтение это JSON-файл
    with open(file_json, mode='r', encoding='utf-8') as file:
        # Все данные из JSON-файла записываем в список словарей, который возвращаем
        data_candidates = json.load(file)
    return data_candidates


def get_candidate_by_id(id: int) -> dict:
    """
    Выводит данные одного кандитата по выбранному персональному номеру
    :param id: персональный номер кандидата
    :return: необходимые данные выбранного кандидата
    """
    # Получаем и записываем в переменную весь список словарей с данными кандидатов
    data_candidates = load_candidates_from_json()
    # Запускаем цикл по списку словарей с данными кандидатов
    for candidate in data_candidates:
        # Если в общем списке присутствует кандидат с выбранным номером, то выводим его данные
        if candidate['id'] == id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """
    Выводит данные кандидатов по заданному имени
    :param candidate_name: задаваемое имя кандидата
    :return: необходимые данные выбранных кандидатов
    """
    # Получаем и записываем в переменную весь список словарей с данными кандидатов
    data_candidates = load_candidates_from_json()
    # Определяем переменную, куда будет записан список кандидатов с одинаковыми именами
    list_candidates_names = []
    # Запускаем цикл по списку словарей с данными кандидатов
    for candidate in data_candidates:
        # Если в общем списке присутствует кандидат с заданным именем, или фамилией,
        # или имя + фамилия, то...
        if candidate_name.lower() in candidate['name'].lower().split(" ") or \
                candidate_name.lower() == candidate['name'].lower():
            # ...добавляем найденного кандидата в список
            list_candidates_names.append(candidate)
    return list_candidates_names


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """
    Выводит данные кандидатов, имеющих заданное знание-умение
    :param skill_name: название заданного знания-умения
    :return: данные кандидатов с выбранным знанием-умением
    """
    # Получаем и записываем в переменную весь список словарей с данными кандидатов
    data_candidates = load_candidates_from_json()
    # Определяем переменную, куда будет записан список кандидатов с одинаковыми умениями
    list_candidates_skill = []
    # Запускаем цикл по списку словарей с данными кандидатов
    for candidate in data_candidates:
        # Если в общем списке присутствует кандидат с заданным умением, то...
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            # ...добавляем найденного кандидата в список
            list_candidates_skill.append(candidate)
    return list_candidates_skill
