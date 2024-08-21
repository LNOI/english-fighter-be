import httpx
import asyncio

BASE_URL = "http://localhost:8000"


async def get_toiec(toiec_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/toiec/{toiec_id}")
        print(response.json())


if __name__ == "__main__":
    asyncio.run(get_toiec("bc16611f-687b-4d06-b5e4-a3e7f2f12915"))
