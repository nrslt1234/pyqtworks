import sqlite3


conn= sqlite3.connect("DB.db")
cur = conn.cursor()

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, create_engine, select, insert, delete, update
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship



# database_url = "sqlite:///DB.db"
database_url = "postgresql+psycopg2://postgres:03092006@localhost:5432/Games"
engine = create_engine(database_url, echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    FIO: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    passport: Mapped[str] = mapped_column()

    guess_prog: Mapped["GuessProg"] = relationship(back_populates="user")
    progress: Mapped["Progress"] = relationship(back_populates="user")


    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.FIO!r}, fullname={self.email!r})"


class Progress(Base):
    __tablename__ = "progress"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    wins: Mapped[int] = mapped_column()
    draw: Mapped[int] = mapped_column()
    loss: Mapped[int] = mapped_column()

    user: Mapped["User"] = relationship(back_populates="progress")


    def __repr__(self) -> str:
        return f"Progress(id={self.id!r}, wins={self.wins!r}, draw={self.draw!r}, loss={self.loss!r})"


class GuessProg(Base):
    __tablename__ = "guess_prog"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    history: Mapped[int] = mapped_column()
    my_choice: Mapped[int] = mapped_column()

    user: Mapped["User"] = relationship(back_populates="guess_prog") # guess_prog.user.id

    def __repr__(self) -> str:
        return f"GuessProg(id={self.id!r}, history = {self.history!r}, my_choice = {self.my_choice!r})"



def check_user(email, password):
    stmt = select(User).where(User.email == email, User.passport == password)
    user = session.execute(stmt).scalar_one_or_none()
    if user is None:
        return  False, user
    else:
        return True, user

def check_user_his_email(email):
    stmt = select(User).where(User.email == email)
    user = session.execute(stmt).scalar_one_or_none()
    return user


Base.metadata.create_all(bind = engine)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
# def check_user(email, password):
#     user = cur.execute(f"SELECT * FROM user WHERE email = '{email}' AND passport= '{password}'").fetchone()
#     if user is None:
#         return  False, user
#     else:
#         return True, user


def check_registration(email, password):
    # user = cur.execute(f"INSERT INTO user(email, passport) values('{email}', '{password}')")
    # conn.commit()

    user = User(email=email, passport=password)
    session.add(user)
    session.commit()


# def check_user_his_email(email):
#     user = cur.execute(f"SELECT * FROM user WHERE email = '{email}'").fetchone()
#     if user:
#         return True
#     else:
#         return False

def update_password(email, new_password):
    # cur.execute(f"UPDATE user SET passport = '{new_password}' WHERE email = '{email}'")
    # conn.commit()

    stmt = update(User).where(User.email == email).values(passport = new_password)
    session.execute(stmt)
    session.commit()


def update_new_result(user_id, wins=0, loss=0, draw=0):
    # current_progress = cur.execute(f"SELECT wins, loss, draw FROM progress WHERE user_id = {user_id}").fetchone()
    # как здесь написать, когда нужен return
    stmt = select(Progress).where(Progress.user_id == user_id)
    current_progress = session.execute(stmt).scalar_one_or_none()

    if current_progress is None:
        # progress = cur.execute(f"INSERT INTO progress(user_id, wins, loss, draw) values({user_id}, {wins}, {loss}, {draw})")
        # conn.commit()
        progress = Progress(user_id=user_id, wins=wins,loss = loss, draw = draw)
        session.add(progress)
        session.commit()
    else:
        if wins == 1:
            # cur.execute(f"UPDATE progress SET wins = {current_progress.wins + 1} WHERE user_id = {user_id}")
            stmt = update(Progress).where(Progress.user_id == user_id).values(wins = current_progress.wins + 1)



        if loss == 1:
            # cur.execute(f"UPDATE progress SET loss = {current_progress.loss + 1} WHERE user_id = {user_id}")
            stmt = update(Progress).where(Progress.user_id == user_id).values(wins=current_progress.loss + 1)

        if draw == 1:
            # cur.execute(f"UPDATE progress SET draw = {current_progress.draw + 1} WHERE user_id = {user_id}")
            stmt = update(Progress).where(Progress.user_id == user_id).values(wins=current_progress.draw + 1)

        session.execute(stmt)
        session.commit()


def delete_progress(user_id):
    # cur.execute(f"DELETE from progress WHERE user_id = {user_id}")
    # conn.commit()

    stmt = delete(Progress).where(Progress.user_id == user_id)
    session.commit()

def add_history_from_guess_the_number(user_id, history, my_choice):
    # guess_prog = cur.execute(f"INSERT INTO guess_prog (history, my_choice, user_id) values({history}, {my_choice}, {user_id})")
    # conn.commit()
    # 1 способ
    guess_prog = GuessProg(history=history, my_choice=my_choice, user_id= user_id)
    session.add(guess_prog)
    session.commit()

    # 2 способ
    stmt = insert(GuessProg).values(history=history, my_choice=my_choice, user_id= user_id)
    session.execute(stmt)
    session.commit()


def select_my_result(user_id):
    # res = cur.execute(f"SELECT wins, loss, draw FROM progress WHERE user_id = {user_id}").fetchone()
    # return res

    stmt = select(Progress).where(Progress.user_id == user_id)
    progress = session.execute(stmt).scalar_one_or_none()
    return progress

def select_add_history_from_guess_the_number(user_id):

    # guess_prog = cur.execute(f"SELECT fio, history, my_choice FROM guess_prog INNER JOIN user ON guess_prog.user_id = user.id WHERE guess_prog.user_id = {user_id}").fetchall()
    # return guess_prog

    stmt = select(GuessProg)
    guess_prog = session.execute(stmt).scalars().all()
    return guess_prog
    #Как написать метод с Join

def rate_person_by_win(user_id):

    # winning = cur.execute(f"SELECT FIO, wins FROM progress INNER JOIN user ON progress.user_id = user.id ORDER BY wins DESC").fetchall()
    # return winning
    stmt = select(Progress).order_by(-Progress.wins)
    progress = session.execute(stmt).scalars().all()
    return progress # [progress@162371623, progress@17253981]


def rate_person_by_loss(user_id):

    # lossing = cur.execute(f"SELECT FIO, loss FROM progress INNER JOIN user ON progress.user_id = user.id ORDER BY loss DESC").fetchall()
    # return lossing

    stmt = select(Progress).order_by(-Progress.loss)
    progress = session.execute(stmt).scalars().all()
    return progress

def rate_person_by_draw(user_id):

    stmt = select(Progress).order_by(-Progress.draw)
    progress = session.execute(stmt).scalars().all()
    return progress

    # drawing = cur.execute(f"SELECT FIO, draw FROM progress INNER JOIN user ON progress.user_id = user.id ORDER BY draw DESC").fetchall()
    # return drawing



