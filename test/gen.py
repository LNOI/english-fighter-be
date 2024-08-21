import json


def gen_part_1():
    data = []
    for i in range(1, 7):
        d = {
            "name": "Group Question 1",
            "group_question_text": "",
            "group_question_audio": "",
            "number_of_questions": 1,
            "questions": [],
        }
        format_question = {
            "question_text": "What time is it?",
            "order": 1,
            "question_audio": "http://localhost:9000/englishfighter/toiec/audio/toiec_lr_part1_1.mp3",
            "image": "",
            "type_input": "audio",
            "type_toiec": "LISTENING",
            "answer_choices": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
            ],
            "correct_answer": "A",
        }
        question = format_question.copy()
        question["order"] = i
        d["questions"].append(question)
        data.append(d)
    return data


def gen_part_2():
    # 25 sentent from order 7 to 31
    data = []
    for i in range(7, 32):
        d = {
            "name": "Group Question 1",
            "group_question_text": "",
            "group_question_audio": "",
            "number_of_questions": 1,
            "questions": [],
        }
        format_question = {
            "question_text": "What time is it?",
            "order": 1,
            "question_audio": "http://localhost:9000/englishfighter/toiec/audio/toiec_lr_part1_1.mp3",
            "image": "",
            "type_input": "audio",
            "type_toiec": "LISTENING",
            "answer_choices": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
            ],
            "correct_answer": "A",
        }
        question = format_question.copy()
        question["order"] = i
        d["questions"].append(question)
        data.append(d)

    return data


