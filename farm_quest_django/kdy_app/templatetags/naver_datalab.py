import urllib.request
# import datetime
import json
import glob
import sys
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
# pip install Cython 설치 이후 fbprophet 인스톨 진행
# import Cython
# from fbprophet import Prophet
import warnings

from flask import Flask, render_template
from io import BytesIO
import base64
# app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(debug=True)


# warnings.filterwarnings(action='ignore')
# plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.grid'] = False
# pd.set_option('display.max_columns', 250)
# pd.set_option('display.max_rows', 250)
# pd.set_option('display.width', 100)
# pd.options.display.float_format = '{:.2f}'.format



class NaverDataLabOpenAPI():

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.keywordGroups = []
        self.url = "https://openapi.naver.com/v1/datalab/search"


    def add_keyword_groups(self, group_dict):
            keyword_gorup = {
                'groupName': group_dict['groupName'],
                'keywords': group_dict['keywords']
            }
            
            self.keywordGroups.append(keyword_gorup)
            print(f">>> Num of keywordGroups: {len(self.keywordGroups)}")


    def get_data(self, startDate, endDate, timeUnit, device, ages, gender):
            body = json.dumps({
                "startDate": startDate,
                "endDate": endDate,
                "timeUnit": timeUnit,
                "keywordGroups": self.keywordGroups,
                "device": device,
                "ages": ages,
                "gender": gender
            }, ensure_ascii=False)

            request = urllib.request.Request(self.url)
            request.add_header("X-Naver-Client-Id",self.client_id)
            request.add_header("X-Naver-Client-Secret",self.client_secret)
            request.add_header("Content-Type","application/json")
            response = urllib.request.urlopen(request, data=body.encode("utf-8"))
            rescode = response.getcode()

            if(rescode==200):
                result = json.loads(response.read())                
                df = pd.DataFrame(result['results'][0]['data'])[['period']]
                for i in range(len(self.keywordGroups)):
                    tmp = pd.DataFrame(result['results'][i]['data'])
                    tmp = tmp.rename(columns={'ratio': result['results'][i]['title']})
                    df = pd.merge(df, tmp, how='left', on=['period'])
                self.df = df.rename(columns={'period': '날짜'})
                self.df['날짜'] = pd.to_datetime(self.df['날짜'])
                
            else:
                print("Error Code:" + rescode)
                
            return self.df


    def month_trend(self):
            colList = self.df.columns[1:]
            n_col = len(colList)

            fig = plt.figure(figsize=(12,6))
            plt.title('월 별 검색어 트렌드', size=20, weight='bold')
            for i in range(n_col):
                sns.lineplot(x=self.df['날짜'], y=self.df[colList[i]], label=colList[i])
            plt.legend(loc='upper right')
            
            # 그래프를 BytesIO 객체로 저장
            img_data = BytesIO()
            fig.savefig(img_data, format="png")
            img_data.seek(0)

            # BytesIO 객체를 base64로 변환
            img_base64 = base64.b64encode(img_data.read()).decode()

            return img_base64



















































    # def month_trend_show(client_id, client_secret):

    #     api = NaverDataLabOpenAPI(client_id, client_secret)

    #     # 검색어 그룹 추가
    #     group_dict = {
    #         'groupName': '지역 숙소 테마 통합 검색 트렌드',  # 그룹의 이름
    #         'keywords': ['서울', '리조트', '맛집']  # 검색어 리스트
    #     }
    #     api.add_keyword_groups(group_dict)

    #     # 날짜 범위와 기타 필수 정보 설정
    #     startDate = "2023-01-01"
    #     endDate = "2023-10-26"
    #     timeUnit = "month"  # "date", "week", "month" 중 하나
    #     device = "pc"  # "pc" 또는 "m" (모바일)
    #     ages = ["1"]  # 연령대 리스트, 예: ["1", "2", "3"]
    #     gender = "m"  # "m" (남성), "f" (여성)

    #     # 데이터 가져오기
    #     api.get_data(startDate, endDate, timeUnit, device, ages, gender)

    #     # 월 별 검색어 트렌드 그래프 출력
    #     graph_url = api.month_trend()
    #     # fig_show = plt.show()

    #     # return graph_url


# client_id = "XZc22eND2hDwZOrJ3uAv"
# client_secret = "Ys7etJVJZ5"

# NaverDataLabOpenAPI.month_trend_show(client_id, client_secret)

