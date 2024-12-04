import random


Jomle_ha = {
    "ehsasi": {
        "شروع": ["Ah", "Vay", "Chegadr", "Che"],
        "میانه": ["delam", "galbam", "ehsasam", "vujudam"],
        "پایان": ["baraye to mitapad!", "az shog labriz ast!", "por az eshg ast!", "baraye hamishe mandegar ast!"]
    },
    "khabari": {
        "شروع": ["Emroz", "In hafte", "Tebge gozaresh", "Dar shahre ma"],
        "میانه": ["hava", "vaziyat", "sharayet"],
        "پایان": ["aftabi ast.", "barani ast.", "besyar khob ast.", "moshakhas nist."]
    },
    "porseshi": {
        "شروع": ["Aya", "Chera", "Chegone"],
        "میانه": ["in etefag", "in masale"],
        "پایان": ["ra midani?", "ra dark mikoni?", "ra mitavanid hal konid?", "ra mifahmi?"]
    },
    "amri": {
        "شروع": ["Lotfan", "Hatman", "Khaheshan"],
        "میانه": ["in kar", "in masale", "moshkel"],
        "پایان": ["ra hal kon.", "ra barrasi kon.", "ra beband.", "ra anjam bede."]
    },
    "eltemasi": {
        "شروع": ["Khahesh mikonam", "Lotfan", "Estedaa daram", "Az shoma darkhast daram"],
        "میانه": ["be man", "be in mozoe", "be oo", "be ma"],
        "پایان": ["komak konid.", "lotf konid.", "mehrabani konid.", "tavajoh konid."]
    },
    "enshai": {
        "شروع": ["Be nazar man", "Fekr mikonam", "Ehsas mikonam", "Moetagedam"],
        "میانه": ["in film", "in mozoe", "in vaziat", "in dastan"],
        "پایان": ["jaleb ast.", "ajib ast.", "zibast."]
    },
    "tosifi": {
        "شروع": ["In", "An", "In makan", "In fard"],
        "میانه": ["kheili ziba", "besyar jazzab", "binazir", "be yadmandani"],
        "پایان": ["ast.", "mibashad.", "be nazar miresad.", "neshan dade mishavad."]
    },
    "taajobi": {
        "شروع": ["vay", "ajab", "che"],
        "میانه": ["ettefage ajibi", "lahze zibayi", "mozoe jalebi", "ettefage gheire montazerei"],
        "پایان": ["ast!", "bod!", "shod!"]
    }
}


def barrasi_noee_jomle(user_input):
    user_input = user_input.strip().lower()  
    for noee_jomle in Jomle_ha.keys():
        if noee_jomle in user_input:  
            return noee_jomle
    return None


def sakht_jomle(user_input):
    noee_jomle = barrasi_noee_jomle(user_input)
    if noee_jomle:  
        start = random.choice(Jomle_ha[noee_jomle]["شروع"])
        middle = random.choice(Jomle_ha[noee_jomle]["میانه"])
        end = random.choice(Jomle_ha[noee_jomle]["پایان"])
        return f"{start} {middle} {end}"
    else:
        return "man az in noe jomle agahi nadaram. bebakhshid!"


print("che noe jomlei mikhahid barayetan dorost konam? (ehsasi,khabari,porseshi,amri,eltemasi,enshai,tosifi,taajobi):")
user_input = input(">>>")


result = sakht_jomle(user_input)
print("jomlei ke barayetan dorost kardam:")
print(result)
