import s from './Channels.module.scss'
import { FC } from 'react'
import clock from '../../../assets/img/clock.gif'

interface IChannels {
    condition: number;
    handleCondition(): void;
    handleScrollDown(): void;
}

const Channels: FC<IChannels> = ({ condition, handleCondition, handleScrollDown }) => {
    const firstCondition = { color: 'red' }
    const secondCondition = { color: 'blue' }
    const lastCondition = { color: 'cyan' }

    return (
        <section>
            <div className={s.container}>
                <div className={s.captionContainer}>
                    <h2 className={s.caption}>Каналы, каналы, каналы, как же мы любим наши каналы</h2>
                </div>
                <div className={s.right}>
                    <p className={s.text}>Нам уже всем всем надоело, что на наших любимых каналах очень много бесполезной и ненужной информации, а тем более еще и огромное количество рекламы, которая только лишь мешает погружаться в информационный поток</p>
                    <p className={s.text}>Нашему ассистенту это тоже не нравится, поэтому вместе с ним мы предлагаем вам новый и современный взгляд на получение информации</p>
                </div>
                <div>
                    <div className={s.enough}>
                        <h2 className={s.enoughHeader}>С нас хватит!</h2>
                    </div>
                </div>
                <div className={s.left}>
                    <p className={s.text}>Время - это очень ценный ресурс, который мы предлагаем использовать разумно. Вместе с нами вы перестанете тратить время на долгий поиск интересующей вас информации!</p>
                    <div className={s.btnContainer}>
                        <img src={clock} alt="" />

                        <button className={s.btn} onClick={condition === 1 ? handleScrollDown : handleCondition} style={condition === 3 ? firstCondition : condition === 2 ? secondCondition : condition === 1 ? lastCondition : undefined}>
                            Сэкономить время
                        </button>
                        <img src={clock} alt="" />

                    </div>
                </div>
            </div>
        </section>
    );
}

export default Channels;