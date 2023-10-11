import s from "./Channels.module.scss";
import robot from "../../../assets/img/angryRobotAnime.png";
import AdsSwiper from "../../../components/AdsSwiper/AdsSwiper";
import FadeInWhenVisible from "../../../components/FadeInWhenVisible/FadeInWhenVisible";

const Channels = () => {
    return (
        <section className={s.section}>
            <div className={s.container}>
                <div className={s.captionContainer}>
                    <FadeInWhenVisible fadeIn={true}>
                        <h2 className={s.caption}>
                            Каналы, каналы, каналы, как же мы любим наши каналы
                        </h2>
                    </FadeInWhenVisible>
                </div>
                <div className={s.swiperContainer}>
                    <AdsSwiper></AdsSwiper>
                </div>
                <div className={s.right}>
                    <img src={robot} alt="" />
                    <div className={s.rightContent}>
                        <FadeInWhenVisible fadeIn={true}>
                            <p className={s.text}>
                                Нам уже всем всем надоело, что на наших любимых
                                каналах очень много бесполезной и ненужной
                                информации, а тем более еще и огромное
                                количество рекламы, которая только лишь мешает
                                погружаться в информационный поток
                            </p>
                            <p className={s.text}>
                                Нашему ассистенту это тоже не нравится, поэтому
                                вместе с ним мы предлагаем вам новый и
                                современный взгляд на получение информации
                            </p>
                        </FadeInWhenVisible>
                    </div>
                </div>
                <div>
                    <div className={s.enoughContainer}>
                        <div className={s.enough}>
                            <h2 className={s.enoughHeader}>С нас хватит!</h2>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Channels;
