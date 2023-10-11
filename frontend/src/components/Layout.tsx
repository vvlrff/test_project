import { Outlet } from 'react-router-dom';
import Nav from './Nav/Nav';
import Footer from './Footer/Footer';
import Messenger from './Messenger/Messenger';
import ProgressBar from './ProgressBar/ProgressBar';

const Layout = () => {
  return (
    <>
      <header>
        <Nav />
      </header>
      <ProgressBar></ProgressBar>
      <Messenger></Messenger>
      <Outlet />
      <Footer></Footer>
    </>
  );
};

export default Layout;