import { Link, Outlet } from 'react-router-dom';

const Layout = () => {
  return (
    <>
      <header>
        <Link to='/'>Главная </Link>
        <Link to='/posts'>Посты </Link>
      </header>
      <Outlet />
    </>
  );
};

export default Layout;