import json

with open("PetrKuznetsov.json", "r", encoding="utf-8") as f:
    param = json.load(f)
    print("Всего вопросов", len(param["answers"]))
    true_ansewer = 0

    for i in param["answers"]:
        if i == "0":
            true_ansewer += 1


result = (true_ansewer / len(param["answers"])) * 100
print(str(round(result, 2)) + "%")
