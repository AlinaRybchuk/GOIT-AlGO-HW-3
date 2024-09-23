import sys
from datetime import datetime, timedelta
import httpx
import asyncio
import platform

class HttpError(Exception):
    pass

class ICurrencyService:
    async def get_currency_rates(self, index_days: int) -> dict:
        raise NotImplementedError

class PrivatBankCurrencyService(ICurrencyService):
    async def get_currency_rates(self, index_days: int) -> dict:
        d = datetime.now() - timedelta(days=index_days)
        shift = d.strftime("%d.%m.%Y")
        try:
            response = await request(f'https://api.privatbank.ua/p24api/exchange_rates?date={shift}')
            return response
        except HttpError as err:
            print(err)
            return None

async def request(url: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            result = r.json()
            return result
        else:
            raise HttpError(f"Error status: {r.status_code} for {url}")

async def main(index_days: int):
    currency_service = PrivatBankCurrencyService()
    rates = await currency_service.get_currency_rates(index_days)
    if rates:
        print(rates)

if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    index_days = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    asyncio.run(main(index_days))