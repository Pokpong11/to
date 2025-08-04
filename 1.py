income = float(input("กรุณาใส่รายได้ต่อเดือน (บาท): "))

if income < 15000:
    print("คุณไม่มีสิทธิ์ในการทำบัตรเครดิต")
else:
    if income < 30000:
        print("วงเงินน้อยสุด ไม่มีการทำบัตร")
    elif income <= 89999:
        print("คุณจะได้สิทธิ์บัตรเงิน")
    elif income <= 99999:
        print("คุณจะได้สิทธิ์บัตรทอง")
    else:
        print("คุณจะได้สิทธิ์บัตร Platinum")