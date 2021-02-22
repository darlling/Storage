# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from asyncio import gather, run, sleep

from requests import post

wpsid = (
    "1105730197",  # MINE
    "1087505057",  # HF
    "375805850",  # ZY
    "479170710"  # MQT
)

invite_sid = [
    "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
    "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
    "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
    "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
    "V02ScVbtm2pQD49ArcgGLv360iqQFLs014c8062e000b6c37b6",
    "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
    "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
    "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
    "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
    "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
    "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
    "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d"
]


async def invite(userid: int) -> None:
    for index, item in enumerate(invite_sid):
        header = {'sid': item}
        res = post("https://zt.wps.cn/2018/clock_in/api/invite",
                   headers=header,
                   data={'invite_userid': userid})
        if res.status_code == 200:
            print(f"{userid}: 邀请第 {index+1} 人成功")
        else:
            print(f"{userid}: 邀请第 {index+1} 人失败")
        await sleep(5)


async def main():
    await gather(invite(wpsid[0]), invite(wpsid[1]), invite(wpsid[2]),
                 invite(wpsid[3]))


def main_handler():
    return run(main())
