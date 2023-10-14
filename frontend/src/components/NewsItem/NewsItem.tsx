import React, { FC } from "react";
import { INews } from "../../models/INews";
import { Link } from "react-router-dom";
import s from "./NewsItem.module.scss";
import placeholder from "../../assets/img/placeholder.png";
import { Variants, motion } from "framer-motion";

interface NewsItemProps {
    news: INews;
    animationVariants?: Variants;
}

const NewsItem: FC<NewsItemProps> = ({ news, animationVariants }) => {
    const splitedMessage = news.msg.split(" ");
    const slicedMessage = splitedMessage.slice(0, 30);
    const cutMessage = slicedMessage.concat("...");
    const finalMessage = cutMessage.join(" ");

    return (
        <motion.li variants={animationVariants} className={s.item}>
            <div className={s.top}>
                <img
                    className={s.img}
                    src={news.photo ? news.photo : placeholder}
                    alt="photoImg"
                />
                <div className={s.topContent}>
                    <p className={s.date}>{news.date}</p>
                    {/* <p className={s.relevance}>
                        {news.relevant_score < 4 ? relevanceOptions.bad.text : news.relevant_score < 7 ? relevanceOptions.normal.text : relevanceOptions.good.text}
                    </p> */}
                    {news.url ? (
                        <Link className={s.link} to={news.url}>
                            К источнику
                        </Link>
                    ) : (
                        <p className={s.link}>Источник новости отсутствует</p>
                    )}
                </div>
            </div>
            <div className={s.content}>
                <p className={s.text}>{finalMessage}</p>
                {/* <button onClick={() => handleDelete()}>Удалить</button> */}
                <div className={s.buttonContainer}>
                    <Link to={`/news/${news}`} className={s.button}>
                        Подробнее
                    </Link>
                </div>
            </div>
        </motion.li>
    );
};

export default NewsItem;
