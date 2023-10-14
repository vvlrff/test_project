import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import Layout from './components/Layout';
import HomePage from './pages/HomePage/HomePage';
import NewsPage from './pages/NewsPage/NewsPage';
import NotFoundPage from './pages/NotFoundPage/NotFoundPage';
import AuthPage from './pages/AuthPage/AuthPage';
import RegisterPage from './pages/RegisterPage/RegisterPage';
import { ProtectedRoute } from './components/ProtectedRoute';
import { useEffect } from 'react';
import { setUser } from './features/authSlice';
import { useAppDispatch } from './app/hooks';
import IdPage from './pages/IdPage/IdPage';


const router = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />}>
    <Route index element={<HomePage />} />
    <Route path='auth' element={<AuthPage />} />
    <Route path='register' element={<RegisterPage />} />
    <Route element={<ProtectedRoute />}>
      <Route path='news' element={<NewsPage />} />
      <Route path='news/:id' element={<IdPage />} />
    </Route>
    <Route path='*' element={<NotFoundPage />} />
  </Route>
));

function App() {
  const dispatch = useAppDispatch();
  const user = JSON.parse(localStorage.getItem("user") || "{}");
  console.log(user)

  useEffect(() => {
    dispatch(setUser(user));
  }, []);

  return (
    <RouterProvider router={router} />
  );
}

export default App;
