import pandas as pd
import requests
import urllib.parse
from libgensearch.downloadbar import downloadbar
from libgensearch.textsimilarity import compare


def search(title, similaritythreshold, language, extensions):
    maxsimilarity = -2
    selectedbook = False
   
    ids = pd.read_html(
        f'http://libgen.li/search.php?req={urllib.parse.quote(title)}',
        match="Extension",
        header=0)[0]['ID'].astype(str)
    books = requests.get(
        f'http://libgen.li/json.php?lg_topic=libgen&ids={",".join(ids)}'
    ).json()

    if "error" not in books:

        for book in books:
            if (book['extension'] in extensions and
                language.lower() == book['language'].lower()):
                
                    similarity = compare(book['title'], title)

                    if similarity > maxsimilarity:
                        selectedbook = book
                        maxsimilarity = similarity
        if selectedbook:
            if similaritythreshold < maxsimilarity:
                downloadbar(
                    f'http://libgen.gs/get.php?md5={selectedbook["md5"]}&mirr=1',
                    selectedbook['title']
                )
            else:
                response = input(f'The maximum similarity was {maxsimilarity} and the book is called \"{selectedbook["title"]}\". Download still? Y/N ').lower()
                if response == 'y':
                    downloadbar(
                        f'http://libgen.gs/get.php?md5={selectedbook["md5"]}&mirr=1', 
                        selectedbook['title']
                    )


        else:
            print("No books found with the requested language and extension")
    else:
        print("No books found for that term")
