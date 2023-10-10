import { Outlet } from 'react-router-dom';
import Nav from './Nav/Nav';
import Footer from './Footer/Footer';
import Messenger from './Messenger/Messenger';

const Layout = () => {
  return (
    <>
      <header>
        <Nav></Nav>
      </header>
      <Messenger></Messenger>
      <Outlet />
      <Footer></Footer>
    </>
  );
};

export default Layout;