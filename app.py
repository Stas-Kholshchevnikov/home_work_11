import utils
from flask import Flask, render_template


def main():
    # Создание объекта Flask
    app = Flask(__name__)

    # Роут для вывода списка всех кандидатов
    @app.route("/")
    def page_all():
        return render_template('list.html', candidates=utils.load_candidates_from_json())

    # Роут для вывода кандидата по его id
    @app.route("/candidate/<int:pk>")
    def page_candidate_id(pk):
        return render_template('single.html', candidate_id=utils.get_candidate(pk))

    # Роут для вывода списка кандидатов через поиск по имени
    @app.route("/search/<name>")
    def page_candidate_name(name):
        return render_template('search.html', candidate_name=utils.get_candidates_by_name(name), name=name)

    # Роут для вывода списка кандидатов через поиск по навыкам
    @app.route("/skill/<skill_name>")
    def page_candidate_skills(skill_name):
        return render_template('skill.html', candidate_skills=utils.get_candidates_by_skill(skill_name), skill=skill_name)

    # Запуск приложения
    app.run()


if __name__ == "__main__":
    main()


