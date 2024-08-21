import httpx
import asyncio


async def list_toiec():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001/toiec/")
        print(response.json())


async def get_toiec(toiec_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8001/toiec/{toiec_id}")
        print(response.json())


if __name__ == "__main__":
    # asyncio.run(list_toiec())
    asyncio.run(get_toiec("8453abc9-e092-4dfe-9fb5-611a41ad7220"))
