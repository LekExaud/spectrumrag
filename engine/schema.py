# engine/schema.py
from pydantic import BaseModel, Field

class FrequencyLookupSchema(BaseModel):
    band_name: str = Field(description="The standard designation of the frequency band, e.g., C-band, mmWave, UHF.")
    frequency_start_mhz: float = Field(description="Starting frequency of the range in MHz.")
    frequency_end_mhz: float = Field(description="Ending frequency of the range in MHz.")
    region: str = Field(description="ITU Region or national jurisdiction, e.g., Region 1, TCRA.")

# OpenAI tool definition format
SPECTRUM_TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "lookup_spectrum_band",
        "description": "Look up frequency allocation and regulatory status for a given telecom band.",
        "parameters": FrequencyLookupSchema.model_json_schema()
    }
}