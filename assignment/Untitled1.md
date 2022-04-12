# 하기전 서버 실행

# 서버 한대 열고
201710933 > _gethNow.bat

# 연결하고
201710933 > geth attach http://localhost:8445
# ganache 서버 열기
201710933 > _ganacheNow.bat
# ganache 연결
201710933 > node
> var Web3 = require('web3');

> var web3 = new Web3('http://localhost:8345');

# ---------------------------------------------------------------

# 서버 -> note book 차이
* eth.accounts[0] => web3.eth.accounts[0]
* console.log => print
* var A = ~ => A = ~

* 파이썬에서 서버로 직접 연결해서 서버 코드 그대로 쓸때는

!geth --exec '서버코드' attach http://localhost:8445

## 설치 파일


```python
pip install web3
```


```python
pip install ecdsa
```

## 8445 노드에 접속


```python
from web3 import Web3
import json

url = 'http://localhost:8445' 
web3 = Web3(Web3.HTTPProvider(url)) #해당 노드에 접속 
```


```python
#jslint devel: true
primary = web3.eth.accounts[0]
bal = web3.eth.getBalance(primary)

print("balance in Wei: ",bal) #Wei 출력
print("balance in ether", web3.fromWei(bal,"ether")) #Wei를 ether로
print("blocknumber: ", web3.eth.blockNumber) #blocknumber 수
print("coinbase: ", web3.eth.coinbase) #코인베이스의 지갑계좌
```

    balance in Wei:  469999999999999970000
    balance in ether 469.99999999999997
    blocknumber:  208
    coinbase:  0x60c0Ca8790e0177B4aEDbD37a4079bCa28e41375
    

## 현재 peer 노드의 수 확인하기


```python
print('peer count: ', web3.net.peerCount) #노드수 찾기
print('net.listening: ', web3.net.listening)# peer 찾고 있는 중인지?
```

    peer count:  0
    net.listening:  True
    

## nonce 값 구하기


```python
web3.eth.getTransactionCount(web3.eth.accounts[0])
```




    0



## Hash rate


```python
!geth --exec "miner.getHashrate()" attach http://localhost:8445
```

    0
    

## 계좌확인하기


```python
!geth --exec "eth.accounts" attach http://localhost:8445 #서버코드로 직접
```

    ["0x60c0ca8790e0177b4aedbd37a4079bca28e41375", "0x2c647c0376a1123d89d07a4fa494acd44b3d2975", "0x474c4efb8e4b7fbbf2642029f1825898a2c3fa54", "0x1dad809e9812e5c4bf22445241cb6c434243c952"]
    


```python
web3.eth.accounts #파이썬에서 작성
```




    ['0x60c0Ca8790e0177B4aEDbD37a4079bCa28e41375',
     '0x2c647C0376A1123D89D07a4FA494ACd44B3d2975',
     '0x474c4eFB8E4B7fBbf2642029F1825898A2C3Fa54',
     '0x1daD809E9812E5c4bF22445241cB6c434243C952']



## 계정생성하기


```python
web3.personal.newAccount('12345') #파이썬에서 진행안되면 !geth이용!
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-34-ac47dfecae95> in <module>
    ----> 1 web3.personal.newAccount('12345')
    

    AttributeError: 'Web3' object has no attribute 'personal'



```python
!geth --exec "personal.newAccount('12345')" attach http://localhost:8445 #서버 코드로 하니 적용
        
web3.eth.accounts #하나 더 만들어짐
```

    "0xd66e3df975c2599b98f607e49c48954bf1beb3d8"
    

## coinbase로 정하기, 바꾸기


```python
web3.eth.coinbase
web.miner.setEtherbase(eth.accounts[1]) #안되니까 서버 코드로!!
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-39-6b0490f18ae6> in <module>
          1 web3.eth.coinbase
    ----> 2 web.miner.setEtherbase(eth.accounts[1])
    

    NameError: name 'web' is not defined



```python
!geth --exec "eth.coinbase" attach http://localhost:8445 #주계좌확인
!geth --exec "miner.setEtherbase(eth.accounts[1])" attach http://localhost:8445 #1번계좌로 coinbase변경

!geth --exec "eth.coinbase" attach http://localhost:8445 #1번계좌로 바꼈다! 다시 원래대로 돌려놓자.
!geth --exec "miner.setEtherbase(eth.accounts[0])" attach http://localhost:8445 #1번계좌로 coinbase변경
        
web3.eth.coinbase
```

    "0x60c0ca8790e0177b4aedbd37a4079bca28e41375"
    true
    "0x2c647c0376a1123d89d07a4fa494acd44b3d2975"
    true
    




    '0x60c0Ca8790e0177B4aEDbD37a4079bCa28e41375'



# 문제 : 마이닝 해보기
### 1건만 마이닝 하기 (채굴하기)


```python
!geth --exec "miner.start(1);admin.sleepBlocks(1);miner.stop()" attach http://localhost:8445
```

    null
    

# 문제 : 정리

### 1. 계정 생성 (2개)


```python
!geth --exec "personal.newAccount('12345')" attach http://localhost:8445
!geth --exec "personal.newAccount('12345')" attach http://localhost:8445

web3.eth.accounts #확인
```

### 2. 5ether 이상 충전


```python
!geth --exec "miner.setEtherbase(eth.accounts[A])" attach http://localhost:8445 #첫 번째 만든걸로 주 계쫘
!geth --exec "miner.start(1);admin.sleepBlocks(5);miner.stop()" attach http://localhost:8445 #조금 충전

!geth --exec "miner.setEtherbase(eth.accounts[B])" attach http://localhost:8445 #두 번째 만든걸로 주 계쫘
!geth --exec "miner.start(1);admin.sleepBlocks(5);miner.stop()" attach http://localhost:8445 #조금 충전
        
!geth --exec "miner.setEtherbase(eth.accounts[0])" attach http://localhost:8445 #다시 원래 계좌로 
```

### 3. 현재 블록 번호를 출력


```python
web3.eth.blockNumber
#!geth --exec "eth.blockNumber" attach http://localhost:8445
```

    205
    

### 4. 자신의 enode값을 출력


