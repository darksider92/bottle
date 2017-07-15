from collections import defaultdict
import json
question_test = defaultdict(list)

with open('test1', mode='r', encoding='utf-8') as f:
    # Защита от дурака которая проверяет чтобы в файле сначала была
    # строка с вопросом
    question = None

    for line in f:
        # Удаление ' ', '\n', '\t', '\r' из начала и конца строки
        line = line.strip()

        # Защита от дурака которая проверяет чтобы строка не была пустой
        if not line:
            continue

        type_line = line[0]
        if type_line == '!':
            question = line[1:]
            continue

        if type_line not in '-+':
            continue

        if not question:
            continue

        question_test[question].append(line)


with open("test.json", "w", encoding="utf-8") as file:
    json.dump(question_test, file,ensure_ascii=False, indent=4)
