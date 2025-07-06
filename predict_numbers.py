import pandas as pd
from collections import Counter
import random

# 1. 데이터 불러오기
df = pd.read_csv("lotto_results.csv")
all_numbers = [int(n) for n in df[['번호1', '번호2', '번호3', '번호4', '번호5', '번호6']].values.flatten()]

# 2. 등장 횟수 계산
counter = Counter(all_numbers)
top_20 = [num for num, cnt in counter.most_common(20)]

# 3. 상위 20개 중 무작위로 6개 선택
main_numbers = sorted(random.sample(top_20, 6))

# 4. 보너스 번호 (겹치지 않도록)
remaining = [n for n in top_20 if n not in main_numbers]
bonus = random.choice(remaining)

# 5. 결과 출력
print("🎯 예측 추천 번호:")
print(f"메인 번호: {main_numbers}")
print(f"보너스 번호: {bonus}")
