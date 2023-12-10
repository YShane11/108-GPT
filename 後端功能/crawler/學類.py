import requests
from bs4 import BeautifulSoup as bs
import csv

def main(url, header):

    response = requests.get(url, headers= {"User-Agent": header})
    soup = bs(response.text, "html.parser") 


    margin_1 = soup.find_all(style="margin: 20px")


    name = soup.find(style='font-size:22pt').text
    what = soup.find(style="margin-left:20px").text
    thisone = margin_1[2].find("p",style="margin-left:20px").text
    notknow = margin_1[3].find("p",style="margin-left:20px")
    if not notknow:
        notknow = "資料準備中"
    else:
        notknow = notknow.text


    margin_2 = soup.find(style="margin: 20px;")
    if not margin_2:
        courses = "資料準備中"
    else:
        courses = margin_2.find("p",style="margin-left:20px").text



    margin_3 = soup.find("div",style="padding: 10px; margin: 20px;")
    if not margin_3:
        cores = "資料準備中"
    else:
        cores = {}
        row_1 = margin_3.find("div",class_="row")
        cores_1 = [i.text.strip(' Complete') for i in row_1.find_all('span',class_="sr-only")]
        cores_2 = [i.text for i in row_1.find_all('span',class_="progress-type")]
        for i in range(len(cores_1)):
            cores[cores_2[i]] = cores_1[i]

    tab3 = soup.find(id='tab3default')
    if not tab3:
        abilities = "資料準備中"
        traits = "資料準備中"
    else:
        row_2 = tab3.find_all("div",class_="row")
        abilities = {}
        abilities_1 = [i.text.strip(' Complete') for i in row_2[0].find_all('span',class_="sr-only")]
        abilities_2 = [i.text.split("：")[0] for i in row_2[0].find_all('span',class_="progress-type")]
        for i in range(len(abilities_1)):
            abilities[abilities_2[i]] = abilities_1[i]

        traits = {}
        traits_1 = [i.text.strip(' Complete') for i in row_2[1].find_all('span',class_="sr-only")]
        traits_2 = [i.text.split("：")[0] for i in row_2[1].find_all('span',class_="progress-type")]
        for i in range(len(traits_1)):
            traits[traits_2[i]] = traits_1[i]

    result = {'學類':name,'這個學類學什麼？':what,'就要你這款':thisone,'你所不知道的大學生活':notknow,'必修或核心課程？':courses,'核心素養':cores,'多元能力':abilities,'性格特質':traits}
    return result


if __name__ == "__main__":
    response = requests.get('https://collego.edu.tw/Highschool/MajorList', headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"})
    soup = bs(response.text, "html.parser") 
    a = soup.find_all("a")
    all_href = []
    for i in range(23,204):
        all_href.append('https://collego.edu.tw/'+a[i]['href'])
    
    a = 0
    with open('學類.csv', 'a', newline='',encoding='utf-8') as csvfile:   
        csv_writer = csv.DictWriter(csvfile, fieldnames = ['學類','這個學類學什麼？','就要你這款','你所不知道的大學生活','必修或核心課程？', '核心素養', '多元能力', '性格特質'])
        csv_writer.writeheader()
        for i in all_href:
            csv_writer.writerow(main(url = i,
                                header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"))
            print(a)
            a += 1

