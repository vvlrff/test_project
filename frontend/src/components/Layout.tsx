import { Outlet } from "react-router-dom";
import Nav from "./Nav/Nav";
import Footer from "./Footer/Footer";
import Messenger from "./Messenger/Messenger";
import ProgressBar from "./ProgressBar/ProgressBar";
import { motion } from "framer-motion";
import { useAppDispatch, useAppSelector } from "../app/hooks";
import { selectAuth } from "../features/authSlice";

const Layout = () => {
    const { access_token } = useAppSelector(selectAuth);

    return (
        <>
            <header>
                <Nav />
            </header>
            <motion.main
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 1 }}
            >
                <ProgressBar />
                {access_token && <Messenger />}
                <Outlet />
            </motion.main>
            <Footer />
        </>
    );
};

export default Layout;
