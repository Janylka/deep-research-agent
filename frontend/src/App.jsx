import { useState } from 'react'

function App() {
  const [query, setQuery] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!query.trim()) return

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('/api/research', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query.trim() }),
      })

      if (!response.ok) {
        throw new Error('Research failed')
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-slate-900 mb-3">
            🔍 Deep Research Agent
          </h1>
          <p className="text-slate-600 text-lg">
            AI-powered research with SerpAPI + JinaAI + Claude
          </p>
        </div>

        {/* Search Form */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-8">
          <form onSubmit={handleSubmit} className="flex gap-3">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Enter your research topic..."
              className="flex-1 px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              disabled={loading}
            />
            <button
              type="submit"
              disabled={loading || !query.trim()}
              className="px-8 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 disabled:bg-slate-300 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? 'Researching...' : 'Research'}
            </button>
          </form>
        </div>

        {/* Loading State */}
        {loading && (
          <div className="bg-white rounded-2xl shadow-lg p-8 text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
            <p className="text-slate-600">Analyzing sources and generating report...</p>
          </div>
        )}

        {/* Error State */}
        {error && (
          <div className="bg-red-50 border border-red-200 rounded-2xl p-6 mb-8">
            <p className="text-red-800 font-semibold">❌ Error: {error}</p>
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="space-y-6">
            {/* Search Results */}
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h2 className="text-2xl font-bold text-slate-900 mb-4">
                📡 Search Results
              </h2>
              <div className="text-sm text-slate-600 mb-2">
                Query: <span className="font-semibold">{result.query}</span>
              </div>
              <div className="text-sm text-slate-600">
                Found {result.search_results.length} sources
              </div>
            </div>

            {/* Sources */}
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h2 className="text-2xl font-bold text-slate-900 mb-4">
                📚 Sources Analysis
              </h2>
              <div className="space-y-4">
                {result.sources.map((source, idx) => (
                  <div
                    key={idx}
                    className="border border-slate-200 rounded-lg p-4 hover:border-blue-300 transition-colors"
                  >
                    <div className="flex items-start gap-3">
                      <div className="flex-shrink-0 w-8 h-8 bg-blue-100 text-blue-700 rounded-full flex items-center justify-center font-bold">
                        {idx + 1}
                      </div>
                      <div className="flex-1">
                        <h3 className="font-semibold text-slate-900 mb-1">
                          {source.title}
                        </h3>
                        <a
                          href={source.url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-sm text-blue-600 hover:underline mb-2 block"
                        >
                          {source.url.substring(0, 80)}...
                        </a>
                        <div className="mt-3">
                          <p className="text-xs font-semibold text-slate-500 uppercase mb-2">
                            Key Points:
                          </p>
                          <ul className="space-y-1">
                            {source.summary.map((bullet, bidx) => (
                              <li key={bidx} className="text-sm text-slate-700">
                                {bullet}
                              </li>
                            ))}
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Final Report */}
            <div className="bg-white rounded-2xl shadow-lg p-6">
              <h2 className="text-2xl font-bold text-slate-900 mb-4">
                📝 Research Report
              </h2>
              <div className="prose prose-slate max-w-none">
                <div className="whitespace-pre-wrap text-slate-800 leading-relaxed">
                  {result.report}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Footer */}
        <div className="text-center mt-12 text-slate-500 text-sm">
          <p>Built with React, Tailwind, FastAPI, Claude AI</p>
        </div>
      </div>
    </div>
  )
}

export default App
