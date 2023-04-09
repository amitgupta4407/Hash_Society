ls = {'GOOG', 'SGEN', 'EQIX', 'HZNP', 'SWKS', 'GMAB', 'CTAS', 'SNPS', 'AVGO', 'KLAC', 'PCAR', 'REGN', 'CSCO', 'FANG', 'TSLA', 'FTNT', 'ADP', 'AAPL', 'CHTR', 'TECH', 'ISRG', 'TMUS', 'ZM', 'TROW', 'VTRS', 'INTU', 'MAR', 'MSFT', 'CME', 'CSGP', 'ETSY', 'TSCO', 'GLPI', 'KHC', 'ABNB', 'NVCR', 'MDB', 'AXON', 'ZBRA', 'TEAM', 'HTHT', 'COST', 'NDSN', 'AMZN', 'LKQ', 'EBAY', 'IEP', 'PODD', 'MPWR', 'FSLR', 'MCHP', 'HOLX', 'TCOM', 'UTHR', 'SIVB', 'LBRDK', 'MRVL', 'NBIX', 'LI', 'SPLK', 'CINF', 'BMRN', 'ENPH', 'INCY', 'TRMB', 'CHKP', 'PDD', 'WBA', 'POOL', 'SBUX', 'CRWD', 'VOD', 'TW', 'AZPN', 'LPLA', 'FOXA', 'CSX', 'TTWO', 'NTRS', 'MU', 'QCOM', 'SAN', 'SBAC', 'CTSH', 'TTD', 'VRTX', 'ALGN', 'AMGN', 'JKHY', 'VRSK', 'FWONK', 'AMD', 'PARAA', 'ORLY', 'CMCSA', 'ADBE', 'MTCH', 'ZS', 'DLTR', 'DXCM', 'TXN', 'GILD', 'VRSN', 'LRCX', 'ALNY', 'AZN', 'VZ', 'ACGL', 'BKNG', 'ARGX', 'EXC', 'JBHT', 'NDAQ', 'APA', 'WMG', 'META', 'PAYX', 'ABMD', 'PFG', 'ASML', 'NICE', 'ROST', 'EXPD', 'ON', 'INTC', 'TER', 'MRNA', 'WDAY', 'KDP', 'LNT', 'CPRT', 'FAST', 'IDXX', 'LSXMB', 'SEDG', 'ODFL', 'FDS', 'MELI', 'NXPI', 'SIRI', 'ADSK', 'AEP', 'XEL', 'ERIE', 'MDLZ', 'CDW', 'ANSS', 'FITB', 'IBKR', 'ADI', 'STLD', 'AKAM', 'EXPE', 'DDOG', 'NTAP', 'ILMN', 'ULTA', 'SSNC', 'PYPL', 'PEP', 'EA', 'PTC', 'BIIB', 'MNST', 'UAL', 'FISV', 'AMAT', 'NVDA', 'LULU', 'NFLX', 'GRMN', 'CDNS', 'HBAN'}

def extract_company_details(s):
  s = str(s).split()
  for j in s:
    # if len(j)<2: continue
    if j[0] == "$" and j[1:] in ls:
      return j[1:]
  return "No stock found"
#defining a function to remove unrequired asswmb
import re
def remove_char(tweet):
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?:\/\/.[\r\n]', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r'[0-9]', '', tweet)
    
    return tweet

# s = remove_char("$TSLA saw loss in its stock price during covid ")
# print(extract_company_details(s))
#AFINN sentiment analysis in Python: Wordlist-based approach for sentiment analysis.
from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def getVanderSentiment(score):    
    if (score >= 0.05): 
        return "Positive"
    
    elif (score < 0.05 and score > -0.05):
        return "Neutral"
    
    elif (score <= -0.05):    
        return "Negative"
    
    return score
	
# def getVanderScore(tweet):    
#     vs = vanderSentimentAnalyzer.polarity_scores(tweet)
#     score = vs['compound']
#     return score
	
def vander_score(s):
	afinn = Afinn()
	res = afinn.score(s)
	vs = SentimentIntensityAnalyzer().polarity_scores(s)
	return getVanderSentiment(vs['compound'])

# s = remove_char("$TSLA saw loss in its stock price during covid ")
# print("loss  ==>   ", vander_score(s))
# s = remove_char("$TSLA saw decrease in its stock price during covid ")
# print("decrease ==>  ", vander_score(s))
# s = remove_char("$TSLA saw increase in its stock price during covid ")
# print("increase  ==>   ", vander_score(s))