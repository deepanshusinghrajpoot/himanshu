/*


APPRENTICE – DATA OPS INTERVIEW QUESTIONS
==========================================

🔴 1. SQL — HIGHEST PRIORITY
=============================

BASIC SQL
---------

1. What is SQL?
2. What is the difference between SQL and MySQL?
3. What are DDL, DML, DCL, and TCL?
4. What is a primary key?
5. What is a foreign key?
6. What is a candidate key?
7. What is a composite key?
8. What is a UNIQUE constraint?
9. Difference between WHERE and HAVING?
10. Difference between DELETE, TRUNCATE, and DROP?
11. What is NULL?
12. How do you check for NULL values?
13. What is COALESCE()?
14. What is CASE WHEN?
15. What is an alias?


JOINS
-----

16. Explain INNER JOIN.
17. Explain LEFT JOIN.
18. Explain RIGHT JOIN.
19. Explain FULL OUTER JOIN.
20. What is CROSS JOIN?
21. What is SELF JOIN?
22. Difference between INNER JOIN and LEFT JOIN?
23. Find employees who don't have a department.
24. Find customers who never placed an order.
25. Find records existing in one table but not another.


AGGREGATION
-----------

26. What are aggregate functions?
27. Explain COUNT().
28. Difference between COUNT(*) and COUNT(column)?
29. Explain SUM(), AVG(), MIN(), and MAX().

30. How do you find duplicate records?
31. How do you remove duplicate records?
32. Find the department having the highest average salary.
33. Find the second-highest salary.
34. Find the Nth-highest salary.
35. Find employees earning more than the department average.


WINDOW FUNCTIONS
----------------

36. What is a window function?
37. What is the OVER() clause?
38. Difference between ROW_NUMBER(), RANK(), and DENSE_RANK()?
39. When would you use ROW_NUMBER()?
40. When would you use RANK()?
41. Explain PARTITION BY.
42. Difference between PARTITION BY and GROUP BY?
43. Explain ORDER BY inside a window function.
44. Explain LEAD().
45. Explain LAG().
46. Find the second-highest salary using a window function.
47. Find the top 3 employees in every department.
48. Find the first transaction of every customer.
49. Find the previous transaction of every customer.
50. Calculate a running total.
51. Calculate a moving average.
52. Find duplicate records using ROW_NUMBER().


SUBQUERIES / CTE
---------------

53. What is a subquery?
54. What is a correlated subquery?
55. Difference between subquery and JOIN?
56. What is a CTE?
57. Why do we use CTEs?
58. Difference between CTE and temporary table?
59. Can a CTE be recursive?
60. Write a query using multiple CTEs.


SQL PERFORMANCE
---------------

61. What is an index?
62. Why do we use indexes?
63. Advantages and disadvantages of indexes?
64. Clustered vs non-clustered index?
65. What is query optimization?
66. What is an execution plan?
67. How can you optimize a slow SQL query?
68. Why can too many indexes be bad?
69. What is normalization?
70. Explain 1NF, 2NF, and 3NF.
71. What is denormalization?
72. When would you denormalize a database?



🐍 2. PYTHON — VERY IMPORTANT
==============================

PYTHON BASICS
-------------

73. Why is Python used in data engineering?
74. What are Python's main data types?
75. Difference between list and tuple?
76. Difference between list and set?
77. Difference between set and dictionary?
78. What is a mutable object?
79. What is an immutable object?
80. What is list comprehension?
81. What is dictionary comprehension?
82. What are functions?
83. What are *args and **kwargs?
84. What is exception handling?
85. Explain try, except, else, and finally.
86. How do you read a file in Python?
87. How do you write data to a file?
88. What is a module?
89. What is a package?
90. What is pip?


PYTHON CODING
-------------

91. Reverse a string.
92. Check whether a string is palindrome.
93. Find duplicate elements in a list.
94. Find the frequency of each element.
95. Find the largest and smallest number.
96. Find the second-largest number.
97. Remove duplicates from a list.
98. Count words in a string.
99. Find common elements between two lists.
100. Sort a dictionary by value.
101. Find missing numbers from a list.
102. Check whether a number is prime.
103. Generate Fibonacci numbers.
104. Find factorial.
105. Find the maximum occurring character.



🐼 3. PANDAS & NUMPY — VERY IMPORTANT
======================================

PANDAS
------

106. What is Pandas?
107. What is a Series?
108. What is a DataFrame?
109. How do you read a CSV file?
110. How do you write a DataFrame to CSV?
111. How do you inspect a DataFrame?
112. Difference between loc and iloc?
113. How do you filter rows?
114. How do you select specific columns?
115. How do you handle missing values?
116. Difference between dropna() and fillna()?
117. How do you remove duplicate records?
118. How does groupby() work?
119. Explain merge().
120. Difference between merge(), join(), and concat()?
121. How do you rename columns?
122. How do you change a column's datatype?
123. How do you sort a DataFrame?
124. How do you apply a function to a column?
125. How do you detect duplicate data?
126. How do you handle inconsistent data?
127. How do you process a large CSV file?
128. What is chunking in Pandas?


NUMPY
-----

129. What is NumPy?
130. Why use NumPy instead of Python lists?
131. What is an ndarray?
132. What is vectorization?
133. What is broadcasting?
134. Difference between scalar and vector operations?
135. Explain reshape().
136. Explain concatenate().
137. Difference between hstack() and vstack()?
138. What is the use of axis?



🏗️ 4. DATA ENGINEERING / DATA OPS — HIGHEST PRIORITY
=====================================================

139. What is Data Engineering?
140. What is Data Operations?
141. What does a DataOps engineer do?
142. Difference between Data Engineering and DataOps?
143. What is ETL?
144. Explain Extract, Transform, Load.
145. What is ELT?
146. Difference between ETL and ELT?
147. What is a data pipeline?
148. What are the stages of a data pipeline?
149. What is data ingestion?
150. What is data transformation?
151. What is data validation?
152. What is data quality?
153. What is data cleansing?
154. What is data profiling?
155. What is data lineage?
156. What is data governance?
157. What is data monitoring?
158. What is pipeline monitoring?
159. What is pipeline failure?
160. How would you troubleshoot a failed pipeline?
161. How do you identify bad data?
162. What is data reconciliation?
163. What is an SLA?
164. What is an SLO?
165. What is an incident?
166. What is incident management?
167. What is root-cause analysis?
168. What is an RCA?
169. What is L1 support?
170. What is L2 support?
171. Difference between L1 and L2 troubleshooting?
172. What is ticket management?
173. What is Jira?
174. How would you prioritize multiple data issues?
175. What is automation in DataOps?
176. What repetitive data task would you automate?



🥇 5. DATA WAREHOUSE PROJECT — EXTREMELY IMPORTANT
==================================================

177. Explain your Data Warehouse project.
178. Why did you use Medallion Architecture?
179. What is the Bronze Layer?
180. What is the Silver Layer?
181. What is the Gold Layer?
182. Why separate data into Bronze, Silver, and Gold?
183. How does data move from Bronze → Silver → Gold?
184. What transformations happen in the Silver Layer?
185. What is a fact table?
186. What is a dimension table?
187. What is a star schema?
188. Why did you use a star schema?
189. Fact table vs dimension table?
190. What is a surrogate key?
191. What is a natural key?
192. What is dimensional modeling?
193. What is a stored procedure?
194. Why did you use stored procedures?
195. What is BULK INSERT?
196. How did you load CSV data?
197. How did you handle bad records?
198. How did you handle duplicate records?
199. How did you handle NULL values?
200. How did you validate transformed data?
201. How did you optimize your queries?
202. What indexes did you use?
203. What is incremental loading?
204. How would you implement incremental loading?
205. What is Slowly Changing Dimension?
206. Explain SCD Type 1.
207. Explain SCD Type 2.
208. How would you handle a customer's address changing?
209. How would you monitor your pipeline?
210. What happens if the Silver pipeline fails?
211. How would you troubleshoot a pipeline failure?
212. What would you do if source data suddenly changed its schema?



🔧 6. TROUBLESHOOTING / SCENARIO-BASED QUESTIONS
================================================

213. A pipeline normally takes 20 minutes but suddenly takes 2 hours.
     What will you check?

214. A customer reports that yesterday's data is missing.
     How will you investigate?

215. Your SQL query is suddenly taking much longer.
     What will you do?

216. A scheduled job failed at 2 AM.
     You receive the ticket at 9 AM.
     What will you check first?

217. Source data contains unexpected NULL values.
     What will you do?

218. You receive duplicate records from the source.
     How will you handle them?

219. Source schema changed unexpectedly.
     What steps will you take?

220. A pipeline succeeded, but output contains incorrect data.
     What will you investigate?

221. One customer has incorrect data while others are correct.
     How would you debug it?

222. You have 10 tickets and all are marked urgent.
     How do you prioritize them?

223. A production issue occurs and you don't know the solution.
     What do you do?

224. A job fails repeatedly after retrying.
     What will you do?

225. How would you distinguish between a data issue and a code issue?

226. How would you prevent the same production issue from happening again?



🏥 7. HEALTHCARE DATA QUESTIONS
================================

227. What is healthcare data?
228. What types of healthcare data exist?
229. What is a patient record?
230. What is an encounter?
231. What is a claim?
232. What is a diagnosis?
233. What is a procedure?
234. What is a provider?
235. What is a payer?
236. What is a healthcare data pipeline?
237. Why is data quality important in healthcare?
238. What problems can duplicate patient records cause?
239. How would you validate patient data?
240. How would you handle missing patient information?
241. Why is healthcare data sensitive?
242. How would you protect sensitive data?
243. What is data privacy?
244. What is HIPAA?
245. Why is access control important for healthcare data?



🗄️ 8. DBMS
==========

246. What is DBMS?
247. DBMS vs RDBMS?
248. What is normalization?
249. Explain 1NF.
250. Explain 2NF.
251. Explain 3NF.
252. What is BCNF?
253. What is ACID?
254. Explain Atomicity.
255. Explain Consistency.
256. Explain Isolation.
257. Explain Durability.
258. What is a transaction?
259. What is database indexing?
260. What is referential integrity?
261. What is a constraint?
262. What is deadlock?
263. What is database locking?
264. What is a view?
265. View vs table?
266. What is a stored procedure?
267. Stored procedure vs function?
268. What is a trigger?



📊 9. DATA MODELING
===================

269. What is data modeling?
270. What is conceptual data modeling?
271. What is logical data modeling?
272. What is physical data modeling?
273. What is dimensional modeling?
274. What is a star schema?
275. What is a snowflake schema?
276. Star schema vs snowflake schema?
277. What is a fact table?
278. What is a dimension table?
279. What is a factless fact table?
280. What is the grain of a fact table?
281. What is a surrogate key?
282. What is a degenerate dimension?
283. What is a slowly changing dimension?



⚙️ 10. SCHEDULING & AUTOMATION
==============================

284. What is job scheduling?
285. Why is scheduling important in DataOps?
286. What is a cron job?
287. What happens if a scheduled job fails?
288. How would you retry a failed job?
289. What is dependency management?
290. What is workflow orchestration?
291. What is Apache Airflow?
292. What is a DAG?
293. What is task dependency?
294. What is task retry?
295. What is backfilling?
296. How would you automate a repetitive SQL/data task?



📈 11. BI / ANALYTICS
=====================

297. What is Business Intelligence?
298. What is Power BI?
299. What is Tableau?
300. What is a dashboard?
301. What is a KPI?
302. What is data visualization?
303. Difference between dashboard and report?
304. What is a data source?
305. What is a data model in Power BI?
306. What is a measure?
307. What is a calculated column?
308. What makes a good dashboard?



🧪 12. DATA QUALITY
===================

309. What is data quality?
310. What are the dimensions of data quality?

Important dimensions:

    - Accuracy
    - Completeness
    - Consistency
    - Timeliness
    - Uniqueness
    - Validity

311. How do you check data completeness?
312. How do you check data uniqueness?
313. How do you detect duplicate records?
314. How do you validate data types?
315. How do you validate business rules?
316. What is data reconciliation?
317. What is a data quality check?
318. How would you create automated data quality checks?



🧠 13. BASIC DSA
===============

319. Reverse an array.
320. Find maximum/minimum.
321. Find second-largest element.
322. Remove duplicates.
323. Find duplicate elements.
324. Find missing number.
325. Two Sum.
326. Reverse a string.
327. Check palindrome.
328. Count character frequency.
329. Find first non-repeating character.
330. Check anagram.
331. Fibonacci.
332. Factorial.
333. Prime number.
334. Binary search.
335. Linear search.
336. Sort an array.
337. Merge two sorted arrays.
338. Find intersection of two arrays.
339. Count frequency using hashmap.
340. Find majority element.



👨‍💻 14. GIT / LINUX / TOOLS
=============================

341. What is Git?
342. Git vs GitHub?
343. What is a repository?
344. What is a branch?
345. What is a merge?
346. What is a pull request?
347. What is git clone?
348. What is git pull?
349. What is git push?
350. What is git commit?
351. What is git stash?
352. What is a merge conflict?
353. How do you resolve a merge conflict?
354. What basic Linux commands do you know?
355. How do you check running processes?
356. How do you search logs?
357. How do you check file permissions?
358. How do you schedule a script?



👨‍💼 15. HR / BEHAVIORAL QUESTIONS
==================================

359. Tell me about yourself.
360. Why do you want to join Innovaccer?
361. Why DataOps?
362. Why not software development?
363. What do you understand about the DataOps role?
364. Why should we hire you?
365. What are your strengths?
366. What is your weakness?
367. Tell me about your biggest technical challenge.
368. Tell me about a project you worked on.
369. Tell me about a time you solved a difficult problem.
370. Tell me about a time you made a mistake.
371. How did you handle the mistake?
372. How do you handle pressure?
373. How do you prioritize tasks?
374. How do you handle repetitive work?
375. How do you handle tight deadlines?
376. What do you do when you don't know something?
377. Are you comfortable learning new technologies?
378. Are you comfortable working with SQL every day?
379. Are you comfortable with support/troubleshooting work?
380. Are you comfortable working in shifts if required?
381. Are you comfortable relocating?
382. Where do you see yourself in 3–5 years?
383. What are your salary expectations?
384. Do you have any questions for us?



🔥 TOP 30 — PREPARE THESE FIRST
================================

1.  Tell me about yourself.
2.  Explain your Data Warehouse project.
3.  What is DataOps?
4.  Data Engineering vs DataOps.
5.  Explain ETL.
6.  Explain Bronze, Silver, and Gold layers.
7.  What is a data pipeline?
8.  How do you troubleshoot a failed pipeline?
9.  What is data quality?
10. What is data validation?
11. INNER JOIN vs LEFT JOIN.
12. WHERE vs HAVING.
13. GROUP BY.
14. ROW_NUMBER vs RANK vs DENSE_RANK.
15. PARTITION BY.
16. What is a CTE?
17. What is a subquery?
18. What is indexing?
19. How do you optimize a slow query?
20. Find the second-highest salary.
21. Find duplicate records.
22. Find top 3 employees per department.
23. What is normalization?
24. What is a star schema?
25. Fact table vs dimension table.
26. What is incremental loading?
27. Explain SCD Type 1 and Type 2.
28. Pandas merge(), groupby(), fillna().
29. Python exception handling.
30. Why Innovaccer and why DataOps?



🎯 RECOMMENDED PREPARATION ORDER
================================

1. SQL
   ↓
2. DataOps concepts
   ↓
3. Your Data Warehouse Project
   ↓
4. Python
   ↓
5. Pandas + NumPy
   ↓
6. DBMS
   ↓
7. Data Quality
   ↓
8. Troubleshooting Scenarios
   ↓
9. Healthcare Data Basics
   ↓
10. HR / Behavioral
   ↓
11. Basic DSA


⭐ IMPORTANT FOR YOUR PROFILE
=============================

Your strongest areas should be:

    SQL
    ↓
    Data Warehouse
    ↓
    ETL
    ↓
    Bronze-Silver-Gold
    ↓
    Star Schema
    ↓
    Fact & Dimension Tables
    ↓
    Window Functions
    ↓
    Indexing
    ↓
    Python
    ↓
    Pandas / NumPy
    ↓
    Data Quality
    ↓
    Troubleshooting


DSA PRIORITY:

    Easy → Very Important
    Medium → Important
    Hard → Low Priority


PySpark:

    Learn the basics if time permits,
    but don't sacrifice SQL, Python, DataOps,
    troubleshooting, and your project preparation
    just to cover advanced PySpark.


*/