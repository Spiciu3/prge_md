from fastapi import APIRouter
router = APIRouter()

def connect_to_db()
    return create_engine(
        f'postgresql://postgres:postgres@localhost:5432/postgres',
    )




@router.get('/insert user')
async def inster_user():
    try db.connection =



    except Exception as e:
        print(e)
        raise e

return {'status': 1}