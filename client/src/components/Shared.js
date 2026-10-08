import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function Spinner({ size = "md" }) {
  return (
    <div className={`d-flex justify-content-center align-items-center py-5`}>
      <div className={`spinner-border text-primary spinner-border-${size}`} role="status">
        <span className="visually-hidden">Loading…</span>
      </div>
    </div>
  );
}

export function Alert({ type = "danger", children, onClose }) {
  return (
    <div className={`alert alert-${type} alert-dismissible`} role="alert">
      {children}
      {onClose && (
        <button type="button" className="btn-close" onClick={onClose} />
      )}
    </div>
  );
}

export function ProtectedRoute({ children, adminOnly = false }) {
  const { user, isAdmin } = useAuth();
  if (!user) return <Navigate to="/login" replace />;
  if (adminOnly && !isAdmin) return <Navigate to="/dashboard" replace />;
  return children;
}

export function EmptyState({ icon = "inbox", text }) {
  return (
    <div className="text-center py-5 text-muted">
      <i className={`bi bi-${icon} display-4`} />
      <p className="mt-3">{text}</p>
    </div>
  );
}
