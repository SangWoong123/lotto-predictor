import requests
import csv

# 전체 회차 수 설정 (예: 1 ~ 1120회차까지)
START = 1121
END = 1175  # 최신 회차까지는 수동 입력

def get_lotto_numbers(draw_no):
    url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    response = requests.get(url)
    data = response.json()
    if data['returnValue'] == 'success':
        numbers = [data[f'drwtNo{i}'] for i in range(1, 7)]
        bonus = data['bnusNo']
        return [draw_no] + numbers + [bonus]
    else:
        return None

# CSV 파일로 저장
with open('lotto_results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['회차', '번호1', '번호2', '번호3', '번호4', '번호5', '번호6', '보너스'])

    for i in range(START, END + 1):
        result = get_lotto_numbers(i)
        if result:
            print(f"{i}회 데이터를 저장 중...")
            writer.writerow(result)
