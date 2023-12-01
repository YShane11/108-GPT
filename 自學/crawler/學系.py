import requests
from bs4 import BeautifulSoup as bs
import csv


def main(url, header):
    response = requests.get(url, headers= {"User-Agent": header})
    soup = bs(response.text, "html.parser")

    class_row=soup.find_all('div', class_='row')
    list_style = soup.find_all("ul", style="list-style-type:none")
    class_row_col = soup.find_all("div",class_="row col-xs-12 col-sm-6")
    muted = soup.find_all("p",class_="text-muted")

    col = muted[0].find_all("a")[-1].text.strip(" ")
    school = soup.find("b",style="padding-left:15px;font-size:5vh").text
    department = soup.find("b",style="padding-left:15px;font-size:5vh;").text
    website = soup.find("a",target="_blank")['href']
    features = class_row[0].find('p',class_='card-text')

    if features:
        features = features.text
    else:
        features = "資料準備中"  

    meanings = class_row[2].find('p',class_='card-text')

    if meanings:
        meanings = meanings.text
    else:
        meanings = "資料準備中"  

    method = class_row[4].find('p',class_='card-text')

    if method:
        method = method.text
    else:
        method = "資料準備中"   

    if list_style:
        works = [item.text for item in list_style[0].find_all("h4")]
    else:
        works = "資料準備中"

    abilitys = [item.text.split("：")[0] for item in class_row_col[0].find_all("span",class_="progress-type")]
    if not abilitys:
        abilitys = "資料準備中"
    Traits = [item.text.split("：")[0] for item in class_row_col[1].find_all("span",class_="progress-type")]
    if not Traits:
        Traits = "資料準備中"

    result = {'學校':school,'系所':department,"學系特色":features,"學科意涵":meanings,"高中階段可以準備的學習方法或方向":method,"適合從事工作":works,"多元能力":abilitys,"性格特質":Traits,"網址":website,"學類":col}
 
    return result

if __name__ == "__main__":
    with open('Alldepartment.txt', 'r', encoding="utf-8") as file:
        file = file.readlines()

    with open('學系.csv', 'a', newline='',encoding='utf-8') as csvfile:   
        csv_writer = csv.DictWriter(csvfile, fieldnames = ['學校','系所','學系特色','學科意涵','高中階段可以準備的學習方法或方向','適合從事工作','多元能力','性格特質','網址',"學類"])
        # 寫入標題（字典的鍵）
        # csv_writer.writeheader()
        for i in range(0,len(file)):
            file[i] = int(file[i].split("\t")[0])

        # 寫入數據（字典的值）
            csv_writer.writerow(main(url = f"https://collego.edu.tw/Highschool/DepartmentIntro?dept_id={file[i]:06d}",
                            header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"))
            print(i)
        

