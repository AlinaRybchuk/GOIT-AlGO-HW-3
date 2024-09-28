-- Запит 3. Знайти середній бал у групах з певного предмета.

SELECT s.name, AVG(g.grade) AS average_grade
FROM group g
JOIN students s ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
WHERE gr.subject_id = 1  -- Вказати ID предмета
GROUP BY g.id