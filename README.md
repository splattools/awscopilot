# awscopilot

前提として実行するのは適切なロールが付与された、publicサブネット上のEC2であること。


### 導入手順
```
sudo dnf install -y git
sudo dnf install -y docker
sudo systemctl start docker
sudo gpasswd -a $(whoami) docker
sudo chgrp docker /var/run/docker.sock
sudo service docker restart
sudo systemctl enable docker

sudo curl -L "https://github.com/docker/compose/releases/download/v2.32.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

curl -Lo copilot https://github.com/aws/copilot-cli/releases/latest/download/copilot-linux
chmod +x copilot
sudo mv copilot /usr/local/bin/copilot
```

### 動作確認

```
git clone https://github.com/splattools/awscopilot.git
cd awscopilot
docker-compose up -d
curl localhost
```

from flask!と表示されること