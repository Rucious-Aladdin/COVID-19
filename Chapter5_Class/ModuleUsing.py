import ModuleIntro #같은 디렉토리에 내장된 모듈을 로드하여 사용할 수 있다.

from ModuleIntro import * # *은 ModuleIntro내의 모듈함수 전부를 로드한다.

print(ModuleIntro.add(3,4))

print(add(3, 6)) # from 예약어를 이용하면, 앞에 ModuleIntro를 생략하고 사용할 수 있다.
