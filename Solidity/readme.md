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

