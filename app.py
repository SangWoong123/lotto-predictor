from flask import Flask, render_template, jsonify
import pandas as pd
from collections import Counter
import random
import os
import csv
from datetime import datetime

app = Flask(__name__)

# 로또 번호 생성 함수 (보너스 제외)
def generate_prediction():
    df = pd.read_csv(r"C:\Users\swbar\Desktop\py\lotto101\lotto_results.csv")
    all_numbers = [int(n) for n in df[['번호1', '번호2', '번호3', '번호4', '번호5', '번호6']].values.flatten()]
    counter = Counter(all_numbers)
    top_20 = [num for num, cnt in counter.most_common(20)]
    main = sorted(random.sample(top_20, 6))
    return main

# 예측 번호 기록
def log_prediction(numbers):
    path = os.path.join(os.path.dirname(__file__), 'prediction_log.csv')
    with open(path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        row = [now, *numbers]
        writer.writerow(row)

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 예측 요청
@app.route('/predict')
def predict():
    main = generate_prediction()
    log_prediction(main)
    return jsonify({'main': main})

# 최근 예측 결과 반환
@app.route('/recent')
def recent():
    path = os.path.join(os.path.dirname(__file__), 'prediction_log.csv')
    if not os.path.exists(path):
        return jsonify([])

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()[-5:]
        result = []
        for line in lines:
            parts = line.strip().split(',')
            result.append({
                'time': parts[0],
                'numbers': parts[1:7]
            })
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)