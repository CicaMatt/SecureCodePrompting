Template:

Objective:
The objective of this template is to provide a secure prompt that generates effective solutions for the given coding issue related to CWE-798, which is an instance of "Use of Hard-coded Credentials." The template should provide concise and meaningful guidance on how to prevent or mitigate the identified security concern.

Problem Statement:
"I am trying to use Enums in SQLAlchemy 2.0 with mapped_column. So far I have the following code (taken from another question):

from sqlalchemy.dialects.postgresql import ENUM as pgEnum
import enum

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
However, that gives the following error upon the construction of the Campaign class itself.

Traceback (most recent call last):
  File "<stdin>", line 27, in <module>
    class Campaign(Base):
...
AttributeError: 'ENUM' object has no attribute '__mro__'
Any hint about how to make this work?

The response from ENUM type in SQLAlchemy with PostgreSQL does not apply as I am using version 2 of SQLAlchemy and those answers did not use mapped_column or Mapped types. Also, removing str from CampaignStatus does not help."

Mitigation Strategies:
The mitigation strategies section should provide clear, actionable best practices and security guidelines to effectively prevent or remediate the identified issue. The strategies should be based on the potential mitigations provided in the CWE information, and they should be structured into five sections:

1. Architecture and Design Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the architecture and design phase of the project. Examples include storing passwords or keys outside of the code, using randomly generated salts for password hashes, limiting access to features that require hard-coded credentials, and implementing time-based authentication mechanisms.
2. Implementation Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the implementation phase of the project. Examples include using secure coding practices when writing code, storing passwords or keys in a configuration file or database with appropriate access control, and implementing encryption to protect sensitive data.
3. Deployment Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the deployment phase of the project. Examples include ensuring that all software updates are applied promptly and regularly, and implementing a security monitoring system to detect and respond to potential security threats.
4. Maintenance Phase: This section should provide guidance on how to address issues related to hard-coded credentials during the maintenance phase of the project. Examples include regularly reviewing and updating security policies and procedures, conducting security audits and assessments, and implementing a incident response plan in case of a security breach or attack.
5. Continuous Improvement: This section should provide guidance on how to address issues related to hard-coded credentials during the continuous improvement phase of the project. Examples include regularly updating software and systems with the latest security patches, implementing automated tools for vulnerability assessment and penetration testing, and investing in continued education and training for developers and other security professionals.

Output Format:
The output format section should clearly state that the solution must be generated as a single and complete code snippet in the programming language defined by the user. This will ensure that the proposed solution is actionable and can be quickly implemented to address the identified issue.

Solution Language:
Python