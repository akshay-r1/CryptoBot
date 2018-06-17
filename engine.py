intent_response_dict = {
    "intro": ["This is a cryptocurrency bot. Feel free to query anything related to cryptocurrency values"],
    "greet":["Hey","Hello","Hi","Howdy", "How do you do?"],
    "goodbye":["Bye","It was nice talking to you","See you"],
    "affirm":["Cool","I know you would like it"]
}


def AttributesKnowledgeBase(data):
    try:
        response= data.columns.values.tolist()
        return str(response)[1:-1]
    except Exception as e:
        print(e)
        response_text="Oops seems like something is wrong with my database. Try again in some time"
        return response_text

def GetHighestValueByName(data,crypto):
    try:
        data = data.groupby('name')['high'].max()
        crypto=str(crypto).title()
        return str(data[crypto])
    except Exception as e:
        print(e)
        response_text = "Oops seems like something wrong with database. Error: " + str(e)
        return response_text
def GetStatusByName(data,entities):
    try:
        final = data[-1]
        print (final)
        response_text = "The atrributes available to me include "
        for x in final:
            print str(x)
            response_text += str(x) + " , "
        response_text = str(response_text[0:-3])
        print (response_text)
        return response_text
    except Exception as e:
        print(e)
        response_text = "Oops seems like something is wrong with my database. Try again in some time"
        return response_text

def CryptoList(data):
    try:
        response_text = "The list of cryptos currently in my database include "
        final_data = data.name.unique()
        final_data = str(final_data)
        response_text = response_text + final_data[1:-1]
        return response_text
    except Exception as e:
        print(e)
        response_text = "Oops seems like something is wrong with my database. Try again in some time"
        return response_text


        
'''if intent==CryptoList:
            CryptoList()
        if intent==GetHighestValueByName:
            GetHighestValueByName()
        if intent==GetStatusByName:
            GetStatusByName()
        '''
''' def CryptoList():
        
    def GetHighestValueByName():

    def GetStatusByName():

'''


