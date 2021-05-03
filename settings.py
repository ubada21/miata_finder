def get_location(str):
    if len(str.split('<meta') )== 15:
        return str.split('<meta')[13].split('"')[1]
    else:
        return str.split('<meta')[14].split('"')[1]

def get_listing(str):
    if len(str.split('<meta')) == 15:
        return str.split('<meta')[5].split('"')[1].split('-')[0]
    else:
        return  str.split('<meta')[6].split('"')[1].split('-')[0]

def get_price(prc):
    return str(prc[0]).split('<span class="price">')[1].split('</span>')[0]

def get_datetime(dttm):
    return str(dttm[1]).split('<')[-2].split('>')[1]

def get_makemodel(mkmdl):
    return str(mkmdl[0]).split('<span>')[1].split('<b>')[1].split('</b>')[0]


