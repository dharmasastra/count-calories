
def count_age(age):
    #fuzzifikasi muda
    if (age<=25):
        value_muda = 1
    elif (age>40):
        value_muda =0
    else:
        value_muda = (40-age)/(40-25)
    
    #fuzzifikasi parobaya
    if (age <= 35 or age >= 60):
        value_parobaya = 0
    elif (age == 40):
        value_parobaya = 1
    elif (age > 35 and age < 40):
        value_parobaya = (age-35)/(40-35)
    else:
        value_parobaya = (60-age)/(60-40)

    #fuzzifikasi Tua
    if (age <= 55 or age >= 70):
        value_tua = 0
    elif (age == 60):
        value_tua = 1
    elif (age > 55 and age < 60):
        value_tua = (age-55)/(60-55)
    else:
        value_tua = (70-age)/(70-60)

    #fuzzifikasi sangat tua
    if (age <= 65):
        value_sangat_tua = 0
    elif (age >= 70):
        value_sangat_tua = 1
    else:
        value_sangat_tua = (age-65)/(70-65)

    return value_muda, value_parobaya, value_tua, value_sangat_tua