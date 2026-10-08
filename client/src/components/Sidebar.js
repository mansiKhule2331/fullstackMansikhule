import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const userLinks = [
  { to: "/dashboard",  icon: "house-fill",       label: "Dashboard" },
  { to: "/languages",  icon: "globe2",            label: "Languages" },
  { to: "/progress",   icon: "bar-chart-fill",    label: "My Progress" },
];

const adminLinks = [
  { to: "/admin",           icon: "speedometer2",     label: "Analytics" },
  { to: "/admin/languages", icon: "translate",        label: "Manage Languages" },
  { to: "/admin/topics",    icon: "journal-text",     label: "Manage Topics" },
  { to: "/admin/questions", icon: "patch-question-fill", label: "Manage Questions" },
  { to: "/admin/users",     icon: "people-fill",      label: "All Users" },
];

export default function Sidebar() {
  const { user, logout, isAdmin } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => { logout(); navigate("/login"); };

  const linkClass = ({ isActive }) =>
    `nav-link d-flex align-items-center gap-2 px-3 py-2 rounded mb-1 ${
      isActive ? "active bg-primary text-white fw-semibold" : "text-dark"
    }`;

  return (
    <div
      className="d-flex flex-column bg-white border-end shadow-sm"
      style={{ width: 240, minHeight: "100vh", position: "sticky", top: 0 }}
    >
      {/* Brand */}
      <div className="p-3 border-bottom">
        <div className="d-flex align-items-center gap-2">
          <div className="bg-primary rounded-2 p-2">
            <i className="bi bi-mortarboard-fill text-white fs-5" />
          </div>
          <div>
            <div className="fw-bold lh-1">LearnQuiz</div>
            <small className="text-muted">{isAdmin ? "Admin Panel" : "Learning Hub"}</small>
          </div>
        </div>
      </div>

      {/* User Info */}
      <div className="px-3 py-2 border-bottom bg-light">
        <div className="d-flex align-items-center gap-2">
          <div className="rounded-circle bg-primary d-flex align-items-center justify-content-center text-white fw-bold"
               style={{ width: 34, height: 34, fontSize: 14 }}>
            {user?.name?.[0]?.toUpperCase()}
          </div>
          <div style={{ minWidth: 0 }}>
            <div className="fw-semibold text-truncate" style={{ fontSize: 14 }}>{user?.name}</div>
            <span className={`badge ${isAdmin ? "bg-danger" : "bg-secondary"}`} style={{ fontSize: 10 }}>
              {user?.role}
            </span>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-grow-1 p-3 overflow-auto">
        {!isAdmin && (
          <>
            <div className="text-uppercase text-muted fw-semibold mb-2" style={{ fontSize: 11, letterSpacing: 1 }}>
              Learning
            </div>
            {userLinks.map(l => (
              <NavLink key={l.to} to={l.to} className={linkClass} end={l.to === "/dashboard"}>
                <i className={`bi bi-${l.icon}`} />
                <span style={{ fontSize: 14 }}>{l.label}</span>
              </NavLink>
            ))}
          </>
        )}

        {isAdmin && (
          <>
            <div className="text-uppercase text-muted fw-semibold mb-2" style={{ fontSize: 11, letterSpacing: 1 }}>
              Admin
            </div>
            {adminLinks.map(l => (
              <NavLink key={l.to} to={l.to} className={linkClass} end={l.to === "/admin"}>
                <i className={`bi bi-${l.icon}`} />
                <span style={{ fontSize: 14 }}>{l.label}</span>
              </NavLink>
            ))}
            <hr />
            <div className="text-uppercase text-muted fw-semibold mb-2" style={{ fontSize: 11, letterSpacing: 1 }}>
              User View
            </div>
            {userLinks.map(l => (
              <NavLink key={l.to + "-u"} to={l.to} className={linkClass} end={l.to === "/dashboard"}>
                <i className={`bi bi-${l.icon}`} />
                <span style={{ fontSize: 14 }}>{l.label}</span>
              </NavLink>
            ))}
          </>
        )}
      </nav>

      {/* Logout */}
      <div className="p-3 border-top">
        <button className="btn btn-outline-danger btn-sm w-100 d-flex align-items-center justify-content-center gap-2"
                onClick={handleLogout}>
          <i className="bi bi-box-arrow-left" />
          Sign Out
        </button>
      </div>
    </div>
  );
}
