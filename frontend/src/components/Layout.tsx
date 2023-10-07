import { Link, Outlet } from 'react-router-dom';

const Layout = () => {
  return (
    <>
      <header>
        <Link to='/'>Главная </Link>
        <Link to='/news'>Новости </Link>
      </header>
      <Outlet />
    </>
  );
};

export default Layout;