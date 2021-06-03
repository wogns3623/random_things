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
```c++
class Foo {
  public:
    Foo() : bar_{} {} ///< like this

  private:
    int bar_[4];
}
```
* TODO: https://modoocode.com/286, https://boycoding.tistory.com/246 등에서 값의 초기화 방법 자세히 알아보기