### (error: use of deleted function 에러)[https://stackoverflow.com/questions/5966698/error-use-of-deleted-function]
```console
In file included from D:/coding/project/engine/libs/googletest/googletest/include/gtest/gtest.h:62,
                 from D:\coding\project\engine\tests\engine\quadtree\area_test.cpp:1:
D:/coding/project/engine/libs/googletest/googletest/include/gtest/internal/gtest-internal.h: In instantiation of 'testing::Test* testing::internal::TestFactoryImpl<TestClass>::CreateTest() [with TestClass = QuadTreeAreaTest_split_sub_area_Test]':
D:/coding/project/engine/libs/googletest/googletest/include/gtest/internal/gtest-internal.h:472:9:   required from here
D:/coding/project/engine/libs/googletest/googletest/include/gtest/internal/gtest-internal.h:472:40: error: use of deleted function 'QuadTreeAreaTest_split_sub_area_Test::QuadTreeAreaTest_split_sub_area_Test()'
   Test* CreateTest() override { return new TestClass; }
```
* 컴파일 시 위와 같이 `error: use of deleted function` 에러가 발생함
* 원인은 테스트 클래스를 생성하는 과정에서 멤버를 초기화하지 못해서
```c++
class FooTest : public ::testing::Test {
  protected:
    Bar x;
}
```
* 이 때 `Bar`에 기본 생성자가 없다면 `Bar`를 초기화하지 못해 위와 같은 오류가 발생하게 됨
* 해결법은 `Bar`에 기본 생성자를 정의해주는 것
```c++
class Bar {
  public:
    Bar() = default; ///< like this
}
```
