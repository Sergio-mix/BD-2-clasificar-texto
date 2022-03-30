import pandas as pd


def readExcel(url):
    try:
        list = []
        df = pd.read_excel(url, sheet_name='Sheet1')
        for i in range(len(df)):
            text = str(df['text'].values[i]).lower()
            likes = df['likes'].values[i]
            comments = df['comments'].values[i]
            shares = df['shares'].values[i]
            list.append(
                {
                    'text': text,
                    'likes': likes,
                    'comments': comments,
                    'shares': shares,
                    'product': '',
                    'value': ''
                }
            )
        return list
    except Exception as e:
        print(e)
