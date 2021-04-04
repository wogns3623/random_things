# syntax

## 변수 선언
``` kotlin
var count: Int = 10
val MAX_COUNT: Int = 100
```
- 변수는 `var` 및 `val`로 선언
- `val`은 값이 변경되지 않는 변수
- `var`은 값이 변경될 수 있는 변수
- `Byte`, `Short`, `Long`, `Float`, `Double`, `String` 등 여러 자료형이 있음

### 타입 추론
``` kotlin
val name = "Kotlin"
val score = 93.6

// fails to compile
// name.inc()
```
- 타입 추론 기능이 있음
- 정적 타입 언어임

### Null safe
``` kotlin
// fails to compile
// val name: String = null
val name: String? = null
```

- 자료형 뒤에 ? 를 붙여 nullable로 만들 수 있음

## 분기
``` kotlin
if (count == 42) {
  println("Hello")
} else if (count < 42) {
  println("world")
} else {
  println("!")
}
```
- 일반적인 형태의 분기문

### 삼항 연산자
``` kotlin
val answer: String = if (count == 42) {
  "Hello"
} else if (count < 42) {
  "world"
} else {
  "!"
}

println(answer)
```
- if문이 삼항 연산자 대신 사용될 수 있음(기존 삼항연산자는 없음)

### when
``` kotlin
val answer = when {
  count == 42 -> "Hello"
  count < 42 -> "world"
  else -> "!"
}

println(answer)
```
- else if 가 많아지면 더 간결한 when 표현식을 사용하면 좋음
- 조건 -> 결과 꼴로 쓰여짐
- else는 조건 대신 else를 쓰면 됨

### 스마트 변환
``` kotlin
val name: String? = null

// 일반적인 사용 예
// 안전 호출 연산자 ? 를 사용해 nullable을 처리함
println(name?.toUpperCase())

if (name != null) {
  // 분기에서 이미 null값이 아님이 확인되 null인지 또 따질 필요가 없음
  println(name.toUpperCase())
}
```
- 분기로 null이 아님이 확인되면 내부 코드블록에서는 변수를 non-nullable로 간주하고 처리할 수 있음
- [타입 검사](https://kotlinlang.org/docs/typecasts.html#is-and-is-operators), [contracts](https://kotlinlang.org/docs/whatsnew13.html#contracts) 등에도 이 스마트 변환이 적용됨

## 함수
``` kotlin
fun generateAnswerString(countThreshold: Int): String {
  val answer = if (count == countThreshold) {
    "Hello"
  } else if (count < countThreshold) {
    "world"
  } else {
    "!"
  }
  
  return answer
}

println(generateAnswerString(42))
```
- `fun funcName(argName: type): returnType {codeBlock}`형태로 작성됨

### 단순화된 선언
``` kotlin
fun add(a: Int, b: Int): Int = a+b
```
- 함수 선언시 바로 결과값을 할당하는 식으로 작성도 가능함

### 익명 함수
``` kotlin
val strlen: (String) -> Int = { input -> input.length }
```
- 익명 함수는 인자 -> 결과값의 형태로 쓰여짐
- strlen의 타입이 `(String) -> Int`, 값이 `{ input -> input.length }`인듯

### [고차 함수](https://kotlinlang.org/docs/lambdas.html)
``` kotlin
fun stringMapper(str: String, mapper: (String) -> Int): Int {
  return mapper(str)
}

stringMapper("Hello", { input -> input.length })

// this can be possible
stringMapper("Hello") { input ->
  input.length
}
```
고차함수의 마지막 매개변수로 들어가는 익명 함수는 괄호 바깥에 쓰여질 수 있음

## [클래스](https://kotlinlang.org/docs/properties.html)
``` kotlin
class Cookie(val shape: String, val spectialIngredient: List<String>) {
  val fixedValue = "never change"
  val basicIngredient = listOf("flour", "egg")
  private val secretIngredient = listOf("something secret")
  

  fun mix(): List<String> {
    return basicIngredient + spectialIngredient + secretIngredient
  }

  fun make(): String {
    val ingredient = mix()
    //make cookie...
  }
}
```

``` kotlin
var cookie = Cookie("circle", listOf("chocolate"))
println(cookie.getIngredient())

// fails to compile
println(cookie.secretIngredient)
```