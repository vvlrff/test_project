import s from "./HowTo.module.scss";
import { motion } from "framer-motion";
import clock from "../../../assets/img/clock.gif";
import { useState, useRef } from "react";
import FadeInWhenVisible from "../../../components/FadeInWhenVisible/FadeInWhenVisible";
import { BsArrowRight } from "react-icons/bs";

const HowTo = () => {
    const container = {
        hidden: { height: 200, width: 300 },
        visible: {
            height: 500,
            width: "100%",
            transition: {
                duration: 0.5,
                delay: 0.5,
                delayChildren: 0.8,
                staggerChildren: 0.2,
            },
        },
    };

    const item = {
        hidden: { y: 20, opacity: 0 },
        visible: {
            y: 0,
            opacity: 1,
        },
    };
    const ref = useRef<HTMLDivElement>(null);

    const [condition, setCondition] = useState<boolean>(false);

    const handleCondition = (): void => {
        setCondition(true);
        setTimeout(() => handleClick(), 1);
    };

    const handleClick = (): void => {
        ref.current?.scrollIntoView({ behavior: "smooth" });
    };

    return (
        <section className={s.section}>
            <div className={s.left}>
                <FadeInWhenVisible fadeIn={true}>
                    <p className={s.text}>
                        Время - это очень ценный ресурс, который мы предлагаем
                        использовать разумно. Вместе с нами Вы перестанете
                        тратить время на долгий поиск интересующей Вас
                        информации!
                    </p>
                    <div className={s.btnContainer}>
                        <img src={clock} alt="" />
                        <button className={s.btn} onClick={handleCondition}>
                            Как начать?
                        </button>
                        <img src={clock} alt="" />
                    </div>
                </FadeInWhenVisible>
            </div>

            {condition ? (
                <>
                    <h2 className={s.header}>Как это работает?</h2>
                    <div className={s.container}>
                        <motion.ul
                            className={s.placeholderContainer}
                            initial="hidden"
                            whileInView="visible"
                            variants={container}
                            viewport={{ once: false }}
                        >
                            <motion.li
                                className={s.placeholder}
                                variants={item}
                            ></motion.li>
                            <motion.li
                                className={s.placeholder}
                                variants={item}
                            ></motion.li>
                            <motion.li
                                className={s.placeholder}
                                variants={item}
                            ></motion.li>
                            <motion.div className={s.line} variants={item}>
                                <div>
                                    <p>Зарегистрируйтесь на сервисе </p>
                                </div>
                                <div>
                                    <p>
                                        Введите запрос и выберите временной
                                        интервал для поиска
                                    </p>
                                </div>
                                <div>
                                    <p>
                                        Получите результат и проконсультируйтесь
                                        с умным помощником
                                    </p>
                                </div>
                            </motion.div>
                        </motion.ul>
                    </div>
                    <div
                        ref={ref}
                    ></div>
                </>
            ) : null}
        </section>
    );
};

export default HowTo;
