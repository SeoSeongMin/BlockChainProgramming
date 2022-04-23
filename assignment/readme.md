# 기본 명령어
## 접속
### geth 콘솔 접속
```
from web3 import Web3
import json

url = 'http://localhost:8445' 
web3 = Web3(Web3.HTTPProvider(url))
```
### geth접속 / ganachi접속
```
geth attach http:localhost:8445
geth attach http:localhost:8435
```

--------------------------

### 계정
* 생성 
```
!geth --exec "personal.newAccount('12345')" attach http://localhost:8445
```

* 계정확인
```
web3.eth.accounts
web3.eth.accounts[?]
!geth --exec web3.personal.listAccounts attach http://localhost:8445
```

* 잔고확인 (Wei)
```
web3.eth.get_balance(web3.eth.accounts[?])
!geth --exec web3.eth.getBalance(eth.accounts[?]) attach http://localhost:8445
```

* 잔고확인 (ether)
```
amount = web3.fromWei(web3.eth.get_balance(web3.eth.accounts[?]), 'ether')
print(account, ':', amount, 'ether')
```

--------------------------

### Coinbase(주계정)
* Coinbase(주계좌) 확인
``` 
web3.eth.coinbase
```

* Coinbase 바꾸기
```
!geth --exec "miner.setEtherbase(eth.accounts[?])" attach http://localhost:8445
```

---------------------------

### Mining (마이닝)
* 충전
```
!geth --exec "miner.start(1);admin.sleepBlocks(5);miner.stop()" attach http://localhost:8445
```

* 블록번호 출력
```
web3.eth.blockNumber
```

--------------------------

### Miner commands
* Hash Rate 구하기
```
!geth --exec "miner.getHashrate()" attach http://localhost:8445
```

-------------------------

### Txpool
* transaction pool 상황 출력
```
!geth --exec "txpool.inspect" attach http://localhost:8445
```

* transaction pool 개수 출력
```
!geth --exec "txpool.status" attach http://localhost:8445
```

-----------------------

### 상세사항
* enode 출력
```
!geth --exec admin.nodeInfo.enode attach http://localhost:8445
```

* peer 여부
```
web3.net.listening
```

* peer 개수
```
web3.net.peerCount
```

-------------------------------

### 트랜잭션
* 대기하는 트랜잭션 수
```
!geth --exec "eth.pendingTransactions" attach http://localhost:8445
```

* 트랜잭션 횟수
```
!geth --exec "eth.getTransactionCount(eth.coinbase)" attach http://localhost:8445
```

--------------------------------

### secp256k1
* private key
```
import secrets
import pycoin.ecdsa as ecdsa

privKey = secrets.randbelow(ecdsa.generator_secp256k1.order())
print("private key: ", privKey)
print("private key in hex: ", hex(privKey))
```

* public Key
```
pubKey = (ecdsa.generator_secp256k1 * privKey).pair()
print("pubKey: ", pubKey)
```

* sign
```
import hashlib
import codecs

msg = "let's meet in my office at 10 in the morning."
hashByte = hashlib.sha3_256(msg.encode("utf8")).digest()
msgHash = int.from_bytes(hashByte, byteorder="big")
signature = ecdsa.sign(ecdsa.generator_secp256k1,privKey,msgHash)
print("signature", signature)
```

* verify
```
valid = ecdsa.verify(ecdsa.generator_secp256k1, pubKey, msgHash,signature)
print("valid: ", valid)
```

----------------


