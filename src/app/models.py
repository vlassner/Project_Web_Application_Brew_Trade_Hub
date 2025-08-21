from enum import Enum
from datetime import date, datetime
from typing import Set, List
from uuid import uuid1

from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin

class UserType(Enum):
    user = "User"
    administrator = "Administrator"

class User(db.Model, UserMixin):
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    password = mapped_column(db.LargeBinary)
    user_type: Mapped[UserType] = mapped_column()
    creationDate: Mapped[date] = mapped_column(db.Date, default=date.today())
    email: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    state: Mapped[str] = mapped_column()
    website: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

class OfferStatus(Enum):
    opened = 'opened'
    accepted = 'accepted'
    shipped = 'shipped'
    received = 'received'

class Catalog(db.Model):
    id: Mapped[str] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(nullable=True)
    representative_name: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    password = mapped_column(db.LargeBinary)
    user_type: Mapped[UserType] = mapped_column()
    offers: Mapped[Set['Offer']] = relationship() # backpops the users relationship (in Offer class)

class Offer(db.Model):
    __tablename__ = "offer"

    code: Mapped[str] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    productType: Mapped[str] = mapped_column()
    brand: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column(nullable=True)
    status: Mapped[OfferStatus] = mapped_column()
    catalog_id: Mapped[str] = mapped_column(ForeignKey(Catalog.id), nullable=True)
    buyer_id: Mapped[str] = mapped_column(ForeignKey(User.id), nullable=True)
    seller_id: Mapped[str] = mapped_column(ForeignKey(User.id))

User.purchases: Mapped[List[Offer]] = relationship('Offer', foreign_keys=[Offer.buyer_id])
User.sales: Mapped[List[Offer]] = relationship('Offer', foreign_keys=[Offer.seller_id])

class Review(db.Model):
    __tablename__ = "review"
    user_id: Mapped[str] = mapped_column(ForeignKey(User.id))
    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid1()))
    dateAndTime: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.today())
    star_rating: Mapped[int] = mapped_column(default=0) # should only range from 1 to 5 (will need to be change to account for .5 stars if we want).
    comment: Mapped[str] = mapped_column()

User.reviews: Mapped[Set[Review]] = relationship('Review')

class Reply(db.Model):
    __tablename__ = "reply"
    review_id: Mapped[str] = mapped_column(ForeignKey(Review.id), primary_key=True)
    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid1()))
    dateAndTime: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.today())
    comment: Mapped[str] = mapped_column()

Review.replies: Mapped[List[Reply]] = relationship('Reply') # make sure these are chronological, might need a new class to hold reply dates?
