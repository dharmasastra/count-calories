import pandas as pd
import itertools
from fastapi import APIRouter, Response, status

from src.models.kalori import KaloriModel
from src.utils.count_age import count_age
from src.utils.count_weight import count_weight
from src.utils.count_activity import count_activity

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
    imt, value_sangat_kurus, value_kurus, value_normal, value_gemuk, value_sangat_gemuk = count_weight(calori.weight, calori.height)
    value_aktivitas, value_istirahat, value_ringan, value_sedang, value_berat, value_sangat_berat= count_activity(calori.activity, calori.gender)
    # return {"value_muda": value_muda, "value_parobaya": value_parobaya, "value_tua": value_tua, "value_sangat_tua": value_sangat_tua}
    
    path = "src/utils/data.csv"
    data = pd.read_csv(path)
    
    predikat = []
    first = [value_muda, value_parobaya, value_tua, value_sangat_tua]
    second = [value_sangat_kurus, value_kurus, value_normal, value_gemuk, value_sangat_gemuk]
    third = [value_istirahat, value_ringan, value_sedang, value_berat, value_sangat_berat]

    age = []
    beartBadan = []
    aktifitas = []
    z = []

    for _ in range(2):
        for i in range (4):
            for j in itertools.repeat(first[i], 25):
                age.append(j)
    for _ in range(8):
        for i in range(5):
            for k in itertools.repeat(second[i], 5):
                beartBadan.append(k)

    for _ in range(40):
        for i in range(5):
            for l in itertools.repeat(third[i], 1):
                aktifitas.append(l)

    for i in range(200):
        if(data["Jenis Kelamin"][i] == "L" and calori.gender == "L"):
                predikat.append(min(age[i], beartBadan[i], aktifitas[i]))
                z.append(min(age[i], beartBadan[i], aktifitas[i]) * pd.Series(data["Kalori"][i]).str.replace(',', '').astype(int)[0])
        elif(data["Jenis Kelamin"][i] == "P" and calori.gender == "P"):
                predikat.append(min(age[i], beartBadan[i], aktifitas[i]))
                z.append(min(age[i], beartBadan[i], aktifitas[i]) * pd.Series(data["Kalori"][i]).str.replace(',', '').astype(int)[0])

    sum_predikat = sum(predikat)
    sum_z = sum(z)
    cal_final = sum_z / sum_predikat
    # return {"fuzzyfication_age": count_age(calori.age), "fuzzyfication_weight": count_weight(calori.weight, calori.height), "fuzzyfication_activity": count_activity(calori.activity, calori.gender)}
    return {"kalori": cal_final}