```python
!geth --exec admin.nodeInfo attach http://localhost:8445
```

    {
      enode: "enode://6a10dc58d69a6cd3ceadcb3fc7afe9ff1aaf473b81b5d870b1516846718f0fca12a23b940fb3eb492f1eca908c9a10e587123b0e7d48057d3343bb3f3582fbae@175.211.75.208:38445",
      enr: "0xf89cb8403834d3c54847adf953e3ab920c5061a0d4068cc33c41e91c92e5cffee8a707777db134f90869f16d8ea320af52fca28a3cfd6575e31ceec1b28e6b2e86ed5cb50b83636170ccc5836574683ec5836574683f82696482763482697084afd34bd089736563703235366b31a1026a10dc58d69a6cd3ceadcb3fc7afe9ff1aaf473b81b5d870b1516846718f0fca8374637082962d8375647082962d",
      id: "775e937404733f82cda5e987e469fe9f6ca102ad04d90302d9474d0e202a79f3",
      ip: "175.211.75.208",
      listenAddr: "[::]:38445",
      name: "Geth/tjtjd/v1.8.20-stable-24d727b6/windows-amd64/go1.11.2",
      ports: {
        discovery: 38445,
        listener: 38445
      },
      protocols: {
        eth: {
          config: {
            chainId: 33,
            eip150Block: 0,
            eip150Hash: "0x0000000000000000000000000000000000000000000000000000000000000000",
            eip155Block: 0,
            eip158Block: 0,
            homesteadBlock: 0
          },
          difficulty: 27490761,
          genesis: "0x5704d029fe80f4fb605c0cb5e31d591511f10a46a0cb8166f97d8d559f9bc5b0",
          head: "0xa8f8a91354d6b7707d40ef09f0278fc2d4c803f333cf731c93492da677671006",
          network: 33
        }
      }
    }
    

### 5. peer가 있는지? 있으면 그 peer을 출력


```python
print(web3.net.listening) # peer 있는가?
print(web3.net.peerCount) #peer 개수는?
```

    True
    0
    

### 6. 계정 목록을 출력


```python
print(web3.eth.accounts)
!geth --exec "personal.listAccounts" attach http://localhost:8445
```

    ['0x60c0Ca8790e0177B4aEDbD37a4079bCa28e41375', '0x2c647C0376A1123D89D07a4FA494ACd44B3d2975', '0x474c4eFB8E4B7fBbf2642029F1825898A2C3Fa54', '0x1daD809E9812E5c4bF22445241cB6c434243C952', '0xD66E3Df975c2599b98f607E49c48954bF1Beb3d8']
    ["0x60c0ca8790e0177b4aedbd37a4079bca28e41375", "0x2c647c0376a1123d89d07a4fa494acd44b3d2975", "0x474c4efb8e4b7fbbf2642029f1825898a2c3fa54", "0x1dad809e9812e5c4bf22445241cb6c434243c952", "0xd66e3df975c2599b98f607e49c48954bf1beb3d8"]
    

### 7. 각 계정의 잔액을 ether 로 출력


```python
for account in web3.eth.accounts:
    amount = web3.eth.get_balance(account) #Wei를 이더로
    amount = web3.fromWei(amount, 'ether')
    print(account, ':', amount, 'ether')
    
#!geth --exec "web3.fromWei(eth.getBalance(eth.accounts[0]), 'ether')" attach http://localhost:8445
```

    0x60c0Ca8790e0177B4aEDbD37a4079bCa28e41375 : 469.99999999999997 ether
    0x2c647C0376A1123D89D07a4FA494ACd44B3d2975 : 285.00000000000003 ether
    0x474c4eFB8E4B7fBbf2642029F1825898A2C3Fa54 : 285 ether
    0x1daD809E9812E5c4bF22445241cB6c434243C952 : 0 ether
    0xD66E3Df975c2599b98f607E49c48954bF1Beb3d8 : 0 ether
    

### 8. 코인베이스를 2번째로 변경하고, 변경 전과 변경 후의 coinbase를 출력


```python
!geth --exec "eth.coinbase" attach http://localhost:8445

!geth --exec "miner.setEtherbase(eth.accounts[2])" attach http://localhost:8445 #바꾸고
!geth --exec "eth.coinbase" attach http://localhost:8445
        
!geth --exec "miner.setEtherbase(eth.accounts[0])" attach http://localhost:8445 #원래대로
!geth --exec "eth.coinbase" attach http://localhost:8445        
```

    "0x474c4efb8e4b7fbbf2642029f1825898a2c3fa54"
    true
    "0x474c4efb8e4b7fbbf2642029f1825898a2c3fa54"
    true
    "0x60c0ca8790e0177b4aedbd37a4079bca28e41375"
    

### 9. 현재 대기하는 트랜잭션 수를 출력


```python
!geth --exec "eth.pendingTransactions" attach http://localhost:8445
```

    []
    

# 연습문제
## Hash

* (원본) "The Japanese acted without the consent of his Majesty the Emperor of Korea."
* (위조) "The Japanese acted with the consent of his Majesty the Emperor of Korea."

### 1) 원본을 해싱하고 출력


```python
import hashlib
import codecs

msg = "The Japanese acted without the consent of his Majesty the Emperor of Korea."
hashBytes = hashlib.sha256(msg.encode("utf-8")).digest()#바이트형식
print("Hashing : ", hashBytes)
```

    Hashing :  b'\x1b\xb1\xde\x8ew"\xd2\xd8\xaf\x05\xc65l\x9fo\x08F\xe7\xbch\xd4\xab\x1d\xe4\x9eO\xfa\x99C\x08v\x9e'
    

### 2) 위조를 해싱하고 출력


```python
msg2 = "The Japanese acted with the consent of his Majesty the Emperor of Korea."
hashBytes2 = hashlib.sha256(msg2.encode("utf-8")).digest() #바이트형식
print("Hashing : ", hashBytes2)
```

    Hashing :  b'\xbb!\x03\xf4\xa1#\x0eZ\x1b\x19\x8f\x84]\xa9\xf3,z\x82\xf8\xe70\xc8\x8c"\x0c\xeb\xefg}s\x17\xa9'
    

### 3) 원본과 위조에서 구한 해시의 바이트 수, 차이를 출력


```python
origin = hashlib.sha256(msg.encode()).digest_size
change = hashlib.sha256(msg2.encode()).digest_size
print("원본 : ",origin," 위조 : ",change) #왜 같은가...? 각각 3글짜가 차이나는데..
print("해시의 차이는 ", origin - change)
```

    원본 :  32  위조 :  32
    해시의 차이는  0
    

### 4. 1번을 사인해서 인증결과를 출력


