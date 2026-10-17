from datetime import date
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class UserProfile:
    name: str
    age: int
    career_goal: str
    major_or_grade: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "age": self.age,
            "career_goal": self.career_goal,
            "major_or_grade": self.major_or_grade
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "UserProfile":
        return cls(
            name = data["name"],
            age = data["age"],
            career_goal = data["career_goal"],
            major_or_grade = data["major_or_grade"]
        )

@dataclass
class Goal:
    title: str
    is_completed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "is_completed": self.is_completed
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Goal":
        return cls(
            title = data["title"],
            is_completed = data.get("is_completed", False)
        )

@dataclass
class Task:
    title: str
    is_completed: bool = False
    priority: str = "Medium"

    def to_dict(self) -> Dict[str, Any]:
        return{
            "title": self.title,
            "is_completed": self.is_completed,
            "priority": self.priority
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(
            title = data["title"],
            is_completed = data.get("is_completed", False),
            priority = data.get("priority", "Medium")
        )

@dataclass
class StudySession:
    subject: str
    minutes: int
    logged_date: str = field(default_factory=lambda: str(date.today()))

    def to_dict(self) -> Dict[str, Any]:
        return{
            "subject": self.subject,
            "minutes": self.minutes,
            "logged_date": self.logged_date
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "StudySession":
        return cls(
            subject = data["subject"],
            minutes = data["minutes"],
            logged_date = data.get("logged_date", str(date.today()))
        )