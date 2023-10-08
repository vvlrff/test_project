import React, { useEffect } from 'react';
import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import Layout from './components/Layout';
import HomePage from './pages/HomePage/HomePage';
import NewsPage from './pages/NewsPage/NewsPage';
import NotFoundPage from './pages/NotFoundPage/NotFoundPage';
import AuthPage from './pages/AuthPage/AuthPage';
import RegisterPage from './pages/RegisterPage/RegisterPage';
import { useAppDispatch } from './app/hooks';
import { setUser } from './features/authSlice';

const router = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />}>
    <Route index element={<HomePage />} />
    <Route path='auth' element={<AuthPage />} />
    <Route path='register' element={<RegisterPage />} />
    <Route path='news' element={<NewsPage />} />
    <Route path='*' element={<NotFoundPage />} />
  </Route>
));

function App() {
  const dispatch = useAppDispatch();
  const user = JSON.parse(localStorage.getItem("user") || "{}");

  useEffect(() => {
    dispatch(setUser(user));
  }, []);

  return (
    <RouterProvider router={router} />
  );
}

export default App;
