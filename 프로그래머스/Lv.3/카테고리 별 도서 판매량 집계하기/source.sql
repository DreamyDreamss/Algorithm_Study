SELECT BK.CATEGORY,SUM(BS.SALES) AS TOTAL_SALES FROM BOOK_SALES BS,BOOK BK
WHERE  BK.BOOK_ID = BS.BOOK_ID 
AND TO_CHAR(BS.SALES_DATE,'YYYYMM') = '202201'
GROUP BY BK.CATEGORY
ORDER BY CATEGORY ASC