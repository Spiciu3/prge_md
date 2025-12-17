from fastapi import APIRouter

@app.get('/endpoint')
async def endpoint():
    return [
        {'imie': 'Adrian'},
        {'imie': 'Mateusz'},
        {'imie': 'Bassam'},
    ]