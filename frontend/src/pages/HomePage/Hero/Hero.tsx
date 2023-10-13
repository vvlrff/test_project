import s from "./Hero.module.scss";
import { TypeAnimation } from "react-type-animation";
import FadeInWhenVisible from "../../../components/FadeInWhenVisible/FadeInWhenVisible";
import Robot from "../../../components/Robot/Robot";
import { useNavigate } from "react-router-dom";

const Hero = () => {
    const navigate = useNavigate();

    const handleRedirect = () => {
        navigate("/news");
    };

    return (
        <>
            <section className={s.hero}>
                <div className={s.sectionContainer}>
                    <div className={s.container}>
                        <FadeInWhenVisible fadeIn={true}>
                            <h1 className={s.header}>
                                <TypeAnimation
                                    sequence={[
                                        "Интеллектуальный",
                                        2000,
                                        "Непревзойдённый",
                                        2000,
                                        "Сообразительный",
                                        2000,
                                        "Уникальный",
                                        2000,
                                    ]}
                                    wrapper="span"
                                    speed={25}
                                    style={{ display: "inline-block" }}
                                    repeat={Infinity}
                                />
                                <span className={s.headerSpan}>
                                    поиск информации в Telegram
                                </span>
                            </h1>
                            <p className={s.text}>
                                Благодаря нашему сервису Вы можете быстро найти
                                интересующую Вас информацию из Telegram-каналов.
                                Мы объединили передовые алгоритмы и технологии с
                                удобным и современным интерфейсом, чтобы
                                предоставить пользователям быстрый и удобный
                                доступ к необходимым данным
                            </p>
                            <div className={s.btnContainer}>
                                <button
                                    className={s.btn}
                                    onClick={() => handleRedirect()}
                                >
                                    Попробовать
                                </button>
                            </div>
                        </FadeInWhenVisible>
                    </div>
                    <div className={s.bottomContainer}>
                        <div
                            className={`${s.captionContainer} ${s.captionInline}`}
                        >
                            <FadeInWhenVisible fadeIn={true}>
                                <h2 className={s.caption}>
                                    Более 100 каналов – огромное информационное
                                    пространство!
                                </h2>
                            </FadeInWhenVisible>
                        </div>
                        <div className={s.robotContainer}>
                            <Robot></Robot>
                        </div>
                    </div>
                </div>
                <div className={s.captionContainer}>
                    <FadeInWhenVisible fadeIn={true}>
                        <h2 className={s.caption}>
                            Более 100 каналов – огромное информационное
                            пространство!
                        </h2>
                    </FadeInWhenVisible>
                </div>
            </section>
        </>
    );
};

export default Hero;
