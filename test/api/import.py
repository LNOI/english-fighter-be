import httpx
import asyncio
import json


async def import_config_toiec():
    url = "http://localhost:8001/toiec/config"
    extend_config = {}
    data = {
        "name": "Config Toiec Listening Reading",
        "type": "LISTENING_READING",
        "audio": "",
        "image": "http://localhost:9000/englishfighter/toiec/image/toiec_lr_part1_1.jpg",
        "description": "This is a description",
        "extend_config": json.dumps(extend_config),
        "default": True,
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        print(response.json())


if __name__ == "__main__":
    asyncio.run(import_config_toiec())
