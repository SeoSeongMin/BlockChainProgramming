# 지갑 주소 발급
```
!node src/getMyAddr.js
```
#### 출력
[
  'A,
  'B,
  .....,
]

------------------------------------------------

# 1단계 컨트랙 개발
```
%%writefile src/'SAVE_NAME'.sol
pragma solidity 0.4.25;

contract '클래스'{
    '변수 선언'
    
    function '함수명'('유닛타입' '변수명') public{
        '변수' = '변수 값';
    }
    function '함수명2'('유닛타입2' '변수명2') public returns('유닛타입2'){
        return 값;
    }
    function '함수명3'() view public returns('유닛타입2'){ //함수명3선언시 함수명3 리턴값 호출
        return 값;
    }
}
```

----------------------------------------------

# 2단계 컴파일
```
!solc --abi --bin --gas src/'SAVE_NAME'.sol
```
#### 출력
```
# Binary: 123987123987123987 ~~~~
# Contract JSON ABI : [{"constant":false,"inputs":[{"name":"_greeting","type":"bytes32"}] ~~~~ }]
# Gas estimation ~~~
```

------------------------------------------------

# 3단계 배포
```
%%writefile src/'SAVE_NAME_Deploy'.js

var Web3 = require('web3');
var web3;

if (typeof web3 !== 'undefined') {
    web3 = new Web3(web3.currentProvider);
} else {
    web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
}

var _abi = [{"constant":false,"inputs":[{"name":"_greeting","type":"bytes32"}] ~~~~ }];
var _bin = "123987123987123987 ~~~~";
var _contract = new web3.eth.Contract(_abi);

_contract
    .deploy({ data: "0x"+_bin })
    .send({
     from: 'A(지갑 첫 번째 주소)',
     gas: '1000000'
    })
    .then(function(newContractInstance){
        console.log("contract address: "+newContractInstance.options.address)
    });
```
```
!node src/'SAVE_NAME_Deploy'.js
```
#### 출력
```
0xE4c0....
```

--------------------------------------------------

# 4단계 사용
```
%%writefile src/'SAVE_NAME_USE'.js
var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));

var _abi = [{"constant":false,"inputs":[{"name":"_greeting","type":"bytes32"}] ~~~~ }];
var 변수명 = new web3.eth.Contract(_abi, "0xE4c0....(배포에서 얻은 지갑)");


var str = web3.utils.toHex("Hello World!");

변수명.methods.함수명(str).send({from: "A(첫 번째 지갑에서 얻은 주소", gas: 1000000});
변수명.methods.함수명3().call().then(function(value) { console.log(web3.utils.hexToUtf8(value)); });  
변수명.methods.함수명().call().then(function(value) { console.log(value)});
```
