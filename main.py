
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """
    '''
    100016578654 6800xt 26 11:00
    100008550195 3080 26 11:00
    100019176614 6700xt 26 11:00
    100016046826 3070 26 11:00
    100016672406 3090 26 11:00

    
    100008979445 3070 26 15:00
    10027264803895 3060ti 27 12:00
    100016914910 3060ti 29 11:00
    '''
    sku_ids = ['10027096289578']  # 商品id
    # sku_ids = ['100019084146', '10026477628123', '10026477628125', '10026477628127', '10026477628129', '10026477628131']
    area = '1_2800_4209'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    for i in sku_ids:
        asst.exec_reserve_seckill_by_time(sku_id=i, buy_time='2021-03-26 00:00:04.997')


    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=3)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
