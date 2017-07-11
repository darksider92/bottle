import json


with open("test1", "r", encoding="utf-8") as file:
    with open("test.json", "w", encoding="utf-8") as f:
        question_test = dict()
        answer_list = list()
        for line in file.readlines():
            if line[0] == "!":
                qwestion = line
                question_test[qwestion] = []
            elif line[0] == "-":
                false_answer = line
                answer_list.append(false_answer)
                negative_answer = line
            elif line[0] == "+":
                tru_anser = line
                answer_list.append(tru_anser)
            elif line[0] == "#":
                del answer_list[:]
            question_test[qwestion] = answer_list
        json.dump(question_test, f, ensure_ascii=False, indent=2)

