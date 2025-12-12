
from dotenv import dotenv_values
import os
from contextlib import contextmanager
from dataclasses import dataclass

from sqlalchemy import (
    create_engine, String, ForeignKey, Numeric, CheckConstraint, select
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship, Session, sessionmaker
)
from sqlalchemy.sql import text

# -----------------------------------------------------------------------------
# CONFIG
# -----------------------------------------------------------------------------
CONFIG = dotenv_values(".env")
DATABASE_URL = CONFIG.get("DATABASE_URl")

engine = create_engine(
    DATABASE_URL,
    echo=False,            # включите True для отладки SQL
    pool_pre_ping=True,   # проверка соединения
)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# -----------------------------------------------------------------------------
# MODELS
# -----------------------------------------------------------------------------
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    accounts: Mapped[list["Account"]] = relationship(back_populates="user")

class Account(Base):
    __tablename__ = "accounts"
    __table_args__ = (
        CheckConstraint("balance >= 0", name="ck_balance_non_negative"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    currency: Mapped[str] = mapped_column(String(3), nullable=False)  # ISO: RUB, USD...
    balance: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False, default=0)

    user: Mapped[User] = relationship(back_populates="accounts")

Base.metadata.create_all(bind = engine)

def create_user(email: str, name: str, initial_balance: float):
    with Session(engine) as session, session.begin():   # транзакция
        user = User(email=email, name=name)
        session.add(user)
        session.flush()  # получаем user.id

        acc = Account(user_id=user.id, currency = "RUB", balance=initial_balance)
        session.add(acc)
        return user.id
def transfer(account_from_id: int, account_to_id: int, amount: float):
    with Session(engine) as session, session.begin():   # транзакция
        acc_from = session.get(Account, account_from_id, with_for_update=True)
        acc_to = session.get(Account, account_to_id, with_for_update=True)

        if acc_from.balance < amount:
            raise ValueError("Недостаточно средств")

        acc_from.balance -= amount
        acc_to.balance += amount

def clear_tables():
    with Session(engine) as session:
        session.query(Account).delete()
        session.query(User).delete()
        session.commit()

cl = clear_tables()

# # создаём пользователей
u1 = create_user("alice@example.com", "Alice", 1000)
u2 = create_user("bob@example.com", "Bob", 200)

# достаём счета пользователей
with Session(engine) as session:
    acc1 = session.scalars(select(Account).where(Account.user_id == u1)).first()
    acc2 = session.scalars(select(Account).where(Account.user_id == u2)).first()
    print("Before transfer:", acc1.balance, acc2.balance)

# перевод
transfer(acc1.id, acc2.id, 150)

# подключение к сессии
with Session(engine) as session:
    acc1 = session.scalars(select(Account).where(Account.user_id == u1)).first()
    acc2 = session.scalars(select(Account).where(Account.user_id == u2)).first()
    print("After transfer:", acc1.balance, acc2.balance)

