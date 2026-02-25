from pydantic import BaseModel, EmailStr, Field


# ── Auth ──────────────────────────────────────────────────────────────────────

class RegisterUser(BaseModel):
    email: EmailStr
    username: str
    password: str = Field(min_length=6)


class LoginUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


# ── Habits ────────────────────────────────────────────────────────────────────

class CreateHabit(BaseModel):
    name: str


class UpdateHabit(BaseModel):
    name: str