```python
#개인키 private Key
from ecdsa import SigningKey, SECP256k1
import sha3
import secrets
import pycoin.ecdsa as ecdsa

privKey = secrets.randbelow(secp256k1_generator.order())# 무작위수를 생성하는 모듈 randbelow()
print("private key: ", privKey)
print("private key in hex: ", hex(privKey))
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-77-562b5f753517> in <module>
          5 import pycoin.ecdsa as ecdsa
          6 
    ----> 7 privKey = secrets.randbelow(secp256k1_generator.order())# 무작위수를 생성하는 모듈 randbelow()
          8 print("private key: ", privKey)
          9 print("private key in hex: ", hex(privKey))
    

    NameError: name 'secp256k1_generator' is not defined



```python
#공중키 Public Key
# secp256k1 시작점와 privKey의 곱셈 연산에서 pubKey를 구한다.
pubKey = (secp256k1_generator * privKey)
print("pubKey: ", pubKey)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-70-5f999cf12b41> in <module>
          1 #공중키 Public Key
          2 # secp256k1 시작점와 privKey의 곱셈 연산에서 pubKey를 구한다.
    ----> 3 pubKey = (secp256k1_generator * privKey)
          4 print("pubKey: ", pubKey)
    

    NameError: name 'secp256k1_generator' is not defined



```python
#사인
import hashlib
import codecs
import hashlib, secrets
import numpy as np


msgHash=int.from_bytes(hashBytes, byteorder="big") # was working for python3
signature = web3.eth.account.signHash(hashBytes,private_key = privKey)


#signature=ecdsa.sign(ecdsa.generator_secp256k1,privKey,msgHash)
print("signature: ", signature)
```

    signature:  SignedMessage(messageHash=HexBytes('0x1bb1de8e7722d2d8af05c6356c9f6f0846e7bc68d4ab1de49e4ffa994308769e'), r=44121059455197967568466001603228221518274469400355257968096180158644956937827, s=24689206568327511827881137802282272476507832477240896387335495608050474060601, v=28, signature=HexBytes('0x618ba27b0f87395eac51006baba0e4b8ac04933dafffb029ab7b55602f5fbe6336959880969c9797fa000f272c20654d05957475057c0cb8653f89933c108b391c'))
    


```python
# 인증
#실패
```

# Chapter 5. 블록체인의 거래 연결

### 머클루트 Merkle Root 구하기


```python
import hashlib

txA = "Hello"
txB = 'How are you?'
txC = 'This is Thursday'
txD = 'Happy new Year'
```

### 해싱


```python
"Hello".encode() #encode()는 문자열을 바이트문자열려 변환
```




    b'Hello'



### 더블 해싱


```python
_hashA = hashlib.sha256(hashlib.sha256(txA.encode()).digest()).hexdigest()
_hashB = hashlib.sha256(hashlib.sha256(txB.encode()).digest()).hexdigest()
```

### 바이트 형식, 16진수 형식 출력


```python
print(hashlib.sha256(txA.encode()).digest())
print(hashlib.sha256(txA.encode()).hexdigest())
```

    b'\x18_\x8d\xb3"q\xfe%\xf5a\xa6\xfc\x93\x8b.&C\x06\xec0N\xdaQ\x80\x07\xd1vH&8\x19i'
    185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
    

### 바이트 교환


```python
print(_hashA)

for i in range(0, hashlib.sha256(txA.encode()).digest_size*2,2):
    print(_hashA[i:i+2], end=" ")
```

    70bc18bef5ae66b72d1995f8db90a583a60d77b4066e4653f1cead613025861c
    70 bc 18 be f5 ae 66 b7 2d 19 95 f8 db 90 a5 83 a6 0d 77 b4 06 6e 46 53 f1 ce ad 61 30 25 86 1c 

### 전체 크기 구하기


```python
hashlib.sha256(txA.encode()).digest_size
```




    32



### 리버스


```python
hashAswap="".join(reversed([_hashA[i:i+2] for i in range(0, hashlib.sha256(txA.encode()).digest_size*2, 2)]))
hashBswap="".join(reversed([_hashB[i:i+2] for i in range(0, hashlib.sha256(txB.encode()).digest_size*2, 2)]))
```

### 해싱 결합


```python
hashAB=hashAswap+hashBswap
```

### 더블해싱


```python
_hashAB=hashlib.sha256(hashlib.sha256(hashAB.encode()).digest()).hexdigest()
```

## 더블해싱의 바이트 교환


```python
hashABswap="".join(reversed([_hashAB[i:i+2] for i in range(0, 32*2, 2)]))
```

## 해싱 - 바이트교환 함수


```python
def doubleHashByteSwap(raw):
    import hashlib
    size=hashlib.sha256(raw.encode()).digest_size
    _hash=hashlib.sha256(hashlib.sha256(raw.encode()).digest()).hexdigest()
    hashSwap="".join(reversed([_hash[i:i+2] for i in range(0, size*2, 2)]))
    return hashSwap

hA=doubleHashByteSwap(txA)
hB=doubleHashByteSwap(txB)
hAB=doubleHashByteSwap(hA+hB)

print("hashA: {0}\nhashB: {1}\nhashAB: {2}".format(hA, hB, hAB))
```

    hashA: 1c86253061adcef153466e06b4770da683a590dbf895192db766aef5be18bc70
    hashB: d0e7719d7633fb945d596090dfa31a95ae81b18d90352d63fc49af7f35ce2710
    hashAB: 032916ba0fc9c63fc5440a3b20069370da1b5d3c605797b28ac1a5a5876dc7e0
    

# 마이닝


```python
import hashlib
ntry=1
found=False
blockNumber=54 # hex
NONCE=0
data='Hello'
previousHash='5d7c7ba21cbbcd75d14800b100252d5b428e5b1213d27c385bc141ca6b47989e'
while found==False:
    z=str(blockNumber)+str(NONCE)+data+previousHash
    guessHash=hashlib.sha256(z.encode('utf-8')).hexdigest()
    if guessHash[:4]=='0000':
        found=True
    NONCE+=1
    if(NONCE%10000000==0):   #print guessHash every 10000000
        print("NONCE: ",NONCE, guessHash)
print("Solved ", "NONCE: ", NONCE, "guessHash: ", guessHash)
```

    Solved  NONCE:  94280 guessHash:  000043ce4a61d02bff0e68ba18a7daf448cb3b93691fdd4850f6cd3f85b7a13f
    

### gas 한도


```python
!geth --exec "eth.getBlock('latest').gasLimit" attach http://localhost:8445
```

    109856254
    

### gas 계산 (실행비용-execution costs)


