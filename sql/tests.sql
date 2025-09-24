GRANT ALL PRIVILEGES ON DATABASE sustainability TO pguser;

-- Quick checks 

-- List extensions:
SELECT extname, extversion FROM pg_extension WHERE extname = 'pgcrypto';

-- List tables:
SELECT tablename FROM pg_tables WHERE schemaname='public' ORDER BY tablename;

-- Describe a table
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'raw_search_events'
ORDER BY ordinal_position;

-- Check indexes:
SELECT indexname, indexdef FROM pg_indexes WHERE tablename='raw_search_events';

-- If counts matter, r:
SELECT COUNT(*) FROM raw_search_events;
