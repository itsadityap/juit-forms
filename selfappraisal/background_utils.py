
from scholarly import scholarly
from selfappraisal.models import Publication

YEARS_VALID = ['2022', '2023']


def add_research_paper(author_id, main_form):
    author = scholarly.search_author_id(author_id)

    author = scholarly.fill(author)

    for publication in author['publications']:
        try:
            # Get the details of the publication
            if publication.get('bib', {}).get('pub_year') not in YEARS_VALID:
                continue


            publication = scholarly.fill(publication)

            publication_bib = publication.get('bib')

            Publication.objects.update_or_create(
                author_names=publication_bib.get('author'),
                title_reference=publication_bib.get('title'),
                form=main_form,

                defaults={
                    "publication_choice": 1,
                    "publication_type": publication.get('container_type'),
                    "author_names": publication_bib.get('author'),
                    "title_reference": publication_bib.get('title'),
                    "form": main_form,
                }
            )
        except Exception as e:
            print(e)

from bs4 import BeautifulSoup
import requests

def add_juit_pub(author_id, main_form):
    URL = f"https://www.juit.ac.in/faculty.php?id={author_id}&dep=cse&year1={2023}"
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        book_div = soup.find('div', class_='small-heading', text='Book(s) :')
        book_list = book_div.find_next('ul', class_='bullet')


        for li in book_list.find_all('li'):
            try:
                all_text = li.get_text(strip=True)
                author_names = li.get_text(strip=True).split(f'({2023}).')[0]
                Publication.objects.update_or_create(
                    author_names=author_names,
                    title_reference=all_text,
                    form=main_form,

                    defaults={
                        "publication_choice": 2,
                        "publication_type": "Book",
                        "author_names": author_names,
                        "title_reference": all_text,
                        "form": main_form,
                    }
                )
            except:
                continue

    except:
        print("Book Error")

    try:
        # Extract journal information
        journal_div = soup.find('div', class_='small-heading', text='Journal(s) :')
        journal_list = journal_div.find_next('ul', class_='bullet')

        for li in journal_list.find_all('li'):
            try:    
                all_text = li.get_text(strip=True)
                author_names = li.get_text(strip=True).split(f'({2023}).')[0]
                Publication.objects.update_or_create(
                    author_names=author_names,
                    title_reference=all_text,
                    form=main_form,

                    defaults={
                        "publication_choice": 1,
                        "publication_type": "Journal",
                        "author_names": author_names,
                        "title_reference": all_text,
                        "form": main_form,
                    }
                )
            except:
                continue
    except:
        print("Journal Error")


    try:    
        # Extract journal information
        conference = soup.find('div', class_='small-heading', text='Conference(s) :')
        conference_list = conference.find_next('ul', class_='bullet')

        for li in conference_list.find_all('li'):
            try:    
                all_text = li.get_text(strip=True)
                author_names = li.get_text(strip=True).split(f'({2023}).')[0]
                Publication.objects.update_or_create(
                    author_names=author_names,
                    title_reference=all_text,
                    form=main_form,

                    defaults={
                        "publication_choice": 1,
                        "publication_type": "Conference",
                        "author_names": author_names,
                        "title_reference": all_text,
                        "form": main_form,
                    }
                )
            except:
                continue
    except:
        print("Conference Error")

    