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
    function '함수명2'('유닛타입2' '변수명2') public pure returns('유닛타입2'){
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

# 3단계 '노드'에서 배포 (+ ganache 배포 8345)
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

# 3단계 '노드'에서 배포  (+ ganache 배포 8345)
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
    }, function (e, transactionHash){
        console.log(e, transactionHash);
    })
    .then(function(newContractInstance){
        console.log("contract address: "+newContractInstance.options.address)
    });
```
# 3단계 Geth 배포
```
%%writefile src/timerDeploy-ganache2.js
var Web3 = require('web3');
var _abiBinJson = require('./Timer.json');     

var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));

contractName=Object.keys(_abiBinJson.contracts); 
console.log("- contract name: ", contractName);
_abi=_abiBinJson.contracts[contractName].abi;
_abiArray=JSON.parse(_abi);      //JSON parsing needed!!
_bin=_abiBinJson.contracts[contractName].bin;

console.log("- ABI: " + _abiArray);
console.log("- Bytecode: " + _bin);

async function deploy() {
    const accounts = await web3.eth.getAccounts();
    console.log("Deploying the contract from " + accounts[0]);
    var deployed = await new web3.eth.Contract(_abiArray)
        .deploy({data: "0x"+_bin})
        .send({from: accounts[0], gas: 364124}, function(err, transactionHash) {
                if(!err) console.log("hash: " + transactionHash); 
        })
        //.then(function(newContractInstance){
        //    console.log(newContractInstance)
        //});
    console.log("---> The contract deployed to: " + deployed.options.address)
}
deploy()
```

# 3단계 REMIX 배포
```
http://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.6.0+commit.26b70077.js
* 1. 파일버튼을 눌러 Timer.sol이라는 파일을 만들고 pragma ~부터 오른쪽에 붙여넣는다.
* 2. 왼쪽 solidy compile누르고 버전 0.4.25를 눌른다. 그후 compile Timer.sol을 누른다.
* 3. 왼쪽 아래 배포(deploy)를 누르고 'ENVIRONMENT'에서 JavaScript VM (London)을 누르고 Deploy를 누른다.
* 4. Deployed Contratcts 아래에 >TIMER AT ~~파일이 생긴다. 복사한다. 우리는
* 5. 0xd9145CCE52D386f254917e481eB44e9943F39138 <- 배포된 주소가 나온다.
* 6. TIMER AT~~부분 화살표를 내려보면 우리가 만들어놓은 함수마다 버튼이 생긴다.(3개)
* 7. start를 누르고 오른쪽 (녹색 체크모양)를 자세히 살펴보면 from, to, gas등 볼 수 있다.
* 8. 에러가 안나면 이 코드는 에러없이 잘 됐다고 생각하면 된다.

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

-------------------------------------------------------

# dApp
```
%%writefile scripts/'클래스 네임'.html
<!doctype>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/web3@1.3.5/dist/web3.min.js"></script>
<script type="text/javascript">
    var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8345"));
    
    function 여기서 새로운 함수명() {
        var 변수 = new web3.eth.Contract([{"constant":false,"inputs":[{"name":"_greeting","type":"bytes32"}] ~~~~ }],
                                          "0xE4c0....");
        변수.methods.함수명2(int 정수).call().then(function(str) {
            document.getElementById('함수명2').innerText = "2^32: "+str; //str에는 바로 위 function(str)의 str 계산값
        });
    }
</script>
</head>

<body>
    <h1>MATH</h1>
    <button type="button" onClick="여기서 새로운 함수명();">함수명2(powerOf2)</button>
    <div></div>
    <div id="함수명2(powerOf2)"></div>
</body>
</html>
```
#### 접속
```
http://localhost:8045/scripts/클래스 .html
```
