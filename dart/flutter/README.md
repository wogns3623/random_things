# Flutter

## What is flutter?

- 구글에서 개발한 안드로이드/ios/웹/데스크톱 모두 하나의 코드로 커버 가능한 플랫폼?
- 암튼 좋다고 함

## [installation](https://flutter-ko.dev/docs/get-started/install)

- 원하는 곳에 압축 해제하고(시스템 권한이 필요한 폴더 제외) 편한 사용을 위해 환경 변수에 등록 ({이전 경로}/flutter/bin)
- flutter는 안드로이드 플랫폼에 종속적인 부분이 있어 [안드로이드 스튜디오](https://developer.android.com/studio)도 함께 설치해야 함
- cmd나 flutter 콘솔에 flutter doctor를 입력해 flutter 구동을 위한 종속성들이 제대로 만족되는지를 확인할 수 있음

### Android lisence status unknown issue

- 안드로이드 스튜디오를 통해 안드로이드sdk까지 설치한 후, `flutter doctor`로 확인해봤더니 > Android lisence status unknown 이라면서 `flutter doctor --android-licenses` 를 실행하라고 함
- 근데 해도 안됨ㅋㅋ;
- [깃헙 이슈](https://github.com/flutter/flutter/issues/57017#issuecomment-653636142)를 찾아본 결과 자바 JDK 버전과 관련된 이슈인 것 같음
- JDK 버전을 8로 재설치
- 환경변수도 등록

  - 시스템 변수에 새로 만들기 -> JAVA_HOME이라는 이름으로 C:\Program Files\Java\jdk1.8.0_221추가(JDK 8이 설치된 경로)
    - 기존에 이미 JAVA_HOME이 있다면 경로만 수정
  - 시스템 변수에 Path 편집 -> %JAVA_HOME%\bin 추가
  - console에 javac -version을 입력해 제대로 됬는지 확인

  ```console
  C:\Users\Administrator>javac -version
  javac 1.8.0_221
  ```

- 아래와 같이 뜨면 성공. 이후 y를 입력해주면 됨

```console
C:\Users\Administrator> flutter doctor --android-licenses
Warning: File C:\Users\Administrator\.android\repositories.cfg could not be loaded.
[================                       ] 42% Fetch remote repository...
```

## setting editor

- vscode에 flutter와 dart extention 설치
- 정상적으로 설치되었는지는 f1 -> Flutter: Run Flutter Doctor로 확인

## test run

1. f1 -> Flutter: New Application Project로 프로젝트 생성 -> lib/main.dart가 정상적으로 생성되었는지 확인
2. vscode 상태표시줄에 Flutter 버전 왼쪽에 Device Selector 영역이 있음. 여기에서 원하는 기기를 선택해 시뮬레이터를 돌려볼 수 있음

![image](https://user-images.githubusercontent.com/42717042/110302951-2bbb7d00-803d-11eb-915b-0b32263a4db5.png)

3. f5 또는 디버그 메뉴에서 앱 실행 가능

### Hot reload

- 앱을 중단하지 않은 채로 코드를 변경하면 재시작하거나 현재 상태를 잃어버리지 않고 변경 사항이 반영됨(Stateful Hot Reload)
