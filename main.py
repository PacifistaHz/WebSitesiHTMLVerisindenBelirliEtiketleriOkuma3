from bs4 import BeautifulSoup
import requests

url = "https://tureng.com/tr/turkce-ingilizce/su"

try:
    response = requests.get(url)
    response.raise_for_status()  # HTTP isteği sırasında hata kontrolü
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"HTTP isteğinde bir hata oluştu: {e}")
    html_content = ""

if html_content:
    soup = BeautifulSoup(html_content, "html.parser")

    # Tüm tablo elemanlarını yazdır
    all_tables = soup.find_all("table")
    print(all_tables)

    # Belirli ID'ye sahip tabloyu bul ve yazdır
    english_results_table = soup.find_all("table", {"id": "englishResultsTable"})
    print(english_results_table)

    # Belirli sınıf ve dil özelliklerine sahip <td> elemanlarını yazdır
    english_terms = soup.find_all("td", {"class": "en tm", "lang": "en"})
    for term in english_terms:
        print(term)

    # İngilizce sonuç tablosunu bul
    level_1 = soup.find_all("table", {"id": "englishResultsTable"})
    level_2 = BeautifulSoup(str(level_1), "html.parser")
    level_2_terms = level_2.find_all("td", {"class": "en tm", "lang": "en"})
    level_3 = BeautifulSoup(str(level_2_terms), "html.parser")
    level_3_links = level_3.find_all("a")
    print(level_3_links[3] if level_3_links else "Link bulunamadı")
