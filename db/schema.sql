CREATE TABLE missions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url TEXT,
  attack_vector TEXT,
  profile TEXT,
  status TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE payloads (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code TEXT,
  vector TEXT,
  used INTEGER DEFAULT 0,
  last_used TIMESTAMP
);

CREATE TABLE detections (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  payload_id INTEGER,
  mission_id INTEGER,
  response_code INTEGER,
  response_length INTEGER,
  detected BOOLEAN,
  notes TEXT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
