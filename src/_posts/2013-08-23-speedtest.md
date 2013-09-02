---
layout: post.html
title: Server Benchmark 工具
tags: [OpenSource, Benchmark]
author: Lucemia
type: project
---

# Python寫的網路測速程式
為了能夠比較不同hosting的對特定區域的網路速度而寫的簡單程式,透過speedtest-cli的服務+能夠指定國家測試, 測試結果以 csv 的方式記錄下來. 並且提供將結果匯入到 sqlite 裡面方便計算的工具

[GIT REPO](https://github.com/lucemia/GCEvsAWS)

## Requirement
需要先安裝 [speedtest-cli](https://github.com/sivel/speedtest-cli) 與 [clime](https://github.com/moskytw/clime‎)

~~~ { shell }
pip install speedtest-cli
~~~

~~~ { shell }
pip install clime
~~~

## Install

~~~ { shell }
git clone https://github.com/lucemia/GCEvsAWS.git
~~~

## Usage

### 執行國別測試
~~~ { shell }
python test.py speed-test --country=[測試國家] [server_name]
~~~

範例:

~~~ { shell }
python test.py speed-test --country=Taiwan localhost
~~~

結果會存在 `[server_name].csv` 中

~~~ { csv }
mac,2013-08-21 21:52:30.608635,True,2133,Taiwan Fixed Network,Taipei,Taiwan,9592.46,Telus Communications,154.5.56.215,112.772,9.23,0.64
mac,2013-08-21 21:52:30.608635,True,2181,kbro CO.LTD,Taipei,Taiwan,9592.46,Telus Communications,154.5.56.215,68.347,8.80,0.65
mac,2013-08-21 21:52:30.608635,True,2182,kbro CO.LTD,Hsinchu,Taiwan,9644.62,Telus Communications,154.5.56.215,111.341,7.39,0.59
~~~


### 對特定server測試
~~~ { shell }
python test.py test-server [server_id] [log_path]
~~~

範例:

~~~ { shell }
python test.py test-server 999 999.log
~~~

回傳結果:

~~~ { python }
{
 'distance': '8468.27',
 'host_name': 'InternetONE',
 'download': '2.49',
 'ip': '216.232.96.61',
 'test_from': 'Telus Communications',
 'ping': '104.666',
 'upload': '0.62',
 'location': 'Varese'
}
~~~

### 將測試結果匯入 sqlite

~~~ { shell }
python test.py import-csv [csv_path]
~~~

範例:

~~~ { shell }
python test.py import-csv localhost.csv
~~~

結果會匯入到 `speeddata.db` 中


### 計算結果

~~~ { sql }
select host, avg(server_upload), avg(server_download)
    from speeddata
    group by host
~~~



