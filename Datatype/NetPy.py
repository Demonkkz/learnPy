import requests
from bs4 import BeautifulSoup
import time
import MySQLdb


def get_page(url):
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, features="html.parser")
    return soup


def get_links(link_url):
    soup = get_page(link_url)
    links_div = soup.find_all('div', class_="content__list--item")
    links = ["http://hz.lianjia.com"+div.a.get('href') for div in links_div]
    return links
# 获取租房页面下链接


def get_house_info(house_url):
    soup = get_page(house_url)
    price = soup.find('p', class_="content__aside--title").text[:8]
    house_normal = soup.find('p', class_='content__article__table').text
    area = house_normal[11:14].strip()
    typ = house_normal[4:10]
    way = house_normal[1:3]
    orient = house_normal[14:17].strip()
    info = {
        '价格': price,
        '面积': area,
        '户型': typ,
        '出租方式': way,
        '朝向': orient
    }
    return info


DATABASE = {
    'host': 'localhost',
    'database': 'Lianjia',
    'user': 'root',
    'password': '123456',
    'charset': 'utf8mb4'
}


def get_db(setting):
    return MySQLdb.connect(**setting)


def insert(db, house):
    values = "'{}',"*4 + "'{}'"
    sql_values = values.format(house['价格'], house['面积'], house['户型'], house['出租方式'], house['朝向'])
    sql = """
    insert into house(price,area,typ,way,orient)
    values({});
    """.format(sql_values)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()


url = "https://hz.lianjia.com/zufang"
links = get_links(url)
db = get_db(DATABASE)

for link in links:
    house = get_house_info(link)
    insert(db, house)
    print(house)
    time.sleep(2)

