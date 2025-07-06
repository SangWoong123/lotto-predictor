import pandas as pd
from collections import Counter

# 데이터 로드
df = pd.read_csv("lotto_results.csv")

# 번호 열만 가져오기
all_numbers = df[['번호1', '번호2', '번호3', '번호4', '번호5', '번호6']].values.flatten()

# 등장 횟수 세기
counter = Counter(all_numbers)

# 가장 많이 나온 번호 TOP 6 출력
top_6 = counter.most_common(6)
print("🎯 자주 나온 번호 TOP 6:")
for num, cnt in top_6:
    print(f"번호 {num}: {cnt}회")
