from fastapi import APIRouter, Response, status
from src.models.kalori import KaloriModel
from src.utils.count_age import count_age

router = APIRouter(
    prefix="/kalori",
    tags=["Kalori"],
    responses={404: {"description": "Not Found"}},
)

@router.post("/countCalories")
async def count_calories(calori: KaloriModel, response: Response):
    
    if(calori.gender=="L"):
        value_bmr = 66.5+(13.7 * calori.weight)+(5*calori.height)-(6.8 * calori.age)
    elif(calori.gender=="P"):
        value_bmr = 65.5+(9.6*calori.weight)+(1.8*calori.height)-(4.7*calori.age)
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "gender error"}

    value_muda, value_parobaya, value_tua, value_sangat_tua = count_age(calori.age)

    # return {"value_muda": value_muda, "value_parobaya": value_parobaya, "value_tua": value_tua, "value_sangat_tua": value_sangat_tua}
    return {"fuzzyfication_age": count_age(calori.age)}