```python
txdata = "606060405260405160808061067283398101604090815281516020830151918301516060909301519092905b42811161003457fe5b60008054600181016100468382610100565b916000"
#예제 데이터

def count_zero_bytes(data):#2자리씩 읽어서 0인지 아닌지 갯수를 산정한다.
    count = 0
    for i in range(0, len(data), 2):
        byte = data[i:i+2]
    if byte == "00":
        count += 1
    return count

def count_non_zero_bytes(data):
    return (len(data) / 2) - count_zero_bytes(data)

print("zero-bytes: {0}".format(count_zero_bytes(txdata)))
print("non-zero-bytes: {0}".format(count_non_zero_bytes(txdata)))
#1 * 4 + 73 * 68 = 실행비용
```

    zero-bytes: 1
    non-zero-bytes: 73.0
    

## 거래건수


```python
!geth --exec "eth.getTransactionCount('0x8078e6bc8e02e5853d3191f9b921c5aea8d7f631')" attach http://localhost:8345
```

    0
    


```python
!geth --exec "eth.getBlock('latest')" attach http://localhost:8345
```

    {
      baseFeePerGas: "0x3b9aca00",
      difficulty: 1,
      extraData: "0x",
      gasLimit: 30000000,
      gasUsed: 0,
      hash: "0xec7f4bc877a068f3fffbc98a333719e4d1c692b1bee9952d11364847c6bfe587",
      logsBloom: "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      miner: "0x0000000000000000000000000000000000000000",
      mixHash: "0x0000000000000000000000000000000000000000000000000000000000000000",
      nonce: "0x0000000000000000",
      number: 0,
      parentHash: "0x0000000000000000000000000000000000000000000000000000000000000000",
      receiptsRoot: "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      sha3Uncles: "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
      size: 514,
      stateRoot: "0x0f01c6aff92bd50f6247c97699136fc13171ddaa374036adbf321126ede5cbcb",
      timestamp: 1649671087,
      totalDifficulty: 1,
      transactions: [],
      transactionsRoot: "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      uncles: []
    }
    


```python
!geth --exec "eth.getBlock('latest')" attach http://localhost:8345
```

    {
      baseFeePerGas: "0x3b9aca00",
      difficulty: 1,
      extraData: "0x",
      gasLimit: 30000000,
      gasUsed: 0,
      hash: "0xec7f4bc877a068f3fffbc98a333719e4d1c692b1bee9952d11364847c6bfe587",
      logsBloom: "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      miner: "0x0000000000000000000000000000000000000000",
      mixHash: "0x0000000000000000000000000000000000000000000000000000000000000000",
      nonce: "0x0000000000000000",
      number: 0,
      parentHash: "0x0000000000000000000000000000000000000000000000000000000000000000",
      receiptsRoot: "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      sha3Uncles: "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
      size: 514,
      stateRoot: "0x0f01c6aff92bd50f6247c97699136fc13171ddaa374036adbf321126ede5cbcb",
      timestamp: 1649671087,
      totalDifficulty: 1,
      transactions: [],
      transactionsRoot: "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421",
      uncles: []
    }
    

# 연습문제

## 같은기계에서 다른 계정으로 송금, 전송하기


```python
%%writefile src/e_testTran.js
miner.setEtherbase(eth.accounts[0]);
console.log('coinbase',eth.coinbase);
var bal1 = eth.getBalance(eth.coinbase);
var bal2 = eth.getBalance(eth.accounts[1]);
console.log('sender balance in ether: ',web3.fromWei(bal1,"ether"));
console.log('receiver balance in ether: ',web3.fromWei(bal2,"ether"));
console.log('median gas price: ',eth.gasPrice);
console.log('block number: ',eth.blockNumber);
console.log("nonce(Transaction): ", eth.getTransactionCount(eth.coinbase));

eth.sendTransaction({from:eth.coinbase, to:eth.accounts[1],value:10000});
console.log('...mining start');
miner.start(1);admin.sleepBlocks(1);miner.stop();
console.log('mining done...');

var bal1new=eth.getBalance(eth.coinbase);
var bal2new=eth.getBalance(eth.accounts[1]);
console.log('- new sender balance in ether: ', web3.fromWei(bal1new,"ether"));
console.log('- new receiver balance in ether: ', web3.fromWei(bal2new,"ether"));
console.log('- block number: ', eth.blockNumber);
console.log('- transaction count: ', eth.getTransactionCount(eth.coinbase));


```

    Overwriting src/e_testTran.js
    

12: from 주계좌 코인베이스에서 to 계좌 1번으로 10000만큼 전송한다.

14 코인베이스에서 1만큼 마이닝하고 중지한다.

아래 결과는 이 단위 기준으로는 1만큼 잘 이동됐다.

계좌가 잠겨있다면 personal.unlockAccount(eth.accounts[0]) #코인베이스 계좌 풀기


```python
!geth --exec "loadScript('src/e_testTran.js')" attach http://localhost:8445
```

    coinbase 0x60c0ca8790e0177b4aedbd37a4079bca28e41375
    sender balance in ether:  464.99999999999998
    receiver balance in ether:  285.00000000000002
    median gas price:  1000000000
    block number:  207
    nonce(Transaction):  2
    ...mining start
    mining done...
    - new sender balance in ether:  469.99999999999997
    - new receiver balance in ether:  285.00000000000003
    - block number:  208
    - transaction count:  3
    true
    

# gas비 계산 몰루
"Let's meet in my office at 10 AM."의 거래비용 gas를 계산하시오.


```python
txdata = "Let's meet in my office at 10 AM."

def count_zero_bytes(data):#2자리씩 읽어서 0인지 아닌지 갯수를 산정한다.
    count = 0
    for i in range(0, len(data), 2):
        byte = data[i:i+2]
    if byte == "00":
        count += 1
    return count

def count_non_zero_bytes(data):
    return (len(data) / 2) - count_zero_bytes(data)

print("zero-bytes: {0}".format(count_zero_bytes(txdata)))
print("non-zero-bytes: {0}".format(count_non_zero_bytes(txdata)))
#1 * 4 + 73 * 68 = 실행비용
```

    zero-bytes: 0
    non-zero-bytes: 16.5
    


```python

```

# Hash 맞추기
해시는 100미만의 양수로 정해진다고 하자.

NONCE는 반복회수로만 쓰이고 무작위 수를 생성하는데 입력되지는 않는다.

목표해시는 난이도에 따라 결정이 된다고 하자.

마이닝을 해서, 목표 해시를 찾아보자.

90을 목표해시로 정하고 몇 회만에 마이닝에 성공하는지 출력

10을 목표해시로 정하고 몇 회만에 마이닝에 성공하는지 출력


