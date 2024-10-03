from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options


url = 'https://l-a-b-a.com/uk/lecture'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
}

""" Links """


""" pag_links_file = open('pag_links.txt', 'w', encoding='utf')
links = open('course_links.txt', 'w', encoding='utf-8')
req = requests.get(url, headers=headers)
src = req.text
soup = BeautifulSoup(src, 'lxml')

count = 1
while True:
    doc = soup.find(class_='pagination-btn pagination-btn__next')
    if doc:

        url = 'https://l-a-b-a.com/uk/lecture/' + str(count)
        local_req = requests.get(url, headers=headers)
        local_soup = BeautifulSoup(local_req.text, 'lxml')
        pag_links_file.write(url + '\n')
        text_for_link = local_soup.find(class_='courses__list').find_all('a')
        for i in text_for_link:
            ch = i.get('href')
            links.write(f'https://l-a-b-a.com{ch}\n')
        doc = local_soup.find(class_='pagination-btn pagination-btn__next')
        if doc is None:
            break
        else:
            count += 1
    else:
        break
pag_links_file.close
links.close() """

file = open('course_links.txt', 'r', encoding='utf-8')
info = open('laba_data.txt', 'w', encoding='utf-8')
for f in file:
    f = f[0:-1]
    req = requests.get(f)
    soup = BeautifulSoup(req.text, 'lxml')

    """ Title """

    title = soup.find('title')
    
    tmp = title.text.strip()
    tmp = tmp.replace("| Laba (Лаба)", " ")
    tmp = tmp.replace("| LABA", " ")
    tmp = tmp.replace("| Laba", " ")
    tmp = tmp.replace("| LABA (ЛАБА)", " ")
    tmp = tmp.replace("(ЛАБА)", " ")
    info.write(f'Назва : {tmp} \n')
    
    """ Date """

    start_date = soup.find(class_='promo__date wow fadeInUp')
    if  start_date != None and start_date.text != '':
        st = start_date.text.replace('\n', ' ')
        info.write('Дата : ' + st.strip() + '\n')
    else:
        start_date = soup.find(class_='info__data-interval caps-sm')
        if start_date == None or start_date.text == '':
            info.write("Відкрита попередня реєстрація\n")
        else:
            st = start_date.text.replace('\n', '')
            info.write('Дата : ' + st.strip() + '\n')

    """ Description """

    disc = soup.find(class_='promo__subtitle wow fadeInLeft')
    
    if disc != None :
        disc1 = disc.next_element
        disc_res = disc.text + disc1.text
        info.write(f'Опис : {disc_res.strip()}\n')

    else:
        disc = soup.find(class_='info__desc reg-lg')
        if disc == None:
            disc = soup.find(class_='hero__info')
            if disc == None:
                disc = soup.find(class_='desk__from')
                if disc == None:
                    disc = soup.find(class_='l_intro-greetings')
                    info.write(f'Опис : {disc.text.strip()}\n')
                else:
                    info.write(f'Опис : {disc.text.strip()}\n')
            else:
                info.write(f'Опис : {disc.text.strip()}\n')

        else:
            info.write(f'Опис : {disc.text.strip()}\n')

    info.write(f'Посилання : {f} \n')
    info.write("================================================ \n")

info.close()
