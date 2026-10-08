import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import api from "../api/axios";

// ── Login ────────────────────────────────────────────────────────────────────
export function LoginPage() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const set = (k) => (e) => setForm((f) => ({ ...f, [k]: e.target.value }));

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(""); setLoading(true);
    try {
      const user = await login(form.email, form.password);
      navigate(user.role === "admin" ? "/admin" : "/dashboard");
    } catch (err) {
      setError(err.response?.data?.error || "Login failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-vh-100 d-flex align-items-center justify-content-center bg-light">
      <div className="card shadow-lg border-0" style={{ width: 420 }}>
        <div className="card-body p-5">
          <div className="text-center mb-4">
            <div className="bg-primary rounded-3 d-inline-flex p-3 mb-3">
              <i className="bi bi-mortarboard-fill text-white fs-2" />
            </div>
            <h3 className="fw-bold">Welcome back</h3>
            <p className="text-muted mb-0">Sign in to LearnQuiz</p>
          </div>

          {error && (
            <div className="alert alert-danger py-2 d-flex align-items-center gap-2">
              <i className="bi bi-exclamation-circle-fill" />
              <span>{error}</span>
            </div>
          )}

          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label className="form-label fw-semibold">Email</label>
              <div className="input-group">
                <span className="input-group-text"><i className="bi bi-envelope" /></span>
                <input type="email" className="form-control" placeholder="you@example.com"
                  value={form.email} onChange={set("email")} required />
              </div>
            </div>
            <div className="mb-4">
              <label className="form-label fw-semibold">Password</label>
              <div className="input-group">
                <span className="input-group-text"><i className="bi bi-lock" /></span>
                <input type="password" className="form-control" placeholder="••••••••"
                  value={form.password} onChange={set("password")} required />
              </div>
            </div>
            <button className="btn btn-primary w-100 py-2 fw-semibold" type="submit" disabled={loading}>
              {loading ? <><span className="spinner-border spinner-border-sm me-2" />Signing in…</> : "Sign In"}
            </button>
          </form>

          <p className="text-center text-muted mt-4 mb-0">
            Don't have an account? <Link to="/register" className="text-primary fw-semibold">Register</Link>
          </p>

          {/* Demo credentials */}
          {/* <div className="mt-4 p-3 bg-light rounded-2 border" style={{ fontSize: 13 }}>
            <strong className="d-block mb-1"><i className="bi bi-info-circle me-1" />Demo credentials</strong>
            <div>Admin: <code>admin@learnquiz.com</code> / <code>admin123</code></div>
            <div>User: <code>alice@example.com</code> / <code>alice123</code></div>
          </div> */}
        </div>
      </div>
    </div>
  );
}

// ── Register ─────────────────────────────────────────────────────────────────
export function RegisterPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: "", email: "", password: "", confirm: "" });
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);

  const set = (k) => (e) => setForm((f) => ({ ...f, [k]: e.target.value }));

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (form.password !== form.confirm) { setError("Passwords do not match"); return; }
    setError(""); setLoading(true);
    try {
      await api.post("/register", { name: form.name, email: form.email, password: form.password });
      setSuccess(true);
      setTimeout(() => navigate("/login"), 1800);
    } catch (err) {
      setError(err.response?.data?.error || "Registration failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-vh-100 d-flex align-items-center justify-content-center bg-light">
      <div className="card shadow-lg border-0" style={{ width: 440 }}>
        <div className="card-body p-5">
          <div className="text-center mb-4">
            <div className="bg-success rounded-3 d-inline-flex p-3 mb-3">
              <i className="bi bi-person-plus-fill text-white fs-2" />
            </div>
            <h3 className="fw-bold">Create account</h3>
            <p className="text-muted mb-0">Join LearnQuiz today</p>
          </div>

          {error && <div className="alert alert-danger py-2">{error}</div>}
          {success && <div className="alert alert-success py-2"><i className="bi bi-check-circle me-2" />Registered! Redirecting to login…</div>}

          <form onSubmit={handleSubmit}>
            {[
              { key: "name",    label: "Full Name", type: "text",     icon: "person",    ph: "Alice Johnson" },
              { key: "email",   label: "Email",     type: "email",    icon: "envelope",  ph: "alice@example.com" },
              { key: "password",label: "Password",  type: "password", icon: "lock",      ph: "Min. 6 characters" },
              { key: "confirm", label: "Confirm",   type: "password", icon: "lock-fill", ph: "Re-enter password" },
            ].map(f => (
              <div key={f.key} className="mb-3">
                <label className="form-label fw-semibold">{f.label}</label>
                <div className="input-group">
                  <span className="input-group-text"><i className={`bi bi-${f.icon}`} /></span>
                  <input type={f.type} className="form-control" placeholder={f.ph}
                    value={form[f.key]} onChange={set(f.key)} required minLength={f.key === "password" ? 6 : undefined} />
                </div>
              </div>
            ))}
            <button className="btn btn-success w-100 py-2 fw-semibold mt-1" type="submit" disabled={loading || success}>
              {loading ? <><span className="spinner-border spinner-border-sm me-2" />Creating…</> : "Create Account"}
            </button>
          </form>

          <p className="text-center text-muted mt-4 mb-0">
            Already have an account? <Link to="/login" className="text-primary fw-semibold">Sign in</Link>
          </p>
        </div>
      </div>
    </div>
  );
}