```python
import hashlib
import random

found = False
NONCE = 0

while found == False:
    guessHash = random.randint(1, 99)
    if (guessHash < 90):
        found = True
    NONCE += 1
    print("NONCE: ",NONCE, "guessHash: ",guessHash)
print("Solved NONCE: ", NONCE, "guessHash: ", guessHash)
print("90을 목표해시로 정했을 경우", NONCE, "회 만에 마이닝에 성공")
```

    NONCE:  1 guessHash:  38
    Solved NONCE:  1 guessHash:  38
    90을 목표해시로 정했을 경우 1 회 만에 마이닝에 성공
    


```python
found = False
NONCE = 0

while found == False:
    guessHash = random.randint(1, 99)
    if (guessHash < 10):
        found = True
    NONCE += 1
    print("NONCE: ",NONCE, "guessHash: ",guessHash)
print("Solved NONCE: ", NONCE, "guessHash: ", guessHash)
print("10을 목표해시로 정했을 경우", NONCE, "회 만에 마이닝에 성공")
```

    NONCE:  1 guessHash:  70
    NONCE:  2 guessHash:  98
    NONCE:  3 guessHash:  3
    Solved NONCE:  3 guessHash:  3
    10을 목표해시로 정했을 경우 3 회 만에 마이닝에 성공
    

# 블록헤더 데이터의 해시 값에 NONCE를 증가시키면서

앞 자리의 0의 개수를 맞출 때까지 반복한다.

### (1) 찾고자 하는 해시가 ```0000```로 시작한다고 하자. 몇 회만에 찾는지 출력하세요.




```python
import hashlib
ntry=1   #시도 횟수
found=False  #bollen type
blockNumber=54 # hex 임의
NONCE=0
data='Hello'
previousHash='5d7c7ba21cbbcd75d14800b100252d5b428e5b1213d27c385bc141ca6b47989e'
#이전 블록 헤더의 해쉬값
while found==False: #발견할 동안 Ture가 될 동안 반복
    z=str(blockNumber)+str(NONCE)+data+previousHash #1) 블록헤더
    guessHash=hashlib.sha256(z.encode('utf-8')).hexdigest()#2)재해싱
    if guessHash[:4]=='0000':#3) Target Hash와 비교
        found=True
    NONCE+=1 #안되면 난스값 하나 추가해서 다시 한번더
    if(NONCE%10000000==0):   #print guessHash every 10000000
        print("NONCE: ",NONCE, guessHash) #이 시기마다 한 번씩 추출력해서 확인
print("Solved ", "NONCE: ", NONCE, "guessHash: ", guessHash)
```

    Solved  NONCE:  94280 guessHash:  000043ce4a61d02bff0e68ba18a7daf448cb3b93691fdd4850f6cd3f85b7a13f
    

### (2) 찾고자 하는 해시가 ```00000```로 시작한다고 하자. 몇 회만에 찾는지 출력하세요.


```python
import hashlib
ntry=1
found=False
blockNumber=54 # hex
NONCE=0
data='Hello'
previousHash='5d7c7ba21cbbcd75d14800b100252d5b428e5b1213d27c385bc141ca6b47989e'
while found==False:
    z=str(blockNumber)+str(NONCE)+data+previousHash
    guessHash=hashlib.sha256(z.encode('utf-8')).hexdigest()
    if guessHash[:5]=='00000':
        found=True
    NONCE+=1
    if(NONCE%10000000==0):   #print guessHash every 10000000
        print("NONCE: ",NONCE, guessHash)
print("Solved ", "NONCE: ", NONCE, "guessHash: ", guessHash)
```

    Solved  NONCE:  315753 guessHash:  000007f9f69a43f1bb6ab92672d873b93d6bafaa2007e44b6151bd19efadf4d1
    

### (3) 찾고자 하는 해시가 ```000000```로 시작한다고 하자. 몇 회만에 찾는지 출력하세요.


```python
import hashlib
ntry=1
found=False
blockNumber=54 # hex
NONCE=0
data='Hello'
previousHash='5d7c7ba21cbbcd75d14800b100252d5b428e5b1213d27c385bc141ca6b47989e'
while found==False:
    z=str(blockNumber)+str(NONCE)+data+previousHash
    guessHash=hashlib.sha256(z.encode('utf-8')).hexdigest()
    if guessHash[:6]=='000000':
        found=True
    NONCE+=1
    if(NONCE%10000000==0):   #print guessHash every 10000000
        print("NONCE: ",NONCE, guessHash)
print("Solved ", "NONCE: ", NONCE, "guessHash: ", guessHash)
```

    NONCE:  10000000 660b9e057377381579f5c54347901cf462fce656c069a4d0f26bdd4cf1e05e66
    NONCE:  20000000 c31d3ddd7bb92312bcc2a88263d92e94c6d17a641ac9e59ac262c775c7f58925
    NONCE:  30000000 236077716f4ce428ec83f12bf74fb7ab76450bad60bc3f21d924e200c39a9fa4
    NONCE:  40000000 5b07929bd7088f11d6caf0e65a6f44ab3b7f82d32900430cc7c7244b2917e04d
    Solved  NONCE:  45576417 guessHash:  0000003d02b95604bb1ec436ff20e08168dd339f2ec0f9941bfc58bad039994e
    


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

# 수업 - Estimated gas

### 다시 시작할때마다 주소가 달라지므로 다시 해줘야한다.


```python
%%writefile src/HelloDeployGas.js
var Web3=require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
var shelloContract = new web3.eth.Contract([{"inputs":[],"name":"sayHello","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"}]);
shelloContract.deploy({
        //from: '0x4aae75084f715390Aad4a251DC70327AfEf8a03c',
        data: '0x608060405234801561001057600080fd5b50610139806100206000396000f3fe608060405234801561001057600080fd5b5060043610610048576000357c010000000000000000000000000000000000000000000000000000000090048063ef5fb05b1461004d575b600080fd5b6100556100d0565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561009557808201518184015260208101905061007a565b50505050905090810190601f1680156100c25780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b60606040805190810160405280600b81526020017f48656c6c6f20576f726c6400000000000000000000000000000000000000000081525090509056fea165627a7a72305820992c2f4c73a27b9eb53c6aa7b52ba8a5eddba258089eb7d1a3710711703459950029', 
    }).estimateGas().then(function(myGas) {
        console.log("Estimated gas: " + myGas);
        gas = myGas;
    })
    .catch(console.error);
```

    Overwriting src/HelloDeployGas.js
    


```python
!node src/HelloDeployGas.js
```

    Estimated gas: 120415
    

* gas를 산정하기 위해서 EstimateGas()를 구했다.


```python
%%writefile src/getMyAddr.js
var Web3=require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"))
var myAddr0;
web3.eth.getAccounts().then(console.log);
```

    Overwriting src/getMyAddr.js
    

