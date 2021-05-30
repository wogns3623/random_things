### 멤버 변수 접근제어
1. public
  * 어디서나 접근 가능

2. private
  * 오직 자기 자신 내부에서만 접근 가능

3. protected
  * private + 파생 클래스에서도 접근 가능함

#### 파생 클래스에서 부모 클래스 멤버에 접근할 때
* 클래스를 상속받을 때 접근 지정자를 붙여 어떻게 상속받을지를 정의할 수 있음
```c++
class foo : public bar {
  //...
}
```

* public하게 상속받으면 부모 클래스에서 지정한 대로 접근 가능함
* protected 또는 private하게 상속받으면 public했던 변수도 클래스 바깥에서 접근할 수 없게 됨
  * TODO : protected하게 상속받은 클래스를 다른 클래스가 또 상속받을 때 최상위 부모 클래스의 멤버 참조 가능?


### (헤더파일 클래스 선언부에서의 함수 구현)[https://stackoverflow.com/questions/14517546/how-can-a-c-header-file-include-implementation]
* 헤더파일에 선언된 클래스 내부에 함수를 구현하면 자동으로 inline 태그가 붙음
* inline함수는 매크로 함수처럼 함수가 사용된 부분을 함수 내용물로 치환하는 형태로 동작함
* 따라서 선언된 함수의 크기가 크면 컴파일된 프로그램의 용량을 늘리게 되므로 되도록 간단한 함수만 인라인 함수로 작성하는게 좋음