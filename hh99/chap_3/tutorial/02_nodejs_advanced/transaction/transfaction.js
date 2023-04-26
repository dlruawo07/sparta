// -- SPARTA 테이블을 생성합니다.
CREATE TABLE IF NOT EXISTS SPARTA
(
    spartaId      INT(11)      NOT NULL PRIMARY KEY AUTO_INCREMENT,
    spartaName    VARCHAR(255) NOT NULL,
    spartaAddress VARCHAR(255) NOT NULL
);

// -- 1번째 트랜잭션을 실행합니다.
START TRANSACTION;

// -- SPARTA 테이블에 더미 데이터 3개를 삽입합니다.
INSERT INTO SPARTA (spartaName, spartaAddress)
VALUES ('SPARTA1', 'SEOUL'),
       ('SPARTA2', 'BUSAN'),
       ('SPARTA3', 'DAEGU');

// -- 1번째 트랜잭션을 DB에 적용합니다.
COMMIT;


// -- 2번째 트랜잭션을 실행합니다.
START TRANSACTION;

// -- SPARTA 테이블에 더미 데이터 3개를 삽입합니다.
INSERT INTO SPARTA (spartaName, spartaAddress)
VALUES ('SPARTA4', 'SEOUL'),
       ('SPARTA5', 'BUSAN'),
       ('SPARTA6', 'DAEGU');

// -- 2번째 트랜잭션을 롤백합니다.
ROLLBACK;