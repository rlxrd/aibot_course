from app.database.models import async_session
from app.database.models import User, AiType, AiModel, Order
from sqlalchemy import select, update, delete, desc
from decimal import Decimal


def connection(func):
    async def inner(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)
    return inner


@connection
async def set_user(session, tg_id):
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    
    if not user:
        session.add(User(tg_id=tg_id, balance='0'))
        await session.commit()


@connection
async def get_user(session, tg_id):
    return await session.scalar(select(User).where(User.tg_id == tg_id))


@connection
async def get_users(session):
    return await session.scalars(select(User))


@connection
async def calculate(session, tg_id, summ, model_name, user):
    model = await session.scalar(select(AiModel).where(AiModel.name == model_name))
    new_balance = Decimal(Decimal(user.balance) - Decimal(Decimal(model.price) * Decimal(summ)))
    await session.execute(update(User).where(User.id == user.id).values(balance=str(new_balance)))
    await session.commit()
