### 생성자를 다른 멤버 변수 내에서 호출할 수 있는가?
* 안됨!

### 생성자를 다른 생성자 내에서 호출할 수 있는가?
* 됨!
```c++
class Foo {
  public:
    Foo() : Foo(0) {} ///< like this

    Foo(int bar) : bar_(bar) {
      baz_ = bar_++;
    }

  private:
    int bar_;
    int baz_;
};
```

### 클래스 멤버 변수가 배열일 때 초기화하는 법
* 멤버 변수 초기화(member initializer list)를 사용해 배열을 유니폼 초기화하면 됨
```c++
class Foo {
  public:
    Foo() : bar_{} {} ///< like this

  private:
    int bar_[4];
}
```
* TODO: https://modoocode.com/286, https://boycoding.tistory.com/246 등에서 값의 초기화 방법 자세히 알아보기

### 클래스 포인터 멤버변수 초기화 방법
* `foo_()`처럼 비워놓으면 `foo_(nullptr)`처럼 동작함
* `foo_(new Foo())`처럼 `new`를 사용해 메모리를 할당받고 주소를 넣어주면 됨