"""User domain model and schemas."""

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    """Request schema for creating a user."""

    name: str = Field(..., min_length=1)
    email: EmailStr


class UserResponse(BaseModel):
    """Response schema for user."""

    id: str
    name: str
    email: str
