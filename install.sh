pip3 install -r requirements.txt
cp bot_coin.service /etc/systemd/system/bot_coin.service
systemctl start bot_coin.service 
