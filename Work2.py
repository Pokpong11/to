def calculate_bmi(weight_kg, height_m):
    """
    คำนวณค่าดัชนีมวลกาย (BMI) และระบุสถานะน้ำหนัก

    Args:
        weight_kg (float): น้ำหนักเป็นกิโลกรัม
        height_m (float): ส่วนสูงเป็นเมตร

    Returns:
        tuple: ทูเพิลที่ประกอบด้วยค่า BMI (float) และสถานะน้ำหนัก (str)
    """
    if height_m <= 0:
        return None, "ความสูงไม่ถูกต้อง: ความสูงต้องมากกว่า 0"

    bmi = weight_kg / (height_m ** 2)
    
    status = ""
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 25:
        status = "Normal weight"
    elif 25 <= bmi < 30:
        status = "Overweight"
    else:
        status = "Obesity"
    
    return round(bmi, 1), status