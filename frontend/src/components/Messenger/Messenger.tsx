import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { AiOutlineClose } from "react-icons/ai";
import s from "./Messenger.module.scss";

const Messenger = () => {
    const [isMessengerOpen, setIsMessengerOpen] = useState<boolean>(false);

    const handleOpen = (): void => {
        setIsMessengerOpen(true);
    };

    const handleClose = (): void => {
        setIsMessengerOpen(false);
    };

    return (
        <div className={s.container}>
            <AnimatePresence>
                {isMessengerOpen && (
                    <motion.div
                        className={s.popup}
                        initial={{ opacity: 0, y: "100%", x: 75 }}
                        animate={{ opacity: 1, y: '-10%' }}
                        exit={{ opacity: 0, y: "100%" }}
                        transition={{ duration: 1 }}
                    >
                        <div className={s.topContainer}>
                            <div className={s.circle}></div>
                        </div>
                        <div className={s.line}></div>
                        <div className={s.topContent}>
                            <div
                                className={s.iconContainer}
                                onClick={handleClose}
                            >
                                <AiOutlineClose></AiOutlineClose>
                            </div>
                        </div>
                        <div className={s.content}>
                            <div className={s.leftMessage}></div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
            <div className={s.messenger} onClick={handleOpen}></div>
        </div>
    );
};

export default Messenger;
