.PHONY: install
install:
	pip3 install -r requirements.txt
	cp bot.service /etc/systemd/system/bot_coin.service
	systemctl daemon-reload

.PHONY: restart
restart:
	systemctl stop bot_coin.service
	systemctl start bot_coin.service

.PHONY: status
status:
	systemctl status bot_coin.service

.PHONY: stop
stop:
	systemctl stop bot_coin.service