# NOTE: Generated By HttpRunner v3.0.11
# FROM: demoquick.json

from httprunner import HttpRunner, Config, Step, RunRequest


# 注释
class TestCaseDemoquick(HttpRunner):
    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("/")
                .get("https://www.baidu.com/")
                .with_params(**{"tn": "78040160_15_pg", "ch": "9"})
                .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document",
                    "Cookie": "BIDUPSID=64D9BF19B85416AEDCD3B13F3ED33548; PSTM=1588077374; BAIDUID=64D9BF19B85416AE90F63CE268106BC7:FG=1; BDUSS=JiYmdFQjR4VjJUeGF2WXFXd1Boen5UcE5rSnp-THcwM0luVkd4LXU5WFJUTnBlSVFBQUFBJCQAAAAAAAAAAAEAAAB5rSI7d2pnam20psWu1~kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANG~sl7Rv7JeYW; COOKIE_SESSION=9_0_8_4_4_21_0_0_6_6_1_6_829969_0_6_0_1589602551_0_1589602545%7C9%230_0_1589602545%7C1; BD_UPN=12314753; BDRCVFR[j-y5gma3amt]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=1425_31325_21094_31845; delPer=0; BD_CK_SAM=1; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=f9e7yjuFZZT6b6YF99wRc2PqvqJTgHLaXNH9KlgvJgoKGMY6C%2Bo%2FHw49%2BNd5Zgit0CbQZn4; BDSVRTM=0",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "text/html;charset=utf-8")
        ),
        Step(
            RunRequest("/sugrec")
                .get("https://www.baidu.com/sugrec")
                .with_params(
                **{
                    "prod": "pc_his",
                    "from": "pc_web",
                    "json": "1",
                    "sid": "1425_31325_21094_31845",
                    "hisdata": '[{"time":1588077394,"kw":"音速地精"},{"time":1588077405,"kw":"音速小子"}]',
                    "req": "2",
                    "csor": "0",
                }
            )
                .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.baidu.com/?tn=78040160_15_pg&ch=9",
                    "Cookie": "BIDUPSID=64D9BF19B85416AEDCD3B13F3ED33548; PSTM=1588077374; BAIDUID=64D9BF19B85416AE90F63CE268106BC7:FG=1; BDUSS=JiYmdFQjR4VjJUeGF2WXFXd1Boen5UcE5rSnp-THcwM0luVkd4LXU5WFJUTnBlSVFBQUFBJCQAAAAAAAAAAAEAAAB5rSI7d2pnam20psWu1~kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANG~sl7Rv7JeYW; COOKIE_SESSION=9_0_8_4_4_21_0_0_6_6_1_6_829969_0_6_0_1589602551_0_1589602545%7C9%230_0_1589602545%7C1; BD_UPN=12314753; BDRCVFR[j-y5gma3amt]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=1425_31325_21094_31845; delPer=0; BD_CK_SAM=1; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=f9e7yjuFZZT6b6YF99wRc2PqvqJTgHLaXNH9KlgvJgoKGMY6C%2Bo%2FHw49%2BNd5Zgit0CbQZn4",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "text/plain; charset=UTF-8")
        ),
        Step(
            RunRequest("/home/xman/data/tipspluslist")
                .get("https://www.baidu.com/home/xman/data/tipspluslist")
                .with_params(
                **{
                    "indextype": "manht",
                    "_req_seqid": "0xa8243c94002e90d0",
                    "asyn": "1",
                    "t": "1591454019383",
                    "sid": "1425_31325_21094_31845",
                }
            )
                .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.baidu.com/?tn=78040160_15_pg&ch=9",
                    "Cookie": "BIDUPSID=64D9BF19B85416AEDCD3B13F3ED33548; PSTM=1588077374; BAIDUID=64D9BF19B85416AE90F63CE268106BC7:FG=1; BDUSS=JiYmdFQjR4VjJUeGF2WXFXd1Boen5UcE5rSnp-THcwM0luVkd4LXU5WFJUTnBlSVFBQUFBJCQAAAAAAAAAAAEAAAB5rSI7d2pnam20psWu1~kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANG~sl7Rv7JeYW; COOKIE_SESSION=9_0_8_4_4_21_0_0_6_6_1_6_829969_0_6_0_1589602551_0_1589602545%7C9%230_0_1589602545%7C1; BD_UPN=12314753; BDRCVFR[j-y5gma3amt]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=1425_31325_21094_31845; delPer=0; BD_CK_SAM=1; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=f9e7yjuFZZT6b6YF99wRc2PqvqJTgHLaXNH9KlgvJgoKGMY6C%2Bo%2FHw49%2BNd5Zgit0CbQZn4",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "text/html;charset=utf-8")
        ),
        Step(
            RunRequest("/home/hit/v.gif")
                .get("https://www.baidu.com/home/hit/v.gif")
                .with_params(
                **{
                    "mod": "mantpl:news",
                    "submod": "index",
                    "utype": "0",
                    "superver": "supernewplus",
                    "portrait": "79ad776a676a6db4a6c5aed7f9223b",
                    "glogid": "3978013791",
                    "type": "2011",
                    "pid": "315",
                    "isLogin": "1",
                    "version": "PCHome",
                    "terminal": "PC",
                    "qid": "0xa8243c94002e90d0",
                    "sid": "1425_31325_21094_31845",
                    "super_frm": "",
                    "from_login": "",
                    "from_reg": "",
                    "query": "",
                    "curcard": "2",
                    "curcardtab": "",
                    "_r": "0.39155761161512737",
                    "m": "mantpl:news_newsShow",
                    "logactid": "0200100000",
                    "showType": "hotword",
                    "words": '["1\n                高雄市长韩国瑜被罢免","2\n                广西砍伤39名师生保安被批捕","3\n                撒贝宁播新闻联播什么样","4\n                忘记28年房子现住户已搬家","5\n                美民众发起装死抗议","6\n                黄奕聂远同框","7\n                天津新增1例境外输入","8\n                父杀女案罪犯韦乐被执行死刑","9\n                世卫组织更新口罩使用建议","10\n                俄罗斯新增8855例确诊病例"]',
                    "pagenum": "0",
                }
            )
                .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Dest": "image",
                    "Referer": "https://www.baidu.com/?tn=78040160_15_pg&ch=9",
                    "Cookie": "BIDUPSID=64D9BF19B85416AEDCD3B13F3ED33548; PSTM=1588077374; BAIDUID=64D9BF19B85416AE90F63CE268106BC7:FG=1; BDUSS=JiYmdFQjR4VjJUeGF2WXFXd1Boen5UcE5rSnp-THcwM0luVkd4LXU5WFJUTnBlSVFBQUFBJCQAAAAAAAAAAAEAAAB5rSI7d2pnam20psWu1~kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANG~sl7Rv7JeYW; COOKIE_SESSION=9_0_8_4_4_21_0_0_6_6_1_6_829969_0_6_0_1589602551_0_1589602545%7C9%230_0_1589602545%7C1; BD_UPN=12314753; BDRCVFR[j-y5gma3amt]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=1425_31325_21094_31845; delPer=0; BD_CK_SAM=1; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=f9e7yjuFZZT6b6YF99wRc2PqvqJTgHLaXNH9KlgvJgoKGMY6C%2Bo%2FHw49%2BNd5Zgit0CbQZn4",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "image/gif")
        ),
        Step(
            RunRequest("/content-search.xml")
                .get("https://www.baidu.com/content-search.xml")
                .with_headers(
                **{
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "no-cors",
                    "Sec-Fetch-Dest": "empty",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
                    "Cookie": "BIDUPSID=64D9BF19B85416AEDCD3B13F3ED33548; PSTM=1588077374; BAIDUID=64D9BF19B85416AE90F63CE268106BC7:FG=1; BDUSS=JiYmdFQjR4VjJUeGF2WXFXd1Boen5UcE5rSnp-THcwM0luVkd4LXU5WFJUTnBlSVFBQUFBJCQAAAAAAAAAAAEAAAB5rSI7d2pnam20psWu1~kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANG~sl7Rv7JeYW; COOKIE_SESSION=9_0_8_4_4_21_0_0_6_6_1_6_829969_0_6_0_1589602551_0_1589602545%7C9%230_0_1589602545%7C1; BD_UPN=12314753; BDRCVFR[j-y5gma3amt]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=1425_31325_21094_31845; delPer=0; BD_CK_SAM=1; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=f9e7yjuFZZT6b6YF99wRc2PqvqJTgHLaXNH9KlgvJgoKGMY6C%2Bo%2FHw49%2BNd5Zgit0CbQZn4",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "application/xml")
        ),
        Step(
            RunRequest("/home/msg/data/personalcontent")
                .get("https://www.baidu.com/home/msg/data/personalcontent")
                .with_params(
                **{
                    "num": "8",
                    "indextype": "manht",
                    "_req_seqid": "0xa8243c94002e90d0",
                    "asyn": "1",
                    "t": "1591454019391",
                    "sid": "1425_31325_21094_31845",
                }
            )
                .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.baidu.com/?tn=78040160_15_pg&ch=9",
                    "Cookie": "BIDUPSID=64D9BF19B85416AEDCD3B13F3ED33548; PSTM=1588077374; BAIDUID=64D9BF19B85416AE90F63CE268106BC7:FG=1; BDUSS=JiYmdFQjR4VjJUeGF2WXFXd1Boen5UcE5rSnp-THcwM0luVkd4LXU5WFJUTnBlSVFBQUFBJCQAAAAAAAAAAAEAAAB5rSI7d2pnam20psWu1~kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANG~sl7Rv7JeYW; COOKIE_SESSION=9_0_8_4_4_21_0_0_6_6_1_6_829969_0_6_0_1589602551_0_1589602545%7C9%230_0_1589602545%7C1; BD_UPN=12314753; BDRCVFR[j-y5gma3amt]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=1425_31325_21094_31845; delPer=0; BD_CK_SAM=1; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=f9e7yjuFZZT6b6YF99wRc2PqvqJTgHLaXNH9KlgvJgoKGMY6C%2Bo%2FHw49%2BNd5Zgit0CbQZn4",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "text/html;charset=utf-8")
        ),
        Step(
            RunRequest("/home/msg/data/personalcontent")
                .get("https://www.baidu.com/home/msg/data/personalcontent")
                .with_params(
                **{
                    "num": "8",
                    "indextype": "manht",
                    "_req_seqid": "0xa8243c94002e90d0",
                    "asyn": "1",
                    "t": "1591454019399",
                    "sid": "1425_31325_21094_31845",
                }
            )
                .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.baidu.com/?tn=78040160_15_pg&ch=9",
                    "Cookie": "BIDUPSID=64D9BF19B85416AEDCD3B13F3ED33548; PSTM=1588077374; BAIDUID=64D9BF19B85416AE90F63CE268106BC7:FG=1; BDUSS=JiYmdFQjR4VjJUeGF2WXFXd1Boen5UcE5rSnp-THcwM0luVkd4LXU5WFJUTnBlSVFBQUFBJCQAAAAAAAAAAAEAAAB5rSI7d2pnam20psWu1~kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANG~sl7Rv7JeYW; COOKIE_SESSION=9_0_8_4_4_21_0_0_6_6_1_6_829969_0_6_0_1589602551_0_1589602545%7C9%230_0_1589602545%7C1; BD_UPN=12314753; BDRCVFR[j-y5gma3amt]=mk3SLVN4HKm; BD_HOME=1; H_PS_PSSID=1425_31325_21094_31845; delPer=0; BD_CK_SAM=1; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_645EC=f9e7yjuFZZT6b6YF99wRc2PqvqJTgHLaXNH9KlgvJgoKGMY6C%2Bo%2FHw49%2BNd5Zgit0CbQZn4",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "text/html;charset=utf-8")
        ),
    ]


if __name__ == "__main__":
    TestCaseDemoquick().test_start()
