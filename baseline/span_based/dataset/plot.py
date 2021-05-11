import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tabulate import tabulate
sns.set(style="whitegrid")

stats = {
    "UCP": [0.014823599169878446,['if/elif/else']],
    "WHNP": [0.014823599169878446,['whichever party']],
    "LANGUAGE": [0.014823599169878446,['English.']],
    "NML": [0.014823599169878446,['knock-and-announce']],
    "SINV": [0.029647198339756892,['Is that the definition of gross income cuts across the tax code.', 'offline confirms']],
    "SBARQ": [0.029647198339756892,['`which flask` would show the path on posix', '`y = self.address, t.to_string(header=None, index=False)`']],
    "EVENT": [0.07411799584939224,['Civil War', 'Winning the War on War']],
    "WORK_OF_ART": [0.11858879335902757,['Nobel Peace Prize', 'Late Night']],
    "PRODUCT": [0.13341239252890602,['section on EnronOnline', 'Confessions of a Surgeon']],
    "LST": [0.17788319003854136,['1964(b)', 'X-rays']],
    "FAC": [0.17788319003854136,['708 Third Avenue, 4th Floor New York, NY 10017', 'northern Great Plains']],
    "QUANTITY": [0.2223539875481767,['two meters', '5 foot 1 -- 5 foot 2 inches']],
    "FRAG": [0.28164838422769045,['"Never."', 'By adding a `syntax-local-introduce` in the right spot.']],
    "ADVP": [0.29647198339756897,['Automatically', 'Recently']],
    "LOC": [0.3112955825674474,['Ricki Lake', 'Bay State']],
    "INTJ": [0.37058997924696113,['No', 'no']],
    "LAW": [0.4743551734361103,['Fourth Amendment', 'Fourth Amendment']],
    "SBAR": [0.5484731692855026,['If the search was done in public view', 'because that just gets overstuffed with junk.']],
    "VP": [0.5632967684553809,['have no any obligation to save the injunction', 'trump']],
    "PERCENT": [0.6077675659650162,['47%', 'A million percent']],
    "X": [0.6818855618144086,['"call by name"', 'kate']],
    "ADJP": [0.7708271568336793,['bad', 'very old']],
    "ORDINAL": [0.9931811443818559,['50th Floor Boardroom Video Connections', 'Fourth']],
    "TIME": [1.0524755410613698,['Tonight',"A little before 11 o'clock, about 10,50 or so", ]],
    "PP": [1.260005929439668,['with `syntax-local-lift-module`', 'During lunch']],
    "NORP": [1.2896531277794248,['white Caucasian American','Republicans', 'white Caucasian American']],
    "MONEY": [1.556477912837237,['$250,000', '$45']],
    "S": [5.44026089534539,['need to use an external store for state', 'DrRacket icon have error']],
    "GPE": [8.908983101096947,['Chicago', 'Afghanistan and Iraq']],
    "CARDINAL": [9.620515861251112,['page 66, volume 4', 'one red dwarf']],
    "DATE": [9.620515861251112,['2020','jurisdiction under 28-1257', '2020']],
    "ORG": [11.384524162466647,['Drug Enforcement Authority','ALINA SELYUKH', ]],
    "PERSON": [12.511117699377408,['Tommy Norment', 'Danny Heitman']],
    "NP": [30.43284909576045,['the Pulitzer Prize', 'Trump']]
}

