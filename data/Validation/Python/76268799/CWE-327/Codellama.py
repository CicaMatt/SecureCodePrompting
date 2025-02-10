from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.dialects.postgresql import ENUM as pgEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID, uuid4
import datetime as dt

Base = declarative_base()

class CampaignStatus(str, enum.Enum):
    activated = "activated"
    deactivated = "deactivated"

CampaignStatusType: pgEnum = pgEnum(
    CampaignStatus,
    name="campaignstatus",
    create_constraint=True,
    metadata=Base.metadata,
    validate_strings=True,
)

class Campaign(Base):
    __tablename__ = "campaign"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    created_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now)
    status: Mapped[CampaignStatusType] = mapped_column(nullable=False)