#Simple Intents Dictionary for greet etc.
intent_response_dict = {
    "intro": ["This is a cryptocurrency bot. Feel free to query anything related to cryptocurrency values"],
    "greet":["Hey","Hello","Hi","Howdy", "How do you do?"],
    "goodbye":["Bye","It was nice talking to you","See you"],
    "affirm":["Cool","I know you would like it"]
}

#intent to retrieve attributs of the knowledge base
def AttributesKnowledgeBase(data):
    try:
        response= data.columns.values.tolist()
        return str(response)[1:-1]
    except Exception as e:
        print(e)
        response_text = "Oops seems like something wrong with database. Error: " + str(e)
        return response_text

#Intent to retrieve highest value of a cryptocurrency
def GetHighestValueByName(data,entities):
    try:
        response_text=''
        data = data.groupby('name')['high'].max()
        for i in entities:
            temp = str(i['value']).title()
            response_text = response_text + str(i['value'].title()) + " Highest value ever was $" + str(data[temp]) + "\n"
        print(response_text)
        return response_text
    except Exception as e:
        response_text = "Oops seems like something wrong with database. Error: " + str(e)
        return response_text

#Intent to retrieve last known status of a currency
def GetStatusByName(data,entities):
    try:
        response_text =''
        for i in entities:
            data1 = data.loc[data['name'] == i['value'].title()]
            response_text = response_text + str(i['value'].title()) +' last known value to me for the date ' +str(data1.index[-1].date()) +' is : ' +str(data1['close'][-1]) +"\n"
            print (response_text)
        return response_text
    except Exception as e:
        print(e)
        response_text = "Oops seems like something wrong with database. Error: " + str(e)
        return response_text

#Intent to retrieve list of cryptos
def CryptoList(data):
    try:
        response_text = "The list of cryptos currently in my database include "
        final_data = data.name.unique()
        final_data = str(final_data)
        response_text = response_text + final_data[1:-1]
        return response_text
    except Exception as e:
        print(e)
        response_text = "Oops seems like something wrong with database. Error: " + str(e)
        return response_text

#intent to create a timeseries graph of daily values
def PlotCurrencyGraph(data,crypto):
    import matplotlib.pyplot as plt
    try:
        for i in crypto:
            data1 = data.loc[data['name'] == i['value'].title()]
            plt.plot(data1['high'],label=i['value'].title())
            plt.legend(loc='best')
        plt.savefig('DailyGraph.png')
    except Exception as e:
        print(e)
        response_text = "Oops seems like something wrong with database. Error: " + str(e)
        return response_text

#intent to get closing value for a date        
def GetCloseByDate(data,entities):
    try:
        import pandas as pd
        for i in entities:
            if i['entity'] =='Crypto':
                crypto=str(i['value'].title())
            if i['entity']=='date':
                temp=pd.to_datetime(i['value'],format='%d-%m-%Y')
                data1 = data.loc[data.index == temp]
        x=data1.loc[data1['name']==crypto]
        response_text = "The closing value for " + crypto + " for date " + str(temp.date()) + " is: $" + str(x['close'][0])
        return response_text
    except Exception as e:
        print(e)
        response_text = "Please ensure date is in DD-MM-YYYY format.Error:  " +str(e)
        return response_text
