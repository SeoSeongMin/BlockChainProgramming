```python
pip install bitcoin #필요 라이브러리
```

    ------------------------------------------  
    ############ Hello, Seo Shell! ##############
    ------------------------------------------
    Collecting bitcoin
      Using cached bitcoin-1.1.42.tar.gz (36 kB)
    Building wheels for collected packages: bitcoin
      Building wheel for bitcoin (setup.py): started
      Building wheel for bitcoin (setup.py): finished with status 'done'
      Created wheel for bitcoin: filename=bitcoin-1.1.42-py3-none-any.whl size=44410 sha256=d7f39942c187b86df352fc7e1c96412a4f8e65059d14ff17dd56f5079b321852
      Stored in directory: c:\users\tjtjd\appdata\local\pip\cache\wheels\2d\12\38\7f9a9052a6b622b88ede09f2479471c3402312fafa03de7d88
    Successfully built bitcoin
    Installing collected packages: bitcoin
    Successfully installed bitcoin-1.1.42
    Note: you may need to restart the kernel to use updated packages.
    

## Private key 생성


```python
import bitcoin
privKey = bitcoin.sha256("hello key")
print(privKey)
```

    3e295c8dc78fb7f3865067dfc42fe845263db7661296e7e32e3a37baa1a27a7b
    


```python
import hashlib
privKey = hashlib.sha256("hello key".encode('utf-8')).hexdigest()
print(privKey)
```

    3e295c8dc78fb7f3865067dfc42fe845263db7661296e7e32e3a37baa1a27a7b
    

## Public key 생성


```python
pubKey = bitcoin.privtopub(privKey)
print(pubKey)
```

    04f6cc26cec156c180f8a215cf54db7799d0d42179f1e0b628cf364f09da95f17d5aab7edeeb1f529137a241d07cec555b2d8ec44a4cd24e87cf98001d428f564f
    

## Public key에서 주소 생성


```python
addr = bitcoin.pubtoaddr(pubKey)
print(addr)
```

    1NthZ9kJVbtxrHQiocfjLLTcMH3F2DLcgD
    

## nonce 값


```python
!geth --exec "eth.getTransactionCount(eth.accounts[0])" attach http://localhost:8445
```

    ------------------------------------------  
    ############ Hello, Seo Shell! ##############
    ------------------------------------------
    22
    
