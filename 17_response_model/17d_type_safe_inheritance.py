


class BaseUser(BaseModel):
    username: str
    email: str

class UserIn(BaseUser):  # Inherits base fields
    password: str  # Adds sensitive field

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:  # ✅ Valid type hierarchy
    return user  # FastAPI filters to BaseUser fields