import wikipedia

def get_wiki_article(article):
    wikipedia.set_lang("ru")
    try:
        return f"{wikipedia.summary(article)}"
    except:
        return "Не удалось найти информацию"

if __name__=="__main__":        
    print(get_wiki_article("python"))