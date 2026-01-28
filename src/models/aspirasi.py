"""Aspirasi (Public Aspiration) model."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


class Aspirasi(BaseModel):
    """Represents a public aspiration/concern from citizens."""

    id: int = Field(..., description="Unique identifier for the aspiration")
    source: str = Field(..., description="Region or community source")
    category: str = Field(..., description="Category of the aspiration")
    content: str = Field(..., description="Content of the aspiration")
    priority: Literal["Tinggi", "Sedang", "Rendah"] = Field(
        default="Sedang", description="Priority level"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now, description="When the aspiration was submitted"
    )

    def __str__(self) -> str:
        return f"[{self.priority.upper()}] {self.category}: {self.content[:50]}..."

    def to_prompt_context(self) -> str:
        """Generate context string for LLM prompts."""
        return (
            f"Kategori: {self.category}\n"
            f"Sumber: {self.source}\n"
            f"Isi: {self.content}\n"
            f"Prioritas: {self.priority}"
        )
