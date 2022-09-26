
def count_weight(weight, height):
    imt = weight / ((height/100)**2)

    #fuzzifikasi sangat kurus
    if (imt<=16):
        value_sangat_kurus = 1
    elif (imt>16.5):
        value_sangat_kurus =0
    else:
        value_sangat_kurus = (16.5-imt)/(16.5-16)
        
    #fuzzifikasi kurus
    if (imt <= 16.5 or imt >= 18.5):
        value_kurus = 0
    elif (imt >= 17 and imt <= 18 ):
        value_kurus = 1
    elif (imt > 16.5 and imt < 17):
        value_kurus = (imt-16.5)/(17-16.5)
    else:
        value_kurus = (18.5-imt)/(18.5-18)

    #fuzzifikasi normal
    if (imt <= 18 or imt >= 25):
        value_normal = 0
    elif (imt >= 18.5 and imt <= 24.5 ):
        value_normal = 1
    elif (imt > 18 and imt < 18.5):
        value_normal = (imt-18)/(18.5-18)
    else:
        value_normal = (25-imt)/(25-24.5)

    #fuzzifikasi gemuk
    if (imt <= 24.5 or imt >= 27):
        value_gemuk = 0
    elif (imt >= 25 and imt <= 26.5 ):
        value_gemuk = 1
    elif (imt > 24.5 and imt < 25):
        value_gemuk = (imt-24.5)/(25-24.5)
    else:
        value_gemuk = (27-imt)/(27-26.5)

    #fuzzifikasi sangat gemuk
    if (imt <= 26.5):
        value_sangat_gemuk = 0
    elif (imt >= 27):
        value_sangat_gemuk = 1
    else:
        value_sangat_gemuk = (imt-26.5)/(27-26.5)

    return imt, value_sangat_kurus, value_kurus, value_normal, value_gemuk, value_sangat_gemuk
