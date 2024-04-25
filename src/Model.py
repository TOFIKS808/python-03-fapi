# pylint: disable=R0903, C0103
"""
    Budowa bazy danych
"""
from typing import List
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    """ Base class """


class User(Base):
    """ budowa tabeli users """
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column((String(1000)))
    username: Mapped[str] = mapped_column((String(1000)))
    email: Mapped[str] = mapped_column((String(1000)))
    phone: Mapped[str] = mapped_column((String(1000)))
    website: Mapped[str] = mapped_column((String(1000)))
    company: Mapped["Company"] = relationship(back_populates="user", cascade="all, delete-orphan", lazy="selectin")
    address: Mapped["Address"] = relationship(back_populates="user", cascade="all, delete-orphan", lazy="selectin")
    posts: Mapped[List["Post"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    albums: Mapped[List["Album"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    todos: Mapped[List["Todo"]] = relationship(back_populates="user", cascade="all, delete-orphan")



    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, name={self.name!r}, username={self.username!r}, email={self.email!r}, "
                f"phone={self.phone!r}, website={self.website!r}), "
                f"company={self.company}, "
                f"address={self.address})"
                )


class Company(Base):
    """ budowa tabeli company """
    __tablename__ = "company"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="company")
    name: Mapped[str] = mapped_column((String(1000)))
    catch_phrase: Mapped[str] = mapped_column((String(1000)))
    bs: Mapped[str] = mapped_column((String(1000)))

    def __repr__(self) -> str:
        return (f"Company(id={self.id}, name={self.name!r}, catch_phrase={self.catch_phrase!r}, "
                f"bs={self.bs!r}, user_id={self.user_id!r})")


class Address(Base):
    """ budowa tabeli address """
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="address")
    street: Mapped[str] = mapped_column((String(1000)))
    suite: Mapped[str] = mapped_column((String(1000)))
    city: Mapped[str] = mapped_column((String(1000)))
    zipcode: Mapped[str] = mapped_column((String(1000)))
    geo: Mapped["Geo"] = relationship(back_populates="address", cascade="all, delete-orphan", lazy="selectin")

    def __repr__(self) -> str:
        return (f"Address(id={self.id!r}, user_id={self.user_id!r},  street={self.street!r},"
                f" suite={self.suite!r}, city={self.city!r}, zipcode={self.zipcode!r}, geo={self.geo})")


class Geo(Base):
    """ budowa tabeli geo """
    __tablename__ = "geo"
    id: Mapped[int] = mapped_column(primary_key=True)
    address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))
    address: Mapped["Address"] = relationship(back_populates="geo")
    lat: Mapped[str] = mapped_column((String(1000)))
    long: Mapped[str] = mapped_column((String(1000)))

    def __repr__(self) -> str:
        return f"Geo(id={self.id!r}, address_id={self.address_id}, lat={self.lat!r}, long={self.long!r})"


class Post(Base):
    """ struktura tabeli post """
    __tablename__ = "post"
    __table_args__ = {'sqlite_autoincrement': True}
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(1000))
    body: Mapped[str] = mapped_column(String(1000))
    user: Mapped["User"] = relationship(back_populates="posts")
    comments = relationship("Comment", back_populates="post", passive_deletes=True)

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, user_id={self.user_id!r}, title={self.title!r}, body={self.body!r})"


class Comment(Base):
    """ struktura tabeli comment """
    __tablename__ = "comment"
    id: Mapped[int] = mapped_column(primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column((String(1000)))
    email: Mapped[str] = mapped_column((String(1000)))
    body: Mapped[str] = mapped_column((String(1000)))
    post = relationship('Post', back_populates="comments")

    def __repr__(self) -> str:
        return f"Comment(id={self.id!r}, post_id={self.post_id}, email={self.email!r}, body={self.body!r})"


class Album(Base):
    """ budowa tabeli album """
    __tablename__ = "album"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column((String(1000)))
    user: Mapped["User"] = relationship(back_populates="albums")
    photos: Mapped[List["Photo"]] = relationship(back_populates="album", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"Comment(id={self.id!r}, user_id={self.user_id!r}, title={self.title!r})"


class Photo(Base):
    """ budowa tabeli photo """
    __tablename__ = "photo"
    id: Mapped[int] = mapped_column(primary_key=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("album.id"))
    title: Mapped[str] = mapped_column((String(1000)))
    album: Mapped["Album"] = relationship(back_populates="photos")
    url: Mapped[str] = mapped_column((String(1000)))
    thumbnail_url: Mapped[str] = mapped_column((String(1000)))


class Todo(Base):
    """ budowa tabeli todo """
    __tablename__ = "todo"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column((String(1000)))
    completed: Mapped[bool] = mapped_column(Boolean)
    user: Mapped["User"] = relationship(back_populates="todos")
