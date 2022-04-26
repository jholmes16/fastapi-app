import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

app = _fastapi.FastAPI()

@app.post("/api/v1/users")
async def register_user(
  user: _schemas.UserRequest, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    # call to check if user with email exist
    db_user = await _services.getUserByEmail(email=user.email, db=db)
    # if user found throw exception
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already exist, try with another email!")

    # create the user and return a token
    db_user = await _services.create_user(user=user, db=db)
    return await _services.create_token(user=db_user)
