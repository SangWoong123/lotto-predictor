import requests
import csv

START = 1121
END = 1175  # 최신 회차

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

# 기존 파일에 이어서 저장 (append 모드)
with open('lotto_results.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(START, END + 1):
        result = get_lotto_numbers(i)
        if result:
            print(f"{i}회 데이터를 추가 저장 중...")
            writer.writerow(result)
