import json

def translate(key, lang):
    with open('translations/' + lang + '.txt') as file:
        translations = file.read()

    transDict = json.loads(translations)

    try:
        return transDict[key]
    except KeyError:
        print('There\'s no key defined as: ' + str(key), flush=True)
    except:
        print('Some error happened while translating', flush=True)
