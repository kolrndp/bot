import asyncio
from handlers import all_user_routers
from handlers.loader import bot, dp

async def main():
    for router in all_user_routers:
        dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
