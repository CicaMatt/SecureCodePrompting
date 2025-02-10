from sqlalchemy import Column, Integer, String, Enum

class CampaignStatus(str, enum.Enum):
    activated = "activated"
    deactivated = "deactivated"

class Campaign(Base):
    __tablename__ = "campaign"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    created_at: Mapped[dt.datetime] = mapped_column(default=dt.datetime.now)
    status: Mapped[Enum[CampaignStatus]] = mapped_column(nullable=False)