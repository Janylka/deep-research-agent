# 🚀 Start Project - Quick Guide

## Current Status

✅ Python dependencies installed
✅ Node dependencies installed
✅ `.env` file created
⏳ Need to add API keys

## Step 1: Add API Keys

Edit `backend/.env` file and replace with your real keys:

```env
SERP_API_KEY=your_actual_serpapi_key
ANTHROPIC_API_KEY=your_actual_anthropic_key
```

### Get SerpAPI Key (if you don't have it):
1. Go to: https://serpapi.com/users/sign_up
2. Sign up (free, 100 searches/month)
3. Copy API key from: https://serpapi.com/manage-api-key

## Step 2: Run Backend

Open **Terminal 1**:

```bash
cd backend
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

## Step 3: Run Frontend

Open **Terminal 2** (new terminal):

```bash
cd frontend
npm run dev
```

You should see:
```
  VITE v7.3.0  ready in X ms

  ➜  Local:   http://localhost:3000/
```

## Step 4: Test Application

1. Open browser: http://localhost:3000
2. Enter research topic (e.g., "quantum computing applications")
3. Click "Research" button
4. Wait ~30-60 seconds for results

## Expected Flow

```
Your query → SerpAPI (search) → JinaAI (parse) →
Claude (summarize) → Final report
```

## Troubleshooting

### Backend won't start?
- Check API keys in `.env`
- Make sure port 8000 is free
- Verify Python packages: `pip list | grep fastapi`

### Frontend won't start?
- Make sure port 3000 is free
- Try: `npm install` again
- Check Node version: `node --version` (should be 16+)

### "API Error" in browser?
- Verify API keys are correct
- Check backend is running (http://localhost:8000)
- Look at backend terminal for error messages

## API Endpoints

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs (FastAPI Swagger UI)

---

**Ready to test!** 🎉
