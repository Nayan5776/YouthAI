from typing import List, Optional
from .models import UserProfile, Goal, Task, StudySession
from .storage import StorageManager

class YouthAITracker:

    def __init__(self) -> None:
    
        data = StorageManager.load_data()
        self.profile: Optional[UserProfile] = data["profile"]
        self.goals: List[Goal] = data["goals"]
        self.tasks: List[Task] = data["tasks"]
        self.study_sessions: List[StudySession] = data["study_sessions"]

    def _save(self) -> None:
        
        StorageManager.save_data(self.profile, self.goals, self.tasks, self.study_sessions)

    # --- 1. User Profile Operations ---
    def set_profile(self, name: str, age: int, major_or_grade: str, career_goal: str) -> None:
        self.profile = UserProfile(
            name=name,
            age=age,
            major_or_grade=major_or_grade,
            career_goal=career_goal
        )
        self._save()

    # --- 2. Daily Goals Operations ---
    def add_goal(self, title: str) -> None:
        self.goals.append(Goal(title=title))
        self._save()

    def complete_goal(self, index: int) -> bool:
        if 0 <= index < len(self.goals):
            self.goals[index].is_completed = True
            self._save()
            return True
        return False

    # --- 3. Task Manager Operations ---
    def add_task(self, title: str, priority: str = "Medium") -> None:
        self.tasks.append(Task(title=title, priority=priority))
        self._save()

    def complete_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks[index].is_completed = True
            self._save()
            return True
        return False

    # --- 4. Study Tracker Operations ---
    def log_study_session(self, subject: str, minutes: int) -> None:
        session = StudySession(subject=subject, minutes=minutes)
        self.study_sessions.append(session)
        self._save()

    def get_total_study_minutes(self) -> int:
        return sum(s.minutes for s in self.study_sessions)