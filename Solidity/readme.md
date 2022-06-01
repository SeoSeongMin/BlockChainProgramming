파일명 | 문법 | 내용 
-- | -- | -- 
Solidity1 | send, transfer, deposit(), memory, payable, Event | int, boolean, 바이트 문자열, 구조체, enum, 배열, 송금, 리터널, 저장소, 가시성, 형변환
'' | MyBank.sol | 은행을 경유하지 않고 컨트랙에서 바로 송금하는 프로그램 
Solidity2 | constructor(), view, pure, modifier, +Event | 생성자, 사용자 정의 함수, 제약조건
'' | BankV3.sol | MyBank에 fallback, modifer, async, await추가하여 보안
Solidity3 | forLoop(), If, selfdesturct, mapping, bidirectional map, except | 반복문, 조건문, modifer(조건문 사용 안하고), 컨트랙 삭제, 배열, 은행장고 mapping, 예외
'' | Random.sol | seed를 통한 무작위 수 생성
'' | Members.sol | 원하는 데이터 찾기
Solidity4 | composition, association, import | 여러개의 컨트랙 결합, 배포된 컨트랙에서 결합
'' | C1C2.sol | 한 sol안에 두개의 컨트랙 연결(C2생성자에 C1)
'' | C2.sol | 배포된 컨트랙에서 주소를 가져와 결합
'' | Car.sol | 한 sol안에 2개의 컨트랙을 new로 사용해 결합
'' | SquareArea.sol | 한 sol안에 2개의 컨트랙을 new로 사용해 결합
'' | Area.sol | import문으로 불러와 컨트랙 결합


# 목표
* 컨트랙 코딩을 위한 라이센스 (SPDX)
* 버전을 정하는 Pragma
* import
* 멤버변수와 상태변수, 멤버함수 구현
* boolean, int, string, struct, arr, address
* Opcode

## SPDX
* 저작권에 대해 어떤 규정을 따르는지 적어줘야 한다.
```
//SPDX-License-Identifier: GPL-3.0-or-later
```

## Pragma
* 컴파일러 버전을 선택할 때 이용
```
pragma solidity <버전>;
```

## Import
* filename의 다른 컨트랙, 라이브러리를 읽어들여 사용한다.
```
import "filename" as symbolName
```

## Comments
* 도움말을 적는다.
```
/**
@param p1 The first parameter
@param p2 The second parameter
*/

