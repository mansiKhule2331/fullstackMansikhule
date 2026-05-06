import { useState, useEffect } from "react";
import api from "../api/axios";
import { Spinner, EmptyState } from "../components/Shared";

function StatCard({ icon, label, value, color, sub }) {
  return (
    <div className="col-sm-6 col-xl-3">
      <div className="card border-0 shadow-sm h-100">
        <div className="card-body p-4">
          <div className="d-flex align-items-center justify-content-between mb-3">
            <div className={`bg-${color} bg-opacity-10 rounded-3 p-3`}>
              <i className={`bi bi-${icon} text-${color} fs-3`} />
            </div>
            <span className={`badge bg-${color} bg-opacity-10 text-${color} rounded-pill`}>Live</span>
          </div>
          <div className="fw-bold display-6 mb-1">{value ?? <span className="spinner-border spinner-border-sm" />}</div>
          <div className="text-muted small fw-semibold text-uppercase" style={{ letterSpacing: 1 }}>{label}</div>
          {sub && <div className="text-muted" style={{ fontSize: 12, marginTop: 4 }}>{sub}</div>}
        </div>
      </div>
    </div>
  );
}

export default function AdminAnalyticsPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");

  const load = () => {
    setLoading(true); setError("");
    api.get("/admin/analytics")
      .then(r => { setData(r.data); setLoading(false); })
      .catch(e => { setError(e.response?.data?.error || "Failed to load analytics"); setLoading(false); });
  };

  useEffect(() => { load(); }, []);

  const filtered = (data?.per_user_table || []).filter(u =>
    u.name.toLowerCase().includes(search.toLowerCase()) ||
    u.email.toLowerCase().includes(search.toLowerCase())
  );

  const maxTests = Math.max(...(data?.per_user_table || []).map(u => u.tests_taken), 1);

  return (
    <div>
      {/* Header */}
      <div className="d-flex justify-content-between align-items-start mb-4 flex-wrap gap-3">
        <div>
          <h2 className="fw-bold mb-1">Analytics Dashboard</h2>
          <p className="text-muted mb-0">Real-time platform statistics</p>
        </div>
        <button className="btn btn-outline-primary btn-sm d-flex align-items-center gap-2" onClick={load}>
          <i className="bi bi-arrow-clockwise" />Refresh
        </button>
      </div>

      {error && <div className="alert alert-danger">{error}</div>}

      {/* Stat Cards */}
      <div className="row g-3 mb-4">
        <StatCard icon="people-fill"    label="Total Users"       value={data?.total_users}       color="primary"
                  sub="Registered accounts" />
        <StatCard icon="box-arrow-in-right" label="Total Logins"  value={data?.total_logins}      color="info"
                  sub="Cumulative login count" />
        <StatCard icon="clipboard-check-fill" label="Tests Taken" value={data?.total_tests_taken} color="success"
                  sub="Quiz submissions" />
        <StatCard icon="lightning-charge-fill" label="Active Users" value={data?.active_users}    color="warning"
                  sub="Users who logged in at least once" />
      </div>

      {/* Engagement visual */}
      {data && (
        <div className="row g-3 mb-4">
          <div className="col-md-6">
            <div className="card border-0 shadow-sm h-100">
              <div className="card-body p-4">
                <h6 className="fw-bold text-muted text-uppercase mb-3" style={{ letterSpacing: 1, fontSize: 12 }}>
                  Engagement Rate
                </h6>
                <div className="d-flex align-items-center gap-3 mb-3">
                  <div className="display-5 fw-bold text-success">
                    {data.total_users
                      ? ((data.active_users / data.total_users) * 100).toFixed(1)
                      : 0}%
                  </div>
                  <div className="text-muted small">of users have<br />logged in at least once</div>
                </div>
                <div className="progress" style={{ height: 10, borderRadius: 99 }}>
                  <div className="progress-bar bg-success"
                       style={{ width: `${data.total_users ? (data.active_users / data.total_users) * 100 : 0}%`, borderRadius: 99 }} />
                </div>
                <div className="d-flex justify-content-between mt-1" style={{ fontSize: 12 }}>
                  <span className="text-muted">{data.active_users} active</span>
                  <span className="text-muted">{data.total_users} total</span>
                </div>
              </div>
            </div>
          </div>
          <div className="col-md-6">
            <div className="card border-0 shadow-sm h-100">
              <div className="card-body p-4">
                <h6 className="fw-bold text-muted text-uppercase mb-3" style={{ letterSpacing: 1, fontSize: 12 }}>
                  Avg. Tests per Active User
                </h6>
                <div className="display-5 fw-bold text-primary mb-2">
                  {data.active_users
                    ? (data.total_tests_taken / data.active_users).toFixed(1)
                    : 0}
                </div>
                <p className="text-muted small mb-0">
                  {data.total_tests_taken} total quiz submissions across {data.active_users} active users.
                  {data.total_logins > 0 && ` Average ${(data.total_tests_taken / data.total_logins).toFixed(2)} quizzes per login session.`}
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Per-User Table */}
      <div className="card border-0 shadow-sm">
        <div className="card-header bg-white border-bottom d-flex justify-content-between align-items-center py-3 flex-wrap gap-2">
          <div className="fw-semibold">
            <i className="bi bi-table me-2 text-primary" />Per-User Quiz Statistics
          </div>
          <input className="form-control form-control-sm"
                 style={{ maxWidth: 220 }}
                 placeholder="🔍 Search by name or email…"
                 value={search}
                 onChange={e => setSearch(e.target.value)} />
        </div>
        <div className="card-body p-0">
          {loading
            ? <Spinner />
            : filtered.length === 0
              ? <EmptyState icon="person-x" text="No user data found." />
              : (
                <div className="table-responsive">
                  <table className="table table-hover align-middle mb-0">
                    <thead className="table-light">
                      <tr>
                        <th>#</th>
                        <th>User</th>
                        <th>Role</th>
                        <th>Tests Taken</th>
                        <th style={{ minWidth: 150 }}>Activity Bar</th>
                        <th>Logins</th>
                        <th>Last Login</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filtered.map((u, i) => (
                        <tr key={u.user_id}>
                          <td className="text-muted">{i + 1}</td>
                          <td>
                            <div className="d-flex align-items-center gap-2">
                              <div className="rounded-circle bg-primary bg-opacity-10 d-flex align-items-center justify-content-center text-primary fw-bold"
                                   style={{ width: 32, height: 32, fontSize: 13 }}>
                                {u.name?.[0]?.toUpperCase()}
                              </div>
                              <div>
                                <div className="fw-semibold" style={{ fontSize: 14 }}>{u.name}</div>
                                <div className="text-muted" style={{ fontSize: 12 }}>{u.email}</div>
                              </div>
                            </div>
                          </td>
                          <td>
                            <span className={`badge ${u.role === "admin" ? "bg-danger" : "bg-secondary"}`}>
                              {u.role || "user"}
                            </span>
                          </td>
                          <td>
                            <span className="badge bg-success bg-opacity-10 text-success fw-bold fs-6 px-3">
                              {u.tests_taken}
                            </span>
                          </td>
                          <td>
                            <div className="d-flex align-items-center gap-2">
                              <div className="progress flex-grow-1" style={{ height: 6 }}>
                                <div className="progress-bar bg-primary"
                                     style={{ width: `${(u.tests_taken / maxTests) * 100}%` }} />
                              </div>
                              <span className="text-muted" style={{ fontSize: 12, minWidth: 24 }}>{u.tests_taken}</span>
                            </div>
                          </td>
                          <td className="text-muted">{u.login_count}</td>
                          <td className="text-muted small">
                            {u.last_login ? new Date(u.last_login).toLocaleString() : <em>Never</em>}
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