mapper = {
          "QUANTITY":" Measurements",
          "ADVP":"Adverb Phrase",
          "LOC":"Location",
          "LAW":"Laws documents",
          "X":"Unknown",
          "SBAR":"Clause introduced",
          "VP":"Verb Phrase",
          "PERCENT":"Percentage",
          "ADJP":"Adjective Phrase",
          "ORDINAL":"Oridinal Number",
          "NORP":"Nationalities or religious",
          "TIME":"Time",
          "PP":"Prepositional Phrase",
          "MONEY":"Monetary values",
          "S":"Clause",
          "DATE":"Dates",
          "GPE":"Countries, cities, states",
          "CARDINAL":"Other Numeric",
          "ORG":"Organizations",
          "PERSON":"People, including fictional",
          "NP":"Noun Phrase",
          "FRAG": "Fragment",
          "INTJ":" Interjection",
          "UCP":"Coordinated Phrase",
          "WHNP": "Wh-noun Phrase",
          "LANGUAGE": "Language",
          "NML": "Other",
          "SINV": "Inverted declarative sentence",
          "SBARQ":"Direct question",
          "EVENT":"Named events",
          "WORK_OF_ART":"Titles of books, songs, etc.",
          "PRODUCT": "Objects, vehicles, foods",
          "LST":"List marker",
          "FAC": "Buildings, airports, highways"
}


table = []
other = 0.0
for k,v in stats.items():
    if v[0]<1.0:
        other += v[0]
    else:
        table.append([mapper[k],v[0],v[1][0]])
print(other)
print(tabulate(table,headers=["Answer type","Percentage","Example"], floatfmt=("", ".1f",""),tablefmt="latex"))


clr = {
          "QUANTITY":sns.color_palette("Set2")[0],
          "ADVP":sns.color_palette("Set2")[2],
          "LOC":sns.color_palette("Set2")[0],
          "LAW":sns.color_palette("Set2")[0],
          "X":sns.color_palette("Set2")[2],
          "SBAR":sns.color_palette("Set2")[2],
          "VP":sns.color_palette("Set2")[2],
          "PERCENT":sns.color_palette("Set2")[0],
          "ADJP":sns.color_palette("Set2")[2],
          "ORDINAL":sns.color_palette("Set2")[0],
          "NORP":sns.color_palette("Set2")[0],
          "TIME":sns.color_palette("Set2")[0],
          "PP":sns.color_palette("Set2")[2],
          "MONEY":sns.color_palette("Set2")[0],
          "S":sns.color_palette("Set2")[2],
          "DATE":sns.color_palette("Set2")[0],
          "GPE":sns.color_palette("Set2")[0],
          "CARDINAL":sns.color_palette("Set2")[0],
          "ORG":sns.color_palette("Set2")[0],
          "PERSON":sns.color_palette("Set2")[0],
          "NP":sns.color_palette("Set2")[2],
          "FRAG": sns.color_palette("Set2")[2],
          "INTJ": sns.color_palette("Set2")[2],
          "UCP":sns.color_palette("Set2")[2],
          "WHNP": sns.color_palette("Set2")[2],
          "LANGUAGE": sns.color_palette("Set2")[0],
          "NML": sns.color_palette("Set2")[2],
          "SINV": sns.color_palette("Set2")[2],
          "SBARQ":sns.color_palette("Set2")[2],
          "EVENT":sns.color_palette("Set2")[0],
          "WORK_OF_ART":sns.color_palette("Set2")[0],
          "PRODUCT": sns.color_palette("Set2")[0],
          "LST":sns.color_palette("Set2")[2],
          "FAC": sns.color_palette("Set2")[0]
}


color_arr = [clr[k] for k, v in stats.items()]

types = [mapper[k] for k, v in stats.items()]
num   = [v[0] for k, v in stats.items()]

df = pd.DataFrame({'Answer type':types, 
                    'Percentage': num})
fig, axes = plt.subplots(nrows=1, ncols=1)
# sns.set(rc={‘figure.figsize’:(10,12)})
ax = sns.barplot(y="Answer type",x="Percentage", data=df,palette=color_arr,label="small") #palette="GnBu_d"
plt.yticks(fontsize=8)
colors = {'Named Entities':sns.color_palette("Set2")[0], 'Consituent Parser':sns.color_palette("Set2")[2]}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
fig.tight_layout()

plt.savefig("test.png",dpi=400)