import re
import requests
import numpy as np
import pandas as pd
import plotly.offline as plyo
import cufflinks
from bs4 import BeautifulSoup


def get_response(end_date):
    url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?'
    SERVICE_KEY = 'iq7mlnFcFNOTr5dYWWXp8KNHKM2wM3kbT4c0y+nQele+YvLip6tuF1arCglqWSHsSxWnKYxpHvGUp2h9FGiLyQ=='

    params = {
        'ServiceKey': SERVICE_KEY,
        'startCreateDt': 20211201,
        'endCreateDt': end_date
    }

    return requests.get(url, params)


if __name__ == "__main__":
    res = get_response(20220101)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'xml.parser')
        decide_cnt_list = []
        for decidecnt in soup.select('decideCnt'):
            cnt = re.findall('\d+', str(decidecnt))
            decide_cnt_list.append(*cnt)

        index = pd.date_range('2021-12-01', periods=len(decide_cnt_list))
        df = pd.DataFrame(decide_cnt_list, columns=['decideCnt'], index=index)

        plyo.iplot(df.iplot(asFigure=True))

        # result = xmltodict.parse(res.text)
        # dict = json.loads(json.dumps(result))
        # print(dict)