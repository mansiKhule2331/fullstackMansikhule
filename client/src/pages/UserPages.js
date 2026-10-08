import { useState, useEffect, useCallback } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../api/axios";
import { useAuth } from "../context/AuthContext";
import { Spinner, EmptyState } from "../components/Shared";

// ── Dashboard ────────────────────────────────────────────────────────────────
export function DashboardPage() {
  const { user } = useAuth();
  const [progress, setProgress] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/progress").then(r => { setProgress(r.data); setLoading(false); });
  }, []);

  const avg = progress.length
    ? (progress.reduce((a, p) => a + p.score, 0) / progress.length).toFixed(1)
    : 0;
  const best = progress.length ? Math.max(...progress.map(p => p.score)).toFixed(1) : 0;

  return (
    <div>
      <div className="mb-4">
        <h2 className="fw-bold mb-1">Welcome back, {user?.name?.split(" ")[0]}! 👋</h2>
        <p className="text-muted">Here's your learning overview</p>
      </div>

      {/* Stat cards */}
      <div className="row g-3 mb-4">
        {[
          { label: "Quizzes Taken",   value: progress.length, icon: "clipboard-check", color: "primary" },
          { label: "Average Score",   value: `${avg}%`,        icon: "graph-up",        color: "success" },
          { label: "Best Score",      value: `${best}%`,       icon: "trophy",          color: "warning" },
        ].map(c => (
          <div key={c.label} className="col-sm-6 col-lg-4">
            <div className="card border-0 shadow-sm h-100">
              <div className="card-body d-flex align-items-center gap-3">
                <div className={`bg-${c.color} bg-opacity-10 rounded-3 p-3`}>
                  <i className={`bi bi-${c.icon} text-${c.color} fs-4`} />
                </div>
                <div>
                  <div className="text-muted small">{c.label}</div>
                  <div className="fw-bold fs-4">{loading ? "—" : c.value}</div>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Recent progress */}
      <div className="card border-0 shadow-sm">
        <div className="card-header bg-white border-bottom fw-semibold">
          <i className="bi bi-clock-history me-2 text-primary" />Recent Quiz Attempts
        </div>
        <div className="card-body p-0">
          {loading ? <Spinner /> : progress.length === 0
            ? <EmptyState icon="clipboard" text="No quizzes taken yet. Start learning!" />
            : (
              <div className="table-responsive">
                <table className="table table-hover mb-0 align-middle">
                  <thead className="table-light">
                    <tr>
                      <th>Topic</th><th>Score</th><th>Correct</th><th>Date</th>
                    </tr>
                  </thead>
                  <tbody>
                    {progress.slice().reverse().slice(0, 10).map(p => (
                      <tr key={p._id}>
                        <td className="fw-semibold">{p.topic_name}</td>
                        <td>
                          <span className={`badge bg-${p.score >= 70 ? "success" : p.score >= 40 ? "warning" : "danger"}`}>
                            {p.score}%
                          </span>
                        </td>
                        <td className="text-muted">{p.correct}/{p.total}</td>
                        <td className="text-muted small">
                          {p.attempt_date ? new Date(p.attempt_date).toLocaleDateString() : "—"}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
        </div>
      </div>
    </div>
  );
}

// ── Languages ────────────────────────────────────────────────────────────────
export function LanguagesPage() {
  const [langs, setLangs] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    api.get("/languages").then(r => { setLangs(r.data); setLoading(false); });
  }, []);

  const langIcons = { Python: "", JavaScript: "", SQL: "", default: "code-slash" };
  const langColors = { Python: "warning", JavaScript: "info", SQL: "success", default: "secondary" };
  if (loading) return <Spinner />;
  return (
    <div>
      <h2 className="fw-bold mb-1">Languages</h2>
      <p className="text-muted mb-4">Choose a programming language to explore topics and quizzes</p>
      {langs.length === 0
        ? <EmptyState icon="globe2" text="No languages available yet." />
        : (
          <div className="row g-4">
            {langs.map(l => {
              const icon = langIcons[l.language_name] || langIcons.default;
              const color = langColors[l.language_name] || langColors.default;
              return (
                <div key={l._id} className="col-sm-6 col-xl-4">
                  <div className="card border-0 shadow-sm h-100 hover-shadow"
                       style={{ cursor: "pointer", transition: "transform .2s" }}
                       onClick={() => navigate(`/topics/${l._id}`)}
                       onMouseOver={e => e.currentTarget.style.transform = "translateY(-3px)"}
                       onMouseOut={e => e.currentTarget.style.transform = "translateY(0)"}>
                    <div className="card-body p-4">
                      <div className={`bg-${color} bg-opacity-10 rounded-3 d-inline-flex p-3 mb-3`}>
                        <i className={`bi bi-${icon} text-${color} fs-3`} />
                      </div>
                      <h5 className="fw-bold">{l.language_name}</h5>
                      <p className="text-muted small mb-3">{l.description}</p>
                      <span className="btn btn-outline-primary btn-sm">
                        View Topics <i className="bi bi-arrow-right ms-1" />
                      </span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        )}
    </div>
  );}
// ── Topics ───────────────────────────────────────────────────────────────────
export function TopicsPage() {
  const { langId } = useParams();
  const [topics, setTopics] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  useEffect(() => {
    api.get(`/topics/${langId}`).then(r => { setTopics(r.data); setLoading(false); });
  }, [langId]);
  if (loading) return <Spinner />;
  return (
    <div>
      <button className="btn btn-link text-decoration-none ps-0 mb-3" onClick={() => navigate("/languages")}>
        <i className="bi bi-arrow-left me-1" /> Back to Languages
      </button>
      <h2 className="fw-bold mb-1">Topics</h2>
      <p className="text-muted mb-4">Select a topic to study content and take a quiz</p>
      {topics.length === 0
        ? <EmptyState icon="journal" text="No topics available for this language yet." />
        : (
          <div className="row g-3">
            {topics.map((t, i) => (
              <div key={t._id} className="col-md-6">
                <div className="card border-0 shadow-sm h-100">
                  <div className="card-body p-4">
                    <div className="d-flex align-items-start gap-3">
                      <div className="bg-primary bg-opacity-10 rounded-2 px-3 py-2 fw-bold text-primary">
                        {String(i + 1).padStart(2, "0")}
                      </div>
                      <div className="flex-grow-1">
                        <h5 className="fw-bold mb-1">{t.topic_name}</h5>
                        <p className="text-muted small mb-3">
                          {t.content?.split("\n")[0]?.replace(/^#+\s*/, "").slice(0, 80) || "Click to view content"}
                        </p>
                        <div className="d-flex gap-2">
                          <button className="btn btn-primary btn-sm"
                                  onClick={() => navigate(`/topic/${t._id}`)}>
                            <i className="bi bi-book me-1" />Study
                          </button>
                          <button className="btn btn-outline-success btn-sm"
                                  onClick={() => navigate(`/quiz/${t._id}`)}>
                            <i className="bi bi-pencil-square me-1" />Take Quiz
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
    </div>
  );
}
// ── Topic Content ─────────────────────────────────────────────────────────────
export function TopicContentPage() {
  const { topicId } = useParams();
  const [topic, setTopic] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();
  useEffect(() => {
    // We load all questions for navigation purposes + content via language list
    api.get(`/questions/${topicId}`).then(() => {}).catch(() => {});
    // Fetch topic info by navigating through languages
    api.get("/languages").then(async r => {
      for (const lang of r.data) {
        const topics = await api.get(`/topics/${lang._id}`);
        const found = topics.data.find(t => t._id === topicId);
        if (found) { setTopic(found); break; }
      }
      setLoading(false);
    });
  }, [topicId]);
  if (loading) return <Spinner />;
  if (!topic) return <EmptyState icon="exclamation-circle" text="Topic not found." />;
  // Simple markdown-like renderer
  const renderContent = (text) =>
    text.split("\n").map((line, i) => {
      if (line.startsWith("### ")) return <h5 key={i} className="fw-bold mt-4 mb-2">{line.slice(4)}</h5>;
      if (line.startsWith("## "))  return <h4 key={i} className="fw-bold mt-4 mb-2">{line.slice(3)}</h4>;
      if (line.startsWith("# "))   return <h3 key={i} className="fw-bold mt-4 mb-2">{line.slice(2)}</h3>;
      if (line.startsWith("```"))  return null;
      if (line.startsWith("- "))   return <li key={i} className="mb-1">{line.slice(2)}</li>;
      if (line.trim() === "")      return <br key={i} />;
      if (line.includes("`"))
        return <p key={i}>{line.split(/(`[^`]+`)/g).map((s, j) =>
          s.startsWith("`") ? <code key={j} className="bg-light px-1 rounded">{s.slice(1, -1)}</code> : s
        )}</p>;
      return <p key={i} className="mb-1">{line}</p>;
    });
  return (
    <div>
      <button className="btn btn-link text-decoration-none ps-0 mb-3"
              onClick={() => navigate(-1)}>
        <i className="bi bi-arrow-left me-1" /> Back
      </button>
      <div className="card border-0 shadow-sm">
        <div className="card-body p-4 p-lg-5">
          <div className="d-flex justify-content-between align-items-start mb-4 flex-wrap gap-3">
            <h3 className="fw-bold mb-0">{topic.topic_name}</h3>
            <button className="btn btn-success" onClick={() => navigate(`/quiz/${topicId}`)}>
              <i className="bi bi-pencil-square me-2" />Take Quiz
            </button>
          </div>
          <div className="content-body" style={{ lineHeight: 1.8 }}>
            {renderContent(topic.content || "")}
          </div>
        </div>
      </div>
    </div>
  );
}
// ── Quiz ─────────────────────────────────────────────────────────────────────
export function QuizPage() {
  const { topicId } = useParams();
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [current, setCurrent] = useState(0);
  const navigate = useNavigate();
  useEffect(() => {
    api.get(`/questions/${topicId}`).then(r => { setQuestions(r.data); setLoading(false); });
  }, [topicId]);
  const handleAnswer = (qid, opt) => setAnswers(a => ({ ...a, [qid]: opt }));

  const handleSubmit = async () => {
    setSubmitting(true);
    try {
      const { data } = await api.post("/submit-quiz", { topic_id: topicId, answers });
      setResult(data);
    } catch { alert("Submission failed. Please try again."); }
    finally { setSubmitting(false); }
  };

  if (loading) return <Spinner />;
  if (questions.length === 0) return (
    <div>
      <EmptyState icon="patch-question" text="No questions available for this topic." />
      <div className="text-center"><button className="btn btn-primary" onClick={() => navigate(-1)}>Go Back</button></div>
    </div>
  );

  if (result) {
    const pct = result.score;
    const color = pct >= 70 ? "success" : pct >= 40 ? "warning" : "danger";
    return (
      <div className="mx-auto" style={{ maxWidth: 700 }}>
        <div className="card border-0 shadow-sm mb-4">
          <div className={`card-header bg-${color} text-white text-center py-4`}>
            <div className="display-4 fw-bold">{pct}%</div>
            <div className="fs-5">
              {pct >= 70 ? "🎉 Excellent!" : pct >= 40 ? "👍 Good effort!" : "😅 Keep practicing!"}
            </div>
          </div>
          <div className="card-body p-4 text-center">
            <div className="row g-3 mb-4">
              <div className="col-4"><div className="bg-success bg-opacity-10 rounded-3 p-3"><div className="fw-bold fs-4 text-success">{result.correct}</div><small className="text-muted">Correct</small></div></div>
              <div className="col-4"><div className="bg-danger bg-opacity-10 rounded-3 p-3"><div className="fw-bold fs-4 text-danger">{result.total - result.correct}</div><small className="text-muted">Wrong</small></div></div>
              <div className="col-4"><div className="bg-primary bg-opacity-10 rounded-3 p-3"><div className="fw-bold fs-4 text-primary">{result.total}</div><small className="text-muted">Total</small></div></div>
            </div>
            <div className="d-flex gap-2 justify-content-center">
              <button className="btn btn-primary" onClick={() => { setResult(null); setAnswers({}); setCurrent(0); }}>
                <i className="bi bi-arrow-repeat me-2" />Retry
              </button>
              <button className="btn btn-outline-secondary" onClick={() => navigate("/dashboard")}>
                <i className="bi bi-house me-2" />Dashboard
              </button>
            </div>
          </div>
        </div>

        {/* Answer review */}
        <h5 className="fw-bold mb-3">Review Answers</h5>
        {result.results.map((r, i) => (
          <div key={r.question_id} className={`card border-0 shadow-sm mb-3 border-start border-3 border-${r.is_correct ? "success" : "danger"}`}>
            <div className="card-body p-3">
              <div className="d-flex gap-2 mb-2">
                <span className={`badge bg-${r.is_correct ? "success" : "danger"}`}>
                  {r.is_correct ? "✓ Correct" : "✗ Wrong"}
                </span>
                <span className="text-muted small">Q{i + 1}</span>
              </div>
              <div className="fw-semibold mb-2">{r.question_text}</div>
              {!r.is_correct && <div className="text-danger small">Your answer: {r.your_answer || "Not answered"}</div>}
              <div className="text-success small">Correct: {r.correct_answer}</div>
            </div>
          </div>
        ))}
      </div>
    );
  }

  const q = questions[current];
  const answered = Object.keys(answers).length;

  return (
    <div className="mx-auto" style={{ maxWidth: 700 }}>
      {/* Progress bar */}
      <div className="d-flex justify-content-between align-items-center mb-2">
        <span className="text-muted small">Question {current + 1} of {questions.length}</span>
        <span className="text-muted small">{answered}/{questions.length} answered</span>
      </div>
      <div className="progress mb-4" style={{ height: 6 }}>
        <div className="progress-bar bg-primary" style={{ width: `${((current + 1) / questions.length) * 100}%` }} />
      </div>

      <div className="card border-0 shadow-sm mb-4">
        <div className="card-body p-4">
          <h5 className="fw-semibold mb-4">{q.question_text}</h5>
          <div className="d-flex flex-column gap-2">
            {q.options.map(opt => {
              const sel = answers[q._id] === opt;
              return (
                <button key={opt}
                  className={`btn text-start p-3 border rounded-3 ${sel ? "btn-primary" : "btn-outline-secondary"}`}
                  style={{ transition: "all .15s" }}
                  onClick={() => handleAnswer(q._id, opt)}>
                  <span className={`badge me-2 ${sel ? "bg-white text-primary" : "bg-secondary"}`}>
                    {["A","B","C","D"][q.options.indexOf(opt)]}
                  </span>
                  {opt}
                </button>
              );
            })}
          </div>
        </div>
      </div>

      <div className="d-flex justify-content-between">
        <button className="btn btn-outline-secondary" disabled={current === 0}
                onClick={() => setCurrent(c => c - 1)}>
          <i className="bi bi-chevron-left me-1" />Previous
        </button>
        {current < questions.length - 1
          ? <button className="btn btn-primary" onClick={() => setCurrent(c => c + 1)}>
              Next <i className="bi bi-chevron-right ms-1" />
            </button>
          : <button className="btn btn-success" onClick={handleSubmit} disabled={submitting}>
              {submitting ? <><span className="spinner-border spinner-border-sm me-2" />Submitting…</> : <><i className="bi bi-check-circle me-2" />Submit Quiz</>}
            </button>
        }
      </div>

      {/* Question navigator */}
      <div className="mt-4">
        <div className="text-muted small mb-2">Jump to question:</div>
        <div className="d-flex flex-wrap gap-2">
          {questions.map((_, i) => (
            <button key={i}
              className={`btn btn-sm ${i === current ? "btn-primary" : answers[questions[i]._id] ? "btn-success" : "btn-outline-secondary"}`}
              style={{ width: 36, height: 36 }}
              onClick={() => setCurrent(i)}>
              {i + 1}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

// ── Progress ─────────────────────────────────────────────────────────────────
export function ProgressPage() {
  const [progress, setProgress] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/progress").then(r => { setProgress(r.data.reverse()); setLoading(false); });
  }, []);

  if (loading) return <Spinner />;

  return (
    <div>
      <h2 className="fw-bold mb-1">My Progress</h2>
      <p className="text-muted mb-4">All your quiz attempts and scores</p>

      {progress.length === 0
        ? <EmptyState icon="clipboard" text="No quiz attempts yet. Start learning!" />
        : (
          <div className="card border-0 shadow-sm">
            <div className="table-responsive">
              <table className="table table-hover align-middle mb-0">
                <thead className="table-light">
                  <tr><th>#</th><th>Topic</th><th>Score</th><th>Result</th><th>Date</th></tr>
                </thead>
                <tbody>
                  {progress.map((p, i) => {
                    const color = p.score >= 70 ? "success" : p.score >= 40 ? "warning" : "danger";
                    return (
                      <tr key={p._id}>
                        <td className="text-muted">{i + 1}</td>
                        <td className="fw-semibold">{p.topic_name}</td>
                        <td>
                          <div className="d-flex align-items-center gap-2">
                            <div className="progress flex-grow-1" style={{ height: 6, minWidth: 80 }}>
                              <div className={`progress-bar bg-${color}`} style={{ width: `${p.score}%` }} />
                            </div>
                            <span className="text-muted small fw-semibold">{p.score}%</span>
                          </div>
                        </td>
                        <td><span className={`badge bg-${color}`}>{p.correct}/{p.total} correct</span></td>
                        <td className="text-muted small">
                          {p.attempt_date ? new Date(p.attempt_date).toLocaleString() : "—"}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        )}
    </div>
  );
}
