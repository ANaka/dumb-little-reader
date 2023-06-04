from pydantic import BaseModel
from typing import List, Optional
from enum import Enum


class ReactionType(str, Enum):
    liked = "liked"
    loved = "loved"
    disliked = "disliked"


class Feed(BaseModel):
    url: str
    title: Optional[str] = None
    link: Optional[str] = None
    description: Optional[str] = None


class Item(BaseModel):
    title: str
    link: str
    description: Optional[str] = None
    pub_date: Optional[str] = None
    read: bool = False
    reaction: Optional[ReactionType] = None


class Reaction(BaseModel):
    item_id: str
    reaction_type: ReactionType