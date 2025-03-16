# Resume Bot

![License](https://img.shields.io/badge/license-Educational_Use_Only-red)
![Python](https://img.shields.io/badge/python-3.13+-blue)
![Docker](https://img.shields.io/badge/docker-ready-brightgreen)

**Resume Bot** - A microservice-based application for enhancing resumes using AI through a Telegram bot.

## ⚠️ License

**WARNING**: This project is provided strictly for educational and demonstration purposes only.

- Commercial use is PROHIBITED
- Redistribution is PROHIBITED
- Use in production systems is PROHIBITED

The project may be used solely for studying microservice architecture patterns and as an example of AI service integration.

## 🚀 Tech Stack

### Backend
- **Python 3.13+** - core programming language
- **aiogram 3** - Telegram bot framework
- **Apache Kafka** - message broker for inter-service communication
- **Redis** - caching of processed resumes and state management
- **PostgreSQL** - main database for users and metadata
- **MinIO** - S3-compatible object storage for files
- **Docker & Docker Compose** - containerization and orchestration

### AI & API
- **Claude API** - AI for processing and enhancing resumes
- **Tinkoff API** - payment solution for monetization

## 🏗️ Project Architecture

The project is built on a microservice architecture:

```
+-----------------+           +------------------+
|                 |           |                  |
|  Bot Service    |<---+----->|  AI Processor    |
|  (Telegram Bot) |    |      |  Service         |
|                 |    |      |                  |
+--------+--------+    |      +---------+--------+
         |             |                |
         |             |                |
         |     +-------+-------+        |
         |     |               |        |
         +---->|    Kafka      |<-------+
               |               |
         +---->|               |<-------+
         |     +-------+-------+        |
         |             |                |
         |             |                |
+--------+--------+    |      +---------+--------+
|                 |    |      |                  |
|  Callback       |<---+----->|  Storage         |
|  Service        |           |  Service         |
|                 |           |                  |
+-----------------+           +------------------+
```

## 🔧 System Components

### Bot Service
- User interaction through Telegram
- Accept resumes in various formats (PDF, DOCX, TXT)
- Send processing requests via Kafka

### AI Processor Service
- Integration with Claude API
- Resume processing according to prompts
- Saving processing results

### Callback Service
- Receiving resume processing results
- Sending enhanced versions back to users
- Error handling and user notifications

### Storage Service
- User data storage in PostgreSQL
- Result caching in Redis
- File storage in MinIO (S3)
- Database migrations

## 🛠️ Installation & Deployment

### Prerequisites
- Docker and Docker Compose
- Telegram Bot Token (obtain via @BotFather)
- Claude API key
- Tinkoff API keys (optional, for payment processing)

### Setup and Launch

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/resume-bot.git
   cd resume-bot
   ```

2. Create and configure the `.env` file based on `.env.example`
   ```bash
   cp .env.example .env
   # Edit .env with your editor
   ```

3. Launch the project with Docker Compose
   ```bash
   docker-compose up -d
   ```

4. Verify services are running
   ```bash
   docker-compose ps
   ```

## 📊 Monitoring & Management

For monitoring and debugging:

```bash
# View all logs
docker-compose logs -f

# View logs for a specific service
docker-compose logs -f ai_processor

# Restart a service
docker-compose restart callback
```

## 💼 Business Logic

- Users get one free resume processing
- Subsequent processing costs $1
- Support for various formats (PDF, DOCX, TXT)
- Different prompts for various industries and specializations

## 📝 Developer's Note

This project was developed for educational purposes and demonstrates principles of building microservice architectures using modern technologies.

---

© 2025 | Educational Project