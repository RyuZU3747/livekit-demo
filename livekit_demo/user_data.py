from livekit.agents import RunContext
from livekit.agents.voice import Agent
from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class UserData:
    agents: Dict[str, Agent]
    prev_agent: Optional[Agent]
    user_id: str

RunContext_T = RunContext[UserData]