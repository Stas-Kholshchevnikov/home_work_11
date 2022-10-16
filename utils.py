import os
import json

#Ссылка на файл с кандидатами
URL = "candidates.json"

def load_candidates_from_json():

    """Функция получения полного списка кандидатов"""

    with open(os.path.join(URL), "r", encoding="UTF-8") as file:
        return json.load(file)


def get_candidate(candidate_id):

    """Функция получения кандидата по его id"""

    candidates_list = load_candidates_from_json()
    for candidate in candidates_list:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):

    """Функция поиска кандидатов по имени"""

    candidates_list = load_candidates_from_json()
    result_list = []
    for candidate in candidates_list:
        if candidate_name.lower() in candidate["name"].lower().split(" "):
            result_list.append(candidate)
    return result_list


def get_candidates_by_skill(skill_name):

    """Функция поиска кандидатов по навыкам"""

    candidates_list = load_candidates_from_json()
    result_list = []
    for candidate in candidates_list:
        if skill_name.lower() in candidate["skills"].replace(" ", "").lower().split(","):
            result_list.append(candidate)
    return result_list
