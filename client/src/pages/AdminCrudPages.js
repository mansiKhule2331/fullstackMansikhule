import { useState, useEffect, useCallback } from "react";
import api from "../api/axios";
import { Spinner, EmptyState } from "../components/Shared";

// ── Reusable Modal ────────────────────────────────────────────────────────────
function Modal({ title, onClose, children }) {
  return (
    <div className="modal show d-block" style={{ background: "rgba(0,0,0,.5)" }}>
      <div className="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
        <div className="modal-content border-0 shadow-lg">
          <div className="modal-header border-bottom">
            <h5 className="modal-title fw-bold">{title}</h5>
            <button className="btn-close" onClick={onClose} />
          </div>
          {children}
        </div>
      </div>
    </div>
  );
}

function ConfirmDelete({ name, onConfirm, onCancel, loading }) {
  return (
    <div className="modal show d-block" style={{ background: "rgba(0,0,0,.5)" }}>
      <div className="modal-dialog modal-dialog-centered" style={{ maxWidth: 400 }}>
        <div className="modal-content border-0 shadow-lg">
          <div className="modal-body p-4 text-center">
            <div className="bg-danger bg-opacity-10 rounded-circle d-inline-flex p-3 mb-3">
              <i className="bi bi-exclamation-triangle-fill text-danger fs-3" />
            </div>
            <h5 className="fw-bold">Delete Confirmation</h5>
            <p className="text-muted">Are you sure you want to delete <strong>{name}</strong>? This action cannot be undone.</p>
            <div className="d-flex gap-2 justify-content-center">
              <button className="btn btn-outline-secondary" onClick={onCancel}>Cancel</button>
              <button className="btn btn-danger" onClick={onConfirm} disabled={loading}>
                {loading ? <><span className="spinner-border spinner-border-sm me-2" />Deleting…</> : "Delete"}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

// ══════════════════════════════════════════════════════════════════
// MANAGE LANGUAGES
// ══════════════════════════════════════════════════════════════════
export function AdminLanguagesPage() {
  const [langs, setLangs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [modal, setModal] = useState(null); // null | {mode:'add'|'edit', data}
  const [deleteTarget, setDeleteTarget] = useState(null);
  const [saving, setSaving] = useState(false);
  const [form, setForm] = useState({ language_name: "", description: "" });
  const [alert, setAlert] = useState(null);

  const load = useCallback(() => {
    setLoading(true);
    api.get("/languages").then(r => { setLangs(r.data); setLoading(false); });
  }, []);

  useEffect(() => { load(); }, [load]);

  const openAdd = () => { setForm({ language_name: "", description: "" }); setModal({ mode: "add" }); };
  const openEdit = (l) => { setForm({ language_name: l.language_name, description: l.description }); setModal({ mode: "edit", id: l._id }); };

  const handleSave = async () => {
    if (!form.language_name.trim()) return;
    setSaving(true);
    try {
      if (modal.mode === "add") await api.post("/admin/language", form);
      else await api.put(`/admin/language/${modal.id}`, form);
      setAlert({ type: "success", text: `Language ${modal.mode === "add" ? "added" : "updated"} successfully!` });
      setModal(null); load();
    } catch (e) {
      setAlert({ type: "danger", text: e.response?.data?.error || "Save failed" });
    } finally { setSaving(false); }
  };

  const handleDelete = async () => {
    setSaving(true);
    try {
      await api.delete(`/admin/language/${deleteTarget._id}`);
      setAlert({ type: "success", text: "Language deleted." });
      setDeleteTarget(null); load();
    } catch (e) {
      setAlert({ type: "danger", text: e.response?.data?.error || "Delete failed" });
    } finally { setSaving(false); }
  };

  return (
    <div>
      {modal && (
        <Modal title={modal.mode === "add" ? "Add Language" : "Edit Language"} onClose={() => setModal(null)}>
          <div className="modal-body p-4">
            <div className="mb-3">
              <label className="form-label fw-semibold">Language Name <span className="text-danger">*</span></label>
              <input className="form-control" value={form.language_name}
                onChange={e => setForm(f => ({ ...f, language_name: e.target.value }))} placeholder="e.g. Python" />
            </div>
            <div className="mb-3">
              <label className="form-label fw-semibold">Description</label>
              <textarea className="form-control" rows={3} value={form.description}
                onChange={e => setForm(f => ({ ...f, description: e.target.value }))}
                placeholder="Brief description of the language…" />
            </div>
          </div>
          <div className="modal-footer border-top">
            <button className="btn btn-outline-secondary" onClick={() => setModal(null)}>Cancel</button>
            <button className="btn btn-primary" onClick={handleSave} disabled={saving || !form.language_name.trim()}>
              {saving ? <><span className="spinner-border spinner-border-sm me-2" />Saving…</> : "Save Language"}
            </button>
          </div>
        </Modal>
      )}

      {deleteTarget && (
        <ConfirmDelete name={deleteTarget.language_name} loading={saving}
          onConfirm={handleDelete} onCancel={() => setDeleteTarget(null)} />
      )}

      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
        <div>
          <h2 className="fw-bold mb-1">Manage Languages</h2>
          <p className="text-muted mb-0">{langs.length} language{langs.length !== 1 ? "s" : ""} available</p>
        </div>
        <button className="btn btn-primary d-flex align-items-center gap-2" onClick={openAdd}>
          <i className="bi bi-plus-lg" />Add Language
        </button>
      </div>

      {alert && (
        <div className={`alert alert-${alert.type} alert-dismissible`}>
          {alert.text}
          <button className="btn-close" onClick={() => setAlert(null)} />
        </div>
      )}

      {loading ? <Spinner /> : langs.length === 0 ? (
        <div className="text-center py-5">
          <EmptyState icon="translate" text="No languages yet. Add your first one!" />
          <button className="btn btn-primary mt-3" onClick={openAdd}>Add Language</button>
        </div>
      ) : (
        <div className="row g-3">
          {langs.map(l => (
            <div key={l._id} className="col-md-6 col-xl-4">
              <div className="card border-0 shadow-sm h-100">
                <div className="card-body p-4">
                  <div className="d-flex align-items-start justify-content-between gap-2 mb-2">
                    <h5 className="fw-bold mb-0">{l.language_name}</h5>
                    <div className="d-flex gap-1 flex-shrink-0">
                      <button className="btn btn-outline-primary btn-sm" onClick={() => openEdit(l)} title="Edit">
                        <i className="bi bi-pencil" />
                      </button>
                      <button className="btn btn-outline-danger btn-sm" onClick={() => setDeleteTarget(l)} title="Delete">
                        <i className="bi bi-trash" />
                      </button>
                    </div>
                  </div>
                  <p className="text-muted small mb-0">{l.description || <em>No description</em>}</p>
                </div>
                <div className="card-footer bg-transparent border-top-0 pb-3 px-4">
                  <small className="text-muted"><i className="bi bi-hash me-1" />{l._id}</small>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

// ══════════════════════════════════════════════════════════════════
// MANAGE TOPICS
// ══════════════════════════════════════════════════════════════════
export function AdminTopicsPage() {
  const [langs, setLangs] = useState([]);
  const [topics, setTopics] = useState([]);
  const [selLang, setSelLang] = useState("");
  const [loading, setLoading] = useState(false);
  const [modal, setModal] = useState(null);
  const [deleteTarget, setDeleteTarget] = useState(null);
  const [saving, setSaving] = useState(false);
  const [form, setForm] = useState({ language_id: "", topic_name: "", content: "" });
  const [alert, setAlert] = useState(null);

  useEffect(() => {
    api.get("/languages").then(r => {
      setLangs(r.data);
      if (r.data.length > 0) setSelLang(r.data[0]._id);
    });
  }, []);

  const loadTopics = useCallback((lid) => {
    if (!lid) return;
    setLoading(true);
    api.get(`/topics/${lid}`).then(r => { setTopics(r.data); setLoading(false); });
  }, []);

  useEffect(() => { if (selLang) loadTopics(selLang); }, [selLang, loadTopics]);

  const openAdd = () => {
    setForm({ language_id: selLang, topic_name: "", content: "" });
    setModal({ mode: "add" });
  };
  const openEdit = (t) => {
    setForm({ language_id: t.language_id, topic_name: t.topic_name, content: t.content });
    setModal({ mode: "edit", id: t._id });
  };

  const handleSave = async () => {
    if (!form.topic_name.trim() || !form.language_id) return;
    setSaving(true);
    try {
      if (modal.mode === "add") await api.post("/admin/topic", form);
      else await api.put(`/admin/topic/${modal.id}`, form);
      setAlert({ type: "success", text: `Topic ${modal.mode === "add" ? "added" : "updated"}!` });
      setModal(null); loadTopics(selLang);
    } catch (e) {
      setAlert({ type: "danger", text: e.response?.data?.error || "Save failed" });
    } finally { setSaving(false); }
  };

  const handleDelete = async () => {
    setSaving(true);
    try {
      await api.delete(`/admin/topic/${deleteTarget._id}`);
      setAlert({ type: "success", text: "Topic deleted." });
      setDeleteTarget(null); loadTopics(selLang);
    } catch (e) {
      setAlert({ type: "danger", text: e.response?.data?.error || "Delete failed" });
    } finally { setSaving(false); }
  };

  return (
    <div>
      {modal && (
        <Modal title={modal.mode === "add" ? "Add Topic" : "Edit Topic"} onClose={() => setModal(null)}>
          <div className="modal-body p-4">
            <div className="mb-3">
              <label className="form-label fw-semibold">Language <span className="text-danger">*</span></label>
              <select className="form-select" value={form.language_id}
                onChange={e => setForm(f => ({ ...f, language_id: e.target.value }))}>
                <option value="">-- Select Language --</option>
                {langs.map(l => <option key={l._id} value={l._id}>{l.language_name}</option>)}
              </select>
            </div>
            <div className="mb-3">
              <label className="form-label fw-semibold">Topic Name <span className="text-danger">*</span></label>
              <input className="form-control" value={form.topic_name}
                onChange={e => setForm(f => ({ ...f, topic_name: e.target.value }))} placeholder="e.g. Python Basics" />
            </div>
            <div className="mb-3">
              <label className="form-label fw-semibold">Content <span className="text-muted">(Markdown supported)</span></label>
              <textarea className="form-control font-monospace" rows={12} value={form.content}
                onChange={e => setForm(f => ({ ...f, content: e.target.value }))}
                placeholder="## Topic Title&#10;&#10;Write your learning content here…" />
            </div>
          </div>
          <div className="modal-footer border-top">
            <button className="btn btn-outline-secondary" onClick={() => setModal(null)}>Cancel</button>
            <button className="btn btn-primary" onClick={handleSave}
              disabled={saving || !form.topic_name.trim() || !form.language_id}>
              {saving ? <><span className="spinner-border spinner-border-sm me-2" />Saving…</> : "Save Topic"}
            </button>
          </div>
        </Modal>
      )}

      {deleteTarget && (
        <ConfirmDelete name={deleteTarget.topic_name} loading={saving}
          onConfirm={handleDelete} onCancel={() => setDeleteTarget(null)} />
      )}

      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
        <div>
          <h2 className="fw-bold mb-1">Manage Topics</h2>
          <p className="text-muted mb-0">Create and edit learning content</p>
        </div>
        <button className="btn btn-primary d-flex align-items-center gap-2" onClick={openAdd} disabled={!selLang}>
          <i className="bi bi-plus-lg" />Add Topic
        </button>
      </div>

      {alert && (
        <div className={`alert alert-${alert.type} alert-dismissible`}>
          {alert.text}
          <button className="btn-close" onClick={() => setAlert(null)} />
        </div>
      )}

      {/* Language selector */}
      <div className="card border-0 shadow-sm mb-4">
        <div className="card-body p-3 d-flex align-items-center gap-3 flex-wrap">
          <label className="fw-semibold mb-0 text-muted small text-uppercase" style={{ letterSpacing: 1 }}>Filter by Language:</label>
          <div className="d-flex gap-2 flex-wrap">
            {langs.map(l => (
              <button key={l._id}
                className={`btn btn-sm ${selLang === l._id ? "btn-primary" : "btn-outline-secondary"}`}
                onClick={() => setSelLang(l._id)}>
                {l.language_name}
              </button>
            ))}
          </div>
        </div>
      </div>

      {loading ? <Spinner /> : topics.length === 0 ? (
        <div className="text-center py-5">
          <EmptyState icon="journal-text" text="No topics for this language yet." />
          <button className="btn btn-primary mt-3" onClick={openAdd}>Add Topic</button>
        </div>
      ) : (
        <div className="card border-0 shadow-sm">
          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0">
              <thead className="table-light">
                <tr><th>#</th><th>Topic Name</th><th>Content Preview</th><th>ID</th><th>Actions</th></tr>
              </thead>
              <tbody>
                {topics.map((t, i) => (
                  <tr key={t._id}>
                    <td className="text-muted">{i + 1}</td>
                    <td className="fw-semibold">{t.topic_name}</td>
                    <td className="text-muted small" style={{ maxWidth: 300 }}>
                      <span className="text-truncate d-block" style={{ maxWidth: 280 }}>
                        {t.content?.replace(/#+\s*/g, "").slice(0, 80) || "—"}…
                      </span>
                    </td>
                    <td><code style={{ fontSize: 11 }}>{t._id}</code></td>
                    <td>
                      <div className="d-flex gap-2">
                        <button className="btn btn-outline-primary btn-sm" onClick={() => openEdit(t)}>
                          <i className="bi bi-pencil me-1" />Edit
                        </button>
                        <button className="btn btn-outline-danger btn-sm" onClick={() => setDeleteTarget(t)}>
                          <i className="bi bi-trash me-1" />Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}

// ══════════════════════════════════════════════════════════════════
// MANAGE QUESTIONS
// ══════════════════════════════════════════════════════════════════
export function AdminQuestionsPage() {
  const [langs, setLangs] = useState([]);
  const [topics, setTopics] = useState([]);
  const [questions, setQuestions] = useState([]);
  const [selLang, setSelLang] = useState("");
  const [selTopic, setSelTopic] = useState("");
  const [loading, setLoading] = useState(false);
  const [modal, setModal] = useState(null);
  const [deleteTarget, setDeleteTarget] = useState(null);
  const [saving, setSaving] = useState(false);
  const [form, setForm] = useState({ topic_id: "", question_text: "", options: ["", "", "", ""], correct_answer: "" });
  const [alert, setAlert] = useState(null);

  useEffect(() => {
    api.get("/languages").then(r => {
      setLangs(r.data);
      if (r.data.length > 0) setSelLang(r.data[0]._id);
    });
  }, []);

  useEffect(() => {
    if (!selLang) return;
    api.get(`/topics/${selLang}`).then(r => {
      setTopics(r.data);
      if (r.data.length > 0) setSelTopic(r.data[0]._id);
      else { setSelTopic(""); setQuestions([]); }
    });
  }, [selLang]);

  const loadQuestions = useCallback((tid) => {
    if (!tid) return;
    setLoading(true);
    api.get(`/admin/questions/${tid}`).then(r => { setQuestions(r.data); setLoading(false); });
  }, []);

  useEffect(() => { if (selTopic) loadQuestions(selTopic); }, [selTopic, loadQuestions]);

  const openAdd = () => {
    setForm({ topic_id: selTopic, question_text: "", options: ["", "", "", ""], correct_answer: "" });
    setModal({ mode: "add" });
  };
  const openEdit = (q) => {
    const opts = q.options.length >= 4 ? q.options : [...q.options, ...Array(4 - q.options.length).fill("")];
    setForm({ topic_id: q.topic_id, question_text: q.question_text, options: opts, correct_answer: q.correct_answer });
    setModal({ mode: "edit", id: q._id });
  };

  const setOpt = (i, val) => setForm(f => { const o = [...f.options]; o[i] = val; return { ...f, options: o }; });

  const handleSave = async () => {
    const opts = form.options.filter(o => o.trim());
    if (!form.question_text.trim() || opts.length < 2 || !form.correct_answer) return;
    setSaving(true);
    try {
      const payload = { ...form, options: opts };
      if (modal.mode === "add") await api.post("/admin/question", payload);
      else await api.put(`/admin/question/${modal.id}`, payload);
      setAlert({ type: "success", text: `Question ${modal.mode === "add" ? "added" : "updated"}!` });
      setModal(null); loadQuestions(selTopic);
    } catch (e) {
      setAlert({ type: "danger", text: e.response?.data?.error || "Save failed" });
    } finally { setSaving(false); }
  };

  const handleDelete = async () => {
    setSaving(true);
    try {
      await api.delete(`/admin/question/${deleteTarget._id}`);
      setAlert({ type: "success", text: "Question deleted." });
      setDeleteTarget(null); loadQuestions(selTopic);
    } catch (e) {
      setAlert({ type: "danger", text: "Delete failed" });
    } finally { setSaving(false); }
  };

  const validOpts = form.options.filter(o => o.trim());

  return (
    <div>
      {modal && (
        <Modal title={modal.mode === "add" ? "Add Question" : "Edit Question"} onClose={() => setModal(null)}>
          <div className="modal-body p-4">
            <div className="mb-3">
              <label className="form-label fw-semibold">Topic <span className="text-danger">*</span></label>
              <select className="form-select" value={form.topic_id}
                onChange={e => setForm(f => ({ ...f, topic_id: e.target.value, correct_answer: "" }))}>
                <option value="">-- Select Topic --</option>
                {topics.map(t => <option key={t._id} value={t._id}>{t.topic_name}</option>)}
              </select>
            </div>
            <div className="mb-3">
              <label className="form-label fw-semibold">Question Text <span className="text-danger">*</span></label>
              <textarea className="form-control" rows={3} value={form.question_text}
                onChange={e => setForm(f => ({ ...f, question_text: e.target.value }))}
                placeholder="Enter the question…" />
            </div>
            <div className="mb-3">
              <label className="form-label fw-semibold">Options <span className="text-muted small">(at least 2 required)</span></label>
              <div className="row g-2">
                {form.options.map((opt, i) => (
                  <div key={i} className="col-sm-6">
                    <div className="input-group">
                      <span className="input-group-text bg-primary text-white fw-bold" style={{ width: 38 }}>
                        {["A", "B", "C", "D"][i]}
                      </span>
                      <input className="form-control" value={opt}
                        onChange={e => setOpt(i, e.target.value)}
                        placeholder={`Option ${["A","B","C","D"][i]}`} />
                    </div>
                  </div>
                ))}
              </div>
            </div>
            <div className="mb-3">
              <label className="form-label fw-semibold">Correct Answer <span className="text-danger">*</span></label>
              <select className="form-select" value={form.correct_answer}
                onChange={e => setForm(f => ({ ...f, correct_answer: e.target.value }))}>
                <option value="">-- Select Correct Option --</option>
                {validOpts.map((opt, i) => (
                  <option key={i} value={opt}>{["A","B","C","D"][i]}: {opt}</option>
                ))}
              </select>
            </div>
          </div>
          <div className="modal-footer border-top">
            <button className="btn btn-outline-secondary" onClick={() => setModal(null)}>Cancel</button>
            <button className="btn btn-primary" onClick={handleSave}
              disabled={saving || !form.question_text.trim() || validOpts.length < 2 || !form.correct_answer}>
              {saving ? <><span className="spinner-border spinner-border-sm me-2" />Saving…</> : "Save Question"}
            </button>
          </div>
        </Modal>
      )}

      {deleteTarget && (
        <ConfirmDelete name={`"${deleteTarget.question_text?.slice(0, 40)}…"`} loading={saving}
          onConfirm={handleDelete} onCancel={() => setDeleteTarget(null)} />
      )}

      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
        <div>
          <h2 className="fw-bold mb-1">Manage Questions</h2>
          <p className="text-muted mb-0">Add quiz questions per topic</p>
        </div>
        <button className="btn btn-primary d-flex align-items-center gap-2" onClick={openAdd}
          disabled={!selTopic}>
          <i className="bi bi-plus-lg" />Add Question
        </button>
      </div>

      {alert && (
        <div className={`alert alert-${alert.type} alert-dismissible`}>
          {alert.text}
          <button className="btn-close" onClick={() => setAlert(null)} />
        </div>
      )}

      {/* Filters */}
      <div className="card border-0 shadow-sm mb-4">
        <div className="card-body p-3">
          <div className="row g-2 align-items-center">
            <div className="col-auto">
              <label className="col-form-label fw-semibold small text-muted text-uppercase" style={{ letterSpacing: 1 }}>Language:</label>
            </div>
            <div className="col-auto">
              <select className="form-select form-select-sm" value={selLang}
                onChange={e => { setSelLang(e.target.value); setQuestions([]); }}>
                {langs.map(l => <option key={l._id} value={l._id}>{l.language_name}</option>)}
              </select>
            </div>
            <div className="col-auto">
              <label className="col-form-label fw-semibold small text-muted text-uppercase" style={{ letterSpacing: 1 }}>Topic:</label>
            </div>
            <div className="col-auto">
              <select className="form-select form-select-sm" value={selTopic}
                onChange={e => setSelTopic(e.target.value)} disabled={!topics.length}>
                {topics.map(t => <option key={t._id} value={t._id}>{t.topic_name}</option>)}
              </select>
            </div>
            <div className="col-auto">
              <span className="badge bg-primary bg-opacity-10 text-primary">{questions.length} questions</span>
            </div>
          </div>
        </div>
      </div>

      {loading ? <Spinner /> : questions.length === 0 ? (
        <div className="text-center py-5">
          <EmptyState icon="patch-question" text="No questions for this topic yet." />
          <button className="btn btn-primary mt-3" onClick={openAdd} disabled={!selTopic}>Add Question</button>
        </div>
      ) : (
        <div className="d-flex flex-column gap-3">
          {questions.map((q, i) => (
            <div key={q._id} className="card border-0 shadow-sm">
              <div className="card-body p-4">
                <div className="d-flex justify-content-between align-items-start gap-3 flex-wrap">
                  <div className="flex-grow-1">
                    <div className="d-flex align-items-start gap-3 mb-3">
                      <span className="badge bg-primary rounded-pill" style={{ minWidth: 28 }}>Q{i + 1}</span>
                      <span className="fw-semibold">{q.question_text}</span>
                    </div>
                    <div className="row g-2">
                      {q.options.map((opt, oi) => (
                        <div key={oi} className="col-sm-6">
                          <div className={`p-2 rounded border ${opt === q.correct_answer ? "border-success bg-success bg-opacity-10" : "border-light bg-light"}`}
                               style={{ fontSize: 14 }}>
                            <span className={`badge me-2 ${opt === q.correct_answer ? "bg-success" : "bg-secondary"}`}>
                              {["A","B","C","D"][oi]}
                            </span>
                            {opt}
                            {opt === q.correct_answer && <i className="bi bi-check-circle-fill text-success ms-2" />}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                  <div className="d-flex gap-2 flex-shrink-0">
                    <button className="btn btn-outline-primary btn-sm" onClick={() => openEdit(q)}>
                      <i className="bi bi-pencil" />
                    </button>
                    <button className="btn btn-outline-danger btn-sm" onClick={() => setDeleteTarget(q)}>
                      <i className="bi bi-trash" />
                    </button>
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

// ══════════════════════════════════════════════════════════════════
// ADMIN USERS LIST
// ══════════════════════════════════════════════════════════════════
export function AdminUsersPage() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  useEffect(() => {
    api.get("/admin/users").then(r => { setUsers(r.data); setLoading(false); });
  }, []);

  const filtered = users.filter(u =>
    u.name?.toLowerCase().includes(search.toLowerCase()) ||
    u.email?.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3">
        <div>
          <h2 className="fw-bold mb-1">All Users</h2>
          <p className="text-muted mb-0">{users.length} registered users</p>
        </div>
        <input className="form-control form-control-sm" style={{ maxWidth: 240 }}
          placeholder="🔍 Search by name or email…"
          value={search} onChange={e => setSearch(e.target.value)} />
      </div>

      {loading ? <Spinner /> : (
        <div className="card border-0 shadow-sm">
          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0">
              <thead className="table-light">
                <tr>
                  <th>#</th><th>User</th><th>Role</th>
                  <th>Logins</th><th>Last Login</th><th>Joined</th>
                </tr>
              </thead>
              <tbody>
                {filtered.map((u, i) => (
                  <tr key={u._id}>
                    <td className="text-muted">{i + 1}</td>
                    <td>
                      <div className="d-flex align-items-center gap-2">
                        <div className="rounded-circle bg-primary bg-opacity-10 d-flex align-items-center justify-content-center text-primary fw-bold"
                             style={{ width: 36, height: 36, flexShrink: 0 }}>
                          {u.name?.[0]?.toUpperCase()}
                        </div>
                        <div>
                          <div className="fw-semibold">{u.name}</div>
                          <div className="text-muted small">{u.email}</div>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span className={`badge ${u.role === "admin" ? "bg-danger" : "bg-secondary"}`}>
                        {u.role}
                      </span>
                    </td>
                    <td>
                      <span className="badge bg-info bg-opacity-10 text-info fw-bold">
                        {u.login_count ?? 0}
                      </span>
                    </td>
                    <td className="text-muted small">
                      {u.last_login ? new Date(u.last_login).toLocaleString() : <em className="text-muted">Never</em>}
                    </td>
                    <td className="text-muted small">
                      {u.created_at ? new Date(u.created_at).toLocaleDateString() : "—"}
                    </td>
                  </tr>
                ))}
                {filtered.length === 0 && (
                  <tr><td colSpan={6} className="text-center text-muted py-4">No users match your search.</td></tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
}
