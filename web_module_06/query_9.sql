-- Запит 9. Знайти список курсів, які відвідує студент.

SELECT sub.name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
WHERE g.student_id = 1  -- Вказати ID студента