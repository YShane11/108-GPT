import requests
from bs4 import BeautifulSoup as bs
import csv

def main(url, header):
    response = requests.get(url, headers= {"User-Agent": header})
    soup = bs(response.text, "html.parser") 

    dd = soup.find_all("dd",class_="col-xs-12 col-md-10")

    name = soup.find("b", style="font-size:22pt").text

    introduce = soup.find("p", style="font-size:1.3em")
    if not introduce:
        introduce = "資料準備中"
    else:
        introduce = introduce.text

    learning_content = soup.find("article", style="font-size:1.3em")
    if not learning_content:
        learning_content = "資料準備中"
    else:
        learning_content = learning_content.text


    if len(dd) < 3:
        mains = "資料準備中"
        abilities = "資料準備中"
        traits = "資料準備中"
    else:
        mains = [i.text.strip("\xa0") for i in dd[2].find_all("a")]

        abilities = {}
        for i in dd[8].find_all("nobr"):
            abilities[i.u.text] = i.a['title']

        traits = {}
        for i in dd[9].find_all("nobr"):
            traits[i.u.text] = i.a['title']

    
    result = {'學群':name,'簡要介紹':introduce,'學習內容':learning_content,'主要學類':mains,'多元能力':abilities,'性格特質':traits}
    return result


if __name__ == "__main__":
    with open('學群.csv', 'a', newline='', encoding="utf-8") as csvfile:   
        csv_writer = csv.DictWriter(csvfile, fieldnames = ['學群','簡要介紹','學習內容','主要學類','多元能力','性格特質'])
        csv_writer.writeheader()

        for i in range(1,20):
            csv_writer.writerow(main(url = f"https://collego.edu.tw/Highschool/CollegeIntro?current_college_id={i}",
                            header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"))
            
            print(i)


