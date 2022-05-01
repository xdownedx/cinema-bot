import aiohttp
from urllib.parse import quote
import typing as tp


async def film2info(film: str) -> tp.Dict[str, tp.Any]:
    film_encoded = quote(film)
    url = f"https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={film_encoded}&page=1"
    headers = {'X-API-KEY': '055246f5-a117-4eae-8695-d437404046be', 'Content-Type': 'application/json'}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, ssl=False) as r:
            json_body = await r.json()
            return json_body
