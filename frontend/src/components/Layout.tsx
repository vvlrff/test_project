import { Outlet } from 'react-router-dom';
import Nav from './Nav/Nav';
import Footer from './Footer/Footer';
import Messenger from './Messenger/Messenger';
import ProgressBar from './ProgressBar/ProgressBar';
import { motion } from 'framer-motion'

const Layout = () => {

  return (
    <>
      <header>
        <Nav />
      </header>
      <motion.main
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}>
        <ProgressBar></ProgressBar>
        <Messenger></Messenger>
        <Outlet />
      </motion.main>
      <Footer></Footer>
    </>
  );
};

export default Layout;