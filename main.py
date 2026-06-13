# 파일이름 : 기름값 계산 및 차 기변 시뮬레이션 시스템
# 작 성 자 : 60252139 최민서
data_list = [['아반떼', 12.5, 15000], ['쏘나타', 10.2, 8500]]

try:
    while True:
        print("\n--- 4차 과제 V3.0 메뉴 ---")
        print("1. 데이터 추가  2. 전체 데이터 출력  3. 파일 저장 후 종료")
        
        try: # 예외 처리 1: ValueError 방지 (필수 조건 4)
            menu = int(input("메뉴를 선택하세요: "))
        except ValueError:
            print("숫자만 입력해 주세요!")
            continue

        if menu == 1:
            name = input("차량명 입력: ")
            eff = float(input("연비 입력: "))
            mile = int(input("주행거리 입력: "))
            # 이중 리스트에 데이터 추가 (필수 조건 1)
            data_list.append([name, eff, mile])
            print(f"{name} 데이터가 추가되었습니다.")

        elif menu == 2:
            print("\n=== 현재 차량 등록 리스트 ===")
            # 이중 순회 출력 (필수 조건 2)
            for car in data_list:
                print(f"차량명: {car[0]} | 연비: {car[1]}km/L | 주행거리: {car[2]}km")

        elif menu == 3:
            # 파일 저장 기능 (필수 조건 3)
            with open("car_data.txt", "w", encoding="utf-8") as f:
                for car in data_list:
                    f.write(f"{car[0]},{car[1]},{car[2]}\n")
            print("car_data.txt 파일에 저장 완료! 프로그램을 종료합니다.")
            break
            
except Exception as e:
    print(f"알 수 없는 오류 발생: {e}")