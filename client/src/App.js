import { BrowserRouter, Routes, Route, Navigate, Outlet } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import { ProtectedRoute } from "./components/Shared";
import Sidebar from "./components/Sidebar";

import { LoginPage, RegisterPage } from "./pages/AuthPages";
import {
  DashboardPage, LanguagesPage, TopicsPage,
  TopicContentPage, QuizPage, ProgressPage,
} from "./pages/UserPages";
import AdminAnalyticsPage from "./pages/AdminAnalyticsPage";
import {
  AdminLanguagesPage, AdminTopicsPage,
  AdminQuestionsPage, AdminUsersPage,
} from "./pages/AdminCrudPages";

// Layout wrapper — renders Sidebar + content area
function AppLayout() {
  return (
    <div className="d-flex" style={{ minHeight: "100vh", background: "#f8f9fb" }}>
      <Sidebar />
      <main className="flex-grow-1 p-4" style={{ minWidth: 0 }}>
        <Outlet />
      </main>
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          {/* Public */}
          <Route path="/login"    element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />

          {/* Authenticated layout */}
          <Route element={<ProtectedRoute><AppLayout /></ProtectedRoute>}>
            {/* User routes */}
            <Route path="/dashboard"       element={<DashboardPage />} />
            <Route path="/languages"       element={<LanguagesPage />} />
            <Route path="/topics/:langId"  element={<TopicsPage />} />
            <Route path="/topic/:topicId"  element={<TopicContentPage />} />
            <Route path="/quiz/:topicId"   element={<QuizPage />} />
            <Route path="/progress"        element={<ProgressPage />} />

            {/* Admin routes */}
            <Route path="/admin"                element={<ProtectedRoute adminOnly><AdminAnalyticsPage /></ProtectedRoute>} />
            <Route path="/admin/languages"      element={<ProtectedRoute adminOnly><AdminLanguagesPage /></ProtectedRoute>} />
            <Route path="/admin/topics"         element={<ProtectedRoute adminOnly><AdminTopicsPage /></ProtectedRoute>} />
            <Route path="/admin/questions"      element={<ProtectedRoute adminOnly><AdminQuestionsPage /></ProtectedRoute>} />
            <Route path="/admin/users"          element={<ProtectedRoute adminOnly><AdminUsersPage /></ProtectedRoute>} />
          </Route>

          {/* Fallback */}
          <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
}
