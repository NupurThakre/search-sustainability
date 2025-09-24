-- sql/10_ingest_raw.sql
-- Create staging table (landing area)
CREATE TABLE IF NOT EXISTS raw_search_events_stg (
  query_text TEXT,
  query_hash VARCHAR(64),
  user_pseudonym VARCHAR(128),
  session_id VARCHAR(128),
  event_ts TIMESTAMP WITH TIME ZONE,
  country VARCHAR(128),
  region VARCHAR(64),
  language VARCHAR(8),
  device_type VARCHAR(32),
  user_agent TEXT,
  result_type VARCHAR(64),
  click_count INT,
  raw_payload TEXT
);

-- Insert into canonical table skipping duplicates (exact match on query_hash + user_pseudonym + event_ts)
INSERT INTO raw_search_events (
  query_text, query_hash, user_pseudonym, session_id, event_ts,
  country, region, language, device_type, user_agent, result_type, click_count, raw_payload
)
SELECT s.query_text, s.query_hash, s.user_pseudonym, s.session_id, s.event_ts,
       s.country, s.region, s.language, s.device_type, s.user_agent, s.result_type, COALESCE(s.click_count,0), s.raw_payload::jsonb
FROM raw_search_events_stg s
WHERE NOT EXISTS (
  SELECT 1 FROM raw_search_events r
  WHERE r.query_hash = s.query_hash
    AND r.user_pseudonym = s.user_pseudonym
    AND r.event_ts = s.event_ts
);

-- Optional: create unique index for future ON CONFLICT use
-- CREATE UNIQUE INDEX IF NOT EXISTS ux_raw_qh_user_ts ON raw_search_events (query_hash, user_pseudonym, event_ts);

-- Optionally clear staging
TRUNCATE TABLE raw_search_events_stg;
