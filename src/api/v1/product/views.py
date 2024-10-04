from ninja import Router



router = Router()

@router.get("")
def message():
    return {"message": "Hello, World"}