# encoding=utf-8
"""
This module returns a .txt file of all the russian
nouns via iteration of wiktionary category of 'Русские существительные'
"""

from mwclient import Site

#site = Site('test.wikipedia.org')
# wiktionary asks you to spesify your tool like so:
ua = 'student search engine run by User:Chertousova Eugenia, StPSU'
site = Site('ru.wiktionary.org',  clients_useragent=ua)

root = [site.categories['Русские существительные']]  #root category to begin with
namespace = 14  #namespace of a category
#case_cat is used to store categories that shouldn't be iterated
#and categories that have already been iterated
case_cat = set(['Существительные в винительном падеже',
                 'Существительные в дательном падеже',
                 'Существительные в звательном падеже',
                 'Существительные в предложном падеже',
                 'Существительные в разделительном падеже',
                 'Существительные в родительном падеже',
                 'Существительные в творительном падеже'])


with open('nouns.txt', 'w', encoding='utf-8') as file:

    while root:  #works while root list isn't empty

        category = root.pop(0)

        for page in category:

            if page.name not in case_cat:
                if page.namespace == namespace:
                    root.insert(0, page)
                    case_cat.add(category.name)

                else:
                    file.write(page.name + '\n')
                    case_cat.add(page.name)

            else:
                continue