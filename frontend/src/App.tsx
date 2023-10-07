import React from 'react';
import { Route, RouterProvider, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import Layout from './components/Layout';
import HomePage from './pages/HomePage/HomePage';
import NewsPage from './pages/NewsPage/NewsPage';
import NotFoundPage from './pages/NotFoundPage/NotFoundPage';

const router = createBrowserRouter(createRoutesFromElements(
  <Route path='/' element={<Layout />}>
    <Route index element={<HomePage />} />
    <Route path='news' element={<NewsPage />} />
    <Route path='*' element={<NotFoundPage />} />
  </Route>
));

function App() {
  return (
    <RouterProvider router={router} />
  );
}

export default App;