* 3: web3 객체 만들기
* 5: 비동기 함수이므로 .then


```python
!node src/getMyAddr.js
```

    [
      '0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656',
      '0x79741bB50555F7049F1A45811c59ccBe5C4fe1F2',
      '0x5B9f5A556B76fd7d51696DA0d6702A28D0dcBede',
      '0x2a19fC15E489D3Ed2F36b4b161E7491f03369f11',
      '0x0f2B7a5FE7A68D6c5600458fc5dd064C865BBad7',
      '0xC8D81c558EDc203eD6634311a0e51412E4Edb65a',
      '0xcc1D7FCc0328813961f1A59c14553E855c31C9de',
      '0x836591E2a2e5CA3aF1Fd7567EA28E98ca85bC896',
      '0x430bA1eE9473225BCa6C02061f743c29985fb5c7',
      '0x856D9F57685241865fD0adF0B5E0cF2c56Ea4FCE'
    ]
    

## ganache 배포 web3 1.2


```python
%%writefile src/HelloDeploy.js
var Web3=require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
var shelloContract = new web3.eth.Contract([{"inputs":[],"name":"sayHello","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"}]);
shelloContract
    .deploy({
            data: '0x608060405234801561001057600080fd5b50610139806100206000396000f3fe608060405234801561001057600080fd5b5060043610610048576000357c010000000000000000000000000000000000000000000000000000000090048063ef5fb05b1461004d575b600080fd5b6100556100d0565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561009557808201518184015260208101905061007a565b50505050905090810190601f1680156100c25780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b60606040805190810160405280600b81526020017f48656c6c6f20576f726c6400000000000000000000000000000000000000000081525090509056fea165627a7a72305820992c2f4c73a27b9eb53c6aa7b52ba8a5eddba258089eb7d1a3710711703459950029', 
    })
    .send({
     from: "0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656",
     gas: '4700000'
    }, function (error, transactionHash){ 
            console.log(error, transactionHash); 
    })
    .then(function(newContractInstance){
        console.log(newContractInstance.options.address)
    });
```

    Overwriting src/HelloDeploy.js
    

* 4 : ABI정보가 들어간다. 중간중간에 object라는 말이 있을 수 있는데 Json형식이면 오류가 없고 String이면 오류가 난다. ABI는 항상 문자열인지 json인지 확인해라, abi는 항상 json이다.
* 7 : Ox 붙여아한다.(바이트 코드이므로 16진수,)
* 9 : 인자가 들어가 있고 . function ( callback)이 들어가 transactionHash를 호출한다.
* 10 : 아까 위에 떠블클릭한 내 주소 첫 번째 주소 입력
* gas는 생략해도 되고 적어줘도 되고
* send괄호는 14번째에서 끝난다. 이 안에는 {}괄호가 있는데 Json형태라는 뜻. 아! {}이니까 Json으로 인자가 넘어가는구나!
* 12: send에서 처리되면 transactionHash로 들어간다.
* 15: 출력은 then 함수에서!
* 즉 객체 만들고, delpoiy하고 (send함수니까 send함수로 보내고) then함수로 보내 출룍한다.



```python
!node src/HelloDeploy.js
```

    null 0xd912e915a2e7ca05568f6f7d691b5096943ca0321f27929a3a905b9c8a79f703
    0x2D5613308aFEa0D8DFb4A95D266246720c981af4
    

* 첫 번째 = Hash
* 두 번째 = 주소
* 배포의 최종 목적은 맨 마지막줄 주소를 얻기 위함

## geth 배포


```python
%%writefile src/HelloDeploy2.js
var Web3=require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8445"));
var shelloContract = new web3.eth.Contract([{"constant":true,"inputs":[],"name":"sayHello","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"pure","type":"function"}]);
shelloContract
    .deploy({
            data: '0x608060405234801561001057600080fd5b50610139806100206000396000f3fe608060405234801561001057600080fd5b5060043610610048576000357c010000000000000000000000000000000000000000000000000000000090048063ef5fb05b1461004d575b600080fd5b6100556100d0565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561009557808201518184015260208101905061007a565b50505050905090810190601f1680156100c25780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b60606040805190810160405280600b81526020017f48656c6c6f20576f726c6400000000000000000000000000000000000000000081525090509056fea165627a7a72305820992c2f4c73a27b9eb53c6aa7b52ba8a5eddba258089eb7d1a3710711703459950029', 
    })
    .send({
     from: "0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656",
     gas: '4700000'
    }, function (error, transactionHash){ 
            console.log(error, transactionHash); 
    })
    .on('transactionHash', function(error,transactionHash) {
        console.log("hash-- "+transactionHash);
    })
    .on('receipt', function(receipt) {
        console.log('receipt:: '+receipt.contractAddress);
    })
    .then(function(newContractInstance){
        console.log(newContractInstance.options.address)
    });
```

    Overwriting src/HelloDeploy2.js
    


```python
!node src/HelloDeploy2.js
```

    Error: Returned error: unknown account
        at Object.ErrorResponse (C:\Users\tjtjd\Code\201710933\node_modules\web3-core-helpers\src\errors.js:29:16)
        at C:\Users\tjtjd\Code\201710933\node_modules\web3-core-requestmanager\src\index.js:140:36
        at XMLHttpRequest.request.onreadystatechange (C:\Users\tjtjd\Code\201710933\node_modules\web3-providers-http\src\index.js:110:13)
        at XMLHttpRequestEventTarget.dispatchEvent (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request-event-target.js:34:22)
        at XMLHttpRequest._setReadyState (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:208:14)
        at XMLHttpRequest._onHttpResponseEnd (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:318:14)
        at IncomingMessage.<anonymous> (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:289:61)
        at IncomingMessage.emit (node:events:538:35)
        at endReadableNT (node:internal/streams/readable:1345:12)
        at processTicksAndRejections (node:internal/process/task_queues:83:21) undefined
    

    node:internal/process/promises:279
                triggerUncaughtException(err, true /* fromPromise */);
                ^
    
    Error: Returned error: unknown account
        at Object.ErrorResponse (C:\Users\tjtjd\Code\201710933\node_modules\web3-core-helpers\src\errors.js:29:16)
        at C:\Users\tjtjd\Code\201710933\node_modules\web3-core-requestmanager\src\index.js:140:36
        at XMLHttpRequest.request.onreadystatechange (C:\Users\tjtjd\Code\201710933\node_modules\web3-providers-http\src\index.js:110:13)
        at XMLHttpRequestEventTarget.dispatchEvent (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request-event-target.js:34:22)
        at XMLHttpRequest._setReadyState (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:208:14)
        at XMLHttpRequest._onHttpResponseEnd (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:318:14)
        at IncomingMessage.<anonymous> (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:289:61)
        at IncomingMessage.emit (node:events:538:35)
        at endReadableNT (node:internal/streams/readable:1345:12)
        at processTicksAndRejections (node:internal/process/task_queues:83:21)
    

