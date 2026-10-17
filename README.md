# YouthAI – AI-Powered Student & Youth Life Assistant

AI-powered personal productivity & life management assistant for students and youth. Built with Python.

---

## 🚀 Key Features (Version 0.1)

* 👤 **User Profile Management:** Track personal milestones, academic majors, and long-term career goals.
* 🎯 **Daily Goals Engine:** Set and monitor short-term daily targets to stay consistent.
* 📋 **Task Manager:** Create, prioritise (High, Medium, Low), and complete tasks efficiently.
* ⏱️ **Study Hours Tracker:** Log subject-specific study sessions and monitor cumulative focus hours.
* 💾 **Persistent Data Engine:** Automatic JSON storage ensuring user data persists safely across sessions.

---

## 🛠️ Tech Stack & Concepts Applied

* **Language:** Python 3.10+
* **Architecture:** Object-Oriented Programming (OOP) & Modular Design
* **Data Structures:** Standard Library `@dataclass` for type-safe data modeling
* **Storage:** Clean JSON serialisation & deserialisation (`to_dict` / `from_dict` patterns)
* **Design Patterns:** Separation of Concerns (Models, Storage, Business Logic, and Interface)

---

## 📁 Project Structure

```text
YouthAI/
│
├── youthai/
│   ├── __init__.py      # Package initialisation
│   ├── models.py        # Core data models (Dataclasses)
│   ├── storage.py       # Persistence layer (JSON serialisation)
│   └── tracker.py       # Core application logic & operations
│
├── main.py              # CLI Application Entry Point
├── data.json            # Auto-generated local storage
└── README.md            # Project documentation
