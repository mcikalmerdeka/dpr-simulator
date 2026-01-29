"""DPR Member model."""

from pydantic import BaseModel, Field
from typing import List


class DPRMember(BaseModel):
    """Represents a single DPR (Indonesian Parliament) member."""

    id: int = Field(..., description="Unique identifier for the member")
    name: str = Field(..., description="Name of the DPR member")
    faction: str = Field(..., description="Political faction (Fraksi)")
    komisi: str = Field(..., description="Commission (Komisi I - XIII)")
    dapil: str = Field(..., description="Electoral district (Daerah Pemilihan)")
    province: str = Field(..., description="Province represented")
    expertise: List[str] = Field(
        default_factory=list,
        description="Areas of expertise (ekonomi, pendidikan, etc.)",
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.faction}, {self.komisi}) - {self.dapil}, {self.province}"

    def to_prompt_context(self) -> str:
        """Generate context string for LLM prompts."""
        return (
            f"Nama: {self.name}\n"
            f"Fraksi: {self.faction}\n"
            f"Komisi: {self.komisi}\n"
            f"Daerah Pemilihan: {self.dapil}, {self.province}\n"
            f"Keahlian: {', '.join(self.expertise)}"
        )
