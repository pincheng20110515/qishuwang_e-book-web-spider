import requests
import sys
from urllib.parse import quote
import time
import random
from bs4 import BeautifulSoup
choice=0
coherence=False
exit=False
er_ror = 0
file_name = ''
wrong = 0  # 保存失败（超时）计数
count = 0  # 章节计数
booklink = ''  # 书籍目录链接
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}  # 请求头（避免被禁IP）
links = []  # 链接集合（相对路径）（类似章节的序列号）
name = []
name_box = []
full_links = []  # 链接集合（绝对路径）
bookname = 'https://www.biquuge.com/search.php?q='+quote(input('输入书名'))  # 自动搜索
s = requests.get(bookname, headers=headers)
soup = BeautifulSoup(s.text, 'html.parser')
name_box = soup.find_all('div', class_="row")  # 拿到搜索结果
book_name=['','','','','','','','','','']
book_status = ['', '', '', '', '', '', '', '', '', '']
book_href = ['', '', '', '', '', '', '', '', '', '']
for u in range(10):
    try:
        name = name_box[1].find_all('dl')
        book_name[u] = name[u].find_all('dd')[0].get_text()
        book_status[u] = name[u].find_all('dd')[2].get_text()
        book_href[u] = name[u].find('dt').find('a').get('href')
        print(book_name[u], book_status[u])
    except:
        pass
bookname = input('是哪个？按1，2，3，4，5,6,7,8,9,10选择')
if bookname == '1':
    file_name=book_name[0]
    booklink = 'https://www.biquuge.com' + book_href[0]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '2':
    file_name = book_name[1]
    booklink = 'https://www.biquuge.com' + book_href[1]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '3':
    file_name = book_name[2]
    booklink = 'https://www.biquuge.com' + book_href[2]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '4':
    file_name = book_name[3]
    booklink = 'https://www.biquuge.com' + book_href[3]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '5':
    file_name = book_name[4]
    booklink = 'https://www.biquuge.com' + book_href[4]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '6':
    file_name = book_name[5]
    booklink = 'https://www.biquuge.com' + book_href[5]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '7':
    file_name = book_name[6]
    booklink = 'https://www.biquuge.com' + book_href[6]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '8':
    file_name = book_name[7]
    booklink = 'https://www.biquuge.com' + book_href[7]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '9':
    file_name = book_name[8]
    booklink = 'https://www.biquuge.com' + book_href[8]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
elif bookname == '10':
    file_name = book_name[9]
    booklink = 'https://www.biquuge.com' + book_href[9]  # 书籍链接
    book_link = booklink.replace('https://www.biquuge.com', '')  # 书籍的链接
else:
    sys.exit("程序已终止")
for i in range(1):  # 无用的
    url = booklink  # 无用的赋值
    w = requests.get(url)  # 获取目录的信息
    soup = BeautifulSoup(w.text, 'html.parser')  # 对目录信息进行解析
    list_box = soup.find('div', class_="book_list2")  # 将有章节链接的整个class提取
    if list_box:
        links = list_box.find_all('a')  # 将章节链接（相对路径）初步提取（仍旧有干扰项）
        for n in range(1):
            href = links[n].get('href')  # 直接拿到章节链接（相对路径）
            if href is not None and '.html' in href and book_link in href and 'index' not in href:  # 排除干扰项
                href = href.replace('.html', '')  # 去除杂质
                href = href.replace(book_link, '')  # 去除杂质
                start_id = href  # 得到的第一个章节的链接（相对路径）
    links = []  # 清空列表（方便下一步赋值）
    for q in range(10000):  # 列举10000个可能章节
        current_id = int(start_id)+q  # 列举下一个可能章节
        links.append(str(current_id))  # 将新的可能章节加入列表
        print(links[q])
    for t in range(len(links)):
        full_url = 'https://www.biquuge.com' + \
            book_link+links[t]+''+'.html'  # 拼接出完整链接（第1页）
        full_url2 = 'https://www.biquuge.com'+book_link + \
            links[t]+'_2'+'.html'  # 拼接出完整链接（第2页）
        full_url3 = 'https://www.biquuge.com'+book_link + \
            links[t]+'_3'+'.html'  # 拼接出完整链接（第3页）
        full_links.append(full_url)
        full_links.append(full_url2)
        full_links.append(full_url3)  # 加入链接
    print(full_links)
print(f"开始搬运，请稍候...")
with open(f'/桌面/{file_name}.txt', 'a', encoding='utf-8') as f:  # 保存部分
    for url in full_links:  # 遍历列表拿到链接
        if exit==True:
            break
        while True:
            try:
                if er_ror >= 30:
                    exit=True
                    break
                res = requests.get(url, headers=headers, timeout=None)  # 拿到网页内容
                actual_url = res.url
                print(actual_url)
                if ".html" not in actual_url:  # 如果网页不存在(自动跳转回了目录)
                    if '_' not in actual_url:
                        if coherence == True:
                            er_ror=er_ror+1
                        coherence=True
                        print('该页面不存在')
                        break
                    else:
                        break  # 跳过（说明可能只是这一章比较短）
                res.encoding = 'utf-8'  # 编码转化
                soup = BeautifulSoup(res.text, 'html.parser')  # 解析网页内容
                content_box = soup.find('article', class_='font_max')  # 找到存文章的部分
                if content_box:
                    novel_text = content_box.get_text()  # 拿到具体文章内容
                    f.write(novel_text+'\n')  # 写入本地文件
                    count = count+1  # 章节计数加1
                    coherence=False
                    er_ror=0
                    print('第', count, '页保存成功','目前加载页面失败数：',er_ror)
                    time.sleep(random.uniform(0.1, 0.15))  # 等待（防止被封IP)
                    break
            except:
                time.sleep(random.uniform(1, 1.5))
                continue
print('--- 搞定！书已经存好了')  # 结果打印
