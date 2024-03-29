-- 코드를 입력하세요  
# SELECT OUTS.ANIMAL_ID, OUTS.NAME
# FROM ANIMAL_OUTS OUTS LEFT OUTER JOIN ANIMAL_INS INS
# ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
# ORDER BY OUTS.DATETIME - INS.DATETIME DESC
# LIMIT 2

SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_INS, ANIMAL_OUTS
WHERE ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
ORDER BY ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME DESC
LIMIT 2