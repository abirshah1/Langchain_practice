from pydantic import BaseModel, Field
from typing import List

class ChatResponse(BaseModel):
    answer: str = Field(..., description="The main answer to the user's question.")
    summary: str = Field(..., description="A one-sentence summary of the answer.")
    confidence: float = Field(
        ..., ge=0.0, le=1.0,
        description="Confidence score between 0 and 1."
    )
    category: str = Field(
        ..., description="One of: programming, math, general."
    )
    keywords: List[str] = Field(
        ..., description="3 to 6 key terms extracted from the question."
    )