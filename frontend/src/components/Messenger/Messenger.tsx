import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { AiOutlineClose } from "react-icons/ai";
import s from "./Messenger.module.scss";
import { botApi } from "../../services/botApi";
import Loader from "../Loader/Loader";

const Messenger = () => {
    const [message, setMessage] = useState<string>("");
    const [receivedMessages, setReceivedMessages] = useState<string[]>([]); // Состояние для полученных сообщений
    const [sentMessages, setSentMessages] = useState<string>(''); // Состояние для отправленных сообщений
    const [isMessengerOpen, setIsMessengerOpen] = useState<boolean>(false);
    const [firstClick, setFirstClick] = useState<boolean>(false)

    const [messageToBot, { data, isLoading, error }] = botApi.useSendToGptMessageMutation();

    const handleOpen = (): void => {
        setIsMessengerOpen(true);
        setFirstClick(true);
    };

    const handleClose = (): void => {
        setIsMessengerOpen(false);
    };

    const sendMessage = async () => {
        setSentMessages(message); // Добавляем отправленное сообщение в массив
        setMessage("");
        await messageToBot({ message: message });
    };

    // Если есть новое полученное сообщение, добавляем его в состояние
    // if (data) {
    //     setReceivedMessages([...receivedMessages, data]);
    // }

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
                            {/* {sentMessages.map((message, index) => (
                                <div className={s.rightMessage} key={`sent-${index}`}>
                                    {message}
                                </div>
                            ))}

                            {receivedMessages.map((message, index) => (
                                <div className={s.leftMessage} key={`received-${index}`}>
                                    {message}
                                </div>
                            ))}



                            <div className={s.flex}>
                                <input
                                    className={s.input}
                                    value={message}
                                    placeholder="Введите сообщение"
                                    onChange={e => setMessage(e.target.value)}
                                    type="text"
                                />
                                <button onClick={() => sendMessage()}>Отправить</button>
                            </div> */}


                            {sentMessages && <div className={s.rightMessage}>{sentMessages}</div>}
                            {isLoading && <Loader></Loader>}
                            {error && <h1>Произошла ошибка, попробуйте позже</h1>}


                            {/* ЭТОТ КОД ЕСЛИ ОДНО СООБЩЕНИЕ БОТУ ГПТ */}
                            {data ? (
                                <>
                                    <div className={s.leftMessage}>{data}</div>
                                    <div>Продолжить диалог, перейти на тг бота</div>
                                </>
                            ) : (
                                <div className={s.flex}>
                                    <input
                                        className={s.input}
                                        value={message}
                                        placeholder="Введите сообщение"
                                        onChange={e => setMessage(e.target.value)}
                                        type="text"
                                    />
                                    <button onClick={sendMessage}>Отправить</button>
                                </div>
                            )}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
            <div className={firstClick ? `${s.messenger}` : `${s.messenger} ${s.firstTimeMessenger}`} onClick={handleOpen}></div>
        </div>
    );
};

export default Messenger;
