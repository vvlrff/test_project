import { motion } from "framer-motion";
import { ReactNode } from "react";
import { FC } from "react";

interface IFadeInWhenVisible {
    children: ReactNode;
    fadeIn?: boolean;
    scopeIn?: boolean;
    rotateIn?: boolean;
}

const FadeInWhenVisible: FC<IFadeInWhenVisible> = ({
    children,
    fadeIn,
    scopeIn,
}) => {
    const viewPort = fadeIn ? true : false;
    const delayTime = fadeIn ? 0.1 : 0.5;

    return (
        <motion.div
            initial={fadeIn ? "fadeInHidden" : "scopeInHidden"}
            whileInView={fadeIn ? "fadeInVisible" : "scopeInVisible"}
            viewport={{ once: viewPort }}
            transition={{
                duration: 0.5,
                delay: delayTime,
                delayChildren: 0.3,
                staggerChildren: 0.2,
            }}
            variants={{
                fadeInVisible: { opacity: 1, scale: 1 },
                fadeInHidden: { opacity: 0, scale: 0 },
                scopeInVisible: {
                    height: "600px",
                    width: "100%",
                },
                scopeInHidden: {
                    height: "300px",
                    width: "300px",
                },
            }}
        >
            {children}
        </motion.div>
    );
};

export default FadeInWhenVisible;
