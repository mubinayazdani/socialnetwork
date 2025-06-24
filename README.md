# 🧑‍🤝‍🧑 Django Social Network API

This is a lightweight social network API built using **Django** and **Django REST Framework (DRF)**. Users can create profiles, follow/unfollow each other, post content, like posts, and send or accept friend requests.

---

## ⚙️ Technologies Used

- Python 3.13
- Django 5.x
- Django REST Framework
- SQLite (default database)
- JWT or Session Authentication (optional)

---

## 🚀 Setup & Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/socialnetwork.git
cd socialnetwork

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver


🔑 API Endpoints
Endpoint	Method	Description
/api/user-list/	GET	List all active users
/api/request/	POST	Send a friend request
/api/request-lists/	POST	Accept a received friend request
/api/accept/	POST	Accept a friend request explicitly
/api/friends/	GET	Get the list of friends
/api/posts/	GET/POST	Create or list posts
/api/posts/<id>/like/	POST	Like a specific post




