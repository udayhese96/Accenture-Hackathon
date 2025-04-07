import sqlite3
from typing import List, Dict
import json

class RecruitmentModel:
    def __init__(self, db_path: str = "recruitment.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        cursor = self.conn.cursor()
        
        # Create Job Descriptions table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_descriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            requirements TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create Candidates table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            resume_text TEXT NOT NULL,
            skills TEXT NOT NULL,
            experience INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Create Matches table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER,
            candidate_id INTEGER,
            match_score FLOAT NOT NULL,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (job_id) REFERENCES job_descriptions (id),
            FOREIGN KEY (candidate_id) REFERENCES candidates (id)
        )
        ''')
        
        # Create Interviews table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            match_id INTEGER,
            scheduled_time TIMESTAMP,
            status TEXT DEFAULT 'scheduled',
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (match_id) REFERENCES matches (id)
        )
        ''')
        
        self.conn.commit()
    
    def add_job_description(self, title: str, description: str, requirements: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO job_descriptions (title, description, requirements) VALUES (?, ?, ?)",
            (title, description, requirements)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def add_candidate(self, name: str, email: str, resume_text: str, skills: List[str], experience: int) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO candidates (name, email, resume_text, skills, experience) VALUES (?, ?, ?, ?, ?)",
            (name, email, resume_text, json.dumps(skills), experience)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def create_match(self, job_id: int, candidate_id: int, match_score: float) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO matches (job_id, candidate_id, match_score) VALUES (?, ?, ?)",
            (job_id, candidate_id, match_score)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def schedule_interview(self, match_id: int, scheduled_time: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO interviews (match_id, scheduled_time) VALUES (?, ?)",
            (match_id, scheduled_time)
        )
        self.conn.commit()
        return cursor.lastrowid
    
    def get_job_descriptions(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM job_descriptions ORDER BY created_at DESC")
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_candidates(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM candidates ORDER BY created_at DESC")
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_matches(self, min_score: float = 0.8) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT m.*, j.title, c.name, c.email 
            FROM matches m
            JOIN job_descriptions j ON m.job_id = j.id
            JOIN candidates c ON m.candidate_id = c.id
            WHERE m.match_score >= ?
            ORDER BY m.match_score DESC
        """, (min_score,))
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def get_interviews(self) -> List[Dict]:
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT i.*, j.title, c.name, c.email
            FROM interviews i
            JOIN matches m ON i.match_id = m.id
            JOIN job_descriptions j ON m.job_id = j.id
            JOIN candidates c ON m.candidate_id = c.id
            ORDER BY i.scheduled_time ASC
        """)
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    def __del__(self):
        self.conn.close()