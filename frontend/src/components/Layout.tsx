import { Outlet } from 'react-router-dom';
import Nav from './Nav/Nav';

const Layout = () => {
  return (
    <>
      <header>
        <Nav></Nav>
      </header>
      <Outlet />
    </>
  );
};

export default Layout;