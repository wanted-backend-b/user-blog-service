# π λͺ©μ°¨

1. [User Blog Service](#-user-blog-service)
2. [ν μΈμ](#-ν-μΈμ5λͺ)
3. [μ­ν ](#-μ­ν )
4. [μκ΅¬μ¬ν­ λ° λΆμ](#-μκ΅¬μ¬ν­-λ°-λΆμ)
5. [μ§ν λ°©μ](#-μ§ν-λ°©μ)
6. [κΈ°μ  μ€ν](#-κΈ°μ -μ€ν)
7. [API Endpoints](#-api-endpoints)
8. [ERD](#-erd)
9. [μ°Έμ‘° λ¬Έμ](#-μ°Έμ‘°-λ¬Έμ)


# π User Blog Service
- μ¬λ¬ κ²μνκ³Ό ν¬μ€νλ³ μ‘°ν μ§κ³ κΈ°λ₯μ μ κ³΅νλ μ¬μ΄νΈ

# π κ°λ° κΈ°κ°
- 2022.08.31 ~ 2022.09.05 

# π§π»βπ» ν μΈμ(5λͺ)
- κΉλν(νμ₯), λ°λ―Όν, μ€μ κΈ°, μ μμ, μ‘°νμ°

# π» μ­ν 
#### π κΉλν
- PM/λ¦¬λ κ°λ°μ μ­ν μ λ΄λΉνμ¬ μ μ²΄ νλ‘μ νΈλ₯Ό μ²μλΆν° λκΉμ§ λ¦¬λ©
- νλ‘μ νΈ μ€κ³ λ° κ°λ°νκ²½ μΈν
#### π λ°λ―Όν
* readme μμ±
#### π μ€μ κΈ°
- μ μ  νμκ°μ API κ΅¬ν
- μ μ  λ‘κ·ΈμΈ API κ΅¬ν
- μ μ  νμνν΄ API κ΅¬ν
- μ μ  @login_deco κΈ°λ₯ κ΅¬ν
#### π μ μμ
- λ¨λλ³, λμ΄λ³, μκ°λλ³ κ²μν μ΄μ© ν΅κ³ api κ΅¬ν
- ν΅κ³ api μ λ νμ€ν¬ μ½λ 
#### π μ‘°νμ°
* ERD μμ±
* μ΄μ κ²μν, κ³΅μ§μ¬ν­, μμ  κ²μν API κ΅¬ν
* μ κ·Ό μ μ΄ κΈ°λ₯ κ΅¬ν

# π μκ΅¬μ¬ν­ λ° λΆμ
### 1. κ³΅μ§μ¬ν­, μμ κ²μν, μ΄μκ²μν

- κΆνμ λ°λΌ CRUD κΆν λΆμ¬
    - κ³΅μ§μ¬ν­: μ΄μμ§ CRUD, μΌλ°μ μ  R κΆν
    - μμ  κ²μν : μ΄μμ§ CRUD, μΌλ°μ μ  CRUD
    - μ΄μ κ²μν: μ΄μμ§ CRUD, μΌλ°μ μ  X

### 2. νμ λ±κΈμ λ°λ₯Έ κ²μν κΈ°λ₯ μ κ·Όμ μ΄

- μΌλ° λ±κΈκ³Ό μ΄μ λ±κΈμΌλ‘ λλμ΄ κΆνμ λ°λ₯Έ μ κ·Όμ μ΄

### 3. νμκ°μ, λ‘κ·ΈμΈ, νμνν΄

- JWTν ν°μ μ΄μ©ν νμκ°μ, λ‘κ·ΈμΈ
- νμνν΄

### 4. ν¬μ€νλ³ μ‘°ν μ§κ³
- λ¨μ¬ μ‘°ν λΉμ¨
- μκ°λλ³ ν¬μ€ν μ‘°ν λΉμ¨
- λμ΄λ³(10λ, 20λ, 30λ ..)μ‘°ν λΉμ¨

# π‘ μ§ν λ°©μ
- [git commit μ»¨λ²€μ](https://www.notion.so/f5d4a9d98c81473e8d8fef943fced124)
- [λΈλμΉμ λ΅](https://www.notion.so/f5d4a9d98c81473e8d8fef943fced124)

# π  κΈ°μ  μ€ν
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> | <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# π― API Endpoints
| endpoint | HTTP Method | κΈ°λ₯   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| users/signup/     | POST        | νμκ°μ | name: string <br/>email: string <br/>psword: string <br/>gender: string <br/>age: string <br/>phone_number: string<br/> level: string | νμκ°μ μ±κ³΅μ¬λΆ     |
| users/login/      | POST        | λ‘κ·ΈμΈ  | email: string <br/>psword: string                                                                                         | λ‘κ·ΈμΈ μ±κ³΅μ¬λΆ      |
| users/withdrawal/     | POST        | νμνν΄ | email: string <br/>psword: string                                                                                         | νμνν΄ μ±κ³΅μ¬λΆ     |
| /postings/operatings | GET | μ΄μ κ²μν λ¦¬μ€νΈ μ‘°ν | - | μ΄μ κ²μν λ¦¬μ€νΈ |
| /postings/operatings/detail | GET | μ΄μ κ²μν μμΈ μ‘°ν | posting_id: int | μ΄μ κ²μν μμΈ |
| /postings/operatings/detail | POST | μ΄μ κ²μν μμΈ ν¬μ€ν | title: string, context: string, posting_id: int | - |
| /postings/operatings/detail | DELETE | μ΄μ κ²μν μμΈ μ­μ  | posting_id: int | - |
| /postings/operatings/comment | POST | μ΄μ κ²μν λκΈ | comment: string, posting_id: int | - |
| /postings/notices | GET | κ³΅μ§μ¬ν­ κ²μν λ¦¬μ€νΈ μ‘°ν | - | κ³΅μ§μ¬ν­ κ²μν λ¦¬μ€νΈ |
| /postings/notices/detail | GET | κ³΅μ§μ¬ν­ κ²μν μμΈ μ‘°ν | posting_id: int | κ³΅μ§μ¬ν­ κ²μν μμΈ |
| /postings/notices/detail | POST | κ³΅μ§μ¬ν­ κ²μν μμΈ ν¬μ€ν | title: string, context: string, posting_id: int | - |
| /postings/notices/detail | DELETE | κ³΅μ§μ¬ν­ κ²μν μμΈ μ­μ  | posting_id: int | - |
| /postings/notices/comment | POST | κ³΅μ§μ¬ν­ κ²μν λκΈ | comment: string, posting_id: int | - |
| /postings/freeboards | GET | μμ  κ²μν λ¦¬μ€νΈ μ‘°ν | - | μμ  κ²μν λ¦¬μ€νΈ |
| /postings/freeboards/detail | GET | μμ  κ²μν μμΈ μ‘°ν | posting_id: int | μμ  κ²μν μμΈ |
| /postings/freeboards/detail | POST | μμ  κ²μν μμΈ ν¬μ€ν | title: string, context: string, posting_id: int | - |
| /postings/freeboards/detail | DELETE | μμ  κ²μν μμΈ μ­μ  | posting_id: int | - |
| /postings/freeboards/comment | POST | μμ  κ²μν λκΈ | comment: string, posting_id: int | - |
| /statistics/gender/operate | GET | μ΄μκ²μν λ¨λλ³ μ΄μ© ν΅κ³ μ‘°ν| - | λ¨λλ³ μ΄μ©μ μ |
| /statistics/gender/free | GET | μμ κ²μν λ¨λλ³ μ΄μ© ν΅κ³ μ‘°ν| - | λ¨λλ³ μ΄μ©μ μ |
| /statistics/gender/notice | GET | κ³΅μ§μ¬ν­ λ¨λλ³ μ΄μ© ν΅κ³ μ‘°ν| - | λ¨λλ³ μ΄μ©μ μ |
| /statistics/age/operate | GET | μ΄μκ²μν λμ΄λ³ μ΄μ© ν΅κ³ μ‘°ν| - | λμ΄λ³ μ΄μ©μ μ |
| /statistics/age/free | GET | μμ κ²μν λμ΄λ³ μ΄μ© ν΅κ³ μ‘°ν| - | λμ΄λ³ μ΄μ©μ μ |
| /statistics/age/notice | GET | κ³΅μ§μ¬ν­ λμ΄λ³ μ΄μ© ν΅κ³ μ‘°ν| - | λμ΄λ³ μ΄μ©μ μ |
| /statistics/time/operate | GET | μ΄μκ²μν μκ°λλ³ μ΄μ© ν΅κ³ μ‘°ν| - | μκ°λλ³ μ΄μ©μ μ |
| /statistics/time/free | GET | μμ κ²μν μκ°λλ³ μ΄μ© ν΅κ³ μ‘°ν| - | μκ°λλ³ μ΄μ©μ μ |
| /statistics/time/notice | GET | κ³΅μ§μ¬ν­ μκ°λλ³ μ΄μ© ν΅κ³ μ‘°ν| - | μκ°λλ³ μ΄μ©μ μ |


# π ERD
![](https://velog.velcdn.com/images/miracle-21/post/349b7e0f-3a30-4c92-bd71-3634751ff24b/image.png)

# π μ°Έμ‘° λ¬Έμ
- [Postman API Docs](https://documenter.getpostman.com/view/11682851/VUxVpPbo)
- [λΈμνμ΄μ§](https://www.notion.so/Team-B-7214b88a6c54490baf57a8715f20086b)


