import re
import requests
import json
from utils.RequestUtil import Request
from config.Conf import ConfigYalm


def test_zxx():
    # url = "http://mp-meiduo-python.itheima.net/login/"
    conf_yaml = ConfigYalm()
    url_path = conf_yaml.get_conf_url()
    url = url_path + "login/"
    print(url)
    # r_get = requests.get(url)
    # 使用封装的方法
    request = Request()
    r_get = request.get(url)
    res = r_get.get("body")
    # 登陆时要传入token 使用正则表达式获取token
    token = re.findall('csrfmiddlewaretoken\" value=\"(.+?)\"', res)
    data = {"csrfmiddlewaretoken": token[0],
            "username": "admin",
            "pwd": "admin",
            "remembered": "on"
            }
    # 登陆成功后禁止重定向 allow_redirects=False
    # r = requests.post(url, data=data, allow_redirects=False)
    # allow_redirects = False
    r = request.post(url, data=data, allow_redirects=False)
    # 获取登陆成功之后响应头中的cookie信息中的username和sessionid
    header = r.get("headers").get("Set-Cookie")
    username = re.findall('username=(.+?);', header)
    sessionid = re.findall('sessionid=(.+?);', header)
    cookie = "username="+username[0]+"; sessionid="+sessionid[0]
    print("----------")
    print("登陆：cookie"+cookie)
    # 个人中心
    # url_info = "http://mp-meiduo-python.itheima.net/info/"
    url_info = url_path + "info/"
    print(url_info)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": cookie
    }
    # r_info = requests.get(url_info, headers=headers)
    r_info = request.get(url_info, headers=headers)
    print("个人中心")
    print(r_info)

    # 添加购物车
    # url_carts = "http://mp-meiduo-python.itheima.net/carts/"
    url_carts = url_path + "carts/"
    headers_carts = {
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": cookie
    }
    data_carts = {'sku_id': '18', 'count': '1'}
    # request payload形式传参使用json.dumps(data_carts)
    # res_carts = requests.post(url_carts, data=json.dumps(data_carts), headers=headers_carts)
    # print(res_carts.text)
    res_carts = request.post(url_carts, data=json.dumps(data_carts), headers=headers_carts)
    print("添加购物车")
    print(res_carts)
    # 购物车选择商品
    # url_carts_sel = "http://mp-meiduo-python.itheima.net/carts/"
    url_carts_sel = url_path + "carts/"
    data_carts_sel = {'count': '10', 'selected': 'ture', 'sku_id': '18'}
    headers_carts_sel = {
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": cookie
    }
    # res_carts_sel = requests.put(url_carts_sel, json=data_carts_sel, headers=headers_carts_sel)
    # print(res_carts_sel.json())
    res_carts_sel = request.put(url_carts_sel, json=data_carts_sel, headers=headers_carts_sel)
    print("购物车选择商品")
    print(res_carts_sel)
    # 下订单
    # url_orders = "http://mp-meiduo-python.itheima.net/orders/commit/"
    url_orders = url_path + "orders/commit/"
    headers_orders = {
        "Content-Type": "application/json;charset=utf-8",
        "Cookie": cookie
    }
    data_orders = {'address_id': '5', 'pay_method': 2}
    # res_orders =
    # requests.post(url_orders, data=json.dumps(data_orders), headers=headers_orders, allow_redirects=False)
    # print(res_orders.json())
    res_orders = request.post(url_orders, data=json.dumps(data_orders), headers=headers_orders, allow_redirects=False)
    print("下订单")
    print(res_orders)


if __name__ == '__main__':
    test_zxx()
