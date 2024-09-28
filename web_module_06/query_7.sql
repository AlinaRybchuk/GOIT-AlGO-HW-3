-- Запит 7. Знайти оцінки студентів у окремій групі з певного предмета.

SELECT g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
WHERE s.group_id = 1 AND g.subject_id = 1  -- Вказати ID групи та предмета