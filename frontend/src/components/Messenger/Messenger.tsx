import { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import s from './Messenger.module.scss'

const Messenger = () => {
    const [isMessengerOpen, setIsMessengerOpen] = useState<boolean>(false)

    const handleClick = (): void => {
        setIsMessengerOpen(true)
        console.log('click');
    }

    return (
        <div className={s.container}>
            <div className={s.messenger} onClick={handleClick}>
                <AnimatePresence>
                    {isMessengerOpen && <motion.div className={s.popup}
                        initial={{ opacity: 0, y: 0, x: '-75%' }}
                        animate={{ opacity: 1, y: '-105%' }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 1 }}
                    >
                        <div className={s.topContainer}>
                            <div className={s.circle}></div>
                        </div>
                        <div className={s.line}>
                        </div>
                        <div className={s.content}>
                            <div className={s.leftMessage}>

                            </div>
                        </div>
                    </motion.div>}
                </AnimatePresence>
            </div>
        </div>
    );
}

export default Messenger;