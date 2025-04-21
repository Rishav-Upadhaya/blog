# Django Blog Project

A feature-rich blog application built with Django 5.2, featuring Redis caching and Docker support.

## Features

- 📝 Blog Post Management

  - Create, Read, Update, and Delete blog posts
  - Rich text editing support
  - Post categorization and tagging
  - Admin interface for content management

- ⚡ Performance Optimizations

  - Redis caching integration
  - Request timing middleware for performance monitoring
  - Efficient database queries

- 🔒 Security

  - Django's built-in security features
  - CSRF protection
  - Secure form handling

- 🐳 Docker Support
  - Containerized application
  - Easy deployment and scaling
  - Consistent development environment

## Tech Stack

- Python 3.13
- Django 5.2
- Redis 5.2.1
- SQLite (Database)
- Django Redis 5.4.0

## Prerequisites

- Docker
- Python 3.13+
- Redis Server (for local development)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd blog
```

2. Build and run with Docker:

```bash
docker build -t docker_blog .
docker run -p 8000:8000 docker_blog
```

Or run locally:

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

## Project Structure

```
blog/
├── blog/                 # Project configuration
├── posts/               # Blog posts application
│   ├── models.py       # Database models
│   ├── views.py        # View logic
│   ├── forms.py        # Form definitions
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin interface
│   └── my_middleware.py # Custom middleware
├── templates/          # HTML templates
├── Dockerfile         # Docker configuration
└── requirements.txt   # Python dependencies
```

## Performance Features

- **Redis Caching**: Implemented for improved performance
- **Request Timer Middleware**: Monitors request processing time
- **Optimized Database Queries**: Efficient data retrieval

## Development

- The project uses SQLite for development
- Redis caching can be enabled/disabled in settings
- Custom middleware for performance monitoring

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
