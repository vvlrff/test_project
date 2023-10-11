import s from './ProgressBar.module.scss'
import { motion, useScroll, useSpring } from "framer-motion";


const ProgressBar = () => {
    const { scrollYProgress } = useScroll();
    const scaleX = useSpring(scrollYProgress, {
        stiffness: 100,
        damping: 30,
        restDelta: 0.001
    });

    return (
        <motion.div className={s.progressBar} style={{ scaleX }} ></motion.div>
    );
}

export default ProgressBar;