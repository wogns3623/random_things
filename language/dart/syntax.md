## 코드 구조

```dart
main() {
  // one line comment
  /*
   * multiple
   * line
   * comment
   */
  print("Hello, World!");
}
```

- c언어처럼 코드 시작점이 main 함수
  - main 함수가 없다면 실행이 안됨
- 코드 뒤에 ; 붙임
- 중괄호로 코드 블록을 묶음
- c 스타일 주석

## [Variable](https://dart.dev/guides/language/language-tour#variables)

```dart
var a;
var arr = ["hello", "world"];
String b;
int c = 4;
```

- var로 선언하고 값을 입력하지 않은 변수는 dynamic이라고 아무 타입의 값이나 들어갈 수 있음
- var로 선언하고 동시에 값이 할당된 변수는 타입 추론을 통해 자동으로 타입이 지정됨
- 대체 왜 String은 대문자로 시작하는데 int는 아님?

## Control flow statement

```dart
if (year >= 2001) {
  print('21st century');
} else if (year >= 1901) {
  print('20th century');
}

for (var object in flybyObjects) {
  print(object);
}

for (int month = 1; month <= 12; month++) {
  print(month);
}

while (year < 2016) {
  year += 1;
}
```

- 기본적인 제어구문은 다른 언어들과 비슷함

## [Function](https://dart.dev/guides/language/language-tour#functions)

```dart
int fibonacci(int n) {
  if (n == 0 || n == 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

var result = fibonacci(20);
```

- c언어 형식

```dart
List<int> arr = [1,2,3];
arr
  .map((num) => num*2)
  .forEach(print);
```

- arrow function도 있음

## Class

```dart
class Spacecraft {
  String name;
  DateTime? launchDate;

  // 바로 프로퍼티에 할당 가능
  Spacecraft(this.name, this.launchDate) {
    // Initialization code goes here.
  }

  // Named constructor. 기본 Constructor와 다른 동작을 하게 만들 수 있음
  Spacecraft.unlaunched(String name) : this(name, null);

  // 값을 지정해주지 않는 변수를 선언할 때는 변수 대신 getter 메서드를 사용해 프로퍼티를 정의함
  // 반드시 이렇게 해야되나?
  int? get launchYear => launchDate?.year; // read-only non-final property

  // Method
  // 프로퍼티에 this없이 접근할 수 있음
  void describe() {
    print('Spacecraft: $name');
    var launchDate = this.launchDate; // Type promotion doesn't work on getters.
    if (launchDate != null) {
      int years = DateTime.now().difference(launchDate).inDays ~/ 365;
      print('Launched: $launchYear ($years years ago)');
    } else {
      print('Unlaunched');
    }
  }
}

var voyager = Spacecraft('Voyager I', DateTime(1977, 9, 5));
voyager.describe();

var voyager3 = Spacecraft.unlaunched('Voyager III');
voyager3.describe();
```

## Inheritance

```dart
class Orbiter extends Spacecraft {
  double altitude;

  Orbiter(String name, DateTime launchDate, this.altitude)
      : super(name, launchDate);
}
```

- 단일 상속 가능
