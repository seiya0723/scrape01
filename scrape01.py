#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4,requests,time,random


TIMEOUT     = 10
URL         = "https://noauto-nolife.com/"
DEFAULT_SLEEP   = 3


#try except文
try:

    #URLに対してGETメソッドのリクエストを送信する、10秒待っても応答がない場合はタイムアウトする。

    result  = requests.get(URL, timeout=TIMEOUT)

    #ステータスコード200(正常)以外の場合は例外として扱う。
    result.raise_for_status()
    time.sleep(DEFAULT_SLEEP)


except Exception as e:

    print("ERROR_DOWNLOAD:{}".format(e))

else:

    #BeautifulSoupのオブジェクトを生成する
    #引数は2つ、HTMLのデータ(result.content)とパーサー(構文解析器)の種類
    #パーサーは標準のhtml.parser、未指定でも問題はないが警告が出る
    soup    = bs4.BeautifulSoup(result.content, 'html.parser')

    
    #pタグを全て抜き取る。.find_all()でも良いが、.select()のほうが短く書ける
    paragraph   = soup.select("p")

    print(paragraph)

    #pタグの文字列を全て表示、タグ内の文字列は.textで抜き取れる(.get_text()を使えば、空白除去等の引数指定ができる)
    for p in paragraph:
        print(p.text)


    #aタグを抜き取る
    links   = soup.select("a")

    #aタグのhref属性を抜き取って表示させる
    for link in links:
        print(link.get("href"))

