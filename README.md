# 🔍 Deep Research Agent

AI-powered research assistant that automatically searches the web, analyzes sources, and generates comprehensive reports using SerpAPI, JinaAI Reader, and Claude AI.

## ✨ Features

- **Smart Search**: Finds top 5 most relevant sources via SerpAPI
- **Content Parsing**: Cleans and extracts content with JinaAI Reader
- **AI Summarization**: Compresses each source to 5-7 key bullet points
- **Report Generation**: Synthesizes findings into structured reports
- **Token Optimization**: Context7 cache prevents reprocessing
- **Beautiful UI**: Clean React + Tailwind interface

## 🏗️ Architecture

```
Frontend (React + Tailwind)
    ↓
Backend API (FastAPI)
    ↓
Deep Research Agent
    ├── SerpAPI (search)
    ├── JinaAI Reader (parse)
    ├── Claude AI (analyze)
    └── Context7 Cache (optimize)
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- API Keys:
  - [SerpAPI](https://serpapi.com/) (free tier available)
  - [Anthropic](https://console.anthropic.com/) (Claude AI)

### Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env and add your keys:
# SERP_API_KEY=your_key_here
# ANTHROPIC_API_KEY=your_key_here

# Run server
python main.py
```

Server runs at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Run dev server
npm run dev
```

Frontend runs at `http://localhost:3000`

## 📖 Usage

1. Open `http://localhost:3000`
2. Enter research topic (e.g., "quantum computing applications")
3. Click "Research"
4. View:
   - Search results
   - Source summaries (5-7 bullets each)
   - Final comprehensive report

## 🎯 API Endpoints

### POST `/research`
Execute deep research on a query.

```json
{
  "query": "artificial intelligence in healthcare"
}
```

### GET `/cache/clear`
Clear the Context7 cache.

## 📁 Project Structure

```
deep-research-agent/
├── backend/
│   ├── agent.py           # Main research agent
│   ├── serp_client.py     # SerpAPI integration
│   ├── jina_client.py     # JinaAI Reader client
│   ├── context7.py        # Cache management
│   ├── main.py            # FastAPI server
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── App.jsx        # Main React component
│   │   ├── main.jsx
│   │   └── index.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── agent.md               # Architecture documentation
└── README.md
```

## 🔧 Configuration

### Backend Environment Variables

```env
SERP_API_KEY=your_serpapi_key
ANTHROPIC_API_KEY=your_anthropic_key
```

### Token Optimization

The agent is designed to minimize API costs:

- **Max 5 sources** per query
- **Immediate compression**: Content → 5-7 bullets
- **Context7 caching**: Reuses summaries
- **Smart model selection**:
  - Claude Haiku for summaries (fast, cheap)
  - Claude Sonnet for final reports (quality)

## 🎨 Frontend Features

- Minimalist, clean design
- Real-time loading states
- Responsive layout
- Source cards with key points
- Clickable source URLs
- Comprehensive final report

## 📊 Performance

- **Search**: ~1-2s
- **Per source**: ~5-9s (parse + summarize)
- **Final report**: ~5-10s
- **Total**: ~30-60s for 5 sources

Cached sources return instantly.

## 🛡️ Security

- API keys in `.env` (not tracked in git)
- CORS enabled for localhost
- No sensitive data stored
- Cache stores only public summaries

## 📝 Documentation

See [agent.md](./agent.md) for detailed architecture and workflow documentation.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📄 License

MIT License - feel free to use for any purpose.

## 🙏 Acknowledgments

- [SerpAPI](https://serpapi.com/) - Web search
- [JinaAI](https://jina.ai/) - Content parsing
- [Anthropic](https://anthropic.com/) - Claude AI
- [FastAPI](https://fastapi.tiangolo.com/) - Backend framework
- [React](https://react.dev/) - Frontend framework
- [Tailwind CSS](https://tailwindcss.com/) - Styling

---

**Built with ❤️ using AI-powered tools**
