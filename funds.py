import json

# 对比的指数ETF代码
compare_index = ["510310", "510580"]  #沪深300，中证500

# 2022/1/18观点：虽然降息10个基点，但米国通胀数据非常夸张，为防范未来风险，权益类基金今日减仓1%

# 权益类基金代码
fund = [
        "010728",  #中泰兴诚一年     0.8%
        "011230",  #创金数字经济C    0.4%
        "001445",  #华安国企改革     0.4%
        #----------- 上面处于观察期 -----------
        "009375",  #浦银MSCI A股ETF  7%  （宽基指数，可换为其他公司的指数如华安沪深300C、易方达沪深300C等）
        "001508",  #富国新动力A      7.4%
        "519702",  #交银趋势优先A    6.8%
        "003962",  #易方达瑞程C      6%
        "000006",  #西部量化A        6%  
        "002340",  #富国价值优势     5.3%
        "001366",  #金鹰产业整合     3.6%
        "470098",  #汇添富逆向       3%
        "009707",  #工银新兴制造A    3%
        "001043",  #工银美丽城镇A    2.5%
        "008276",  #财通价值发现A    2.5%
        "161834",  #银华鑫锐A        2.3%
        "163409",  #兴全绿色         1.7%
        "550015",  #中信至远A        1.5%
        #----------- 下面是美股指数 -----------
        "040046",  #华安纳斯达克100  8%
        "050025",  #博时标普500      7%
]
# 仅监控基金经理是否更改，适合偏债券基金
fund_extra = [
    "003547",   #鹏华丰禄     2.5%
    "003859",   #招商昭旭A    3%
    "002704",   #德邦锐兴A    3%
    "006966",   #财通安瑞C    
    "007744",   #长盛安逸A    2.5%
    "000914",   #中加纯债
    "004127",   #鹏华丰康
    "003429",   #兴业高级债指
    #----------- 上纯债，下固收+ -----------
    "001182",   #易方达安心   （高风险玩家可以直接买易方达瑞程C ）
    "004932",   #招商丰拓A    2.5%
    "519769",   #交银优选C    2.5%
    "002742",   #泓德裕祥A   
    "008356",   #中加科丰
    "002087",   #国富新机遇A  2.5%
    "002144",   #华安新优选C  2.5%
    "210010",   #金鹰灵活A    
    "002794",   #天弘永利E
    "013260",   #太平睿享A
]
# 香港基金，暂不支持
fund_hk = [
    "968075",  #百达策略收益
    "968010"   #摩根太平洋    7%
]


def get_funds():
    return {'compare_index': compare_index, 'fund': fund, 'fund_extra': fund_extra}


if __name__ == '__main__':
    with open('data/fund_codes.json', 'w', encoding='utf-8') as fin:
        json.dump(list(set(compare_index + fund + fund_extra)), fin)
