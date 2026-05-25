# 파일이름 : 기름값 계산 및 차 기변 시뮬레이션 시스템
# 작 성 자 : 60252139 최민서

total = 0

def calc(dist, eff):
    global total
    cost = int((dist / eff) * 1650)
    total += cost
    return cost
def get_info():
    model = input("모델명: ")
    eff = float(input("연비: "))
    mile = int(input("주행거리: "))
    return model, eff, mile

def check(mile, eff):
    if mile >= 10000 and eff < 10.0: return "정밀 점검 필요"
    if mile >= 10000 or eff < 8.0: return "소모품 교체 권장"
    return "상태양호"

def run()
    trips = []
    model, eff, mile = get_info()

    while True:
        print("\n1.거리입력 2.분석 3.종료")
        sel = input("메뉴선택: ")

        if sel == '1':
            trips.append(float(input("주행거리(km): ")))

          elif sel == '2':
            dist = sum(trips)
            cost = calc(dist, eff)
            print(f"[{model}] 이번 비용:{cost}원 / 누적: {total}원 / 상태: {check(mile, eff)}")

          elif sel == '3':
            print("종료합니다.")
            break


run()      