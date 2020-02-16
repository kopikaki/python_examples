import paho.mqtt.publish as publish

topic = "test"
payload = "hello from python"
hostname = "mqtttcp-mq01.d1.zetez.com"
port = 15827

publish.single(topic, payload=payload, hostname=hostname, port=port, transport="tcp")



