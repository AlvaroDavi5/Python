import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import os

BASE_URL = "https://subslikescript.com"

def get_episode_links(series_url):
    """Extrai os links de todos os episódios da série."""
    response = requests.get(series_url)
    soup = BeautifulSoup(response.text, "html.parser")

    episodes = {}
    for link in soup.select("a[href^='/series/Kyle_XY-756509/season-']"):
        episode_url = BASE_URL + link["href"]
        title = link.text.strip()        

        # Extraindo temporada e episódio do link
        parts = episode_url.split("/season-")
        if len(parts) > 1 and parts[-1][0].isdigit():
            season = int(parts[-1][0])  # Pega o número da temporada
            episode = (episode_url.split("/episode-")[-1]).split("-")[0]

            if season not in episodes:
                episodes[season] = []
            episodes[season].append((episode+" - "+title, episode_url))

    return episodes

def get_episode_script(url):
    """Extrai o script de um episódio."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    script_div = soup.find("div", class_="full-script")
    return script_div.get_text("\n", strip=True) if script_div else "Script não encontrado."

def save_as_pdf(season, episodes):
    """Salva os episódios de uma temporada em um PDF."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for title, url in episodes:
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, title, ln=True, align="C")
        pdf.ln(10)

        script = get_episode_script(url).encode('latin-1', 'replace').decode('latin-1')
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, script)

    filename = f"Kyle_XY_Season_{season}.pdf"
    pdf.output(filename)
    print(f"PDF da Temporada {season} salvo como {filename}")

def main():
    series_url = "https://subslikescript.com/series/Kyle_XY-756509"
    episodes = get_episode_links(series_url)

    for season in sorted(episodes.keys()):
        print(f"Baixando episódios da Temporada {season}...")
        save_as_pdf(season, episodes[season])

if __name__ == "__main__":
    main()

