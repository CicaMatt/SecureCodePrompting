from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, mapper
from sqlalchemy.dialects.postgresql import ENUM
import enum

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class CampaignStatus(str, enum.Enum):
    activated = "activated"
    deactivated = "deactivated"

CampaignStatusType = ENUM(
    CampaignStatus,
    name="campaignstatus",
    create_constraint=True,
    metadata=Base.metadata,
    validate_strings=True,
)

class Campaign(Base):
    __tablename__ = "campaign"

    id = mapped_column(primary_key=True, default=uuid4)
    created_at = mapped_column(default=dt.datetime.now)
    status = mapped_column(nullable=False)

metadata.create_all(engine)
mapper(Campaign, campaigns)