web3.eth.personal.unlockAccount("0x778ea...","password",1000).then(console.log('unlocked!'));

계좌가 잠겨있다 위로 해체해주면 된다. 그냥 ganache를 이용하자

## 3.4 단계 4: 사용

컨트랙이 배포되고 위 처럼 주소를 얻었다.


```python
%%writefile src/Hello.sol
pragma solidity 0.4.25;
contract Hello {
    function sayHello() pure public returns(string memory) {
        return "Hello World";
    }
}
```

    Overwriting src/Hello.sol
    


```python
%%writefile src/HelloUse.js
var Web3=require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));

var shelloContract = new web3.eth.Contract([{"constant":true,"inputs":[],"name":"sayHello","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"pure","type":"function"}],
                                      "0x2D5613308aFEa0D8DFb4A95D266246720c981af4");
shelloContract.methods.sayHello().call().then(function(str) {console.log(str);});
```

    Overwriting src/HelloUse.js
    

* 5 : 위의 주소  배포해서 한 것 복사해서 넣는다.
* 6: 맨위에 sayHello()라는 함수를 호출해서 쓰는 것이다. (교과서 기준 맨위)
* 6: 위에서 배포된 2번째 계좌를 이용해서 넣어준다.
* send로 호출하면 저렇게 리턴이 안된다! 


```python
!node src/HelloUse.js
```

    Hello World
    

## 4. Greeter 디앱

데이터를 저장하는 컨트랙이며 256비트 당 20,000gas가 필요하다.

### 4.1 단계 1.컨트랙 개발


```python
%%writefile src/greeter.sol
pragma solidity ^0.4.25;

contract Greeter {
    string greeting;

    constructor() public {
        greeting = 'Hello';
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string memory) {
        return greeting;
    }
}
```

    Overwriting src/greeter.sol
    

## 4.2단계 2.컴파일


