
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
