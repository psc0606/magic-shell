# coding = utf-8
import json

from kafka import KafkaProducer
from modules.interactive.HistoryCompleter import HistoryCompleter

producer = KafkaProducer(bootstrap_servers='localhost:9092')

start_uid = 100000


def send_kafka_test_msg(count):
    msg = {
        "productLine": 1,
        "styleType": 21,
        "adId": "12151",
        "accountId": 416384,
        "groupId": 515154,
        "optype": 1,
        "step": 1000,
        "checkstatus": -1,
        "autoAuditMemo": "50003:yintai\u000350003:yintaiwang",
        "adminUserName": "gas-audit",
        "adminUserId": 0,
        "contentVos": [{
            "contentName": "key",
            "contentType": "text",
            "content": "yintaiwang",
            "showContent": "text"
        }],
        "extraInfo": "extraInfoextraInfoextraInfo",
        "rawMsg": "ielog_material_style\t416384\t12151\t515154\tyintaiwang",
        "uid": 0,
        "step2TimeInfoMap": {
            "0": {
                "startTime": 1606449415486,
                "endTime": 1606449415487
            }
        }
    }

    global start_uid
    for uid in range(start_uid, start_uid + int(count)):
        msg['uid'] = uid
        json_msg = json.dumps(msg).encode()
        producer.send('audit_result', json_msg, partition=0)
    start_uid += int(count)


if __name__ == '__main__':
    completer = HistoryCompleter()
    completer.loop_input(send_kafka_test_msg)
    producer.close()
