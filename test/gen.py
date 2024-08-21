import json


def gen_part_2():
    # 25 sentent from order 7 to 31
    data = []
    for i in range(7, 32):
        d = {
            "name": "Group Question 1",
            "group_question": "",
            "number_of_questions": 1,
            "questions": [],
        }
        question = {
            "question": "What time is it?",
            "order": 1,
            "audio": "http://localhost:9000/englishfighter/toiec/audio/toiec_lr_part1_1.mp3",
            "image": "",
            "type_input": "audio",
            "type_toiec": "LISTENING",
            "directions": "",
            "list_answer": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
            ],
            "correct_answer": "A",
        }
        question["order"] = i
        d["questions"].append(question)
        data.append(d)

    with open("./test/gen_data.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def gen_part_3():
    # Include 39 sentences from order 32 to 70 and 13 groups and 3 questions for each group

    data = []
    for i in range(32, 71, 3):
        d = {
            "name": "Group Question 1",
            "group_question": "http://localhost:9000/englishfighter/toiec/audio/toiec_lr_part1_1.mp3",
            "number_of_questions": 3,
            "questions": [],
        }
        question = {
            "question": "What time is it?",
            "order": 0,
            "audio": "",
            "image": "",
            "type_input": "audio",
            "type_toiec": "LISTENING",
            "directions": "",
            "list_answer": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question["order"] = i
        d["questions"].append(question)
        question["order"] = i + 1
        d["questions"].append(question)
        question["order"] = i + 2
        d["questions"].append(question)
        data.append(d)
    with open("./test/gen_data_part_3.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def gen_part_4():
    # Include 30 sentences from order 71 to 100 and 10 groups and 3 questions for each group
    data = []
    for i in range(71, 101, 3):
        d = {
            "name": "Group Question 1",
            "group_question": "http://localhost:9000/englishfighter/toiec/audio/toiec_lr_part1_1.mp3",
            "number_of_questions": 3,
            "questions": [],
        }
        question = {
            "question": "What time is it?",
            "order": 0,
            "audio": "",
            "image": "",
            "type_input": "audio",
            "type_toiec": "LISTENING",
            "directions": "",
            "list_answer": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question["order"] = i
        d["questions"].append(question)
        question["order"] = i + 1
        d["questions"].append(question)
        question["order"] = i + 2
        d["questions"].append(question)
        data.append(d)
    with open("./test/gen_data_part_4.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def gen_part_5():
    # Include 30 sentences from order 101 to 130
    data = []
    for i in range(101, 131):
        d = {
            "name": "Group Question 1",
            "group_question": "",
            "number_of_questions": 1,
            "questions": [],
        }
        question = {
            "question": "What time is ... it?",
            "order": 0,
            "audio": "",
            "image": "",
            "type_input": "text",
            "type_toiec": "READING",
            "directions": "",
            "list_answer": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question["order"] = i
        d["questions"].append(question)
        data.append(d)
    with open("./test/gen_data_part_5.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def gen_part_6():
    # Include 30 sentences from order 131 to 160
    data = []
    for i in range(131, 161, 4):
        d = {
            "name": "Group Question 1",
            "group_question": """Michelle L. Sinnott
The Mitel Limited
45 Landsdowne Road
Seattle, Washington

Dear Ms. Sinnott,

Mr. Steven Davis, who is currently employed as a junior accountant at your firm, has recently shown his interest in a similar post with (13)......... and has provided your name as a reference.

I would be grateful to receive any information regarding his work ethic, character, and achievements. Furthermore, if you can provide your personal views of how his (14)......... with you have been and what your opinion is regarding Mr. Davis taking on full responsibility as an accountant in a very large and busy department, I would appreciate it.

I am (15)........ aware that Mr. Davis graduated from George Brown College with an accounting degree but I am more interested in how he has performed under your supervision since he began working for you.

If there is any other information you feel I (16)........ , I would appreciate it very much. I’d like to thank you in advance and add that any information you provide will be treated as strictly confidential.

Sincerely,""",
            "number_of_questions": 4,
            "questions": [],
        }
        question = {
            "question": "",
            "order": 0,
            "audio": "",
            "image": "",
            "type_input": "text",
            "type_toiec": "READING",
            "directions": "",
            "list_answer": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question["order"] = i
        d["questions"].append(question)

        question["order"] = i + 1
        d["questions"].append(question)

        question["order"] = i + 2
        d["questions"].append(question)

        question["order"] = i + 3
        d["questions"].append(question)

        data.append(d)
    with open("./test/gen_data_part_6.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def gen_part_7():
    # Include 40 sentences from order 161 to 200
    data = []
    for i in range(161, 201, 4):
        d = {
            "name": "Group Question 1",
            "group_question": """Dar Pfeiffer Reports Strong Q2 Profit

On Wednesday, Dar Pfeiffer, one of the largest brokerage firms in the world, reported a second-quarter profit that was 53% larger than expected. The second-quarter profit was attributed to a one-time deal with money manager Tapcourt.

Shareholders saw this profit in the form of a $2.46 increase in share prices. The same period last year showed a $1.07 increase a share. Excluding the deal with Tapcourt, Dar Pfeiffer would have reported a profit 23% larger than expected. Either way, Dar Pfeiffer topped market predictions for performance by at least $1.58 a share.""",
            "number_of_questions": 1,
            "questions": [],
        }
        question = {
            "question": "What time is it?",
            "order": 0,
            "audio": "",
            "image": "",
            "type_input": "text",
            "type_toiec": "READING",
            "directions": "",
            "list_answer": [
                {"answer": "A", "content": "It's 3:30."},
                {"answer": "B", "content": "It's 3:15."},
                {"answer": "C", "content": "It's 3:45."},
                {"answer": "D", "content": "It's 3:00."},
            ],
            "correct_answer": "A",
        }
        question["order"] = i
        d["questions"].append(question)

        question["order"] = i + 1
        d["questions"].append(question)

        question["order"] = i + 2
        d["questions"].append(question)

        question["order"] = i + 3
        d["questions"].append(question)

        data.append(d)
    with open("./test/gen_data_part_7.json", "w") as f:
        f.write(json.dumps(data, indent=4))


gen_part_2()
gen_part_3()
gen_part_4()
gen_part_5()
gen_part_6()
gen_part_7()


#

# Type slide


# Before Start Part 1
# Test slide
# LISTENING_PART_1 = "LISTENING_PART_1"
## Input include Image & audio -> output list answer (A, B, C, D))

# LISTENING_PART_2 = "LISTENING_PART_2"
## Input include audio -> output list answer (A, B, C))


# Part slide
# LISTENING_PART_3 = "LISTENING_PART_3"
## Input include audio -> output list answer (A, B, C,D))

# LISTENING_PART_4 = "LISTENING_PART_4"
## Input include audio -> output list answer (A, B, C,D))
