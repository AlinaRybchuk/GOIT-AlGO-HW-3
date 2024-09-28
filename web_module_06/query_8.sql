-- Запит 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.teacher_id = 1  -- Вказати ID викладача