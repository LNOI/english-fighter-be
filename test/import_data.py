import httpx
import json
import asyncio

# Generate 200 sentences for TOIEC Listening and Reading
# Toiec Listening:
# - 200 sentences
## - part 1: Description about image 6 sentences (1-6) -> Listening from image and choose the correct answer (4 choices for each question)
## - part 2: Convenition 25 sentences (7-31) -> Listening from audio and choose the correct answer (3 choices for each question)
## - port 3: Short conversation 39 sentences (32-70) -> Listening from audio and choose the correct answer (4 choices for each question)
## - part 4: Short talk 30 sentences (71-100) -> Listening from audio and choose the correct answer (4 choices for each question)
## - part 5: Incomplete sentences 30 sentences (101-130) -> Reading and choose the correct answer (4 choices for each question)
## - part 6: Error recognition 30 sentences (131-160) -> Reading and choose the correct answer (4 choices for each question)
## - part 7: Reading comprehension 40 sentences (161-200) -> Reading and choose the correct answer (4 choices for each question)

# Generate 11 sentences for TOIEC Speaking
# Toiec Speaking:
# - 11 sentences

# Generate 9 sentences for TOIEC Writing
# Toiec Writing:
# - 9 sentences


async def generate_practice_toiec():
    BASE_URL = "http://localhost:8001"

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}")
    # print(response.json())
    with open("./test/data_toiec_listening_reading.json", "r") as f:
        data = json.load(f)
        # print(data)
        toiec_name = data["name"]

        # First, create a TOIEC
        url = f"{BASE_URL}/toiec/"
        payload = {
            "title": toiec_name,
            "description": data["description"],
            "level": data["level"],
            "type_toiec": data["type_toiec"],
            "author": data["author"],
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            print(response.json())
        toiec_id = response.json()["id"]

        # Second, create parts for TOIEC
        parts = data["parts"]
        for part in parts:
            url = f"{BASE_URL}/toiec/{toiec_id}/part"
            payload = {
                "toiec_id": toiec_id,
                "part": part["part"],
                "title": part["name"],
                "directions": part["directions"],
            }
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload)
                print(response.json())

            part_id = response.json()["id"]

            # Third, create groups for TOIEC
            groups = part["groups"]
            for group in groups:
                url = f"{BASE_URL}/toiec/{toiec_id}/part/{part_id}/group"
                payload = {
                    "toiec_id": toiec_id,
                    "part_id": part_id,
                    "title": group["name"],
                    "question": group["group_question"],
                }
                async with httpx.AsyncClient() as client:
                    response = await client.post(url, json=payload)
                    print(response.json())

                group_id = response.json()["id"]

                # Fourth, create questions for TOIEC
                questions = group["questions"]
                for question in questions:
                    url = f"{BASE_URL}/toiec/{toiec_id}/part/{part_id}/group/{group_id}/question"
                    payload = {
                        "order": question["order"],
                        "question": question["question"],
                        "type_input": question["type_input"],
                        "type_toiec": question["type_toiec"],
                        "direction": question["directions"],
                        "audio": question["audio"],
                        "list_answer": json.dumps(question["list_answer"]),
                        "suggest_answer": question["correct_answer"],
                    }
                    async with httpx.AsyncClient() as client:
                        response = await client.post(url, json=payload)
                        print(response.json())


if __name__ == "__main__":
    asyncio.run(generate_practice_toiec())
