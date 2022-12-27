from fastapi import FastAPI
from router.router import user

app = FastAPI()

app.include_router(user)


@user.post("/api/user")
def create_user(data_user):
    pass