```python
!solc --abi src/greeter.sol
```

    
    ======= src/greeter.sol:Greeter =======
    Contract JSON ABI 
    [{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]
    


```python
!solc --bin src/greeter.sol
```

    
    ======= src/greeter.sol:Greeter =======
    Binary: 
    608060405234801561001057600080fd5b506040805190810160405280600681526020017f48656c6c6f3100000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b6102d7806101166000396000f30060806040526004361061004c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a413686214610051578063cfae3217146100ba575b600080fd5b34801561005d57600080fd5b506100b8600480360381019080803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919291929050505061014a565b005b3480156100c657600080fd5b506100cf610164565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561010f5780820151818401526020810190506100f4565b50505050905090810190601f16801561013c5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b8060009080519060200190610160929190610206565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156101fc5780601f106101d1576101008083540402835291602001916101fc565b820191906000526020600020905b8154815290600101906020018083116101df57829003601f168201915b5050505050905090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061024757805160ff1916838001178555610275565b82800160010185558215610275579182015b82811115610274578251825591602001919060010190610259565b5b5090506102829190610286565b5090565b6102a891905b808211156102a457600081600090555060010161028c565b5090565b905600a165627a7a723058209fa23c389e1bc231b5b2f76481dccbb76a5d709fd94a6817fe73afd9f7af1a880029
    


```python
!solc --gas src/greeter.sol
```

    
    ======= src/greeter.sol:Greeter =======
    Gas estimation:
    construction:
       infinite + 145400 = infinite
    external:
       greet():	infinite
       setGreeting(string):	infinite
    

### 4.3 단계 3. 컨트랙 배포


```python
%%writefile src/greeterDeploy.js
var Web3=require('web3');
var web3;
if (typeof web3 !== 'undefined') {
    web3 = new Web3(web3.currentProvider);
} else {
    web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
}
var _abiArray=[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}];
var _bin="608060405234801561001057600080fd5b506040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b610323806101166000396000f3fe608060405234801561001057600080fd5b5060043610610053576000357c010000000000000000000000000000000000000000000000000000000090048063a413686214610058578063cfae321714610113575b600080fd5b6101116004803603602081101561006e57600080fd5b810190808035906020019064010000000081111561008b57600080fd5b82018360208201111561009d57600080fd5b803590602001918460018302840111640100000000831117156100bf57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610196565b005b61011b6101b0565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561015b578082015181840152602081019050610140565b50505050905090810190601f1680156101885780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101ac929190610252565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102485780601f1061021d57610100808354040283529160200191610248565b820191906000526020600020905b81548152906001019060200180831161022b57829003601f168201915b5050505050905090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061029357805160ff19168380011785556102c1565b828001600101855582156102c1579182015b828111156102c05782518255916020019190600101906102a5565b5b5090506102ce91906102d2565b5090565b6102f491905b808211156102f05760008160009055506001016102d8565b5090565b9056fea165627a7a72305820e8cd5af384936c8c5f80781ebbc5ca63f8fa0e43133353c27accbb02ee216b550029";
var _contract = new web3.eth.Contract(_abiArray);
//unlock the account with a password provided
//web3.personal.unlockAccount(web3.eth.accounts[0],'password');
_contract
    .deploy({data:"0x"+_bin})
    .send({from: "0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656", gas: 364124, gasPrice: '1000000000'})
    .then(function(newContractInstance){
        console.log(newContractInstance.options.address) // instance with the new contract address
    });
```

    Overwriting src/greeterDeploy.js
    

* 16 : getMyAddr.js에서 구한 첫 번째 주소를 from에 넣어준다.


```python
!node src\greeterDeploy.js
```

    0x36a209cfb995C53bd9677F8d6038835DC8BF7312
    

### 4.4 단계 4.사용


```python
%%writefile src/greeterUse.js
var Web3=require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
var _abiArray=[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}];
var greeter = new web3.eth.Contract(_abiArray,"0x36a209cfb995C53bd9677F8d6038835DC8BF7312");
greeter.methods.greet().call().then(function(value) {console.log(value);});
greeter.methods.setGreeting("Hello SMU").send({from:"0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656",gas:100000});
greeter.methods.greet().call().then(function(value) {console.log(value);});
```

    Overwriting src/greeterUse.js
    

* 5: 바로 위 구한 주소를 넣어주고
* 7: 10개 주소중 첫 번째 주소를 넣어준다 (맨 처음에 구한)


```python
!node src/greeterUse.js
```

    Hello SMU
    Hello SMU
    

## 5. 간단한 계수기
### 5.1 컨트랙 개발


```python
%%writefile src/Counter.sol
pragma solidity ^0.4.25;
contract Counter {
    uint256 counter = 0;
    function add() public {
        counter++;
    }
    function subtract() public {
        counter--;
    }
    function getCounter() public view returns (uint256) {
        return counter;
    }
}
```

    Overwriting src/Counter.sol
    

### 5.2 컴파일

* abi, bin, gas값 컴파일을 통해 구하기


```python
!solc --abi --bin --gas src/Counter.sol
```

    
    ======= src/Counter.sol:Counter =======
    Gas estimation:
    construction:
       5111 + 52000 = 57111
    external:
       add():	20370
       getCounter():	446
       subtract():	20395
    Binary: 
    60806040526000805534801561001457600080fd5b50610104806100246000396000f3006080604052600436106053576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680634f2be91f1460585780636deebae314606c5780638ada066e146080575b600080fd5b348015606357600080fd5b50606a60a8565b005b348015607757600080fd5b50607e60bb565b005b348015608b57600080fd5b50609260cf565b6040518082815260200191505060405180910390f35b6000808154809291906001019190505550565b600080815480929190600190039190505550565b600080549050905600a165627a7a723058208d5ca8dde1f98947b438cdebbf2863aa12d2c0b873e7f3d4de3851c95a9cd5d60029
    Contract JSON ABI 
    [{"constant":false,"inputs":[],"name":"add","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"subtract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getCounter","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]
    

### 5.3단계 3.배포


```python
%%writefile src/counterDeploy.js
var Web3=require('web3');
var web3;
if (typeof web3 !== 'undefined') {
    web3 = new Web3(web3.currentProvider);
} else {
    web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
}
//solc 0.5.0
//var _abiArray=[{"constant":false,"inputs":[],"name":"add","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"subtract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getCounter","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}];
//var _bin="60806040526000805534801561001457600080fd5b5060e6806100236000396000f3fe6080604052348015600f57600080fd5b50600436106059576000357c0100000000000000000000000000000000000000000000000000000000900480634f2be91f14605e5780636deebae31460665780638ada066e14606e575b600080fd5b6064608a565b005b606c609d565b005b607460b1565b6040518082815260200191505060405180910390f35b6000808154809291906001019190505550565b600080815480929190600190039190505550565b6000805490509056fea165627a7a723058201fbaa288a76e68fea3b0373a390c6e375e9bb90c0fd24b0660d64ebb408088d60029";
//solc 0.6.1
var _abiArray=[{"inputs":[],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"subtract","outputs":[],"stateMutability":"nonpayable","type":"function"}];
var _bin="60806040526000805534801561001457600080fd5b5060d3806100236000396000f3fe6080604052348015600f57600080fd5b5060043610603c5760003560e01c80634f2be91f1460415780636deebae31460495780638ada066e146051575b600080fd5b6047606d565b005b604f6080565b005b60576094565b6040518082815260200191505060405180910390f35b6000808154809291906001019190505550565b600080815480929190600190039190505550565b6000805490509056fea2646970667358221220a19d7e0374295c3c6dd75807d6b2bb20a12deb6f736a4ad98c0065f0d9d4bf5764736f6c63430006010033";
var _contract = new web3.eth.Contract(_abiArray);
//unlock the account with a password provided
//web3.personal.unlockAccount(web3.eth.accounts[0],'password');
_contract
    .deploy({data:"0x"+_bin})
    .send({from: "0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656", gas: 364124, gasPrice: '1000000000'})
    .then(function(newContractInstance){
        console.log(newContractInstance.options.address) // instance with the new contract address
    });
```

    Overwriting src/counterDeploy.js
    

* 20: 첫 번째 10개중 주소를 가져온다.


```python
!node src/counterDeploy.js
```

    0x4179fC2e4B993E347EC3E47D63054DE0DE4d6e93
    

### 5.4 단계 4. 사용


```python
%%writefile src/counterUse.js
var Web3=require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
var abi =[{"constant":false,"inputs":[],"name":"add","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"subtract","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getCounter","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}];
var addr = "0x4179fC2e4B993E347EC3E47D63054DE0DE4d6e93";
var counter = new web3.eth.Contract(abi,addr);
counter.methods.getCounter().call().then(function(str) {console.log(str);});
//counter.methods.subtract().send({from:"0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656",gas:100000});
counter.methods.add().send({from:"0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656",gas:100000});
counter.methods.add().send({from:"0x729cC381CD3b0Ff6280f6A7Fcbaf9fC284344656",gas:100000});
counter.methods.getCounter().call().then(function(str) {console.log(str);});
```

    Overwriting src/counterUse.js
    

* 5: 배포된 주소
* 8~10: 원래 사용할 첫번째 계좌

* 8: subtract()를 통해 1만큼 빼는 상태변경이므로 마이닝을 해야 결과가 반영
* 9,10: add()를 통해 1만큼 증가.
* 11: 을 통해 변경된 counter수를 알 수 있다.


```python
!node src/counterUse.js
```

    4
    4
    

    C:\Users\tjtjd\Code\201710933\node_modules\web3-core-helpers\src\errors.js:29
            return new Error('Returned error: ' + message);
                   ^
    
    Error: Returned error: VM Exception while processing transaction: the tx doesn't have the correct nonce. account has nonce of: 41 tx has nonce of: 40 (vm hf=london -> block -> tx)
        at Object.ErrorResponse (C:\Users\tjtjd\Code\201710933\node_modules\web3-core-helpers\src\errors.js:29:16)
        at C:\Users\tjtjd\Code\201710933\node_modules\web3-core-requestmanager\src\index.js:140:36
        at XMLHttpRequest.request.onreadystatechange (C:\Users\tjtjd\Code\201710933\node_modules\web3-providers-http\src\index.js:110:13)
        at XMLHttpRequestEventTarget.dispatchEvent (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request-event-target.js:34:22)
        at XMLHttpRequest._setReadyState (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:208:14)
        at XMLHttpRequest._onHttpResponseEnd (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:318:14)
        at IncomingMessage.<anonymous> (C:\Users\tjtjd\Code\201710933\node_modules\xhr2-cookies\dist\xml-http-request.js:289:61)
        at IncomingMessage.emit (node:events:538:35)
        at endReadableNT (node:internal/streams/readable:1345:12)
        at processTicksAndRejections (node:internal/process/task_queues:83:21)
    


```python

```


```python

```
