import json

compare_index = ["510310", "510580"]

fund = [
        "519066",
        "005738",
        "005760",
        "040020",
        "001473",
        "005267",
        "470098", 
        "001508",
        "001694",
        "000566",
        "008186",
        "168002",
        "673100",
        "000006",
        "006327",
        "501090",
        "001182",
        "163415",
        "163406",
        "003889",
        "001714",
        "000251",
        "001410",
        "001938",
        "519772",
        "007412",
        "005827",
        "002846",
        "001500",
        "001605",
        "009076",
        "519069",
        "519736",
        "005001",
        "160133",
        "000991",
        "000628",
        "450009",
        "160813"
]

fund_extra = [
    "007280",
    "470018",
    "519768",
    "675111",
    "002742",
    "000171",
    "003429",
    "007915",
    "003547",
    "206018",
    "003327",
    "003358"
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
