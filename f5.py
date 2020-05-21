def bmi_f15(msg):
    segments = msg.split()
    height = int(segments[len(segments) - 1])
    weight = int(segments[len(segments) - 2])
    bmic=''
    bmi = weight/(((height)/100)**2)
    print(bmi)
    if ( bmi < 16):
        bmic="severely underweight"
    elif ( bmi >= 16 and bmi < 18.5):
        bmic="underweight"
    elif ( bmi >= 18.5 and bmi < 25):
        bmic="Healthy"
    elif ( bmi >= 25 and bmi < 30):
        bmic="overweight"
    elif ( bmi >=30):
        bmic="severely overweight"
    return "your BMI is:" + "{:.2f}".format(bmi) + " and you are :" + str(bmic)
