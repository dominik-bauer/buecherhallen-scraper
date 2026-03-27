from pydantic import BaseModel, ConfigDict, SecretStr


class BuechhallenAccount(BaseModel):
    displayname: str
    username: str
    password: SecretStr


class LoanItem(BaseModel):
    model_config = ConfigDict(extra="allow")