def gen_part_3():
    data = []
    for i in range(32, 71, 3):
        d = {
            "name": "Group Question 1",
            "group_question_text": "",
            "group_question_audio": "http://localhost:9000/englishfighter/toiec/audio/toiec_lr_part1_1.mp3",
            "number_of_questions": 3,
            "questions": [],
        }
        format_question = {
            "question_text": "What time is it?",
            "order": 0,
            "question_audio": "",
            "image": "",
            "type_input": "audio",
            "type_toiec": "LISTENING",
            "answer_choices": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        for j in range(3):
            question = format_question.copy()
            question["order"] = i + j
            d["questions"].append(question)
        data.append(d)
    return data


def gen_part_4():
    # Include 30 sentences from order 71 to 100 and 10 groups and 3 questions for each group
    data = []
    for i in range(71, 101, 3):
        d = {
            "name": "Group Question 1",
            "group_question_text": "",
            "group_question_audio": "http://localhost:9000/englishfighter/toiec/audio/toiec_lr_part1_1.mp3",
            "number_of_questions": 3,
            "questions": [],
        }
        format_question = {
            "question_text": "What time is it?",
            "order": 0,
            "question_audio": "",
            "image": "",
            "type_input": "audio",
            "type_toiec": "LISTENING",
            "answer_choices": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question = format_question.copy()
        question["order"] = i
        d["questions"].append(question)

        question = format_question.copy()
        question["order"] = i + 1
        d["questions"].append(question)

        question = format_question.copy()
        question["order"] = i + 2
        d["questions"].append(question)
        data.append(d)

    return data


def gen_part_5():
    # Include 30 sentences from order 101 to 130
    data = []
    for i in range(101, 131):
        d = {
            "name": "Group Question 1",
            "group_question_text": "",
            "group_question_audio": "",
            "number_of_questions": 1,
            "questions": [],
        }
        format_question = {
            "question_text": "What time is ... it?",
            "question_audio": "",
            "order": 0,
            "image": "",
            "type_input": "text",
            "type_toiec": "READING",
            "answer_choices": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question = format_question.copy()
        question["order"] = i
        d["questions"].append(question)
        data.append(d)

    return data


def gen_part_6():
    # Include 16 sentences from order 131 to 160
    data = []
    for i in range(131, 147, 4):
        d = {
            "name": "Group Question 1",
            "group_question_text": """Michelle L. SinnottThe Mitel Limited\n45 Landsdowne Road\nSeattle, Washington
\nDear Ms. Sinnott,\nMr. Steven Davis, who is currently employed as a junior accountant at your firm, has recently shown his interest in a similar post with (13)......... and has provided your name as a reference.\nI would be grateful to receive any information regarding his work ethic, character, and achievements. Furthermore, if you can provide your personal views of how his (14)......... with you have been and what your opinion is regarding Mr. Davis taking on full responsibility as an accountant in a very large and busy department, I would appreciate it.\nI am (15)........ aware that Mr. Davis graduated from George Brown College with an accounting degree but I am more interested in how he has performed under your supervision since he began working for you.\nIf there is any other information you feel I (16)........ , I would appreciate it very much. I’d like to thank you in advance and add that any information you provide will be treated as strictly confidential.\nSincerely,""",
            "group_question_audio": "",
            "number_of_questions": 4,
            "questions": [],
        }
        format_question = {
            "question_text": "This is a question",
            "order": 0,
            "question_audio": "",
            "image": "",
            "type_input": "text",
            "type_toiec": "READING",
            "answer_choices": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question = format_question.copy()
        question["order"] = i
        d["questions"].append(question)

        question = format_question.copy()
        question["order"] = i + 1
        d["questions"].append(question)

        question = format_question.copy()
        question["order"] = i + 2
        d["questions"].append(question)

        question = format_question.copy()
        question["order"] = i + 3
        d["questions"].append(question)

        data.append(d)
    # with open("./test/gen_data_part_6.json", "w") as f:
    #     f.write(json.dumps(data, indent=4))
    return data


def gen_part_7():
    # Include 54 sentences from order 145 to 200
    data = []
    for i in range(147, 201, 4):
        d = {
            "name": "Group Question 1",
            "group_question_text": """Dar Pfeiffer Reports Strong Q2 Profit\nOn Wednesday, Dar Pfeiffer, one of the largest brokerage firms in the world, reported a second-quarter profit that was 53% larger than expected. The second-quarter profit was attributed to a one-time deal with money manager Tapcourt.\nShareholders saw this profit in the form of a $2.46 increase in share prices. The same period last year showed a $1.07 increase a share. Excluding the deal with Tapcourt, Dar Pfeiffer would have reported a profit 23% larger than expected. Either way, Dar Pfeiffer topped market predictions for performance by at least $1.58 a share.""",
            "group_question_audio": "",
            "number_of_questions": 4,
            "questions": [],
        }
        format_question = {
            "question_text": "What time is it?",
            "order": 0,
            "question_audio": "",
            "image": "",
            "type_input": "text",
            "type_toiec": "READING",
            "answer_choices": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        for j in range(4):
            question = format_question.copy()
            question["order"] = i + j
            if question["order"] > 200:
                break
            d["questions"].append(question)

        data.append(d)

    return data


def generate_full_data():
    prepare = {
        1: gen_part_1(),
        2: gen_part_2(),
        3: gen_part_3(),
        4: gen_part_4(),
        5: gen_part_5(),
        6: gen_part_6(),
        7: gen_part_7(),
    }
    data = {
        "name": "ETS GLOBAL TOIEC Listening Reading 1",
        "description": "Description about TOIEC Listening Reading 1",
        "level": "C1",
        "type_toiec": "LISTENING_READING",
        "total_part": 7,
        "total_questions": 200,
        "total_time": 120,
        "author": "ETS Global",
        "parts": [],
    }
    for i in range(1, 8):
        part = {
            "part": i,
            "name": f"Part {i}",
            "directions": f"This is a direction for part {i}",
            "groups": prepare[i],
        }

        data["parts"].append(part)

    with open("./test/data_toiec_listening_reading_21_8.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def refactor_order_question():
    with open("./test/data_toiec_listening_reading.json", "r") as f:
        data = json.load(f)
    i = 1
    parts = data["parts"]
    for p in parts:
        groups = p["groups"]
        for g in groups:
            questions = g["questions"]
            for q in questions:
                q["order"] = i
                i += 1

    with open("./test/new_data.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def check_format_toiec_test():
    with open("./test/data_toiec_listening_reading_21_8.json", "r") as f:
        data = json.load(f)
    parts = data["parts"]
    print(len(parts))
    for p in parts:
        print("In part ", p["part"])
        total_questions = 0
        groups = p["groups"]

        for g in groups:
            questions = g["questions"]
            total_questions += len(questions)

        print(total_questions)


# refactor_order_question()
generate_full_data()
check_format_toiec_test()
