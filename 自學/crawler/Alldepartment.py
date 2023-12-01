import requests
from bs4 import BeautifulSoup as bs

def main(url, header):
    response = requests.get(url, headers= {"User-Agent": header})
    soup = bs(response.text, "html.parser")
    return soup.find("title").text

if __name__ == "__main__":
    for i in range(1000,170000):
        try:
            flat = i % 1000
            if flat <= 100:
                result = main(url = f"https://collego.edu.tw/Highschool/DepartmentIntro?dept_id={i:06d}",
                                header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
                print(i)
                print(result)
                if result != "Error":
                    if result != "認識學類":
                        with open("Alldepartment.txt","a",encoding="utf-8") as test:
                            test.write(str(i)+"\t"+result+"\n")
        except:
            with open("Alldepartment.txt","a",encoding="utf-8") as test:
                test.write(str(i)+"\t"+"Error"+"\n")