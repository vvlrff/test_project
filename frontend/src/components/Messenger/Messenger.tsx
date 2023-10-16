import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { AiOutlineClose } from "react-icons/ai";
import s from "./Messenger.module.scss";
import { botApi } from "../../services/botApi";
import MessageLoader from "../MessageLoader/MessageLoader";
import { VscSend } from "react-icons/vsc";

const Messenger = () => {
    const [message, setMessage] = useState<string>("");
    const [sentMessages, setSentMessages] = useState<string>("");
    const [isMessengerOpen, setIsMessengerOpen] = useState<boolean>(false);
    const [firstClick, setFirstClick] = useState<boolean>(false);

    const [messageToBot, { data, isLoading, error }] =
        botApi.useSendToGptMessageMutation();

    const handleOpen = (): void => {
        setIsMessengerOpen(true);
        setFirstClick(true);
    };

    const handleClose = (): void => {
        setIsMessengerOpen(false);
    };

    const sendMessage = async () => {
        setSentMessages(message);
        setMessage("");
        await messageToBot({ message: message });
    };

    return (
        <div className={s.container}>
            <AnimatePresence>
                {isMessengerOpen && (
                    <motion.div
                        className={s.popup}
                        initial={{ opacity: 0, y: "100%", x: 75 }}
                        animate={{ opacity: 1, y: "-10%" }}
                        exit={{ opacity: 0, y: "100%" }}
                        transition={{ duration: 1 }}
                    >
                        <div className={s.globalContainer}>
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
                                {sentMessages && (
                                    <div className={s.rightMessage}>
                                        {sentMessages}
                                    </div>
                                )}
                                {isLoading && <MessageLoader></MessageLoader>}
                                {error && (
                                    <h1>Произошла ошибка, попробуйте позже</h1>
                                )}
                                {data && (<div className={s.leftMessage}>
                                    {data}
                                </div>)}

                                <div className={s.types}>
                                    <input
                                        className={s.input}
                                        value={message}
                                        placeholder="Введите сообщение"
                                        onChange={(e) =>
                                            setMessage(e.target.value)
                                        }
                                        type="text"
                                    />
                                    <div
                                        className={s.sendContainer}
                                        onClick={sendMessage}
                                    >
                                        <VscSend></VscSend>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
            <div
                className={
                    firstClick
                        ? `${s.messenger}`
                        : `${s.messenger} ${s.firstTimeMessenger}`
                }
                onClick={handleOpen}
            ></div>
        </div>
    );
};

export default Messenger;
