-- Запит 6. Знайти список студентів у певній групі

SELECT s.name
FROM students s
WHERE s.group_id = 1  -- Вказати ID групи