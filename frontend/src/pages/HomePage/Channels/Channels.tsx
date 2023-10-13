import s from "./Channels.module.scss";
import robot from "../../../assets/img/angryRobotAnime.png";
import AdsSwiper from "../../../components/AdsSwiper/AdsSwiper";
import FadeInWhenVisible from "../../../components/FadeInWhenVisible/FadeInWhenVisible";

const Channels = () => {
    return (
        <section className={s.section}>
            <div className={s.container}>
                <div className={s.swiperContainer}>
                    <AdsSwiper></AdsSwiper>
                </div>
                <div className={s.right}>
                    <img src={robot} alt="" />
                    <div className={s.rightContent}>
                        <FadeInWhenVisible fadeIn={true}>
                            <p className={s.text}>
                                Наш сервис - это надежный и эффективный способ
                                получить актуальную информацию из
                                Telegram-каналов, который будет полезен как для
                                обычных пользователей, так и для бизнеса. Мы
                                стремимся обеспечить лучший опыт поиска и помочь
                                Вам экономить время и усилия при поиске нужной
                                информации
                            </p>
                            <p className={s.text}>
                                Нам тоже не нравится тратить время впустую,
                                поэтому мы предлагаем Вам новый и современный
                                взгляд на получение информации
                            </p>
                        </FadeInWhenVisible>
                    </div>
                </div>
                <div>
                    <div className={s.enoughContainer}>
                        <div className={s.enough}>
                            <FadeInWhenVisible fadeIn={true}>
                                <h2 className={s.enoughHeader}>
                                    Самая актуальная и релевантная информация!
                                </h2>
                            </FadeInWhenVisible>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Channels;
