-- sql/00_create_schema.sql
-- Postgres schema for Search Sustainability (Day 2)

-- enable pgcrypto for digest() (sha256) if available
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Raw ingestion table (one row per query event)
CREATE TABLE IF NOT EXISTS raw_search_events (
  event_id BIGSERIAL PRIMARY KEY,
  query_text TEXT,
  query_hash VARCHAR(64),               -- sha256(lower(normalized_query))
  user_pseudonym VARCHAR(128),          -- anonymized id (no PII)
  session_id VARCHAR(128),
  event_ts TIMESTAMP WITH TIME ZONE,
  country VARCHAR(128),
  region VARCHAR(64),
  language VARCHAR(8),
  device_type VARCHAR(32),
  user_agent TEXT,
  result_type VARCHAR(64),              -- web, image, maps, zero-click, llm
  click_count INT DEFAULT 0,
  raw_payload JSONB                      -- original event payload for audit
);

-- Normalized queries dimension
CREATE TABLE IF NOT EXISTS queries_dim (
  query_hash VARCHAR(64) PRIMARY KEY,
  query_norm TEXT,
  top_terms TEXT[],                     -- tokenized top terms
  intent_label VARCHAR(64),
  category VARCHAR(64)
);

-- Aggregated daily volumes
CREATE TABLE IF NOT EXISTS daily_query_agg (
  day DATE,
  query_hash VARCHAR(64),
  total_events BIGINT,
  unique_sessions BIGINT,
  avg_pos NUMERIC,
  device_mix JSONB,
  country JSONB,
  PRIMARY KEY (day, query_hash)
);

-- Energy scenario table
CREATE TABLE IF NOT EXISTS energy_params (
  scenario_name VARCHAR(64) PRIMARY KEY,
  energy_kwh_per_query NUMERIC,
  notes TEXT
);

-- Useful indexes
CREATE INDEX IF NOT EXISTS idx_raw_query_hash ON raw_search_events (query_hash);
CREATE INDEX IF NOT EXISTS idx_raw_event_ts ON raw_search_events (event_ts);
CREATE INDEX IF NOT EXISTS idx_raw_user_pseudo ON raw_search_events (user_pseudonym);

