/*



✅ Parent Table (product)

Table: product

| product_category | brand      | product_name  | price |
| ---------------- | ---------- | ------------- | ----- |
| Electronics      | Sony       | TV 55 Inch    | 55000 |
| Electronics      | Samsung    | TV 50 Inch    | 45000 |
| Electronics      | LG         | TV 43 Inch    | 35000 |
| Clothing         | Adidas     | Hoodie        | 3500  |
| Clothing         | Nike       | Jacket        | 5000  |
| Clothing         | Puma       | T-Shirt       | 1500  |
| Groceries        | Aashirvaad | Atta 10kg     | 450   |
| Groceries        | Fortune    | Oil 5L        | 700   |
| Groceries        | Surf       | Detergent 4kg | 520   |



FIRST_VALUE()
==============

✔ Definition

lll FIRST_VALUE returns the first value in a window (partition) based on the ORDER BY clause.
ORDER BY DESC → highest value
ORDER BY ASC → lowest value


⭐ Query 1
Display the most expensive product under each category (show the name for every row)

SELECT *,
FIRST_VALUE(product_name) 
     OVER(PARTITION BY product_category ORDER BY price DESC) AS most_exp_product
FROM product;


🔍 Explanation

We partition by product_category → each category becomes a window
ORDER BY price DESC → highest price comes first
FIRST_VALUE takes that product name and prints it in all rows of that category


| product_cat | brand    | product_name  | price | most_exp_product |
| ----------- | -------- | ------------- | ----- | ---------------- |
| Electronics | Sony     | TV 55 Inch    | 55000 | TV 55 Inch       |
| Electronics | Samsung  | TV 50 Inch    | 45000 | TV 55 Inch       |
| Electronics | LG       | TV 43 Inch    | 35000 | TV 55 Inch       |
| Clothing    | Nike     | Jacket        | 5000  | Jacket           |
| Clothing    | Adidas   | Hoodie        | 3500  | Jacket           |
| Clothing    | Puma     | T-Shirt       | 1500  | Jacket           |
| Groceries   | Fortune  | Oil 5L        | 700   | Oil 5L           |
| Groceries   | Surf     | Detergent 4kg | 520   | Oil 5L           |
| Groceries   | Aashirv. | Atta 10kg     | 450   | Oil 5L           |


LAST_VALUE()
=============

✔ Definition

lll LAST_VALUE returns the last value in a window based on ORDER BY clause.
    But last value works only when full frame rows are visible.

⚠️ By default SQL uses FRAME:
RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

This means:
✔ It can see all rows from the start of the partition
❌ But it cannot see rows after the current row

That is why LAST_VALUE often gives the current row value, not the real last value.

❌ Query with wrong result (default frame)


SELECT *,
LAST_VALUE(product_name)
     OVER(PARTITION BY product_category ORDER BY price DESC) AS least_exp_product
FROM product;


❌ Problem

ORDER BY price DESC → highest → lowest
But default frame stops at the current row, so LAST_VALUE becomes:

➡ "value of the current row" (not the lowest priced one!)

✔ Frame Explanation (Interview Level)
Default Frame

RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

Meaning:

Start → first row of the partition
End → current row only
Future rows are NOT included
So LAST_VALUE cannot look ahead.


✔ Correct frame clause

To allow LAST_VALUE to see ALL rows in partition:

RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

➡ Now the window can see from start → end
➡ LAST_VALUE correctly picks the lowest priced product


⭐ Correct Query

SELECT *,
LAST_VALUE(product_name) 
    OVER(
        PARTITION BY product_category 
        ORDER BY price DESC
        RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS least_exp_product
FROM product;


✔ Output Table (Correct Least Expensive)

| product_cat | product_name  | price | least_exp_product |
| ----------- | ------------- | ----- | ----------------- |
| Electronics | TV 55 Inch    | 55000 | TV 43 Inch        |
| Electronics | TV 50 Inch    | 45000 | TV 43 Inch        |
| Electronics | TV 43 Inch    | 35000 | TV 43 Inch        |
| Clothing    | Jacket        | 5000  | T-Shirt           |
| Clothing    | Hoodie        | 3500  | T-Shirt           |
| Clothing    | T-Shirt       | 1500  | T-Shirt           |
| Groceries   | Oil 5L        | 700   | Atta 10kg         |
| Groceries   | Detergent 4kg | 520   | Atta 10kg         |
| Groceries   | Atta 10kg     | 450   | Atta 10kg         |


⭐ Additional: RANGE BETWEEN 2 PRECEDING AND 2 FOLLOWING
Meaning (very easy):

Look at 2 rows before current row
Look at 2 rows after current row
Window size = 5 rows max







*/
