인스턴스 메서드 VS 클래스 메서드
---------------------

### 인스턴스 변수를 사용하면 '인스턴스 메서드'로

### 클래스 변수를 사용하면 '클래스 메서드'로

-----------------
# Q. 클래스 변수와 인스턴스 변수를 둘 다 쓴다면?
## A. 인스턴스 메소드!
인스턴스 변수, 클래스 변수 모두 사용 가능. BUT 클래스 메소드는 인스턴스 변수 사용 불가.



-----------------
# Q. 인스턴스 없이도 필요한 정보가 있다면?
## A. 클래스 메소드 number_of_users
User.count -> 인스턴스가 하나도 없더라도 필요한 값!
