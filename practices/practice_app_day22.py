from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re
import os

template_folder = os.path.abspath('C:\\Users\\alber\\Documents\\DocumentsAlbert\\CV\\Linkedin projects\\avances\\practices\\templates')
app = Flask(__name__, template_folder=template_folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search']
        base_url = "https://digimon.fandom.com/wiki/List_of_Digimon"
        response = requests.get(base_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            digimon_info = None

      
            digimon_tables = soup.find_all("table", class_="sortable")

            for digimon_table in digimon_tables:
                for row in digimon_table.find_all("tr")[1:]:
                    columns = row.find_all("td")
                    name = columns[1].find("a").text.strip()

                    if search_query.lower() in name.lower():
                        image_url = columns[0].find("a")["href"]
                        original_name = columns[2].get_text(strip=True)
                        alternative_name = columns[3].get_text().strip()
                        digimon_page_url = 'https://digimon.fandom.com/wiki/' + name
                        digimon_info = scrape_digimon_page(digimon_page_url)

                        if digimon_info:
                            digimon_info.update({
                                "name": name,
                                "image_url": image_url,
                                "original_name": original_name,
                                "alternative_name": alternative_name,
                                "digimon_page_url": digimon_page_url,
                                "digimon_image_url": image_url
                            })
                        break  

                if digimon_info:
                    break  

            if digimon_info:
                return render_template('digimon_info.html', digimon_info=digimon_info)
            else:
                return render_template('digimon_not_found.html', search_query=search_query)
        else:
            error_message = f"Failed to retrieve data for Digimon: {search_query}"
            return render_template('error.html', error_message=error_message)

    return render_template('search_form.html')

def scrape_digimon_page(digimon_page_url):
    try:
        response = requests.get(digimon_page_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            script_tag = soup.find("script", string=re.compile(r'"wgCategories":\['))

            if script_tag:
                script_content = script_tag.string

                type_info = "Unknown"
                level_info = "Unknown"
                attribute_info = "Unknown"
                family_info = "Unknown"

                for substring in script_content.split(","):
                    if "type" in substring:
                        type_match = re.search(r'(?<=")(.*?)(?=")', substring)
                        if type_match:
                            type_info = type_match.group(0).strip()
                    elif "level" in substring:
                        level_match = re.search(r'(?<=")(.*?)(?=")', substring)
                        if level_match:
                            level_info = level_match.group(0).strip()
                    elif "attribute" in substring:
                        attribute_match = re.findall(r'(?<=")(.*?)(?=")', substring)
                        if attribute_info != "Unknown":
                            attribute_info = attribute_info + ", ".join(attribute_match).strip()
                        else:
                            attribute_info = ", ".join(attribute_match).strip()
                    elif "family" in substring:
                        break

                description = "No description available"
                description_div = soup.find("meta", property="og:description")
                if description_div:
                    description = description_div["content"]

                return {
                    "type": type_info,
                    "level": level_info,
                    "attribute": attribute_info,
                    "family": family_info,
                    "description": description
                }

    except Exception as e:
        error_message = f"Error scraping Digimon page: {e}"
        print(error_message)
    return None

if __name__ == '__main__':
    app.run(debug=True)
