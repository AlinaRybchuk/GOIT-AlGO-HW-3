-- Запит 10. Список курсів, які певному студенту читає певний викладач.

SELECT sub.name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
WHERE s.students_id = 1 AND sub.teacher_id = 1  -- Вказати ID студента та викладача