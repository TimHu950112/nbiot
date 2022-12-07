from am7020_nb import AM7020NB
from am7020_mqtt import AM7020MQTT




# NBIoT 相關設定
apn = "nbiot"  # 存取點名稱
band = 28  # 通訊頻道
CHECK_NET_INTERVAL_MS = 1000  # 網路檢查間隔時間

# MQTT 相關設定
MQTT_BROKER = "broker.emqx.io"
PORT = 8083
MQTT_USERNAME = ""
MQTT_PASSWORD = ""
# TEMP_TOPIC = MQTT_USERNAME + "/feeds/pico.temperature"
# HUM_TOPIC = MQTT_USERNAME + "/feeds/pico.humidity"
# LED_TOPIC = MQTT_USERNAME + "/feeds/pico.led"
# UPLOAD_INTERVAL_MS = 30000  # 訊息上傳間隔時(毫秒)

nb = AM7020NB(0, 9600, 0, 1, 3, False)  # 建立連線物件
mqtt = AM7020MQTT(nb)  # 建立 MQTT 通訊物件


def nbConnect():  # ⾃訂連線程序
    print("Initializing modem...")
    while((not nb.init() or (not nb.nbiotConnect(apn, band)))):
        print(".")

    print("Waiting for network...")
    while(not nb.waitForNetwork()):
        print(".")
    print(" success")


# def reConnBroker():  # MQTT Broker 重新連線程序
#     print("Connecting to", MQTT_BROKER, end="...")
#     if(mqtt.connBroker(MQTT_BROKER, PORT, MQTT_USERNAME, MQTT_PASSWORD, mqtt_id="ICSHOP_AM7020_MQTT_ID")):
#         print(" success")
#         print("subscribe: ", LED_TOPIC, end="")
#         if(mqtt.subscribe(LED_TOPIC, mqttCallback)):
#             print(" success")
#         else:
#             print(" fail")
#     else:
#         print(" fail")

# MQTT 訂閱內容訊息回呼函數





chk_net_timer = 0  # 連線狀態查詢週期計時器
pub_data_timer = 0  # 訊息發布週期計時器
print("Initializing modem...")
while(not nb.init()):
    print(".")

while(True):
    if(not nb.chkNet()):
        print("ISP Connecting")
        nbConnect()
        print("ISP Connected")
    print("working")

        # if(not mqtt.chkConnBroker()):
        #     oled.fill(0)  # 清除畫面
        #     oled.text("MQTT Connecting", 0, 0)
        #     oled.show()
        #     reConnBroker()
        #     oled.fill(0)  # 清除畫面
        #     oled.text("MQTT Connected", 0, 0)
        #     oled.show()

    # if(ticks_ms() > pub_data_timer):  # 訊息發布週期
    #     pub_data_timer = pub_data_timer + UPLOAD_INTERVAL_MS
    #     print("publish: ", t, end="")
    #     if(mqtt.publish(TEMP_TOPIC, str(t))):
    #         print(" success")
    #     else:
    #         print(" Fail")
    #     print("publish: ", h, end="")
    #     if(mqtt.publish(HUM_TOPIC, str(h))):
    #         print(" success")
    #     else:
    #         print(" Fail")
    # mqtt.procSubs()  # 檢查訂閱頻道狀態
    # oled.text("MQTT Connected", 0, 0)
    # # 加入文字內容
    # oled.text("Temp: ", 0, 10)
    # oled.text(str(t), 50, 10)
    # oled.text("*C", 90, 10)

    # oled.text("Humi: ", 0, 20)
    # oled.text(str(h), 50, 20)
    # oled.text("%", 90, 20)
    # oled.show()  # 顯示繪製內容
