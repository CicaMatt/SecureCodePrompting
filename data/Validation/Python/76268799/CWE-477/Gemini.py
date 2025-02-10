import datetime as dt
from uuid import uuid4

import enum
from sqlalchemy import create_engine, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class CampaignStatus(enum.Enum):
    activated = "activated"
    deactivated = "deactivated"


class Campaign(Base):
    __tablename__ = "campaign"

    id: Mapped[uuid4] = mapped_column(primary_key=True, default=uuid4)
    created_at: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.now
    )
    status: Mapped[CampaignStatus] = mapped_column(
        Enum(CampaignStatus), nullable=False
    )


# Example usage (replace with your database URL)
engine = create_engine("postgresql://user:password@host:port/database")
Base.metadata.create_all(engine)