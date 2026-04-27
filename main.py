# 파일이름 : 기름값 계산 및 차 기변 시뮬레이션 시스템
# 작 성 자 : 60252139 최민서

print("=== 스마트 드라이빙 매니저 V1.0 ===")

model = input("차량 이름을 입력하세요")
fuel_eff = float(input("공인 연비(Km/L): "))
mile = int(input("현재 주행거리(Km): "))
price = 1650
total_cost = 0

trips= []
print("\n최근 3번의 주행거리를 입력 받습니다.")

for i in range(1,4):
  dist = float(input(f"{i}번쨰 주행거리(Km): "))
  trips.append(dist)

total_dist = sum(trips)

gas_needed = total_dist / eff
total_cost += int(gas_needed * price)

print(f"\n[{model} 분석결과]")
print(f"총 주행 거리: {total_dist}km")
print(f"예상 총 주유비: {total_cost}원")

if mile >= 10000 and eff < 10.0:
  print("판정: 정밀 점검이 필요합니다.")
elif mile >= 10000 or eff < 8.0:
  print("판정: 소모품 교체를 권장합니다.")
else:
  print("판정: 차량 상태가 양호합니다.")

print(f"최근 주행 기록: {trip}")
print(f"이번 주행들로 지출된 예상 비용은 {total_cost}원 입니다.")
print("안전운전하세요")
  
