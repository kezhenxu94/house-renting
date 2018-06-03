# -*- coding: utf-8 -*-

# 只需要在这个列表中添加以下 available_cities 中的城市, 如果只需要扒取一个城市也需要使用一个括号包围, 如 (u'广州',)
cities = (u'广州', u'北京')

available_cities = (
    u'北京',

    u'成都', u'重庆', u'长沙',

    u'大连', u'东莞',

    u'佛山',

    u'广州',

    u'杭州', u'惠州', u'合肥',

    u'济南',

    u'廊坊',

    u'南京',

    u'青岛',

    u'上海', u'深圳', u'苏州', u'石家庄', u'沈阳',

    u'天津',

    u'武汉', u'无锡',

    u'厦门', u'西安',

    u'烟台',

    u'中山', u'珠海', u'郑州',
)

available_cities_map = {
    # B
    u'北京': 'https://bj.lianjia.com/zufang/', u'保亭': None, u'保定': None,

    # C
    u'成都': 'https://cd.lianjia.com/zufang/', u'重庆': 'https://cq.lianjia.com/zufang/',
    u'长沙': 'https://cs.lianjia.com/zufang/', u'澄迈': None, u'承德': None, u'滁州': None,

    # D
    u'大连': 'https://dl.lianjia.com/zufang/', u'东莞': 'https://dg.lianjia.com/zufang/',
    u'儋州': None, u'定安': None, u'大理': None, u'德阳': None,

    # F
    u'佛山': 'https://fs.lianjia.com/zufang/',

    # G
    u'广州': 'https://gz.lianjia.com/zufang/',

    # H
    u'杭州': 'https://hz.lianjia.com/zufang/', u'惠州': 'https://hui.lianjia.com/zufang/',
    u'海口': None, u'合肥': 'https://hf.lianjia.com/zufang/', u'衡水': None, u'黄冈': None, u'邯郸': None,

    # J
    u'济南': 'https://jn.lianjia.com/zufang/', u'嘉兴': None, u'晋中': None,

    # K
    u'昆明': None,

    # L
    u'陵水': None, u'廊坊': 'https://lf.lianjia.com/zufang/', u'临高': None, u'乐东': None, u'龙岩': None,
    u'乐山': None,

    # M
    u'眉山': None,

    # N
    u'南京': 'https://nj.lianjia.com/zufang/',

    # Q
    u'青岛': 'https://qd.lianjia.com/zufang/', u'琼海': None, u'琼中': None, u'泉州': None, u'清远': None, u'秦皇岛': None,

    # S
    u'上海': 'https://sh.lianjia.com/zufang/', u'深圳': 'https://sz.lianjia.com/zufang/',
    u'苏州': 'https://su.lianjia.com/zufang/', u'石家庄': 'https://sjz.lianjia.com/zufang/',
    u'沈阳': 'https://sy.lianjia.com/zufang/', u'三亚': None, u'绍兴': None,

    # T
    u'天津': 'https://tj.lianjia.com/zufang/', u'太原': None,

    # W
    u'武汉': 'https://wh.lianjia.com/zufang/', u'无锡': 'https://wx.lianjia.com/zufang/', u'文昌': None, u'万宁': None,
    u'五指山': None, u'威海': None,

    # X
    u'厦门': 'https://xm.lianjia.com/zufang/', u'西安': 'https://xa.lianjia.com/zufang/', u'徐州': None, u'西双版纳': None,
    u'咸宁': None, u'邢台': None,

    # Y
    u'烟台': 'https://yt.lianjia.com/zufang/',

    # Z
    u'中山': 'https://zs.lianjia.com/zufang/', u'珠海': 'https://zh.lianjia.com/zufang/',
    u'郑州': 'https://zz.lianjia.com/zufang/', u'镇江': None, u'张家口': None, u'漳州': None,
}
