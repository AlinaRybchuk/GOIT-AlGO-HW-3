-- Запит 5. Знайти які курси читає певний викладач.

SELECT s.name
FROM subjects s
WHERE s.teacher_id = 1  -- Вказати ID викладача