from pydantic import BaseModel, Field
from typing import Optional

class IDCardModel(BaseModel):
    id_number: Optional[str] = Field(None, description="ID number")
    kh_name: Optional[str] = Field(None, description="Name in Khmer")
    en_name: Optional[str] = Field(None, description="Name in English")
    dob: Optional[str] = Field(None, description="Date of birth in khmer number")
    gender: Optional[str] = Field(None, description="Gender")
    height: Optional[str] = Field(None, description="Height with it unit like ស.ម")
    place_of_birth: Optional[str] = Field(None, description="Place of birth")
    address: Optional[str] = Field(None, description="Address")
    expire: Optional[str] = Field(None, description="Expire date it have start date and end date")
    distinguishing_feature: Optional[str] = Field(None, description="Noted is ភិនភាគ in ID card image")

class ResponseModel(BaseModel):
    id_card: Optional[IDCardModel] = Field(None, description="ID card")