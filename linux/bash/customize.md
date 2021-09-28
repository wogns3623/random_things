# Bash 커스터마이징

## Bash 커스터마이징은 어떻게 하는가?
- 3줄 요약
  1. 설정 파일이 있는데
  2. 전역 설정은 /etc/bashrc, 지역 설정(특정 사용자에게만 적용)은 ~/.bashrc에
  3. PS1 문자열을 원하는대로 바꾸면 됨

## Bash shell script 문법
- bashrc 파일에서도 bash shell script 문법을 사용함

### 주석
```# some_scripts```
- ```#``` 을 사용함

### 변수
- ```<var_name>=<value>```식으로 정의함
- 사용할 때는 ```$<var_name>```, ```${<var_name>}``` 으로 사용
- [중괄호를 붙이면...](https://superuser.com/questions/935374/difference-between-and-in-shell-script)
- 요약하자면 다른 문자 등과 붙여쓸 때 어디까지가 변수명인지 구분해줌

### $() 명령어 치환(command substitution)
- ```$(<Command>)```

### 문자열
- 따옴표와 쌍따옴표 문자열은 다름
- TODO 문자열 정리하기

### 조건문
```bash
if [<Condition>]; then
  <Script>
elif [<Condition>]; then
  <Script>
else
  <Script>
fi
```
- ```<Condition>```에 조건, ```<Script>```에 실행될 스크립트
- if문 끝날때 ```fi``` 넣기

#### [비교 연산](https://wiki.kldp.org/HOWTO/html/Adv-Bash-Scr-HOWTO/comparison-ops.html)

### 함수
```bash
foo() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
```

## 필요한 명령어들
- git branch
- [sed](https://jhnyang.tistory.com/287)

## 색/글씨 효과 넣기
- ```<Esc>[<FormatCode>m```의 형태로 bash에서 색이나 폰트 효과를 줄 수 있음
- ```<Esc>```는 ```\e```, ```^[```, ```\033```, ```\x1B``` 등으로 쓸 수 있음
- ```<FormatCode>```에 정해진 숫자를 입력해 원하는 색이나 폰트 효과를 지정/해제할 수 있음
- bash script에서는 대괄호로 묶어서 사용, 이 때 대괄호는 이스케이프해줘야 함 ```"\[\e[91m\]"```
- ex) ```"hello \[\e[91m\]world\[\e[0m\]"```이면 ```world```부분만 색이 변함
- https://misc.flogisoft.com/bash/tip_colors_and_formatting

## 결과물
```bash
# gcgb: get current git branch
# /dev/null에 git branch 명령어의 stderr을 던저버림
# stdout은 sed에 넘겨 현재 브랜치만 남기고 원하는 형태로 가공
gcgb() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
cb="\[\e[91m\]\$(gcgb)\[\e[0m\]"

# 깃 브랜치 정보를 기존 PS1 뒤에 추가
PS1="$PS1$cb\$ "
```