from sqlalchemy import Column, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
import uuid

Base = declarative_base()

class CampaignStatus(str, Enum):
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

    id: Column[UUID] = Column(String(36), primary_key=True, default=uuid4)
    created_at: Column[dt.datetime] = Column(DateTime, default=dt.datetime.now)
    status: Column[CampaignStatusType] = Column(Enum(CampaignStatus), nullable=False)