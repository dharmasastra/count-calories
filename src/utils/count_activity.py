
def count_activity(activity, gender):
    #fuzzifikasi istirahat
    if (activity<=2):
        value_istirahat = 1
    elif (activity>4):
        value_istirahat = 0
    else:
        value_istirahat = (4-activity)/(4-2)
        
    #fuzzifikasi ringan
    if (activity <= 3 or activity >= 5):
        value_ringan = 0
    elif (activity == 4):
        value_ringan = 1
    elif (activity > 3 and activity < 4):
        value_ringan = (activity-3)/(4-3)
    else:
        value_ringan = (5-activity)/(5-4)

    #fuzzifikasi sedang
    if (activity <= 4 or activity >= 8):
        value_sedang = 0
    elif (activity == 6):
        value_sedang = 1
    elif (activity > 4 and activity < 6):
        value_sedang = (activity-4)/(6-4)
    else:
        value_sedang = (8-activity)/(8-6)

    #fuzzifikasi berat
    if (activity <= 7 or activity >= 9):
        value_berat = 0
    elif (activity == 8):
        value_berat = 1
    elif (activity > 7 and activity < 8):
        value_berat = (activity-7)/(8-7)
    else:
        value_berat = (9-activity)/(9-8)
        
    #fuzzifikasi sangat berat
    if (activity <= 8):
        value_sangat_berat = 0
    elif (activity >= 10):
        value_sangat_berat = 1
    else:
        value_sangat_berat = (activity-8)/(10-8)

    if(activity<2.9):
        value_aktivitas=1.3
    elif (activity<5 and gender=="L"):
        value_aktivitas=1.65
    elif(activity<5 and gender=="P"):
        value_aktivitas=1.55
    elif(activity<7.5 and gender=="L"):
        value_aktivitas=1.76
    elif(activity<5 and gender=="P"):
        value_aktivitas=1.7
    elif(activity<9 and gender=="L"):
        value_aktivitas=2.1
    else:
        value_aktivitas=2

    return value_aktivitas, value_istirahat, value_ringan, value_sedang, value_berat, value_sangat_berat