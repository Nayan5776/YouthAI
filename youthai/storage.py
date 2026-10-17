import json
import os
from typing import Dict, Any, List
from .models import UserProfile, Goal, Task, StudySession

DATA_FILE = "data.json"

class StorageManager:

    @staticmethod
    def save_data(
        profile: UserProfile | None,
        goals: List[Goal],
        tasks: List[Task],
        study_sessions: List[StudySession]
    ) -> None:
        
        data = {
            "profile": profile.to_dict() if profile else None,
            "goals": [goal.to_dict() for goal in goals],
            "tasks": [task.to_dict() for task in tasks],
            "study_sessions": [session.to_dict() for session in study_sessions]
        }
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_data() -> Dict[str, Any]:
        if not os.path.exists(DATA_FILE):
            return {
                "profile": None,
                "goals": [],
                "tasks": [],
                "study_sessions": []
            }

        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            profile = UserProfile.from_dict(data["profile"]) if data.get("profile") else None
            goals = [Goal.from_dict(g) for g in data.get("goals", [])]
            tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
            study_sessions = [StudySession.from_dict(s) for s in data.get("study_sessions", [])]

            return {
                "profile": profile,
                "goals": goals,
                "tasks": tasks,
                "study_sessions": study_sessions
            }
        except (json.JSONDecodeError, KeyError):
            print("Warning: Could not read storage file. Starting with fresh data.")
            return {
                "profile": None,
                "goals": [],
                "tasks": [],
                "study_sessions": []
            }