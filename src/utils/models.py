from pydantic import BaseModel, Field
from typing import List

class ChunkMetadata(BaseModel):
    source: str = Field(..., description="File path of the document")
    chunk: int = Field(..., ge=0, description="Chunk index within the document")

class RetrievedChunk(BaseModel):
    text: str
    meta: ChunkMetadata
    distance: float | None = None #Optional

class LLMResponse(BaseModel):
    answer: str
    sources: List[ChunkMetadata]